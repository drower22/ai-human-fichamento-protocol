#!/usr/bin/env python3
"""Gera os fichamentos da R2 via API (Claude), em paralelo aos assistidos.

generate_article() grava em data/fichamentos/round2/ai/ — este script move
cada saída para data/fichamentos/round2/ai-api/F-R2-Axx-AI.json, mantendo
os fichamentos assistidos (SWE-2) intactos e separados para comparação.

Depois de rodar, reconstroi os assistidos com:
  for a in A17..A32: scripts/build_ai_fichamento.py $a --round 2
E verifica os da API com:
  scripts/verify_fichamento.py $a --round 2 --source ai-api

Uso: scripts/generate_r2_api.py [A17 A18 ...]
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fichamento import paths  # noqa: E402
from fichamento.generate import generate_article  # noqa: E402

MODEL = sys.argv[1] if len(sys.argv) > 1 and "/" in sys.argv[1] \
    else "anthropic/claude-sonnet-5-5"
PROMPT = "1.1.0-calibrated"
VERDICTS = "1.1.0-theory-verdicts"
ARTS = [a for a in sys.argv[1:] if a.startswith("A")] or \
    [f"A{n:02d}" for n in range(17, 33)]

out_dir = paths.DATA / "fichamentos" / "round2" / "ai-api"
out_dir.mkdir(parents=True, exist_ok=True)

for art in ARTS:
    std = paths.fichamento_path(2, art, "ai")
    f = None
    for attempt in range(3):
        try:
            f = generate_article(
                art, 2, MODEL, PROMPT, temperature=1.0,  # único valor suportado pelo sonnet-5-5
                verdicts_version=VERDICTS,
                force=(art == "A32"),  # OCR needs_review — override registrado
                overwrite=True,
            )
            break
        except Exception as e:
            if attempt == 2:
                print(f"{art}: FALHOU — {type(e).__name__}: {e}")
            else:
                print(f"{art}: retry {attempt + 1} após {type(e).__name__}")
    if f is None:
        print(f"{art}: não gerado (ver mensagens acima)")
        continue
    if f is None:
        print(f"{art}: não gerado (ver mensagens acima)")
        continue
    dest = out_dir / std.name
    shutil.move(str(std), dest)
    print(f"{art}: -> {dest.relative_to(paths.ROOT)}")
