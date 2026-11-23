"""Analisa as avaliações dos juízes da R1 (formato real dos E-R1-*.json).

Gera em analysis/reports/round1/:
- scores_long.csv        nota por artigo × posição cega × fonte × seção
- summary_by_source.csv  média/mediana/desvio por fonte × seção (+total)
- paired_diff.csv        diferença IA - humano por artigo × seção
- wilcoxon.csv           Wilcoxon pareado por seção (n, mediana, p, efeito)
- preferences.csv        escolha A/B mapeada à fonte + binomial
- errors_by_source.csv   taxonomia de erros por fonte
- meta_students.csv      autoavaliação do aluno vs nota do juiz (gap)
- report.md              relatório consolidado

Uso:  .venv/bin/python scripts/analyze_r1.py
"""
import csv
import json
import sys
from pathlib import Path

import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "analysis" / "reports" / "round1"
SECS = ["executive_summary", "research_question", "theories",
        "key_concepts", "methodology", "main_findings", "contribution"]
SEC_PT = {"executive_summary": "Resumo", "research_question": "Questão",
          "theories": "Teorias", "key_concepts": "Conceitos",
          "methodology": "Metodologia", "main_findings": "Achados",
          "contribution": "Contribuição"}
DL = Path.home() / "Downloads"


def load_pairmap():
    m = json.loads((ROOT / "data/private/pair-map-round1.json").read_text())
    return {p["article_id"]: p for p in m["pairs"]}


def load_evals():
    d = ROOT / "data/evaluations/round1"
    return [json.loads(p.read_text()) for p in sorted(d.glob("E-R1-*.json"))]


def self_assessment(article_id: str) -> dict | None:
    """Autoavaliação do estudante: schema validado ou arquivo bruto."""
    p = ROOT / f"data/fichamentos/round1/human/F-R1-{article_id}-HUM.json"
    if p.exists():
        g = (json.loads(p.read_text()).get("generator") or {})
        return g.get("self_assessment")
    raws = list(DL.glob(f"S*_{article_id}.json"))
    if raws:
        return json.loads(raws[0].read_text()).get("self_assessment")
    return None


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pmap = load_pairmap()
    evals = load_evals()

    rows, pref_rows, err_rows = [], [], []
    for ev in evals:
        art, jid = ev["article_id"], ev["judge_id"]
        src = {pos: pmap[art][pos] for pos in ("A", "B")}
        for pos in ("A", "B"):
            for sec in SECS:
                rows.append({"article": art, "judge": jid, "position": pos,
                             "source": src[pos], "section": sec,
                             "score": (ev["scores"].get(pos) or {}).get(sec)})
        choice = ev["qualitative"].get("preferred", "")
        pref_rows.append({
            "article": art, "judge": jid, "choice": choice,
            "preferred_source": src.get(choice) if choice in ("A", "B") else "tie",
            "confidence": ev["qualitative"].get("confidence", ""),
            "why": ev["qualitative"].get("why", ""),
        })
        for pos in ("A", "B"):
            for sec, dd in (ev["error_taxonomy"].get(pos, {})
                            .get("by_section") or {}).items():
                for code in dd.get("codes", []):
                    err_rows.append({"article": art, "judge": jid,
                                     "source": src[pos], "section": sec,
                                     "code": code,
                                     "note": dd.get("other_note", "")})

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "scores_long.csv", index=False)

    # --- resumo por fonte × seção -------------------------------------
    g = df.groupby(["source", "section"])["score"]
    summ = g.agg(["mean", "median", "std", "count"]).reset_index()
    summ["section"] = pd.Categorical(summ["section"], SECS, ordered=True)
    summ = summ.sort_values(["section", "source"])
    tot = df.groupby("source")["score"].agg(["mean", "median", "std"])
    summ.to_csv(OUT / "summary_by_source.csv", index=False)

    # --- diferença pareada IA - humano (mesmo artigo, mesmo juiz) -----
    piv = df.pivot_table(index=["article", "judge"], columns="source",
                         values="score", aggfunc="first")
    long_d = df.pivot_table(index=["article", "judge", "section"],
                            columns="source", values="score")
    long_d["diff_ai_minus_human"] = long_d["ai"] - long_d["human"]
    long_d.reset_index().to_csv(OUT / "paired_diff.csv", index=False)

    wil = []
    for sec in SECS:
        d = long_d.xs(sec, level="section")["diff_ai_minus_human"].dropna()
        n = int((d != 0).sum())
        if n == 0:
            wil.append({"section": sec, "n": 0, "median_diff": 0,
                        "p_wilcoxon": None, "rank_biserial": None})
            continue
        res = stats.wilcoxon(d)
        w = res.statistic
        rbc = 1 - 2 * w / (n * (n + 1) / 2)  # rank-biserial correlation
        wil.append({"section": sec, "n": n, "median_diff": d.median(),
                    "mean_diff": round(d.mean(), 2),
                    "p_wilcoxon": round(res.pvalue, 4),
                    "rank_biserial": round(rbc, 3)})
    wall = long_d["diff_ai_minus_human"].dropna()
    n_all = int((wall != 0).sum())
    res_all = stats.wilcoxon(wall)
    rbc_all = 1 - 2 * res_all.statistic / (n_all * (n_all + 1) / 2)
    wil.append({"section": "TOTAL (todas as seções)", "n": n_all,
                "median_diff": wall.median(),
                "mean_diff": round(wall.mean(), 2),
                "p_wilcoxon": round(res_all.pvalue, 4),
                "rank_biserial": round(rbc_all, 3)})
    pd.DataFrame(wil).to_csv(OUT / "wilcoxon.csv", index=False)

    # --- preferência A/B ------------------------------------------------
    pf = pd.DataFrame(pref_rows)
    pf.to_csv(OUT / "preferences.csv", index=False)
    n_ai = int((pf.preferred_source == "ai").sum())
    n_hum = int((pf.preferred_source == "human").sum())
    n_tie = int((pf.preferred_source == "tie").sum())
    n_eff = n_ai + n_hum
    binom = stats.binomtest(n_ai, n_eff, 0.5) if n_eff else None

    # --- erros por fonte -------------------------------------------------
    er = pd.DataFrame(err_rows)
    er.to_csv(OUT / "errors_long.csv", index=False)
    if not er.empty:
        ct = (er.groupby(["source", "code"]).size()
              .unstack(fill_value=0).reset_index())
        ct.to_csv(OUT / "errors_by_source.csv", index=False)
        fich_err = (er.groupby(["article", "source"]).size()
                    .reset_index(name="n_errors"))
        fich_err.to_csv(OUT / "errors_per_fichamento.csv", index=False)

    # --- meta-avaliação: aluno vs juiz -----------------------------------
    meta = []
    for ev in evals:
        art = ev["article_id"]
        sid = pmap[art].get("human_student", "")
        hpos = "A" if pmap[art]["A"] == "human" else "B"
        sa = self_assessment(art) or {}
        for sec in SECS:
            j = (ev["scores"].get(hpos) or {}).get(sec)
            s = sa.get(sec)
            meta.append({"article": art, "student": sid,
                         "judge": ev["judge_id"], "section": sec,
                         "self_score": s, "judge_score": j,
                         "gap": (s - j) if (s is not None and j is not None)
                         else None})
    mdf = pd.DataFrame(meta)
    mdf.to_csv(OUT / "meta_students_long.csv", index=False)
    summ_meta = (mdf.groupby("student")
                 .agg(mean_self=("self_score", "mean"),
                      mean_judge=("judge_score", "mean"),
                      mean_gap=("gap", "mean"),
                      abs_gap=("gap", lambda x: x.abs().mean()),
                      n=("gap", "count"))
                 .round(2).reset_index().sort_values("student"))
    summ_meta.to_csv(OUT / "meta_students.csv", index=False)

    # --- nota baixa (<=4) por fichamento ---------------------------------
    low = (df.assign(low=df.score <= 4)
           .groupby(["article", "source"])["low"].sum()
           .unstack(fill_value=0).reset_index())

    # --- relatório --------------------------------------------------------
    lines = [
        "# Relatório R1 — Avaliações dos juízes (16/16)",
        "",
        f"Avaliações analisadas: {len(evals)} pares, 1 juiz por par.",
        "",
        "## Preferência A/B (métrica primária)",
        "",
        f"- IA preferida: **{n_ai}** | Humano preferido: **{n_hum}**"
        f" | Empate: {n_tie}",
    ]
    if binom:
        lines.append(
            f"- Binomial (excl. empates, n={n_eff}): "
            f"p = {binom.pvalue:.4f} — "
            f"proporção IA = {n_ai / n_eff:.0%}")
    lines += [
        "",
        "## Notas médias por fonte e seção (BARS 1–7)",
        "",
        "| seção | IA | humano |",
        "|---|---|---|",
    ]
    for sec in SECS:
        a = df[(df.source == "ai") & (df.section == sec)]["score"].mean()
        h = df[(df.source == "human") & (df.section == sec)]["score"].mean()
        lines.append(f"| {SEC_PT[sec]} | {a:.2f} | {h:.2f} |")
    lines += [
        f"| **Total** | **{df[df.source=='ai'].score.mean():.2f}** "
        f"| **{df[df.source=='human'].score.mean():.2f}** |",
        "",
        "## Wilcoxon pareado (IA − humano; par = juiz×artigo)",
        "",
        "| seção | n | mediana dif | média dif | p | rank-biserial |",
        "|---|---|---|---|---|---|",
    ]
    for w in wil:
        p = f"{w['p_wilcoxon']}" if w["p_wilcoxon"] is not None else "-"
        rb = f"{w['rank_biserial']}" if w["rank_biserial"] is not None else "-"
        sec = SEC_PT.get(w["section"], w["section"])
        lines.append(
            f"| {sec} | {w['n']} | {w['median_diff']} | "
            f"{w.get('mean_diff','')} | {p} | {rb} |")
    if not er.empty:
        lines += ["", "## Erros por tipo e fonte", "",
                  "| fonte | " + " | ".join(c for c in ct.columns if c != "source") + " | total |",
                  "|---|" + "---|" * len(ct.columns)]
        for _, r in ct.iterrows():
            tot_e = sum(r[c] for c in ct.columns if c != "source")
            lines.append("| " + " | ".join(str(r[c]) for c in ct.columns)
                         + f" | {tot_e} |")
    lines += [
        "",
        "## Meta-avaliação dos alunos (autoavaliação vs juiz)",
        "",
        "| aluno | artigo | média auto | média juiz | gap médio | |gap| médio |",
        "|---|---|---|---|---|---|",
    ]
    for _, r in summ_meta.iterrows():
        art = mdf[mdf.student == r.student]["article"].iloc[0]
        lines.append(
            f"| {r.student} | {art} | {r.mean_self} | {r.mean_judge} | "
            f"{r.mean_gap} | {r.abs_gap} |")
    (OUT / "report.md").write_text("\n".join(lines) + "\n")
    print(f"OK -> {OUT}")
    print(f"preferência: IA {n_ai} x humano {n_hum} (empate {n_tie})")
    if binom:
        print(f"binomial p={binom.pvalue:.4f}")
    print(summ_meta.to_string(index=False))


if __name__ == "__main__":
    main()
