"""CSS compartilhado dos PDFs do protocolo (identidade visual navy).

CSS_FULL: mesma de md2pdf_piloto.py (margens e corpo normais).
Importar daqui evita executar o loop de render de md2pdf_piloto.
"""

CSS_FULL = """
@page { size: A4; margin: 2.4cm 2.6cm; }
body { font-family: 'Segoe UI','Inter',system-ui,sans-serif; color:#1f2937;
       font-size: 10.8pt; line-height: 1.68; margin: 0; }
h1 { font-size: 19pt; color: #1e3a8a; border-bottom: 3px solid #1e3a8a;
     padding-bottom: 10px; margin: 0 0 22px; }
h2 { font-size: 13pt; color: #1e3a8a; margin: 30px 0 10px;
     border-bottom: 1px solid #dbe3f0; padding-bottom: 5px; }
h3 { font-size: 11pt; color: #374151; margin: 18px 0 8px; }
h1, h2, h3 { break-after: avoid; page-break-after: avoid; }
p, li { margin: 7px 0; orphans: 3; widows: 3; }
li { break-inside: avoid; page-break-inside: avoid; }
ul, ol { padding-left: 22px; }
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
