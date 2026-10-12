"""Ingestion of judge evaluations (Google Forms CSV) and human fichamentos.

Forms CSV -> Evaluation JSONs. Column names are defined by
protocol/forms/column-map.json so the Forms export maps 1:1 to the schema.

Human fichamentos: students fill protocol/forms/student-fichamento-template.json
(content fields only); `import_human` wraps it with generator metadata and
validates the full Fichamento.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone

from . import paths
from .blind import load_blindmap, position_to_blind
from .models import (
    ErrorFlag,
    Evaluation,
    Fichamento,
    FichamentoContent,
    HumanGenerator,
    Preference,
    Rating,
    SectionScores,
)

MULTI_SEPARATORS = [";", "|"]


def _split_multi(cell: str) -> list[str]:
    cell = (cell or "").strip()
    if not cell or cell.lower() in ("none", "nan", "nenhum", "nenhuma"):
        return []
    for sep in MULTI_SEPARATORS:
        if sep in cell:
            return [x.strip() for x in cell.split(sep) if x.strip()]
    # Google Forms multi-select often exports "a, b"
    return [x.strip() for x in cell.split(",") if x.strip()]


def _int(cell: str) -> int | None:
    cell = (cell or "").strip()
    return int(cell) if cell.isdigit() else None


def ingest_forms_csv(round_: int, csv_path: str, map_path: str | None = None) -> int:
    colmap = json.loads(
        __import__("pathlib").Path(
            map_path or paths.PROTOCOL_FORMS / "column-map.json"
        ).read_text()
    )
    bmap = load_blindmap(round_)

    with open(csv_path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))

    n_ok = 0
    for i, row in enumerate(rows, 1):
        try:
            judge = row[colmap["judge_id"]].strip()
            article = row[colmap["article_id"]].strip()
            ratings: list[Rating] = []
            for pos in ("A", "B"):
                pm = colmap["per_position"][pos]
                scores = SectionScores(
                    **{s: _int(row[pm[f"score.{s}"]]) for s in [
                        "executive_summary", "research_question", "theories",
                        "key_concepts", "methodology", "main_findings",
                        "contribution",
                    ]}
                )
                err_codes = [
                    c for c in _split_multi(row.get(pm["errors"], ""))
                    if c != "none"
                ]
                err_sections = _split_multi(row.get(pm["error_sections"], ""))
                note = row.get(pm["error_note"], "").strip()
                errors = [
                    ErrorFlag(code=c, sections=err_sections, note=note)
                    for c in err_codes
                ]
                ratings.append(
                    Rating(
                        blind_id=position_to_blind(round_, article, pos),
                        position=pos,  # type: ignore[arg-type]
                        scores=scores,
                        errors=errors,
                        would_question=row.get(pm["would_question"], "").strip(),
                        missing=row.get(pm["missing"], "").strip(),
                    )
                )
            ev = Evaluation(
                evaluation_id=f"E-R{round_}-{article}-{judge}",
                round=round_,  # type: ignore[arg-type]
                article_id=article,
                judge_id=judge,
                confidence=_int(row.get(colmap["confidence"], "")),
                ratings=ratings,
                preference=Preference(
                    choice=row[colmap["preference"]].strip(),  # type: ignore[arg-type]
                    reason=row.get(colmap["preference_reason"], "").strip(),
                ),
                submitted_at=None,
            )
            out = paths.eval_path(round_, article, judge)
            if out.exists():
                print(f"row {i}: {ev.evaluation_id} already exists — skipped")
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(ev.model_dump_json(indent=2))
            n_ok += 1
        except Exception as e:
            print(f"row {i}: FAILED — {e}")
    print(f"{n_ok}/{len(rows)} evaluations ingested for round {round_}")
    return n_ok


def import_human(
    round_: int,
    article_id: str,
    content_json: str,
    participant_id: str,
    elapsed_minutes: int | None = None,
    overwrite: bool = False,
) -> Fichamento | None:
    out = paths.fichamento_path(round_, article_id, "human")
    if out.exists() and not overwrite:
        print(f"{article_id}: human fichamento exists, skipping (--overwrite)")
        return None
    content = FichamentoContent.model_validate_json(
        __import__("pathlib").Path(content_json).read_text()
    )
    fich = Fichamento(
        fichamento_id=f"F-R{round_}-{article_id}-HUM",
        article_id=article_id,
        round=round_,  # type: ignore[arg-type]
        source="human",
        generator=HumanGenerator(
            participant_id=participant_id,
            elapsed_minutes=elapsed_minutes,
            submitted_at=datetime.now(timezone.utc),
        ),
        content=content,
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(fich.model_dump_json(indent=2))
    print(f"{article_id}: human fichamento imported ({participant_id})")
    return fich
