"""Quantitative analysis: BARS scores, paired tests, error rates,
pairwise preference (binomial + Bradley–Terry over producers), and
inter-rater reliability (Krippendorff alpha, interval metric).

Outputs land in analysis/reports/round{N}/ as CSVs + report.md.
"""

from __future__ import annotations

import json
import math
from itertools import combinations

import pandas as pd
from scipy import stats

from . import paths
from .blind import load_blindmap
from .candidates import load_pool
from .models import ERROR_CODES, SECTIONS, Evaluation, Fichamento


def _load_evals(round_: int) -> list[Evaluation]:
    out = []
    for p in sorted(paths.eval_dir(round_).glob("*.json")):
        out.append(Evaluation.model_validate_json(p.read_text()))
    return out


def _long_scores(round_: int) -> pd.DataFrame:
    bmap = {e.blind_id: e for e in load_blindmap(round_).entries}
    rows = []
    for ev in _load_evals(round_):
        for r in ev.ratings:
            entry = bmap[r.blind_id]
            for sec in SECTIONS:
                rows.append(
                    {
                        "round": round_,
                        "article_id": ev.article_id,
                        "judge_id": ev.judge_id,
                        "blind_id": r.blind_id,
                        "position": r.position,
                        "source": entry.source,
                        "fichamento_id": entry.fichamento_id,
                        "section": sec,
                        "score": getattr(r.scores, sec),
                    }
                )
    return pd.DataFrame(rows)


def _long_errors(round_: int) -> pd.DataFrame:
    bmap = {e.blind_id: e for e in load_blindmap(round_).entries}
    rows = []
    for ev in _load_evals(round_):
        for r in ev.ratings:
            entry = bmap[r.blind_id]
            for ef in r.errors:
                rows.append(
                    {
                        "round": round_,
                        "article_id": ev.article_id,
                        "judge_id": ev.judge_id,
                        "source": entry.source,
                        "code": ef.code,
                        "sections": ";".join(ef.sections),
                        "note": ef.note,
                    }
                )
    return pd.DataFrame(rows)


def _preferences(round_: int) -> pd.DataFrame:
    bmap = load_blindmap(round_)
    pos2src = {
        (e.article_id, e.position): (e.source, e.fichamento_id)
        for e in bmap.entries
    }
    rows = []
    for ev in _load_evals(round_):
        choice = ev.preference.choice
        src = pos2src.get((ev.article_id, choice), (None, None))[0] if choice in "AB" else "tie"
        rows.append(
            {
                "round": round_,
                "article_id": ev.article_id,
                "judge_id": ev.judge_id,
                "choice": choice,
                "preferred_source": src,
            }
        )
    return pd.DataFrame(rows)


def _wilcoxon_table(scores: pd.DataFrame) -> pd.DataFrame:
    out = []
    for sec in SECTIONS:
        sub = scores[scores.section == sec]
        pivot = sub.pivot_table(
            index=["article_id", "judge_id"], columns="source",
            values="score", aggfunc="first",
        ).dropna()
        if pivot.empty:
            continue
        diffs = pivot.get("ai", pd.Series(dtype=float)) - pivot.get(
            "human", pd.Series(dtype=float)
        )
        diffs = diffs.dropna()
        n = len(diffs)
        if n and (diffs != 0).any():
            res = stats.wilcoxon(diffs)
            # normal approx for z -> effect size r = z/sqrt(N)
            w = res.statistic
            mu, sigma = n * (n + 1) / 4, math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
            z = (w - mu) / sigma if sigma else 0.0
            out.append(
                {
                    "section": sec,
                    "n_pairs": n,
                    "mean_ai": pivot["ai"].mean(),
                    "mean_human": pivot["human"].mean(),
                    "median_diff": diffs.median(),
                    "wilcoxon_p": res.pvalue,
                    "effect_r": z / math.sqrt(n) if n else None,
                }
            )
        else:
            out.append({"section": sec, "n_pairs": n, "mean_ai": pivot["ai"].mean(),
                        "mean_human": pivot["human"].mean(), "median_diff": 0,
                        "wilcoxon_p": None, "effect_r": None})
    return pd.DataFrame(out)


def _krippendorff_alpha(scores: pd.DataFrame) -> pd.DataFrame:
    """Interval-metric Krippendorff alpha: units=fichamentos, raters=judges."""
    out = []
    for sec in SECTIONS:
        sub = scores[scores.section == sec]
        pivot = sub.pivot_table(index="blind_id", columns="judge_id",
                                values="score", aggfunc="first")
        values = [v for col in pivot.columns for v in pivot[col].dropna()]
        cats = sorted(set(values))
        if len(cats) < 2:
            out.append({"section": sec, "alpha": None, "n_units": len(pivot)})
            continue
        n_raters = pivot.shape[1]
        # Do: mean pairwise squared distance within units
        do = 0.0
        n_pairs = 0
        for _, row in pivot.iterrows():
            vals = row.dropna().tolist()
            for a, b in combinations(vals, 2):
                do += (a - b) ** 2
                n_pairs += 1
        do = do / n_pairs if n_pairs else 0.0
        # De: expected distance over all value pairs weighted by marginals
        freqs = pd.Series(values).value_counts(normalize=True)
        de = sum(
            freqs[a] * freqs[b] * (a - b) ** 2
            for a in cats for b in cats
        )
        out.append(
            {"section": sec, "alpha": 1 - do / de if de else None,
             "n_units": len(pivot), "n_raters": n_raters}
        )
    return pd.DataFrame(out)


def _bradley_terry(pref: pd.DataFrame, fich_src: pd.DataFrame) -> pd.DataFrame:
    """BT ranking over PRODUCERS: 'AI' + each student Sxx.

    Each non-tie preference = one match between the AI producer and the
    human producer of that article's fichamentos.
    """
    prod_of = fich_src.set_index("fichamento_id")["producer"].to_dict()
    bmap_cache: dict[int, dict] = {}
    matches = []
    for _, r in pref[pref.choice.isin(["A", "B"])].iterrows():
        bmap = bmap_cache.setdefault(
            r["round"], {e.blind_id: e for e in load_blindmap(r["round"]).entries}
        )
        # find fichamento ids of both positions of this article
        arts = {e.position: e for e in bmap.values() if e.article_id == r["article_id"]}
        if r["choice"] not in arts or len(arts) < 2:
            continue
        winner = prod_of.get(arts[r["choice"]].fichamento_id)
        loser_pos = "B" if r["choice"] == "A" else "A"
        loser = prod_of.get(arts[loser_pos].fichamento_id)
        if winner and loser:
            matches.append((winner, loser))
    players = sorted({p for m in matches for p in m})
    if not players or not matches:
        return pd.DataFrame(columns=["producer", "bt_rating", "wins", "matches"])
    wins = {p: 0 for p in players}
    n_ij = {tuple(sorted(m)): 0 for m in matches}
    for w, l in matches:
        wins[w] += 1
        n_ij[tuple(sorted((w, l)))] += 1
    w_ = {p: 1.0 for p in players}
    for _ in range(200):
        w_new = {}
        for i in players:
            denom = sum(
                n_ij.get(tuple(sorted((i, j))), 0) / (w_[i] + w_[j])
                for j in players if j != i
            )
            w_new[i] = wins[i] / denom if denom > 0 else w_[i]
        s = sum(w_new.values())
        w_ = {p: v / s for p, v in w_new.items()}
    return pd.DataFrame(
        [{"producer": p, "bt_rating": w_[p], "wins": wins[p],
          "matches": sum(v for k, v in n_ij.items() if p in k)}
         for p in players]
    ).sort_values("bt_rating", ascending=False)


def _load_fich(round_: int, article_id: str, source: str) -> Fichamento | None:
    p = paths.fichamento_path(round_, article_id, source)
    return Fichamento.model_validate_json(p.read_text()) if p.exists() else None


def _theory_agreement(round_: int) -> pd.DataFrame:
    """Per-item AI×human agreement on the closed theory pool.

    Surfaces two objective error signals: AI candidate rejections
    (humans mark does_not_use on ai-origin items) and AI omissions
    (theories students added beyond the pool via content.theories)."""
    article_ids = sorted(
        {p.name.split("-")[2]
         for p in paths.fichamento_dir(round_, "ai").glob("*.json")}
    )
    rows = []
    for aid in article_ids:
        pool = load_pool(round_, aid)
        ai = _load_fich(round_, aid, "ai")
        if pool is None or ai is None:
            continue
        ai_v = {v.item_id: v.verdict for v in ai.content.theory_verdicts}
        hum_files = sorted(
            paths.fichamento_dir(round_, "human").glob(f"F-R{round_}-{aid}-*.json")
        )
        for hum_path in hum_files:
            hum = Fichamento.model_validate_json(hum_path.read_text())
            sid = getattr(hum.generator, "participant_id", "?")
            hum_v = {v.item_id: v for v in hum.content.theory_verdicts}
            for item in pool.items:
                if not item.active:
                    continue
                hv = hum_v.get(item.item_id)
                rows.append({
                    "article_id": aid, "item_id": item.item_id,
                    "theory": item.name, "origin": item.origin,
                    "ai_verdict": ai_v.get(item.item_id),
                    "human_verdict": hv.verdict if hv else None,
                    "student": sid,
                    "agree": bool(hv) and ai_v.get(item.item_id) == hv.verdict,
                })
            for extra in hum.content.theories:
                rows.append({
                    "article_id": aid, "item_id": "+ADD", "theory": extra.name,
                    "origin": "human_added", "ai_verdict": None,
                    "human_verdict": "added", "student": sid, "agree": None,
                })
    return pd.DataFrame(rows)


def analyze(rounds: list[int]) -> None:
    out_root = paths.REPORTS
    out_root.mkdir(parents=True, exist_ok=True)
    per_round = {}
    for r in rounds:
        out_dir = out_root / f"round{r}"
        out_dir.mkdir(parents=True, exist_ok=True)

        tag = _theory_agreement(r)
        if not tag.empty:
            tag.to_csv(out_dir / "theory_agreement.csv", index=False)
            n_rej = int(((tag.origin == "ai") & (tag.human_verdict == "does_not_use")).sum())
            n_add = int((tag.origin == "human_added").sum())
            ok = tag.agree.dropna()
            print(f"  teorias: concordância IA×humano {ok.mean():.0%} ({len(ok)} itens) | "
                  f"candidatos rejeitados: {n_rej} | adições humanas: {n_add}")

        evals = _load_evals(r)
        if not evals:
            print(f"round {r}: no evaluations yet")
            continue
        scores, errors, pref = _long_scores(r), _long_errors(r), _preferences(r)
        per_round[r] = (scores, errors, pref)

        scores.to_csv(out_dir / "scores_long.csv", index=False)
        errors.to_csv(out_dir / "errors_long.csv", index=False)
        pref.to_csv(out_dir / "preferences.csv", index=False)

        summ = (scores.groupby(["source", "section"])["score"]
                .agg(["count", "mean", "std", "median"]).round(3))
        summ.to_csv(out_dir / "scores_by_source.csv")

        wil = _wilcoxon_table(scores)
        wil.to_csv(out_dir / "wilcoxon_paired.csv", index=False)

        alpha = _krippendorff_alpha(scores)
        alpha.to_csv(out_dir / "krippendorff_alpha.csv", index=False)

        if not errors.empty:
            etab = (errors.groupby(["source", "code"]).size()
                    .unstack(fill_value=0)
                    .reindex(columns=ERROR_CODES, fill_value=0))
        else:
            etab = pd.DataFrame(columns=ERROR_CODES)
        etab.to_csv(out_dir / "errors_by_source.csv")

        n_ai = int((pref.preferred_source == "ai").sum())
        n_hum = int((pref.preferred_source == "human").sum())
        n_tie = int((pref.preferred_source == "tie").sum())
        bt = stats.binomtest(n_ai, n_ai + n_hum) if (n_ai + n_hum) else None
        with open(out_dir / "preference_test.json", "w") as fh:
            json.dump(
                {"ai_wins": n_ai, "human_wins": n_hum, "ties": n_tie,
                 "binom_p": bt.pvalue if bt else None},
                fh, indent=2,
            )

        fich_rows = []
        for r_, (sc, _, _) in per_round.items():
            fdf = sc[["fichamento_id", "source"]].drop_duplicates()
            fich_rows.append(fdf)
        fich_df = pd.concat(fich_rows).drop_duplicates("fichamento_id")
        fich_df["producer"] = fich_df.apply(
            lambda x: "AI" if x["source"] == "ai"
            else _student_of(x["fichamento_id"]),
            axis=1,
        )
        bt_df = _bradley_terry(pref, fich_df)
        bt_df.to_csv(out_dir / "bradley_terry_producers.csv", index=False)

        _write_report(out_dir, r, summ, wil, alpha, etab,
                      {"ai_wins": n_ai, "human_wins": n_hum, "ties": n_tie,
                       "binom_p": bt.pvalue if bt else None})
        print(f"round {r}: report → {out_dir / 'report.md'}")

    if len(per_round) == 2:
        _round_comparison(per_round, out_root)


def _student_of(fichamento_id: str) -> str:
    for p in paths.DATA.glob(f"fichamentos/round*/human/{fichamento_id}.json"):
        return json.loads(p.read_text())["generator"]["participant_id"]
    return "?"


def _md_table(df: pd.DataFrame) -> str:
    return "```\n" + df.round(3).to_string() + "\n```"


def _write_report(out_dir, r, summ, wil, alpha, etab, pref) -> None:
    lines = [
        f"# Análise — Rodada {r}",
        "",
        "## Notas médias por fonte e seção (BARS 1–7)",
        _md_table(summ.reset_index()),
        "",
        "## Comparação pareada IA − Humano (Wilcoxon; pares juiz×artigo)",
        _md_table(wil),
        "",
        "## Concordância inter-rater (Krippendorff α, métrica intervalar)",
        _md_table(alpha),
        "",
        "## Erros por tipo e fonte (contagem de flags)",
        _md_table(etab.reset_index()) if not etab.empty else "_sem flags_",
        "",
        "## Preferência A/B (métrica primária)",
        f"- IA preferida: **{pref['ai_wins']}** | Humana: **{pref['human_wins']}**"
        f" | Empates: {pref['ties']}",
        f"- Teste binomial (excl. empates): p = {pref['binom_p']}",
        "",
        "_Detalhe por produtor: bradley_terry_producers.csv_",
    ]
    (out_dir / "report.md").write_text("\n".join(lines))


def _round_comparison(per_round, out_root) -> None:
    rows = []
    for r, (scores, errors, pref) in per_round.items():
        s = scores.groupby(["source", "section"])["score"].mean()
        for (src, sec), v in s.items():
            rows.append({"round": r, "source": src, "section": sec,
                         "mean": v})
    df = pd.DataFrame(rows)
    piv = df.pivot_table(index=["source", "section"], columns="round",
                         values="mean")
    piv.columns = [f"mean_R{c}" for c in piv.columns]
    piv["delta_R2_minus_R1"] = piv.get("mean_R2", pd.Series(dtype=float)) - \
        piv.get("mean_R1", pd.Series(dtype=float))
    piv.round(3).to_csv(out_root / "round_comparison.csv")
    print(f"comparação R1→R2 → {out_root / 'round_comparison.csv'}")
