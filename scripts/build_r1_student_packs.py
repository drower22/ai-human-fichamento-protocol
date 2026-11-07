#!/usr/bin/env python3
"""Build R1 student packs: candidate pools, private gabarito, per-student
JSONs for the personalized-link form, and the private link map.

Inputs (private):
  data/private/r1-pool-build.json      item defs + verdicts + planted flags
  data/private/assignments-round1.json student_id -> article_id (per-student draw)
  data/private/participants.csv        S-code -> real name
Inputs (tracked):
  data/articles/registry.jsonl         article metadata (title/authors/year/venue)
  data/articles/manifests/*.json       md_sha256 provenance

Outputs:
  data/candidates/round1/A{nn}.candidates.json   public pool (no verdicts)
  data/private/theory-gabarito-round1.json       verdicts + planted + refs (PRIVATE)
  site/r1/students/{token}.json                  per-student pack served by the form
  site/r1/students/teste.json                    demo pack (?s=teste)
  data/private/student-links-round1.json         token -> student -> article -> URL
"""

from __future__ import annotations

import csv
import json
import random
import string
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PRIV = DATA / "private"
SITE_R1 = ROOT / "site" / "r1"
BASE_URL = "https://ai-human-fichamento-protocol-site.vercel.app"
TOKEN_ALPHABET = "abcdefghjkmnpqrstuvwxyz23456789"  # sem 0/o/1/l/i — evita erro de digitação
SEED = 20261107


def load() -> tuple[dict, dict, dict, dict]:
    build = json.loads((PRIV / "r1-pool-build.json").read_text())
    assign = json.loads((PRIV / "assignments-round1.json").read_text())
    people = {
        r["participant_id"]: r
        for r in csv.DictReader((PRIV / "participants.csv").read_text().splitlines())
    }
    registry = {}
    for line in (DATA / "articles" / "registry.jsonl").read_text().splitlines():
        if line.strip():
            e = json.loads(line)
            registry[e["article_id"]] = e
    return build, assign, people, registry


def md_sha(article_id: str) -> str:
    p = DATA / "articles" / "manifests" / f"{article_id}.ingestion.json"
    return json.loads(p.read_text())["md_sha256"] if p.exists() else ""


def authors_str(entry: dict) -> str:
    return "; ".join(entry.get("authors", []))


def main() -> None:
    build, assign, people, registry = load()
    rng = random.Random(SEED)
    now = datetime.now(timezone.utc).isoformat()

    cand_dir = DATA / "candidates" / "round1"
    cand_dir.mkdir(parents=True, exist_ok=True)
    students_dir = SITE_R1 / "students"
    students_dir.mkdir(parents=True, exist_ok=True)

    gabarito = {
        "schema_version": "1.0.0",
        "round": 1,
        "description": "Gabarito privado dos pools de teorias da R1. NÃO distribuir — "
        "contém vereditos de referência e flags 'planted'. Fonte: leitura integral "
        "assistida por IA (data/articles/theory-extraction/), revisão humana pendente.",
        "created_at": now,
        "articles": {},
    }

    pools: dict[str, list[dict]] = {}
    for art, spec in sorted(build["articles"].items()):
        items_out, gab_items, pool_items = [], [], []
        for i, it in enumerate(spec["items"], 1):
            tid = f"T{i}"
            items_out.append(
                {
                    "item_id": tid,
                    "kind": "theory",
                    "name": it["n"],
                    "definition": it["df"],
                    "tradition": it["tr"],
                    "origin": "ai",
                    "source_refs": [],
                    "active": True,
                }
            )
            gab_items.append(
                {
                    "item_id": tid,
                    "name": it["n"],
                    "verdict": it["v"],
                    "planted": bool(it.get("planted")),
                    "source_refs": [x.strip() for x in it["r"].split(";") if x.strip()],
                    "quote": it.get("q", ""),
                    "note": it.get("note", ""),
                }
            )
            pool_items.append({"item_id": tid, "name": it["n"], "authors": it["a"]})
        pool = {
            "schema_version": "1.0.0",
            "article_id": art,
            "round": 1,
            "kind": "theory",
            "generated_by": {
                "provider": "devin",
                "model": "swe-2-high (leitura integral assistida; ver theory-extraction/)",
                "prompt_version": "n/a",
                "at": now,
                "md_sha256": md_sha(art),
            },
            "items": items_out,
            "curated": False,
            "curated_by": "",
            "notes": "Pool R1 construído da extração de teorias (leitura integral) + "
            "itens plausíveis-ausentes no padrão do piloto. Vereditos NÃO constam "
            "aqui — estão no gabarito privado. Curadoria humana pendente.",
        }
        (cand_dir / f"{art}.candidates.json").write_text(
            json.dumps(pool, indent=2, ensure_ascii=False)
        )
        gabarito["articles"][art] = {"items": gab_items}
        pools[art] = pool_items

    (PRIV / "theory-gabarito-round1.json").write_text(
        json.dumps(gabarito, indent=2, ensure_ascii=False)
    )

    # per-student packs + link map
    tokens: set[str] = set()
    def new_token() -> str:
        while True:
            t = "".join(rng.choice(TOKEN_ALPHABET) for _ in range(5))
            if t not in tokens:
                tokens.add(t)
                return t

    links = {
        "schema_version": "1.0.0",
        "round": 1,
        "created_at": now,
        "base_url": BASE_URL,
        "note": "PRIVADO — mapa de links pessoais R1. Cada estudante recebe por "
        "e-mail o seu link + o PDF numerado do SEU artigo.",
        "students": [],
    }
    for ent in sorted(assign["entries"], key=lambda e: e["student_id"]):
        sid, art = ent["student_id"], ent["article_id"]
        reg = registry[art]
        person = people.get(sid, {})
        tok = new_token()
        pack = {
            "participant_id": sid,
            "article_id": art,
            "round": 1,
            "title": reg["title"],
            "authors": authors_str(reg),
            "year": reg.get("year"),
            "venue": reg.get("venue", ""),
            "full_name": person.get("name", ""),
            "age": person.get("age", ""),
            "gender": person.get("gender", ""),
            "program": person.get("program", ""),
            "pool": pools[art],
        }
        (students_dir / f"{tok}.json").write_text(
            json.dumps(pack, indent=2, ensure_ascii=False)
        )
        links["students"].append(
            {
                "participant_id": sid,
                "name": person.get("name", "?"),
                "article_id": art,
                "token": tok,
                "url": f"{BASE_URL}/r1/?s={tok}",
                "numbered_pdf": f"data/articles/pdfs/{art}-numerado.pdf",
            }
        )

    # demo pack para teste local/publicado (?s=teste)
    demo = {
        "participant_id": "S00",
        "article_id": "PILOTO",
        "round": 0,
        "demo": True,
        "title": "MODO TESTE — artigo-piloto (não conta no estudo)",
        "authors": "Souza, C. M. L.",
        "year": 2011,
        "venue": "RAC 15(5)",
        "pool": [
            {"item_id": "T1", "name": "Teoria A (exemplo)", "authors": "Autor X"},
            {"item_id": "T2", "name": "Teoria B (exemplo)", "authors": "Autor Y"},
            {"item_id": "T3", "name": "Teoria C (exemplo)", "authors": "Autor Z"},
        ],
    }
    (students_dir / "teste.json").write_text(
        json.dumps(demo, indent=2, ensure_ascii=False)
    )

    (PRIV / "student-links-round1.json").write_text(
        json.dumps(links, indent=2, ensure_ascii=False)
    )

    n_items = sum(len(v["items"]) for v in build["articles"].values())
    n_planted = sum(
        1
        for v in build["articles"].values()
        for it in v["items"]
        if it.get("planted")
    )
    print(f"pools: {len(pools)} artigos, {n_items} itens ({n_planted} planted)")
    print(f"student packs: {len(links['students'])} + teste.json -> {students_dir}")
    print(f"gabarito + links -> {PRIV}")


if __name__ == "__main__":
    sys.exit(main())
