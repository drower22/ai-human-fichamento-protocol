"""Candidate-pool stage: AI proposes theory candidates -> humans classify.

`fichamento candidates --round N` produces, per article:
  - data/candidates/roundN/A{nn}.candidates.json  (pool, editable for curation)
  - data/candidates/roundN/A{nn}.pool.md          (student checklist sheet)

The pool file is meant to be hand-editable: add items with
``origin: "researcher"`` and flip ``active`` instead of deleting, so the
audit trail preserves what the AI proposed.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

from . import paths
from .llm import call_model as _call_model
from .models import CandidateItem, CandidatePool, PoolGenerator
from .pdf2md import check_gate
from .registry import load_articles

POOL_SCHEMA_HINT = """{"items": [{"name": "nome da teoria/framework",
           "tradition": "tradição/campo",
           "definition": "1 frase: o que a teoria diz",
           "source_refs": ["p.N/Lnn"]}]}"""

VERDICT_SCHEMA_HINT = """{"verdicts": [{"item_id": "T1",
              "verdict": "uses | discusses | does_not_use",
              "source_refs": ["p.N/Lnn"],
              "note": "opcional"}]}"""


def build_pool(
    article_id: str,
    round_: int,
    model: str,
    prompt_version: str,
    temperature: float = 0.2,
    force: bool = False,
    overwrite: bool = False,
) -> CandidatePool | None:
    out = paths.pool_path(round_, article_id)
    if out.exists() and not overwrite:
        print(f"{article_id}: pool exists, skipping (use --overwrite)")
        return None

    manifest, problems = check_gate(article_id)
    if manifest is None or (problems and not force):
        for p in problems:
            print(f"{article_id}: GATE — {p}")
        return None

    md = (paths.ROOT / manifest.md_path).read_text()
    tpl = paths.prompt_path(prompt_version).read_text()
    prompt = tpl.format(schema_hint=POOL_SCHEMA_HINT, document=md)
    data, meta = _call_model(model, prompt, temperature)

    items = [
        CandidateItem(
            item_id=f"T{i}",
            name=it["name"],
            tradition=it.get("tradition", ""),
            definition=it.get("definition", ""),
            source_refs=it.get("source_refs", []),
        )
        for i, it in enumerate(data.get("items", []), 1)
    ]
    pool = CandidatePool(
        article_id=article_id,
        round=round_,  # type: ignore[arg-type]
        generated_by=PoolGenerator(
            provider=model.split("/")[0] if "/" in model else "openai",
            model=model,
            prompt_version=prompt_version,
            at=datetime.now(timezone.utc),
            md_sha256=manifest.md_sha256,
        ),
        items=items,
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(pool.model_dump_json(indent=2))
    write_student_sheet(round_, article_id, pool)
    print(f"{article_id}: pool com {len(items)} candidatos → {out.name}")
    return pool


def write_student_sheet(round_: int, article_id: str, pool: CandidatePool) -> None:
    lines = [
        f"# Pool de teorias — {article_id}",
        "",
        "Para cada teoria candidata, marque UMA opção e, se possível, cite a",
        "página/linha que sustenta seu julgamento (p.N ou p.N/Lnn):",
        "",
        "- **usa** — a teoria estrutura o argumento/modelo do artigo",
        "- **discute** — é debatida/citada substantivamente, sem estruturar",
        "- **não usa** — ausente ou apenas menção decorativa",
        "",
    ]
    for it in pool.items:
        if not it.active:
            continue
        lines += [
            f"## {it.item_id} — {it.name}" + (f" ({it.tradition})" if it.tradition else ""),
            f"_{it.definition}_" if it.definition else "",
            "- [ ] usa   - [ ] discute   - [ ] não usa",
            "- evidência: ______   nota: ______",
            "",
        ]
    lines += [
        "## Faltou alguma teoria?",
        "Liste abaixo teorias que o artigo usa/discute e NÃO estão no pool",
        "(vão no campo `theories` do seu fichamento):",
        "",
        "- ...",
    ]
    paths.pool_sheet_path(round_, article_id).write_text("\n".join(lines))


def load_pool(round_: int, article_id: str) -> CandidatePool | None:
    p = paths.pool_path(round_, article_id)
    if not p.exists():
        return None
    return CandidatePool.model_validate_json(p.read_text())


def build_round(round_: int, model: str, prompt_version: str,
                temperature: float = 0.2, force: bool = False,
                overwrite: bool = False) -> None:
    for a in load_articles(round_):
        build_pool(a.article_id, round_, model, prompt_version,
                   temperature, force, overwrite)
