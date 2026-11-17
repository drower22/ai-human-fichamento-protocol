"""Gera site/juizes/j/{slug}/index.html, pagina pessoal de cada juiz com
as instrucoes resumidas e os links dos seus 4 pares da rodada.

O endereco usa o slug do link pessoal (mesma ofuscacao do resto do site):
/juizes/j/nz4f/ etc. O J# e o nome aparecem so na propria pagina.
Cada link mostra o status: pendente ou enviado (avaliacao ja recebida).

Uso:  .venv/bin/python scripts/build_judge_pages.py [--round 1]
"""
import argparse
import html as html_mod
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"

JUDGES = {  # slug: (J#, nome de exibicao na pagina pessoal)
    "nz4f": ("J1", "Natália"), "bq8w": ("J2", "Bruno"),
    "mv3r": ("J3", "Marcos"), "gx6t": ("J4", "Gustavo"),
}

e = lambda s: html_mod.escape(str(s or ""))


def articles_of(round_: int, jid: str) -> list[dict]:
    arts = [json.loads(l) for l in
            (DATA / "articles" / "registry.jsonl").read_text().splitlines()
            if l.strip() and json.loads(l)["round"] == round_
            and json.loads(l)["nominated_by"] == jid]
    arts.sort(key=lambda a: a["article_id"])
    return arts


def eval_done(round_: int, art: str, slug: str) -> bool:
    return (DATA / "evaluations" / f"round{round_}"
            / f"E-R{round_}-{art}-{slug}.json").exists()


PAGE = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Suas avaliações · Rodada {r}</title>
<style>
:root{{--navy:#1e3a8a;--blue:#2563eb;--bg:#f8fafc;--card:#fff;--line:#dbe3f0;--slate:#475569}}
*{{box-sizing:border-box;margin:0}}
body{{background:var(--bg);font-family:"Segoe UI",system-ui,sans-serif;
  color:#1f2937;padding:28px 18px;line-height:1.6}}
.wrap{{max-width:760px;margin:0 auto}}
h1{{color:var(--navy);font-size:22px;margin-bottom:4px}}
.hello{{color:var(--slate);font-size:14px;margin-bottom:20px}}
section{{background:var(--card);border:1px solid var(--line);border-radius:12px;
  padding:18px 22px;margin-bottom:16px}}
h2{{color:var(--navy);font-size:15px;margin-bottom:8px}}
p,li{{font-size:14px}}
ul,ol{{padding-left:22px}}
li{{margin:5px 0}}
.warn{{background:#fffbeb;border-color:#fde68a}}
.warn b{{color:#92400e}}
.links .cta{{font-size:13px;color:var(--slate);margin-bottom:10px}}
.links a{{display:flex;align-items:center;gap:12px;background:#eff6ff;
  border:1.5px solid #bfdbfe;border-radius:10px;padding:12px 16px;margin:8px 0;
  text-decoration:none;color:var(--navy)}}
.links a:hover{{background:#dbeafe;border-color:var(--blue)}}
.links .aid{{font-weight:700;font-size:14px;white-space:nowrap}}
.links .ttl{{flex:1;font-weight:400;color:var(--slate);font-size:12px;line-height:1.35}}
.links .st{{font-size:11px;font-weight:700;border-radius:999px;padding:3px 10px;
  white-space:nowrap}}
.links .st.pend{{background:#fef9c3;color:#854d0e}}
.links .st.done{{background:#dcfce7;color:#166534}}
.links a.done{{opacity:.75}}
.links .arrow{{font-size:16px;color:var(--blue)}}
.foot{{font-size:12px;color:#94a3b8;margin-top:6px}}
</style></head><body><div class="wrap">
<h1>Avaliação cega de fichamentos · Rodada {r}</h1>
<p class="hello">Olá, <b>{nome}</b>. Esta é a sua página pessoal. Guarde o
endereço, ele é só seu.</p>

<section><h2>A pesquisa, em resumo</h2>
<p><b>Pergunta de pesquisa:</b> numa revisão de literatura na escala de
centenas de artigos, fichamentos produzidos por estudantes ou por IA, num
processo rápido de fichamento, sustentam a qualidade necessária para que o
pesquisador revise, analise e só então defina o corpus?</p>
<p style="margin-top:8px"><b>Objetivo geral:</b> validar um protocolo
iterativo IA–humano, auditável, replicável e de ciência aberta, para
produção de fichamentos em escala, medindo objetivamente onde cada
produtor é melhor.</p>
<p style="margin-top:8px"><b>Objetivos específicos:</b></p>
<ul>
<li>comparar a qualidade dos dois produtores por seção e por tipo de erro;</li>
<li>medir a aprendizagem dos estudantes e o efeito da calibração entre rodadas;</li>
<li>viabilizar o desenho final "IA ficha, humano revisa", o mesmo pipeline
que, em escala, pode alimentar aplicações como um <i>knowledge graph</i>
do corpus;</li>
<li>entregar um protocolo público e replicável, com instrumentos, dados e
código auditáveis (ciência aberta).</li>
</ul></section>

<section class="warn"><h2>Leia antes de avaliar</h2>
<p><b>Não é um teste de "adivinhe qual é a IA".</b> A formatação pode fazer o
fichamento de IA parecer evidente, e o humano pode trazer erros de digitação,
ortografia e pontuação. <b>Nada disso está em avaliação.</b> A pergunta real
é se um dos dois fichamentos pode ser usado numa revisão com centenas de
artigos: depois do fichamento rápido, o leitor seguirá um critério rigoroso
de revisão e análise antes de definir o corpus. Avalie o conteúdo:
fidelidade, completude e referências verificáveis.</p>
<p style="margin-top:8px"><b>Fidelidade limita a nota.</b> Como combinamos:
uma seção com conteúdo inventado, extrapolado, inchado ou copiado
literalmente do artigo <b>não passa de 4</b>, mesmo que tenha muitos
acertos.</p>
<p style="margin-top:8px"><b>Transparência:</b> a IA rodou no modo
<i>default</i>. Por isso, em alguns pontos, ela limitou a própria escrita
para não extrapolar o texto, e ela mesma registrou essas limitações.
Vamos discuti-las em grupo depois da rodada.</p></section>

<section><h2>Como avaliar, em 5 passos</h2>
<ol>
<li>Clique no artigo, leia e aceite o TCLE. O par carrega sozinho.</li>
<li>Alterne as abas <b>A | B</b> e dê nota <b>1 a 7</b> em cada uma das 7
seções, pelas âncoras na tela. Marque os tipos de erro quando houver.</li>
<li>Confira as referências <code>p.N Lnnn</code> no PDF numerado do artigo.
Referência que não sustenta o conteúdo conta como erro.</li>
<li>No comparativo: <b>qual você usaria na sua revisão?</b> + por quê +
sua familiaridade com o artigo.</li>
<li>Prazo: <b>até {prazo}</b>. Avalie sem discutir com os demais juízes.</li>
</ol></section>

<section class="links"><h2>Seus {n} pares · Rodada {r}</h2>
<p class="cta"><b>Clique em um artigo para abrir a avaliação.</b> O formulário
já abre com o par certo (depois do aceite do TCLE). Você pode avaliar na
ordem que quiser e voltar aqui para abrir o próximo.</p>
{links}
</section>

<p class="foot">Dúvidas: ismar.drower@ufpr.br · Protocolo de validação
iterativa IA·humano para fichamentos (UFPR).</p>
</div></body></html>
"""


def build(round_: int, prazo: str) -> None:
    for slug, (jid, nome) in JUDGES.items():
        arts = articles_of(round_, jid)
        links = ""
        for a in arts:
            art = a["article_id"]
            done = eval_done(round_, art, slug)
            badge = ('<span class="st done">✓ enviado</span>' if done
                     else '<span class="st pend">pendente</span>')
            links += (f'<a class="{"done" if done else ""}" '
                      f'href="/juizes/?j={slug}&r={round_}&a={art}">'
                      f'<span class="aid">Artigo {art}</span>'
                      f'<span class="ttl">{e(a["title"])}</span>'
                      f'{badge}<span class="arrow">→</span></a>')
        out = SITE / "juizes" / "j" / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(
            PAGE.format(r=round_, nome=e(nome), n=len(arts),
                        links=links, prazo=e(prazo)))
        n_done = sum(eval_done(round_, a["article_id"], slug) for a in arts)
        print(f"{jid} ({slug}): {len(arts)} pares, {n_done} enviados "
              f"-> {out}/index.html")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", type=int, default=1)
    ap.add_argument("--prazo", default="22/11")
    a = ap.parse_args()
    build(a.round, a.prazo)
