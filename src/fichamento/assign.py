"""Seeded, crossed assignment of articles to students.

Design (see protocol/PROTOCOL.md §3): the judge who NOMINATES an article
never has it fichado by his own group — nominations cross to another
group (`cross` map in groups.json, chosen by closest area). The
coordinator (non-judge) runs the draw; the article↔student table stays
private until unblinding.

groups.json lives in data/private/ (template: protocol/forms/groups-template.json).
"""

from __future__ import annotations

import json
import random
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, Field

from . import paths
from .models import SCHEMA_VERSION
from .registry import load_articles


class StudentGroup(BaseModel):
    group_id: str
    advisor_id: str = Field(pattern=r"^J[1-4]$")
    students: list[str] = Field(min_length=1)


class GroupsFile(BaseModel):
    groups: list[StudentGroup]
    cross: dict[str, str]          # advisor_id -> receiving group_id


class AssignmentEntry(BaseModel):
    article_id: str
    student_id: str
    group_id: str
    nominated_by: str


class AssignmentMap(BaseModel):
    schema_version: str = SCHEMA_VERSION
    round: int
    seed: int
    created_at: datetime
    entries: list[AssignmentEntry]


def assignments_path(round_: int) -> Path:
    return paths.PRIVATE / f"assignments-round{round_}.json"


def assign(round_: int, seed: int, groups_file: str | None = None) -> AssignmentMap:
    gf_path = Path(groups_file) if groups_file else paths.PRIVATE / "groups.json"
    if not gf_path.exists():
        raise FileNotFoundError(
            f"{gf_path} not found — copy protocol/forms/groups-template.json "
            "to data/private/groups.json and fill in your groups"
        )
    gf = GroupsFile.model_validate_json(gf_path.read_text())
    groups = {g.group_id: g for g in gf.groups}

    by_judge: dict[str, list[str]] = {}
    for a in load_articles(round_):
        by_judge.setdefault(a.nominated_by, []).append(a.article_id)

    rng = random.Random(f"{seed}-assign-R{round_}")
    entries: list[AssignmentEntry] = []
    for judge, art_ids in sorted(by_judge.items()):
        gid = gf.cross.get(judge)
        if not gid or gid not in groups:
            raise ValueError(f"cross map missing/unknown target for {judge}")
        g = groups[gid]
        if g.advisor_id == judge:
            raise ValueError(
                f"cross map sends {judge}'s articles to his own group {gid} "
                "— that defeats blinding; choose another group"
            )
        arts = sorted(art_ids)
        rng.shuffle(arts)
        students = list(g.students)
        rng.shuffle(students)
        for i, aid in enumerate(arts):
            entries.append(
                AssignmentEntry(
                    article_id=aid,
                    student_id=students[i % len(students)],
                    group_id=gid,
                    nominated_by=judge,
                )
            )

    amap = AssignmentMap(
        round=round_, seed=seed,
        created_at=datetime.now(timezone.utc),
        entries=sorted(entries, key=lambda e: e.article_id),
    )
    out = assignments_path(round_)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(amap.model_dump_json(indent=2))

    per_student: dict[str, list[str]] = {}
    for e in amap.entries:
        per_student.setdefault(e.student_id, []).append(e.article_id)
    for sid in sorted(per_student):
        print(f"  {sid}: {', '.join(sorted(per_student[sid]))}")
    print(f"assignments → {out} (PRIVADO; publicar só após descegamento)")
    return amap
