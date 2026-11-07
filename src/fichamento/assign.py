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
    mode: str = "groups"


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


def assign_per_student(
    round_: int, seed: int, groups_file: str | None = None
) -> AssignmentMap:
    """Um artigo por estudante; única regra: ninguém ficha artigo indicado
    pelo próprio orientador. Emparelha listas embaralhadas (rejection
    sampling: repete se algum par violar a regra — sorteio uniforme).
    """
    gf_path = Path(groups_file) if groups_file else paths.PRIVATE / "groups.json"
    gf = GroupsFile.model_validate_json(gf_path.read_text())
    advisor_of = {sid: g.advisor_id for g in gf.groups for sid in g.students}
    group_of = {sid: g.group_id for g in gf.groups for sid in g.students}

    articles = load_articles(round_)
    nominated = {a.article_id: a.nominated_by for a in articles}
    rng = random.Random(f"{seed}-assign-R{round_}-perstudent")
    students = sorted(advisor_of)
    if len(students) < len(articles):
        raise ValueError(
            f"{len(articles)} artigos para {len(students)} estudantes "
            "— sorteio 1:1 exige estudantes >= artigos"
        )
    attempts = 0
    while True:
        attempts += 1
        if attempts > 10000:
            raise RuntimeError("sorteio não convergiu — restrições fortes demais?")
        arts = [a.article_id for a in articles]
        rng.shuffle(arts)
        studs = list(students)
        rng.shuffle(studs)
        pairs = list(zip(studs[: len(arts)], arts))
        if all(nominated[aid] != advisor_of[sid] for sid, aid in pairs):
            break
    amap = AssignmentMap(
        round=round_, seed=seed,
        created_at=datetime.now(timezone.utc),
        entries=sorted(
            (
                AssignmentEntry(
                    article_id=aid,
                    student_id=sid,
                    group_id=group_of[sid],
                    nominated_by=nominated[aid],
                )
                for sid, aid in pairs
            ),
            key=lambda e: e.article_id,
        ),
        mode="per-student",
    )
    out = assignments_path(round_)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(amap.model_dump_json(indent=2))
    print(f"  (tentativas até sorteio válido: {attempts})")
    for e in amap.entries:
        print(f"  {e.student_id} ({e.group_id}) ← {e.article_id} ({e.nominated_by})")
    print(f"assignments → {out} (PRIVADO; publicar só após descegamento)")
    return amap
