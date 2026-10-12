"""Blinding: assign A/B positions, emit the private map + judge packets."""

from __future__ import annotations

import json
import random
from datetime import datetime, timezone

from . import paths
from .models import BlindEntry, BlindingMap, Fichamento
from .registry import load_articles
from .render import render_fichamento_md


def _load_fichamento(round_: int, article_id: str, source: str) -> Fichamento:
    p = paths.fichamento_path(round_, article_id, source)
    if not p.exists():
        raise FileNotFoundError(f"missing {source} fichamento for {article_id}: {p}")
    return Fichamento.model_validate_json(p.read_text())


def create_blinding(round_: int, seed: int) -> BlindingMap:
    articles = load_articles(round_)
    rng = random.Random(f"{seed}-R{round_}")

    entries: list[BlindEntry] = []
    packets: list[tuple[str, dict[str, Fichamento]]] = []
    counter = 1
    for art in sorted(articles, key=lambda a: a.article_id):
        pair = {
            src: _load_fichamento(round_, art.article_id, src)
            for src in ("ai", "human")
        }
        order = ["ai", "human"]
        rng.shuffle(order)
        by_pos = {"A": order[0], "B": order[1]}
        packets.append((art.article_id, {"A": pair[by_pos["A"]], "B": pair[by_pos["B"]]}))
        for pos in ("A", "B"):
            src = by_pos[pos]
            entries.append(
                BlindEntry(
                    blind_id=f"B{counter:02d}",
                    article_id=art.article_id,
                    fichamento_id=pair[src].fichamento_id,
                    source=src,  # type: ignore[arg-type]
                    position=pos,  # type: ignore[arg-type]
                )
            )
            counter += 1

    bmap = BlindingMap(
        round=round_,  # type: ignore[arg-type]
        seed=seed,
        created_at=datetime.now(timezone.utc),
        entries=entries,
    )
    paths.PRIVATE.mkdir(parents=True, exist_ok=True)
    paths.blindmap_path(round_).write_text(bmap.model_dump_json(indent=2))

    # Nominator-only evaluation: each judge receives packets only for the
    # articles HE nominated -> judge-packets/roundN/J{k}/A{nn}.md
    nominated = {a.article_id: a.nominated_by for a in articles}
    out_dir = paths.packets_dir(round_)
    for article_id, pair in packets:
        judge = nominated[article_id]
        jdir = out_dir / judge
        jdir.mkdir(parents=True, exist_ok=True)
        md = [
            f"# Artigo {article_id} — avaliação às cegas",
            "",
            "Dois fichamentos independentes deste artigo. Avalie-os contra o",
            "artigo original usando a rubrica BARS 1–7 (protocol/rubric.md).",
            "",
            "---",
            "",
            "# Fichamento A",
            "",
            render_fichamento_md(pair["A"]),
            "",
            "---",
            "",
            "# Fichamento B",
            "",
            render_fichamento_md(pair["B"]),
            "",
        ]
        (jdir / f"{article_id}.md").write_text("\n".join(md))
    index = ["judge_id,article_id,packet_file,blind_A,blind_B"]
    for article_id, _ in packets:
        judge = nominated[article_id]
        bA = next(e.blind_id for e in entries if e.article_id == article_id and e.position == "A")
        bB = next(e.blind_id for e in entries if e.article_id == article_id and e.position == "B")
        index.append(f"{judge},{article_id},{judge}/{article_id}.md,{bA},{bB}")
    (out_dir / "index.csv").write_text("\n".join(sorted(index)) + "\n")

    print(
        f"round {round_}: {len(entries)} fichamentos cegados → "
        f"{paths.blindmap_path(round_)} (PRIVADO) + pacotes em {out_dir}"
    )
    return bmap


def load_blindmap(round_: int) -> BlindingMap:
    p = paths.blindmap_path(round_)
    if not p.exists():
        raise FileNotFoundError(
            f"{p} not found — run `fichamento blind --round {round_}` first"
        )
    return BlindingMap.model_validate_json(p.read_text())


def resolve(round_: int, blind_id: str) -> BlindEntry:
    for e in load_blindmap(round_).entries:
        if e.blind_id == blind_id:
            return e
    raise KeyError(f"blind_id {blind_id} not in round {round_} map")


def position_to_blind(round_: int, article_id: str, position: str) -> str:
    for e in load_blindmap(round_).entries:
        if e.article_id == article_id and e.position == position:
            return e.blind_id
    raise KeyError(f"{article_id} position {position} not in round {round_} map")


def load_all_fichamentos(round_: int, source: str) -> list[Fichamento]:
    out = []
    for p in sorted(paths.fichamento_dir(round_, source).glob("*.json")):
        out.append(Fichamento.model_validate_json(p.read_text()))
    return out
