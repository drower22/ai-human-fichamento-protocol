#!/usr/bin/env python3
"""Cria rascunhos dos e-mails da R1 na pasta Rascunhos do Outlook (IMAP).

Nao envia nada: cada mensagem e gravada como rascunho com os dois anexos
(instrucoes-estudantes.pdf + A{nn}-numerado.pdf). Voce revisa e envia
manualmente pelo Outlook.

Uso:
  python scripts/draft_r1_emails.py --eml /tmp/r1-emails   # gera os .eml (arraste p/ Rascunhos no Thunderbird)
  IMAP_USER=voce@ufpr.br IMAP_PASS=senha-de-app \
    python scripts/draft_r1_emails.py            # cria os 16 rascunhos via IMAP
  python scripts/draft_r1_emails.py --dry-run    # so valida, sem conectar
  python scripts/draft_r1_emails.py --only S01   # um destinatario
"""
import argparse, csv, getpass, imaplib, json, os, sys, time
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import formatdate
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINKS = ROOT / "data/private/student-links-round1.json"
EMAILS_CSV = ROOT / "data/private/student-emails.csv"
INSTRUCOES = ROOT / "protocol/instrucoes-estudantes.pdf"
PDFS = ROOT / "data/articles/pdfs"

HOST = os.environ.get("IMAP_HOST", "imap.gmail.com")
PORT = 993

ASSUNTO = "Pesquisa de fichamentos: Rodada 1"
REPLY_TO = "ismar.drower@ufpr.br"  # respostas caem na caixa institucional
PRAZO = "13/11/26 - 23:59"  # ajuste aqui se mudar o prazo

CORPO = """Bom dia, {primeiro_nome}

Estamos começando a Rodada 1 da pesquisa de fichamentos. Em anexo vão as instruções e o seu artigo, já com as linhas numeradas.

Quando puder, é só abrir o seu link e começar:
{link}

Prazo máximo para submissão: {prazo}

Qualquer problema, me chama.

Abraço,
Ismar
"""


def load_recipients():
    links = json.loads(LINKS.read_text(encoding="utf-8"))
    emails = {}
    with open(EMAILS_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sid = (row.get("student_id") or "").strip()
            em = (row.get("email") or "").strip()
            if sid:
                emails[sid] = em
    out = []
    for s in links["students"]:
        sid = s["participant_id"]
        if emails.get(sid, "").upper() == "SKIP":
            continue
        out.append({
            "student_id": sid,
            "name": s["name"],
            "email": emails.get(sid, ""),
            "link": s["url"],
            "pdf": PDFS / f'{s["article_id"]}-numerado.pdf',
        })
    return out


def build_message(rec, sender):
    msg = EmailMessage()
    msg["Subject"] = ASSUNTO
    msg["From"] = sender
    if sender != REPLY_TO:
        msg["Reply-To"] = REPLY_TO
    if "@" in rec["email"]:
        msg["To"] = Address(display_name=rec["name"], addr_spec=rec["email"])
    msg["Date"] = formatdate(localtime=True)
    primeiro = rec["name"].split()[0]
    msg.set_content(CORPO.format(primeiro_nome=primeiro,
                                 link=rec["link"], prazo=PRAZO))

    for path in [INSTRUCOES, rec["pdf"]]:
        data = path.read_bytes()
        msg.add_attachment(data, maintype="application",
                           subtype="pdf", filename=path.name)
    return msg


def find_drafts_folder(conn):
    typ, boxes = conn.list()
    candidates = []
    for b in boxes or []:
        line = b.decode("utf-8", "replace")
        if "\\Drafts" in line:
            candidates.append(line.rsplit(' "', 1)[-1].strip('"'))
    for name in candidates:
        return name
    for guess in ('"Rascunhos"', "Rascunhos", '"Drafts"', "Drafts"):
        typ, _ = conn.select(guess, readonly=True)
        if typ == "OK":
            conn.close()
            return guess.strip('"')
    raise RuntimeError(f"Pasta de rascunhos nao encontrada. Pastas: {boxes}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--eml", help="grava .eml prontos neste diretorio")
    ap.add_argument("--only", help="ex.: S01")
    args = ap.parse_args()

    recs = load_recipients()
    if args.only:
        recs = [r for r in recs if r["student_id"] == args.only]
    if not recs:
        sys.exit("nenhum destinatario")

    missing = [r["student_id"] for r in recs if "@" not in r["email"]]
    missing_pdf = [r["student_id"] for r in recs if not r["pdf"].exists()]
    if not INSTRUCOES.exists():
        sys.exit(f"anexo ausente: {INSTRUCOES}")
    if missing:
        print(f"aviso: {len(missing)} sem e-mail (Para vazio no rascunho): "
              f"{', '.join(missing)}")
    if missing_pdf:
        sys.exit(f"PDFs ausentes: {', '.join(missing_pdf)}")

    if args.dry_run:
        for r in recs:
            print(f'{r["student_id"]} {r["name"]} <{r["email"]}> '
                  f'[{r["pdf"].name}] {r["link"]}')
        print(f"ok: {len(recs)} rascunhos seriam criados")
        return

    if args.eml:
        outdir = Path(args.eml)
        outdir.mkdir(parents=True, exist_ok=True)
        sender = os.environ.get("IMAP_USER") or "ismar.drower@ufpr.br"
        import re, unicodedata
        for r in recs:
            msg = build_message(r, sender)
            base = unicodedata.normalize("NFKD", r["name"]).encode("ascii", "ignore").decode()
            slug = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")
            (outdir / f'{r["student_id"]}-{slug}.eml').write_bytes(msg.as_bytes())
            dest = r["email"] or "(preencher Para)"
            print(f'{r["student_id"]} {r["name"]} -> {dest}: {r["pdf"].name}')
        print(f"pronto: {len(recs)} .eml em {outdir}")
        return

    user = os.environ.get("IMAP_USER") or input("seu e-mail: ").strip()
    pw = os.environ.get("IMAP_PASS") or getpass.getpass("senha/app password: ")

    conn = imaplib.IMAP4_SSL(HOST, PORT)
    conn.login(user, pw)
    try:
        folder = find_drafts_folder(conn)
        print(f"pasta de rascunhos: {folder}")
        for r in recs:
            msg = build_message(r, user)
            typ, resp = conn.append(f'"{folder}"',
                                    "(\\Draft \\Seen)",
                                    imaplib.Time2Internaldate(time.time()),
                                    msg.as_bytes())
            print(f'{r["student_id"]} -> {r["email"]}: {typ} {resp}')
            if typ != "OK":
                sys.exit(f"falha no rascunho de {r['student_id']}")
    finally:
        conn.logout()
    print(f"pronto: {len(recs)} rascunhos criados")


if __name__ == "__main__":
    main()
