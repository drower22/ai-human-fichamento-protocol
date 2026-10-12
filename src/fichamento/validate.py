"""Validate every JSON artefact in data/ against the pydantic contracts.

Exit code 1 on any failure — wired into CI (.github/workflows/validate.yml).
"""

from __future__ import annotations

import json
import sys

from pydantic import ValidationError

from . import paths
from .models import ArticleEntry, BlindingMap, Evaluation, Fichamento, IngestionManifest


def validate_all() -> int:
    errors: list[str] = []
    checked = 0

    def _check(path, model) -> object | None:
        nonlocal checked
        checked += 1
        try:
            return model.model_validate_json(path.read_text())
        except (ValidationError, json.JSONDecodeError) as e:
            errors.append(f"{path.relative_to(paths.ROOT)}: {e}")
            return None

    if paths.REGISTRY.exists():
        for i, line in enumerate(paths.REGISTRY.read_text().splitlines(), 1):
            if not line.strip():
                continue
            checked += 1
            try:
                ArticleEntry.model_validate(json.loads(line))
            except ValidationError as e:
                errors.append(f"registry.jsonl:{i}: {e}")

    manifests = {}
    for p in sorted(paths.ARTICLES.glob("manifests/*.json")):
        m = _check(p, IngestionManifest)
        if m:
            manifests[m.article_id] = m

    fichamentos: dict[str, Fichamento] = {}
    for p in sorted(paths.DATA.glob("fichamentos/round*/*/*.json")):
        f = _check(p, Fichamento)
        if f:
            fichamentos[f.fichamento_id] = f
            src_dir = "ai" if f.source == "ai" else "human"
            if f"/{src_dir}/" not in str(p):
                errors.append(f"{p.name}: file in wrong source dir")

    evals = []
    for p in sorted(paths.DATA.glob("evaluations/round*/*.json")):
        e = _check(p, Evaluation)
        if e:
            evals.append(e)

    bmaps = {}
    for p in sorted(paths.PRIVATE.glob("blinding-map-round*.json")):
        b = _check(p, BlindingMap)
        if b:
            bmaps[b.round] = b

    # cross-checks: evaluations must resolve against the blind map
    for ev in evals:
        bm = bmaps.get(ev.round)
        if not bm:
            errors.append(f"{ev.evaluation_id}: no blinding map for round")
            continue
        by_id = {e.blind_id: e for e in bm.entries}
        for r in ev.ratings:
            ent = by_id.get(r.blind_id)
            if not ent:
                errors.append(f"{ev.evaluation_id}: unknown blind_id {r.blind_id}")
            elif ent.article_id != ev.article_id:
                errors.append(
                    f"{ev.evaluation_id}: blind_id {r.blind_id} belongs to "
                    f"{ent.article_id}, not {ev.article_id}"
                )
            elif ent.fichamento_id not in fichamentos:
                errors.append(
                    f"{ev.evaluation_id}: fichamento {ent.fichamento_id} missing"
                )

    for e in errors:
        print(f"INVALID: {e}")
    print(f"validated {checked} artefact(s): {len(errors)} error(s)")
    return 1 if errors else 0


def main() -> None:
    sys.exit(validate_all())
