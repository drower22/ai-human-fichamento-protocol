"""Converte os .md da reunião de calibração (piloto R0) em PDFs A4.

Uso:  .venv/bin/python scripts/md2pdf_piloto.py
Gera: data/piloto/reuniao-0611/*.pdf
Requer: python-markdown (venv) e google-chrome no PATH.
"""
import markdown, pathlib, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

CSS = """
@page { size: A4; margin: 2.4cm 2.6cm; }
body { font-family: 'Segoe UI','Inter',system-ui,sans-serif; color:#1f2937;
       font-size: 10.8pt; line-height: 1.68; margin: 0; }
h1 { font-size: 19pt; color: #1e3a8a; border-bottom: 3px solid #1e3a8a;
     padding-bottom: 10px; margin: 0 0 22px; }
h2 { font-size: 13pt; color: #1e3a8a; margin: 30px 0 10px;
     border-bottom: 1px solid #dbe3f0; padding-bottom: 5px; }
h3 { font-size: 11pt; color: #374151; margin: 18px 0 8px; }
/* títulos nunca ficam órfãos no fim da página nem se separam do conteúdo */
h1, h2, h3 { break-after: avoid; page-break-after: avoid; }
/* blocos inteiros nunca partem ao meio entre páginas */
p, li { margin: 7px 0; orphans: 3; widows: 3; }
li { break-inside: avoid; page-break-inside: avoid; }
ul, ol { padding-left: 22px; break-inside: avoid; }
blockquote { background: #eef2ff; border-left: 4px solid #1e3a8a;
             margin: 14px 0; padding: 12px 16px; color: #1e3a8a;
             break-inside: avoid; page-break-inside: avoid; }
blockquote p { margin: 0; }
code { background: #f1f5f9; padding: 1px 5px; border-radius: 4px;
       font-family: 'JetBrains Mono',monospace; font-size: 9pt; color:#0f172a; }
table { border-collapse: collapse; width: 100%; margin: 12px 0;
        break-inside: avoid; page-break-inside: avoid; }
th { background: #1e3a8a; color: #fff; font-size: 9pt;
     padding: 7px 10px; text-align: left; }
td { border: 1px solid #dbe3f0; padding: 7px 10px; font-size: 9.5pt; }
tr:nth-child(even) td { background: #f8fafc; }
tr { break-inside: avoid; }
hr { border: none; border-top: 1px solid #dbe3f0; }
a { color: #1e40af; }
.footer { margin-top: 32px; padding-top: 10px; border-top: 1px solid #dbe3f0;
          font-size: 8.5pt; color: #94a3b8; }
"""

DOCS = [
    ("data/piloto/reuniao-0611/01-dispersao-juizes.md", "01-dispersao-juizes",
     "Piloto R0 · Reunião de calibração 06/11 · Diagnóstico: avaliações dos juízes"),
    ("data/piloto/reuniao-0611/02-proposta-ancoras.md", "02-proposta-ancoras",
     "Piloto R0 · Reunião de calibração 06/11 · Decisões: ajuste das âncoras"),
    ("data/piloto/reuniao-0611/03-estudantes-ajustes.md", "03-estudantes-ajustes",
     "Piloto R0 · Reunião de calibração 06/11 · Para os estudantes: ajustes para a R1"),
]

for src, stem, foot in DOCS:
    body = markdown.markdown((ROOT / src).read_text(), extensions=["tables"])
    html = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}<div class=footer>{foot}</div></body></html>"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    pdf = ROOT / "data" / "piloto" / "reuniao-0611" / f"{stem}.pdf"
    subprocess.run(["google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f.name],
                   check=True, capture_output=True)
    print(pdf)
