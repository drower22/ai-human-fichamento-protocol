"""Converte .md de instruções do protocolo em PDFs A4 estilizados.

Uso:  .venv/bin/python scripts/md2pdf.py
Gera: protocol/instrucoes-estudantes.pdf, protocol/instrucoes-juizes.pdf
Requer: python-markdown (venv) e google-chrome no PATH.
"""
import markdown, pathlib, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

CSS = """
@page { size: A4; margin: 2.2cm 2.4cm; }
body { font-family: 'Segoe UI','Inter',system-ui,sans-serif; color:#1f2937;
       font-size: 10.5pt; line-height: 1.55; margin: 0; }
h1 { font-size: 19pt; color: #1e40af; border-bottom: 3px solid #2563eb;
     padding-bottom: 8px; margin: 0 0 18px; }
h2 { font-size: 13pt; color: #1e40af; margin: 22px 0 8px;
     border-bottom: 1px solid #dbe3f0; padding-bottom: 4px; }
h3 { font-size: 11pt; color: #374151; margin: 16px 0 6px; }
/* títulos nunca ficam órfãos no fim da página nem se separam do conteúdo */
h1, h2, h3 { break-after: avoid; page-break-after: avoid; }
p, li { margin: 5px 0; orphans: 3; widows: 3; }
ul, ol { break-inside: avoid; page-break-inside: avoid; }
blockquote { background: #eff6ff; border-left: 4px solid #2563eb;
             margin: 12px 0; padding: 10px 14px; color: #1e3a8a;
             break-inside: avoid; }
blockquote p { margin: 0; }
code { background: #f1f5f9; padding: 1px 5px; border-radius: 4px;
       font-family: 'JetBrains Mono',monospace; font-size: 9pt; color:#0f172a; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; }
th { background: #1e40af; color: #fff; font-size: 9pt; padding: 6px 10px; text-align: left; }
td { border: 1px solid #dbe3f0; padding: 6px 10px; font-size: 9.5pt; }
tr:nth-child(even) td { background: #f8fafc; }
tr { break-inside: avoid; }
hr { border: none; border-top: 1px solid #dbe3f0; }
ul, ol { padding-left: 22px; }
a { color: #2563eb; }
.footer { margin-top: 28px; padding-top: 8px; border-top: 1px solid #dbe3f0;
          font-size: 8.5pt; color: #94a3b8; }
"""

DOCS = [
    ("protocol/student-instructions.md", "instrucoes-estudantes",
     "Protocolo de validação IA–Humano · Fichamento · Instruções aos estudantes"),
    ("protocol/judge-instructions.md", "instrucoes-juizes",
     "Protocolo de validação IA–Humano · Fichamento · Instruções aos juízes"),
]

for src, stem, foot in DOCS:
    body = markdown.markdown((ROOT / src).read_text(), extensions=["tables"])
    html = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}<div class=footer>{foot}</div></body></html>"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    pdf = ROOT / "protocol" / f"{stem}.pdf"
    subprocess.run(["google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f.name],
                   check=True, capture_output=True)
    print(pdf)
