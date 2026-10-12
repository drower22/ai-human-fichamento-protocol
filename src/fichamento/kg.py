"""Export fichamentos as knowledge-graph nodes/edges (JSONL).

Node types: article, theory, concept, method, sector, finding.
Edges carry `evidence`: [{fichamento_id, refs}] — every claim in the graph
traces back to a fichamento AND to the page/line in the source article.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from . import paths
from .models import Fichamento


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def _node_id(kind: str, name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", _norm(name)).strip("_")
    return f"{kind}:{slug}"


def export_kg(out_dir: str, sources: list[str] = None) -> None:
    sources = sources or ["ai", "human"]
    fichamentos: list[Fichamento] = []
    for p in sorted(paths.DATA.glob("fichamentos/round*/*/*.json")):
        f = Fichamento.model_validate_json(p.read_text())
        if f.source in sources:
            fichamentos.append(f)

    nodes: dict[str, dict] = {}
    edges: dict[tuple, dict] = {}

    def node(kind: str, name: str, **props) -> str:
        nid = _node_id(kind, name)
        n = nodes.setdefault(nid, {"id": nid, "type": kind, "name": name,
                                   "sources": set()})
        n.update({k: v for k, v in props.items() if v})
        return nid

    def edge(src: str, rel: str, dst: str, f: Fichamento, refs: list[str]) -> None:
        key = (src, rel, dst)
        e = edges.setdefault(key, {"source": src, "type": rel, "target": dst,
                                   "evidence": []})
        e["evidence"].append({"fichamento_id": f.fichamento_id,
                              "producer": _producer(f), "refs": refs})

    def _producer(f: Fichamento) -> str:
        g = f.generator
        return getattr(g, "participant_id", None) or getattr(g, "model", "ai")

    for f in fichamentos:
        art = node("article", f.article_id)
        nodes[art]["sources"].add(f.source)
        for t in f.content.theories:
            th = node("theory", t.name, tradition=t.tradition)
            nodes[th]["sources"].add(f.source)
            edge(art, "USES_THEORY", th, f, t.source_refs)
        for c in f.content.key_concepts:
            cn = node("concept", c.concept, definition=c.definition)
            nodes[cn]["sources"].add(f.source)
            edge(art, "DEFINES_CONCEPT", cn, f, c.source_refs)
        for m in f.content.methodology.methods:
            mn = node("method", m)
            nodes[mn]["sources"].add(f.source)
            edge(art, "EMPLOYS_METHOD", mn, f, f.content.methodology.source_refs)
        if f.content.methodology.sector:
            sn = node("sector", f.content.methodology.sector)
            nodes[sn]["sources"].add(f.source)
            edge(art, "STUDIES_SECTOR", sn, f, f.content.methodology.source_refs)
        for i, fd in enumerate(f.content.main_findings, 1):
            fid = f"finding:{f.article_id}:{i}"
            nodes[fid] = {"id": fid, "type": "finding", "name": fd.finding,
                          "finding_type": fd.type, "article": f.article_id,
                          "sources": {f.source}}
            edge(art, "REPORTS_FINDING", fid, f, fd.source_refs)

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "nodes.jsonl", "w") as fh:
        for n in nodes.values():
            n["sources"] = sorted(n["sources"])
            fh.write(json.dumps(n, ensure_ascii=False) + "\n")
    with open(out / "edges.jsonl", "w") as fh:
        for e in edges.values():
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"KG export: {len(nodes)} nós, {len(edges)} arestas → {out}")
