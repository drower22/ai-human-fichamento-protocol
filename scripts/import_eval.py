"""Importa avaliacoes recebidas (E-R{round}-{art}-{slug}.json) de
~/Downloads para data/evaluations/roundN/ e regera paginas dos juizes
e painel. Roda a cada avaliacao nova; depois e so commit + deploy.

Uso:  .venv/bin/python scripts/import_eval.py
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DL = Path.home() / "Downloads"
SLUGS = {"nz4f", "bq8w", "mv3r", "gx6t", "teste"}


def main() -> int:
    moved = []
    for f in sorted(DL.glob("E-R*.json")):
        # E-R{round}-{art}-{slug}.json
        parts = f.stem.split("-")
        if len(parts) < 3 or parts[-1] not in SLUGS:
            print(f"ignorado (nome fora do padrao): {f.name}")
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            print(f"ignorado (json invalido): {f.name}")
            continue
        if d.get("kind") != "evaluation":
            print(f"ignorado (nao e avaliacao): {f.name}")
            continue
        rnd = int(parts[0][2:] if parts[0].startswith("E-R") else d.get("round", 0))
        # conferir consistencia nome x conteudo
        if str(d.get("round")) != str(rnd) or d.get("judge_id") != parts[-1]:
            print(f"ignorado (nome != conteudo): {f.name}")
            continue
        dest_dir = DATA / "evaluations" / f"round{rnd}" if rnd else \
            DATA / "piloto" / "evaluations"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / f.name
        if dest.exists():
            print(f"ja existe: {dest.relative_to(ROOT)}")
            f.unlink()
            continue
        shutil.move(str(f), dest)
        moved.append(dest)
        print(f"importado: {dest.relative_to(ROOT)}")

    if moved:
        here = ROOT / ".venv" / "bin" / "python"
        subprocess.run([str(here), "scripts/build_judge_pages.py"], cwd=ROOT)
        subprocess.run([str(here), "scripts/build_painel.py"], cwd=ROOT)
        print("\npaginas + painel regerados; revise, commit e faca deploy.")
    else:
        print("nada novo para importar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
