"""Monta os pares cegos A/B da R1 em site/juizes/pairs/A{nn}-{slug}.json.

- Um arquivo por juiz×artigo, como no piloto (PILOTO-{slug}.json): o form
  busca pairs/{art}-{slug}.json primeiro — cada link ?j={slug}&a={art}
  só carrega o par daquele juiz.
- Orientação A/B balanceada por juiz: dos 4 artigos de cada juiz, 2 têm
  o fichamento humano no lado A e 2 no lado B (seed registrada no mapa
  privado — nunca no site).
- Lado humano: content de data/fichamentos/round1/human/F-R1-Axx-HUM.json;
  se o fichamento ainda não passou na validação de source_refs, usa o
  JSON bruto recebido (~/Downloads/S##_A##.json) e marca no mapa privado
  como "pending_validation" — o juiz nunca vê essa marcação.
- Lado IA: content de data/fichamentos/round1/ai/F-R1-Axx-AI.json.
- Só as 8 chaves de conteúdo vão ao par: nada de participant_id,
  generator, elapsed_minutes, self_assessment ou reflection_log.

Mapa privado: data/private/pair-map-round1.json (quem está em A e em B).

Juízes (slug do link pessoal — o J# nunca aparece em arquivo ou tela).

Uso:  .venv/bin/python scripts/build_pairs_r1.py
"""
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
DL = Path.home() / "Downloads"

SEED = 20261117
JUDGE_SLUG = {"J1": "nz4f", "J2": "bq8w", "J3": "mv3r", "J4": "gx6t"}
CONTENT_KEYS = ("executive_summary", "research_question", "theories",
                "theory_verdicts", "key_concepts", "methodology",
                "main_findings", "contribution")


def content_only(d: dict) -> dict:
    return {k: d.get(k) for k in CONTENT_KEYS}


def human_content(art: str) -> tuple[dict, str, str]:
    """Retorna (content, student_id, origem)."""
    p = DATA / "fichamentos" / "round1" / "human" / f"F-R1-{art}-HUM.json"
    if p.exists():
        d = json.loads(p.read_text())
        sid = (d.get("generator") or {}).get("participant_id", "?")
        return content_only(d["content"]), sid, "validated"
    raws = sorted(DL.glob(f"S*_{art}.json"))
    if not raws:
        raise FileNotFoundError(f"sem fichamento humano para {art}")
    d = json.loads(raws[0].read_text())
    return content_only(d), d.get("participant_id", "?"), "pending_validation"


def ai_content(art: str) -> dict:
    d = json.loads(
        (DATA / "fichamentos" / "round1" / "ai" / f"F-R1-{art}-AI.json").read_text())
    return content_only(d["content"])


def build() -> None:
    arts = [json.loads(l) for l in
            (DATA / "articles" / "registry.jsonl").read_text().splitlines()
            if l.strip() and json.loads(l)["round"] == 1]
    arts.sort(key=lambda a: a["article_id"])

    rng = random.Random(SEED)
    # orientação balanceada por juiz: [humano em A, humano em A, IA em A, IA em A]
    side_by_art: dict[str, str] = {}
    by_judge: dict[str, list[str]] = {}
    for a in arts:
        by_judge.setdefault(a["nominated_by"], []).append(a["article_id"])
    for j, ids in by_judge.items():
        ids.sort()
        flags = ["H", "H", "I", "I"]  # H = humano no lado A
        rng.shuffle(flags)
        side_by_art.update(dict(zip(ids, flags)))

    outdir = SITE / "juizes" / "pairs"
    outdir.mkdir(parents=True, exist_ok=True)
    entries = []
    for a in arts:
        art = a["article_id"]
        hum, sid, origin = human_content(art)
        ai = ai_content(art)
        human_on_a = side_by_art[art] == "H"
        pair = {
            "demo": False,
            "article_id": art,
            "round": 1,
            "title": a["title"],
            "authors": ", ".join(a.get("authors") or []),
            "year": a.get("year"),
            "venue": a.get("venue", ""),
            "A": hum if human_on_a else ai,
            "B": ai if human_on_a else hum,
        }
        slug = JUDGE_SLUG[a["nominated_by"]]
        blob = json.dumps(pair, ensure_ascii=False, indent=1)
        # guarda anti-vazamento: identificadores nunca podem entrar no par
        for bad in ("participant_id", "full_name", "generator", "elapsed_minutes",
                    "self_assessment", "reflection_log", "claude", "openai",
                    "S0", "S1"):
            assert bad not in blob, f"{art}: '{bad}' vazou no par"
        (outdir / f"{art}-{slug}.json").write_text(blob + "\n")
        entries.append({
            "article_id": art,
            "nominated_by": a["nominated_by"],
            "pair_file": f"{art}-{slug}.json",
            "A": "human" if human_on_a else "ai",
            "B": "ai" if human_on_a else "human",
            "human_student": sid,
            "human_source": origin,
        })
        print(f"{art}-{slug} [{a['nominated_by']}] "
              f"A={'HUM' if human_on_a else 'IA '} "
              f"B={'IA ' if human_on_a else 'HUM'} humano={sid} ({origin})")

    mp = DATA / "private" / "pair-map-round1.json"
    mp.write_text(json.dumps({
        "seed": SEED,
        "rule": "orientação A/B balanceada por juiz (2 humano-A + 2 humano-B, "
                "random.Random(seed).shuffle); arquivo único por artigo pois "
                "cada artigo da R1 tem um único juiz",
        "note": "human_source=pending_validation: fichamento bruto que ainda "
                "não passou no gate de source_refs; entrou no par assim mesmo "
                "(faz parte do dado — o juiz não vê a marcação)",
        "pairs": entries,
    }, ensure_ascii=False, indent=1) + "\n")
    print(f"\n{len(entries)} pares -> {outdir}")
    print(f"mapa privado -> {mp}")


if __name__ == "__main__":
    build()
