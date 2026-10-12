"""Render a fichamento's CONTENT as readable markdown — no provenance.

Used to build judge packets: source (ai/human), generator metadata and
elapsed time must never leak into what judges see. source_refs are kept —
judges are encouraged to verify them against the original article.
"""

from __future__ import annotations

from .models import Fichamento


def render_fichamento_md(f: Fichamento) -> str:
    c = f.content
    out = [
        "## Resumo executivo",
        c.executive_summary,
        "",
        "## Questão de pesquisa",
        c.research_question,
        "",
        "## Teorias presentes",
    ]
    for t in c.theories:
        refs = f" [{', '.join(t.source_refs)}]" if t.source_refs else ""
        out.append(f"- **{t.name}** ({t.tradition}) — {t.role}{refs}")
    out += ["", "## Conceitos-chave"]
    for k in c.key_concepts:
        refs = f" [{', '.join(k.source_refs)}]" if k.source_refs else ""
        out.append(f"- **{k.concept}**: {k.definition}{refs}")
    m = c.methodology
    out += [
        "",
        "## Metodologia",
        f"- Design: {m.design}",
        f"- Amostra (N): {m.sample_size if m.sample_size is not None else 'n/d'}",
        f"- Setor: {m.sector}",
        f"- Período: {m.period}",
        f"- Técnicas: {', '.join(m.methods)}",
    ]
    if m.source_refs:
        out.append(f"- Fontes: {', '.join(m.source_refs)}")
    out += ["", "## Achados principais"]
    for fd in c.main_findings:
        refs = f" [{', '.join(fd.source_refs)}]" if fd.source_refs else ""
        out.append(f"- ({fd.type}) {fd.finding}{refs}")
    out += [
        "",
        "## Contribuição",
        f"- Teórica: {c.contribution.theoretical}",
        f"- Prática: {c.contribution.practical}",
    ]
    return "\n".join(out)
