"""Gera site/acompanhar/index.html: painel de acompanhamento das
avaliações dos juízes, 3 colunas (Piloto / R1 / R2).

- Juízes aparecem anonimizados (J1..J4); nomes nunca saem na página.
- Cada juiz avalia só os artigos que indicou (registry.nominated_by).
- Link do form: /juizes/?j=<token>&r=<rodada>&a=<artigo> — trava tudo e
  carrega o par sozinho após o aceite do TCLE. Botão só aparece quando
  o par está publicado em site/juizes/pairs/ (senão o fetch daria 404).
- Status "respondido" = JSON da avaliação já importado em
  data/piloto/evaluations/ (R0) ou data/evaluations/roundN/ (R1/R2).
- Piloto: respostas completas embutidas (notas, preferência, qualitativos,
  taxonomia) num <details> por juiz.

Uso:  .venv/bin/python scripts/build_painel.py
Regerar a cada nova avaliação importada e fazer deploy.
"""
import html as html_mod
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import markdown

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT / "src"))
from fichamento.render import render_fichamento_md  # noqa: E402


def student_html(elapsed, sa: dict | None, refl: dict | None, labels: dict) -> str:
    """Autoavaliação (notas 1-7 por seção) + tempo declarado + log reflexivo.
    who/identidade nunca entra — só S# ou 'respondente i'."""
    out = []
    if elapsed is not None:
        out.append(f'<div class="meta2">tempo declarado: <b>{e(elapsed)} min</b></div>')
    if sa:
        tot = sum(v for v in sa.values() if isinstance(v, int))
        rows = "".join(f"<tr><td>{e(lbl)}</td><td>{e(sa.get(k))}</td></tr>"
                       for k, lbl in SECS)
        out.append('<div class="meta2"><b>autoavaliação (1–7 por seção)</b></div>'
                   f'<table class="sc"><tr><th>seção</th><th>nota</th></tr>{rows}'
                   f'<tr class="tot"><td>total</td><td>{tot}</td></tr></table>')
    if refl:
        items = "".join(
            f'<div class="qside"><b>{e(labels.get(k, k))}:</b> {e(v)}</div>'
            for k, v in refl.items() if v)
        if items:
            out.append(f'<div class="meta2"><b>log reflexivo</b></div>{items}')
    return f'<div class="resp">{"".join(out)}</div>' if out else ""


def _ns(d):
    """dict -> SimpleNamespace recursivo (render sem validação de schema:
    o par do piloto precede o gate de source_refs)."""
    if isinstance(d, dict):
        return SimpleNamespace(**{k: _ns(v) for k, v in d.items()})
    if isinstance(d, list):
        return [_ns(x) for x in d]
    return d

JUDGES = {"J1": "nz4f", "J2": "bq8w", "J3": "mv3r", "J4": "gx6t"}

SECS = [
    ("executive_summary", "Resumo"),
    ("research_question", "Questão de pesquisa"),
    ("theories", "Teorias"),
    ("key_concepts", "Conceitos-chave"),
    ("methodology", "Metodologia"),
    ("main_findings", "Achados"),
    ("contribution", "Contribuição"),
]

ERR_LABEL = {
    "hallucination": "Invenção", "omission": "Omissão",
    "misinterpretation": "Interp. errada", "misattribution": "Atribuição errada",
    "terminology": "Terminologia", "extrapolation": "Extrapolação",
    "invalid_source_ref": "Ref. inválida", "other": "Outro",
}
SEC_LABEL = dict(SECS)

# rótulos das perguntas do log reflexivo (protocol/forms/student-form.md)
REFL_PILOT = {"q1": "O que foi mais difícil?",
              "q2": "O que faria diferente?",
              "q3": "Usou IA ou ferramentas externas?"}
REFL_R1 = {"q1": "Dificuldades com o artigo e o tema",
           "q2": "Dificuldades com o formato da pesquisa (formulário, PDF numerado, referências)",
           "q3": "O que mudaria na abordagem",
           "q4": "Usou IA ou auxílio externo?"}

e = lambda s: html_mod.escape(str(s or ""))


def articles_by_round() -> dict[int, list[dict]]:
    arts = [json.loads(l) for l in (DATA / "articles" / "registry.jsonl").read_text().splitlines() if l.strip()]
    out: dict[int, list[dict]] = {1: [], 2: []}
    for a in arts:
        out.setdefault(a["round"], []).append(a)
    for v in out.values():
        v.sort(key=lambda a: a["article_id"])
    return out


def eval_path(round_: int, article_id: str, token: str) -> Path:
    if round_ == 0:
        return DATA / "piloto" / "evaluations" / f"E-R0-{article_id}-{token}.json"
    return DATA / "evaluations" / f"round{round_}" / f"E-R{round_}-{article_id}-{token}.json"


def eval_done(round_: int, article_id: str, token: str) -> bool:
    return eval_path(round_, article_id, token).exists()


def pair_live(article_id: str) -> bool:
    return (SITE / "juizes" / "pairs" / f"{article_id}.json").exists()


def link_btn(round_: int, art: str, tok: str, live: bool) -> str:
    if live:
        return f'<a class="go" href="/juizes/?j={tok}&r={round_}&a={art}">abrir&nbsp;→</a>'
    return '<span class="go off" title="par ainda não publicado">aguardando</span>'


def judge_row(round_: int, art: str, jid: str, live: bool) -> str:
    tok = JUDGES[jid]
    done = eval_done(round_, art, tok)
    if round_ == 0:  # piloto encerrado: sem link, falta = não respondeu
        status = ('<span class="st done">respondido</span>' if done
                  else '<span class="st pend">não respondeu</span>')
        return f'<div class="jrow"><span class="jname">{jid}</span>{status}</div>'
    status = ('<span class="st done">respondido</span>' if done
              else '<span class="st pend">pendente</span>')
    return (f'<div class="jrow"><span class="jname">{jid}</span>{status}'
            f'{link_btn(round_, art, tok, live)}</div>')


def eval_html(ev: dict) -> str:
    """Renderiza uma avaliação recebida (notas, preferência, qualitativos, erros)."""
    sc = ev.get("scores") or {}
    qual = ev.get("qualitative") or {}
    tax = ev.get("error_taxonomy") or {}
    pref = qual.get("preferred", "")
    conf = qual.get("confidence", "")

    rows = "".join(
        f"<tr><td>{e(lbl)}</td><td>{e((sc.get('A') or {}).get(k))}</td>"
        f"<td>{e((sc.get('B') or {}).get(k))}</td></tr>"
        for k, lbl in SECS)
    tot_a = sum(v for v in (sc.get("A") or {}).values() if isinstance(v, int))
    tot_b = sum(v for v in (sc.get('B') or {}).values() if isinstance(v, int))
    table = (f'<table class="sc"><tr><th>seção</th><th>A</th><th>B</th></tr>{rows}'
             f'<tr class="tot"><td>total</td><td>{tot_a}</td><td>{tot_b}</td></tr></table>')

    def errs(side: str) -> str:
        by = (tax.get(side) or {}).get("by_section") or {}
        if not by:
            return ""
        chips = []
        for sec, d in by.items():
            names = ", ".join(ERR_LABEL.get(c, c) for c in d.get("codes", []))
            note = f' — <i>{e(d["other_note"])}</i>' if d.get("other_note") else ""
            chips.append(f'<div class="errl"><b>{e(SEC_LABEL.get(sec, sec))}:</b> {e(names)}{note}</div>')
        return f'<div class="errs">{"".join(chips)}</div>'

    def qual_side(side: str) -> str:
        q = qual.get(side) or {}
        return (f'<div class="qside"><b>{side} · questionaria:</b> {e(q.get("question_would_ask"))}<br>'
                f'<b>{side} · faltou:</b> {e(q.get("missing"))}</div>')

    pref_txt = {"A": "Fichamento A", "B": "Fichamento B", "empate": "Empate"}.get(pref, pref)
    notes = f'<div class="qside"><b>Observações:</b> {e(ev.get("notes"))}</div>' if ev.get("notes") else ""
    return f"""<div class="resp">
  <div class="prefline"><b>Preferência:</b> {e(pref_txt)} · <b>familiaridade:</b> {e(conf)}</div>
  {table}
  <div class="qside"><b>Por quê:</b> {e(qual.get('why'))}</div>
  {qual_side('A')}{errs('A')}{qual_side('B')}{errs('B')}{notes}
</div>"""


def _fich_html(side_content: dict) -> str:
    """Renderiza o conteúdo de um lado do par como HTML (mesmo render dos pacotes)."""
    md = render_fichamento_md(SimpleNamespace(content=_ns(side_content)))
    return markdown.markdown(md)


def _pilot_respondent(side_content: dict) -> dict | None:
    """Casa um lado do par à resposta X_* do piloto pelo conteúdo —
    full_name fica de fora (anonimização na página)."""
    key = (side_content.get("executive_summary"),
           side_content.get("research_question"))
    for p in sorted((DATA / "piloto" / "responses").glob("X_*.json")):
        d = json.loads(p.read_text())
        if (d.get("executive_summary"), d.get("research_question")) == key:
            return d
    return None


def piloto_pair_block() -> str:
    """Os dois fichamentos do par do piloto. A/B era sorteado por juiz, então
    rotulamos Fichamento 1/2 (convenção da reunião: 1 = maior cobertura).
    Cada um traz autoavaliação + tempo + log reflexivo do respondente."""
    pair = json.loads((DATA / "piloto" / "pairs" / "PILOTO.json").read_text())
    def cov(side):
        s = pair[side]
        return len(s.get("key_concepts") or []) + len(s.get("main_findings") or [])
    sides = sorted(("A", "B"), key=cov, reverse=True)
    out = ['<div class="pairview"><b>O par avaliado</b> '
           '<span class="artt">(ambos produzidos por alunos; '
           'lado A/B variava por juiz; respondentes anônimos)</span>']
    for i, side in enumerate(sides, 1):
        resp = _pilot_respondent(pair[side])
        stu = (student_html(resp.get("elapsed_minutes"), resp.get("self_assessment"),
                            resp.get("reflection_log"), REFL_PILOT)
               if resp else "")
        out.append(
            f'<details class="det"><summary>ver Fichamento {i} '
            f'<span class="artt">({cov(side)} conceitos+achados)</span></summary>'
            f'<div class="fich">{_fich_html(pair[side])}</div>{stu}</details>')
    out.append("</div>")
    return "".join(out)


def piloto_card() -> str:
    rows = []
    for jid, tok in JUDGES.items():
        p = eval_path(0, "PILOTO", tok)
        done = p.exists()
        status = ('<span class="st done">respondido</span>' if done
                  else '<span class="st pend">não respondeu</span>')
        row = f'<div class="jrow"><span class="jname">{jid}</span>{status}</div>'
        if done:
            ev = json.loads(p.read_text())
            row += (f'<details class="det"><summary>ver resposta de {jid}</summary>'
                    f'{eval_html(ev)}</details>')
        rows.append(row)
    return (f'<div class="card"><div class="art">PILOTO '
            f'<span class="pair live">par no ar</span></div>'
            f'<div class="artt">par cego único: todos os juízes avaliaram o mesmo par</div>'
            f'{piloto_pair_block()}{"".join(rows)}</div>')


def _human_fich(round_: int, art: str) -> dict | None:
    p = DATA / "fichamentos" / f"round{round_}" / "human" / f"F-R{round_}-{art}-HUM.json"
    return json.loads(p.read_text()) if p.exists() else None


def card(round_: int, art: str, jid: str, live: bool, title: str = "") -> str:
    badge = ('<span class="pair live">par no ar</span>' if live
             else '<span class="pair soon">par pendente</span>')
    t = f'<div class="artt">{e(title)}</div>' if title else ""
    # lado do estudante: autoavaliação + tempo + log (S# é o id anonimizado)
    fich = _human_fich(round_, art)
    stu = ""
    if fich:
        g = fich.get("generator") or {}
        sid = g.get("participant_id", "")
        stu = (f'<details class="det"><summary>estudante {e(sid)}: '
               f'autoavaliação + log</summary>'
               f'{student_html(g.get("elapsed_minutes"), g.get("self_assessment"),
                               g.get("reflection_log"), REFL_R1)}</details>')
    else:
        raw = list(Path.home().joinpath("Downloads").glob(f"S*_{art}.json"))
        if raw:
            stu = ('<div class="artt">fichamento recebido: '
                   "aguardando validação</div>")
    return (f'<div class="card"><div class="art">{art} {badge}</div>{t}'
            f'{judge_row(round_, art, jid, live)}{stu}</div>')


def build() -> Path:
    by_round = articles_by_round()

    col0 = piloto_card()
    col1 = "".join(card(1, a["article_id"], a["nominated_by"],
                        pair_live(a["article_id"]), a.get("title", ""))
                   for a in by_round[1])
    col2 = "".join(card(2, a["article_id"], a["nominated_by"],
                        pair_live(a["article_id"]), a.get("title", ""))
                   for a in by_round[2])

    now = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
    n_done = sum(eval_done(0, "PILOTO", t) for t in JUDGES.values())
    n1 = sum(eval_done(1, a["article_id"], JUDGES[a["nominated_by"]]) for a in by_round[1])
    n2 = sum(eval_done(2, a["article_id"], JUDGES[a["nominated_by"]]) for a in by_round[2])

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
.jname{{font-size:13px;font-weight:700;color:var(--navy);flex:1}}
.st{{font-size:11px;font-weight:600;border-radius:999px;padding:2px 9px}}
.st.done{{background:#dcfce7;color:#166534}}
.st.pend{{background:#fef9c3;color:#854d0e}}
.go{{font-size:12px;font-weight:600;color:var(--blue);text-decoration:none;
  border:1.5px solid var(--blue);border-radius:8px;padding:3px 10px;white-space:nowrap}}
.go:hover{{background:#eff6ff}}
.go.off{{color:#94a3b8;border-color:#e2e8f0;cursor:default;font-weight:500}}
.det{{margin-top:6px}}
.det summary{{font-size:12px;color:var(--blue);cursor:pointer;font-weight:600}}
.resp{{margin-top:8px;font-size:12px;line-height:1.55}}
.prefline{{background:#eff6ff;border-radius:8px;padding:6px 10px;margin-bottom:8px}}
table.sc{{border-collapse:collapse;width:100%;margin:6px 0;font-size:11.5px}}
table.sc th{{background:var(--navy);color:#fff;padding:3px 8px;text-align:left}}
table.sc td{{border:1px solid var(--line);padding:3px 8px}}
table.sc tr.tot td{{font-weight:700;background:#f1f5f9}}
.qside{{background:#f8fafc;border:1px solid var(--line);border-radius:8px;
  padding:6px 10px;margin:6px 0}}
.errs{{margin:2px 0 6px 8px}}
.errl{{font-size:11px;color:#7f1d1d;margin:2px 0}}
.pairview{{background:#f8fafc;border:1px solid var(--line);border-radius:8px;
  padding:8px 10px;margin:8px 0}}
.fich{{font-size:11.5px;line-height:1.55;margin-top:8px;
  max-height:480px;overflow:auto;border-top:1px solid var(--line);padding-top:6px}}
.fich h2{{font-size:12px;color:var(--navy);margin:10px 0 4px}}
.fich ul{{padding-left:18px}}
.fich blockquote{{border-left:3px solid var(--line);color:#64748b;
  margin:4px 0;padding:2px 10px;font-style:italic}}
.meta2{{font-size:11px;color:#64748b;margin:8px 0 4px}}
.foot{{max-width:1500px;margin:22px auto 0;font-size:11px;color:#94a3b8}}
</style></head><body>
<div style="max-width:1500px;margin:0 auto 16px">
  <h1>Acompanhamento das avaliações</h1>
  <p class="sub">Fichamentos cegos A/B por artigo e status de resposta de cada juiz (J1 a J4).
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
