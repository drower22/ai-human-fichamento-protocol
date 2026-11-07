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
    article_id: str | None,
    content_json: str,
    participant_id: str | None = None,
    elapsed_minutes: int | None = None,
    overwrite: bool = False,
) -> Fichamento | None:
    """Import a human fichamento JSON (template- or HTML-form-generated).

    participant_id / article_id / elapsed_minutes may come from the JSON
    itself; CLI args override. Demographics (full_name, age, gender,
    program) are routed to data/private/participants.csv, never into the
    artifact. Non-corpus article_ids (e.g. PILOTO) land in
    data/piloto/responses/."""
    raw = json.loads(__import__("pathlib").Path(content_json).read_text())
    raw.pop("_LEIA-ME", None)
    raw.pop("consent", None)  # TCLE fica registrado fora do conteúdo avaliável
    article_id = article_id or raw.pop("article_id", None)
    participant_id = participant_id or raw.pop("participant_id", None)
    if elapsed_minutes is None:
        elapsed_minutes = raw.pop("elapsed_minutes", None)
    else:
        raw.pop("elapsed_minutes", None)
    if not article_id or not participant_id:
        raise ValueError("article_id e participant_id são obrigatórios (no JSON ou via CLI)")

    demo = {k: str(raw.pop(k, "") or "") for k in ("full_name", "age", "gender", "program")}
    if any(demo.values()):
        _record_participant(participant_id, demo)

    self_assessment = raw.pop("self_assessment", None)
    reflection_log = raw.pop("reflection_log", None)
    content = FichamentoContent.model_validate(raw)

    if re.fullmatch(r"A\d{2}", article_id) and round_ in (1, 2):
        out = paths.fichamento_path(round_, article_id, "human")
        if out.exists() and not overwrite:
            print(f"{article_id}: human fichamento exists, skipping (--overwrite)")
            return None
        fich = Fichamento(
            fichamento_id=f"F-R{round_}-{article_id}-HUM",
            article_id=article_id,
            round=round_,  # type: ignore[arg-type]
            source="human",
            generator=HumanGenerator(
                participant_id=participant_id,
                elapsed_minutes=elapsed_minutes,
                submitted_at=datetime.now(timezone.utc),
                self_assessment=self_assessment,
                reflection_log=reflection_log,
            ),
            content=content,
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fich.model_dump_json(indent=2))
        print(f"{article_id}: human fichamento imported ({participant_id})")
        return fich

    # pilot / non-corpus: lighter artifact, still content-validated
    payload = {
        "schema_version": "1.0.0",
        "article_id": article_id, "participant_id": participant_id,
        "elapsed_minutes": elapsed_minutes,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "self_assessment": self_assessment,
        "reflection_log": reflection_log,
        "content": content.model_dump(),
    }
    out = paths.DATA / "piloto" / "responses" / f"{participant_id}_{article_id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"{article_id}: fichamento de {participant_id} importado -> {out.relative_to(paths.ROOT)}")
    return None


# ------------------------------------------------- student fichamentos CSV
# One row of the Google Forms export (see protocol/forms/student-form.md)
# becomes one fichamento. Grids export as "title [row]" columns; slot
# fields repeat as "key_concept.{i}.x" / "finding.{i}.x".

import re
from pathlib import Path

_REF_RE = re.compile(
    r"\bp\.\d+(?:-\d+)?(?:[/ ]L\d+(?:-\d+)?)?|\bL\d+(?:-\d+)?")
_VERDICT_COL = re.compile(r"^theory_verdicts \[(.+)\]$")
_SELFASS_COL = re.compile(r"^self_assessment \[(.+)\]$")


def _parse_evidence(text: str) -> tuple[list[str], str]:
    """'(p.5 L165) trecho literal' -> (["p.5 L165"], "trecho literal")."""
    text = (text or "").strip()
    refs = [r.strip() for r in _REF_RE.findall(text)]
    quote = re.sub(r"\s+", " ", _REF_RE.sub("", text)).strip(" ()-—;,")
    return refs, quote


def _norm_role(s: str) -> str:
    s = s.strip().lower()
    return {"usa": "uses", "use": "uses", "uses": "uses",
            "discute": "discusses", "discusses": "discusses",
            "discussão": "discusses"}.get(s, s)


def _int_or_none(s: str):
    s = (s or "").strip()
    return int(s) if s.isdigit() else None


def _record_participant(pid: str, demo: dict[str, str]) -> None:
    """Upsert student demographics into data/private/participants.csv.

    Identity lives ONLY here (gitignored) — never in the fichamento JSON
    that judges read."""
    p = paths.PRIVATE / "participants.csv"
    fields = ["participant_id", "name", "role", "age", "gender", "program", "notes"]
    rows = []
    if p.exists():
        with open(p, encoding="utf-8") as f:
            rows = [{k: (r.get(k) or "") for k in fields} for r in csv.DictReader(f)]
    rows = [r for r in rows if r["participant_id"] != pid]
    rows.append({
        "participant_id": pid, "name": demo.get("full_name", ""),
        "role": "student", "age": demo.get("age", ""),
        "gender": demo.get("gender", ""), "program": demo.get("program", ""),
        "notes": "",
    })
    rows.sort(key=lambda r: r["participant_id"])
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def import_human_csv(
    round_: int,
    csv_path: str,
    map_path: str | None = None,
    pool_path: str | None = None,
) -> list[Path]:
    """Forms CSV -> fichamento JSONs (pilot or corpus rounds).

    `--map` is a canonical->header map; absent keys default to the
    canonical column name itself. `--pool` supplies item names for the
    theory verdicts. Rows whose article_id is not A{nn} (e.g. PILOTO)
    are written to data/piloto/responses/ instead of the corpus dirs.
    """
    cmap = json.loads(Path(map_path).read_text()) if map_path else {}
    pool_names: dict[str, str] = {}
    if pool_path:
        pool = json.loads(Path(pool_path).read_text())
        pool_names = {it["item_id"]: it["name"] for it in pool.get("items", [])}

    outs: list[Path] = []
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        get = lambda name: (row.get(cmap.get(name, name)) or "").strip()
        pid, art = get("participant_id"), get("article_id")
        if not pid or not art:
            print("linha sem participant_id/article_id — pulada")
            continue

        # --- theories: grid verdicts + per-item evidence ---
        verdicts = []
        for k, v in row.items():
            m = _VERDICT_COL.match(k or "")
            if m and (v or "").strip():
                item_m = re.match(r"([A-Z]\d+)", m.group(1).strip())
                item = item_m.group(1) if item_m else m.group(1).strip()
                refs, quote = _parse_evidence(get(f"{item}.evidence"))
                verdicts.append({
                    "item_id": item,
                    "name": pool_names.get(item, item),
                    "verdict": v.strip(),
                    "source_refs": refs,
                    "quote": quote,
                })
        verdicts.sort(key=lambda d: int(re.sub(r"\D", "", d["item_id"]) or 0))

        extra = []
        for line in get("extra_theories").splitlines():
            parts = [p.strip() for p in re.split(r"[—;]", line) if p.strip()]
            if not parts:
                continue
            refs, _ = _parse_evidence(line)
            extra.append({
                "name": parts[0],
                "tradition": parts[1] if len(parts) > 1 else "",
                "role": _norm_role(parts[2]) if len(parts) > 2 else "",
                "source_refs": refs,
            })

        concepts = []
        for i in range(1, 5):
            c = get(f"key_concept.{i}.concept")
            if c:
                refs, quote = _parse_evidence(get(f"key_concept.{i}.evidence"))
                concepts.append({"concept": c,
                                 "definition": get(f"key_concept.{i}.definition"),
                                 "quote": quote, "source_refs": refs})
        findings = []
        for i in range(1, 6):
            fi = get(f"finding.{i}.finding")
            if fi:
                refs, quote = _parse_evidence(get(f"finding.{i}.evidence"))
                findings.append({"finding": fi,
                                 "type": get(f"finding.{i}.type").lower(),
                                 "quote": quote, "source_refs": refs})

        content = {
            "executive_summary": get("executive_summary"),
            "research_question": get("research_question"),
            "theories": extra,
            "theory_verdicts": verdicts,
            "key_concepts": concepts,
            "methodology": {
                "study_type": get("methodology.study_type").lower(),
                "design": get("methodology.design"),
                "sample_type": get("methodology.sample_type"),
                "sample_size": _int_or_none(get("methodology.sample_size")),
                "sector": get("methodology.sector"),
                "period": get("methodology.period"),
                "methods": [m.strip() for m in get("methodology.methods").split(",") if m.strip()],
                "analysis_note": get("methodology.analysis_note"),
                "source_refs": _parse_evidence(get("methodology.source_refs"))[0],
            },
            "main_findings": findings,
            "contribution": {
                "theoretical": get("contribution.theoretical"),
                "practical": get("contribution.practical"),
            },
        }

        self_assessment = None
        sa = {m.group(1).strip(): _int_or_none(v)
              for k, v in row.items() if (m := _SELFASS_COL.match(k or ""))}
        if all(v is not None for v in sa.values()) and sa:
            self_assessment = SectionScores(**sa)
        refl = {q: get(f"reflection.{q}") for q in ("q1", "q2", "q3", "q4")}
        refl = {k: v for k, v in refl.items() if v} or None

        demo = {k: get(k) for k in ("full_name", "age", "gender", "program")}
        if any(demo.values()):
            _record_participant(pid, demo)

        try:
            validated = FichamentoContent.model_validate(content)
        except Exception as e:
            print(f"{art} ({pid}): conteúdo inválido, linha pulada —\n{e}\n")
            continue

        if re.fullmatch(r"A\d{2}", art) and round_ in (1, 2):
            fich = Fichamento(
                fichamento_id=f"F-R{round_}-{art}-HUM",
                article_id=art, round=round_, source="human",  # type: ignore[arg-type]
                generator=HumanGenerator(
                    participant_id=pid,
                    elapsed_minutes=_int_or_none(get("elapsed_minutes")),
                    submitted_at=datetime.now(timezone.utc),
                    self_assessment=self_assessment,
                    reflection_log=refl,
                ),
                content=validated,
            )
            out = paths.fichamento_path(round_, art, "human")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fich.model_dump_json(indent=2))
        else:  # pilot / non-corpus article: lighter artifact, still content-validated
            payload = {
                "schema_version": "1.0.0",
                "article_id": art, "participant_id": pid,
                "elapsed_minutes": _int_or_none(get("elapsed_minutes")),
                "submitted_at": datetime.now(timezone.utc).isoformat(),
                "self_assessment": self_assessment.model_dump() if self_assessment else None,
                "reflection_log": refl,
                "content": validated.model_dump(),
            }
            out = paths.DATA / "piloto" / "responses" / f"{pid}_{art}.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
        outs.append(out)
        print(f"{art}: fichamento de {pid} importado -> {out.relative_to(paths.ROOT)}")
    return outs
