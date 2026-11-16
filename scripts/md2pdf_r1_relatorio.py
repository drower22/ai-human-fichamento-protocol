"""Converte o relatório de aprendizagem piloto→R1 em PDF A4.

Uso:  .venv/bin/python scripts/md2pdf_r1_relatorio.py
Gera: data/r1/relatorio-aprendizagem-piloto-r1.pdf
Requer: python-markdown (venv) e google-chrome no PATH.
"""
import markdown, pathlib, subprocess, tempfile, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pdf_style import CSS_FULL

ROOT = pathlib.Path(__file__).resolve().parent.parent

src = ROOT / "data" / "r1" / "relatorio-aprendizagem-piloto-r1.md"
pdf = src.with_suffix(".pdf")
body = markdown.markdown(src.read_text(), extensions=["tables"])
foot = "Protocolo de fichamentos auditáveis · aprendizagem piloto R0 → R1 · gerado 16/11/2026"
html = f"<html><head><meta charset=utf-8><style>{CSS_FULL}</style></head><body>{body}<div class=footer>{foot}</div></body></html>"
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
    f.write(html)
subprocess.run(["google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
                "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f.name],
               check=True, capture_output=True)
print(pdf)
