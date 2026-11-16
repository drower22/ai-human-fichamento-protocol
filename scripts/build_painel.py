"""Gera site/acompanhar/index.html: painel de acompanhamento das
avaliações dos juízes, 3 colunas (Piloto / R1 / R2).

- Cada juiz avalia só os artigos que indicou (registry.nominated_by).
- Link do form: /juizes/?j=<token>&r=<rodada>&a=<artigo> — trava tudo e
  carrega o par sozinho após o aceite do TCLE.
- Status "respondido" = JSON da avaliação já importado em
  data/piloto/evaluations/ (R0) ou data/evaluations/roundN/ (R1/R2).
- "par no ar" = site/juizes/pairs/<artigo>.json publicado.

Uso:  .venv/bin/python scripts/build_painel.py
Regerar a cada nova avaliação importada e fazer deploy.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"

JUDGES = {
    "J1": ("Natália", "nz4f"),
    "J2": ("Bruno", "bq8w"),
    "J3": ("Marcos", "mv3r"),
    "J4": ("Gustavo", "gx6t"),
}


def articles_by_round() -> dict[int, list[dict]]:
    arts = [json.loads(l) for l in (DATA / "articles" / "registry.jsonl").read_text().splitlines() if l.strip()]
    out: dict[int, list[dict]] = {1: [], 2: []}
    for a in arts:
        out.setdefault(a["round"], []).append(a)
    for v in out.values():
        v.sort(key=lambda a: a["article_id"])
    return out


def eval_done(round_: int, article_id: str, token: str) -> bool:
    if round_ == 0:
        return (DATA / "piloto" / "evaluations" / f"E-R0-{article_id}-{token}.json").exists()
    return (DATA / "evaluations" / f"round{round_}" / f"E-R{round_}-{article_id}-{token}.json").exists()


def pair_live(article_id: str) -> bool:
    return (SITE / "juizes" / "pairs" / f"{article_id}.json").exists()


def judge_row(round_: int, art: str, jid: str) -> str:
    name, tok = JUDGES[jid]
    done = eval_done(round_, art, tok)
    status = ('<span class="st done">respondido</span>' if done
              else '<span class="st pend">pendente</span>')
    return (f'<div class="jrow"><span class="jname">{name} <i>({jid})</i></span>{status}'
            f'<a class="go" href="/juizes/?j={tok}&r={round_}&a={art}">abrir&nbsp;→</a></div>')


def card(round_: int, art: str, jids: list[str], live: bool, title: str = "") -> str:
    badge = ('<span class="pair live">par no ar</span>' if live
             else '<span class="pair soon">par pendente</span>')
    t = f'<div class="artt">{title}</div>' if title else ""
    rows = "".join(judge_row(round_, art, j) for j in jids)
    return f'<div class="card"><div class="art">{art} {badge}</div>{t}{rows}</div>'


def build() -> Path:
    by_round = articles_by_round()

    piloto_rows = "".join(judge_row(0, "PILOTO", j) for j in JUDGES)
    col0 = (f'<div class="card"><div class="art">PILOTO '
            f'<span class="pair live">par no ar</span></div>'
            f'<div class="artt">par cego único: todos os juízes avaliaram o mesmo par</div>'
            f"{piloto_rows}</div>")

    col1 = "".join(
        card(1, a["article_id"], [a["nominated_by"]],
             pair_live(a["article_id"]), a.get("title", ""))
        for a in by_round[1])

    col2 = "".join(
        card(2, a["article_id"], [a["nominated_by"]],
             pair_live(a["article_id"]), a.get("title", ""))
        for a in by_round[2])

    now = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
    n_done = sum(eval_done(0, "PILOTO", t[1]) for t in JUDGES.values())
    n1 = sum(eval_done(1, a["article_id"], JUDGES[a["nominated_by"]][1]) for a in by_round[1])
    n2 = sum(eval_done(2, a["article_id"], JUDGES[a["nominated_by"]][1]) for a in by_round[2])

    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Acompanhamento das avaliações</title>
<style>
:root{{--navy:#1e3a8a;--blue:#2563eb;--bg:#f8fafc;--card:#fff;--line:#dbe3f0}}
*{{box-sizing:border-box;margin:0}}
body{{background:var(--bg);font-family:"Segoe UI",system-ui,sans-serif;
  color:#1f2937;padding:28px 18px}}
h1{{color:var(--navy);font-size:22px;margin-bottom:4px}}
.sub{{color:#64748b;font-size:13px;margin-bottom:20px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;
  max-width:1500px;margin:0 auto;align-items:start}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.col h2{{color:var(--navy);font-size:15px;text-transform:uppercase;
  letter-spacing:.4px;margin-bottom:4px}}
.col .meta{{font-size:12px;color:#64748b;margin-bottom:12px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;
  padding:12px 14px;margin-bottom:10px}}
.art{{font-weight:700;color:var(--navy);font-size:14px;
  display:flex;justify-content:space-between;align-items:center;gap:8px}}
.artt{{font-size:11px;color:#64748b;margin:4px 0 2px;line-height:1.35}}
.pair{{font-size:10px;font-weight:600;border-radius:999px;padding:2px 8px;white-space:nowrap}}
.pair.live{{background:#dcfce7;color:#166534}}
.pair.soon{{background:#f1f5f9;color:#64748b}}
.jrow{{display:flex;align-items:center;gap:8px;margin-top:8px;
  border-top:1px solid var(--line);padding-top:8px}}
.jname{{font-size:13px;flex:1}}
.jname i{{color:#94a3b8;font-style:normal;font-size:11px}}
.st{{font-size:11px;font-weight:600;border-radius:999px;padding:2px 9px}}
.st.done{{background:#dcfce7;color:#166534}}
.st.pend{{background:#fef9c3;color:#854d0e}}
.go{{font-size:12px;font-weight:600;color:var(--blue);text-decoration:none;
  border:1.5px solid var(--blue);border-radius:8px;padding:3px 10px}}
.go:hover{{background:#eff6ff}}
.foot{{max-width:1500px;margin:22px auto 0;font-size:11px;color:#94a3b8}}
</style></head><body>
<div style="max-width:1500px;margin:0 auto 16px">
  <h1>Acompanhamento das avaliações</h1>
  <p class="sub">Fichamentos cegos A/B por artigo e status de resposta de cada juiz.
  O botão abre o formulário já preenchido com juiz, rodada e par.</p>
</div>
<div class="grid">
  <div class="col"><h2>Piloto (R0)</h2><div class="meta">{n_done}/4 avaliações recebidas</div>{col0}</div>
  <div class="col"><h2>Rodada 1</h2><div class="meta">{n1}/{len(by_round[1])} avaliações recebidas · juízes 16–22/11</div>{col1}</div>
  <div class="col"><h2>Rodada 2</h2><div class="meta">{n2}/{len(by_round[2])} avaliações recebidas · início 23/11</div>{col2}</div>
</div>
<p class="foot">Cada juiz avalia apenas os artigos que indicou (4 por rodada).
Atualizado em {now}. Página gerada por scripts/build_painel.py.</p>
</body></html>"""

    out = SITE / "acompanhar" / "index.html"
    out.write_text(html)
    print(f"{out} ({n_done}/4 piloto, {n1}/16 R1, {n2}/16 R2)")
    return out


if __name__ == "__main__":
    build()
