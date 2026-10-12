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
    if c.theory_verdicts:
        # closed-pool instrument: show verdicts; rejected items as footnote
        for v in c.theory_verdicts:
            if v.verdict == "does_not_use":
                continue
            label = "usa" if v.verdict == "uses" else "discute"
            refs = f" [{', '.join(v.source_refs)}]" if v.source_refs else ""
            note = f" — {v.note}" if v.note else ""
            out.append(f"- **{v.name}** — {label}{refs}{note}")
            if v.quote:
                out.append(f'  > "{v.quote}"')
        for t in c.theories:
            refs = f" [{', '.join(t.source_refs)}]" if t.source_refs else ""
            out.append(f"- **{t.name}** ({t.tradition}) — {t.role}{refs} *(adicionada)*")
        rejected = [v.name for v in c.theory_verdicts if v.verdict == "does_not_use"]
        if rejected:
            out.append(f"  _rejeitadas do pool: {', '.join(rejected)}_")
    else:
        for t in c.theories:
            refs = f" [{', '.join(t.source_refs)}]" if t.source_refs else ""
            out.append(f"- **{t.name}** ({t.tradition}) — {t.role}{refs}")
    out += ["", "## Conceitos-chave"]
    for k in c.key_concepts:
        refs = f" [{', '.join(k.source_refs)}]" if k.source_refs else ""
        out.append(f"- **{k.concept}**: {k.definition}{refs}")
        if k.quote:
            out.append(f'  > "{k.quote}"')
    m = c.methodology
    out += [
        "",
        "## Metodologia",
        f"- Tipo: {m.study_type or 'n/d'}",
        f"- Delineamento: {m.design}",
        f"- Tipo de amostra: {m.sample_type or 'n/d'}",
        f"- Amostra (N): {m.sample_size if m.sample_size is not None else 'n/d'}",
        f"- Setor: {m.sector}",
        f"- Período: {m.period}",
        f"- Técnicas: {', '.join(m.methods)}",
    ]
    if m.analysis_note:
        out.append(f"- Análise: {m.analysis_note}")
    if m.source_refs:
        out.append(f"- Fontes: {', '.join(m.source_refs)}")
    out += ["", "## Achados principais"]
    for i, fd in enumerate(c.main_findings, 1):
        refs = f" [{', '.join(fd.source_refs)}]" if fd.source_refs else ""
        out.append(f"- **Achado {i}** ({fd.type}): {fd.finding}{refs}")
        if fd.quote:
            out.append(f'  > "{fd.quote}"')
    out += [
        "",
        "## Contribuição",
        f"- Teórica: {c.contribution.theoretical}",
        f"- Prática: {c.contribution.practical}",
    ]
    return "\n".join(out)
