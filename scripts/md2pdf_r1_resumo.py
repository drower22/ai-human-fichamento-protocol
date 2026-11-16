"""Converte o resumo pós-piloto/R1 (1 página) em PDF A4.

Uso:  .venv/bin/python scripts/md2pdf_r1_resumo.py
Gera: data/r1/resumo-r1-datas.pdf
Requer: python-markdown (venv) e google-chrome no PATH.
CSS: mesma identidade visual de md2pdf_piloto.py, compactada p/ 1 página.
"""
import markdown, pathlib, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

CSS = """
@page { size: A4; margin: 1.5cm 2cm; }
body { font-family: 'Segoe UI','Inter',system-ui,sans-serif; color:#1f2937;
       font-size: 9.4pt; line-height: 1.44; margin: 0; }
h1 { font-size: 15pt; color: #1e3a8a; border-bottom: 3px solid #1e3a8a;
     padding-bottom: 7px; margin: 0 0 10px; }
h2 { font-size: 11pt; color: #1e3a8a; margin: 13px 0 5px;
     border-bottom: 1px solid #dbe3f0; padding-bottom: 4px; }
h1, h2 { break-after: avoid; page-break-after: avoid; }
p, li { margin: 4px 0; orphans: 3; widows: 3; }
li { break-inside: avoid; page-break-inside: avoid; }
ul, ol { padding-left: 20px; }
ul ul { padding-left: 16px; }
blockquote { background: #eef2ff; border-left: 4px solid #1e3a8a;
             margin: 10px 0; padding: 8px 12px; color: #1e3a8a;
             break-inside: avoid; page-break-inside: avoid; }
blockquote p { margin: 0; }
code { background: #f1f5f9; padding: 1px 4px; border-radius: 4px;
       font-family: 'JetBrains Mono',monospace; font-size: 8.5pt; color:#0f172a; }
table { border-collapse: collapse; width: 100%; margin: 8px 0;
        break-inside: avoid; page-break-inside: avoid; }
th { background: #1e3a8a; color: #fff; font-size: 9pt;
     padding: 6px 10px; text-align: left; }
td { border: 1px solid #dbe3f0; padding: 6px 10px; font-size: 9.5pt; }
tr:nth-child(even) td { background: #f8fafc; }
tr { break-inside: avoid; }
hr { border: none; border-top: 1px solid #dbe3f0; }
a { color: #1e40af; }
.footer { margin-top: 18px; padding-top: 8px; border-top: 1px solid #dbe3f0;
          font-size: 8pt; color: #94a3b8; }
"""

src = ROOT / "data" / "r1" / "resumo-r1-datas.md"
pdf = src.with_suffix(".pdf")
body = markdown.markdown(src.read_text(), extensions=["tables"])
foot = "Protocolo de fichamentos auditáveis · resumo pós-piloto R0 → R1 · gerado 13/11/2026"
html = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}<div class=footer>{foot}</div></body></html>"
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
    f.write(html)
subprocess.run(["google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
                "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f.name],
               check=True, capture_output=True)
print(pdf)
