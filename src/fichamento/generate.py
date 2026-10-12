"""Generate AI fichamentos via litellm (multi-provider).

Gate: only runs when the ingestion manifest proves complete coverage and
the markdown checksum still matches. ``--force`` records an override in
the manifest and flags the resulting fichamento (``generator.forced``).
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone

from . import paths
from .llm import call_model as _call_model
from .models import (
    AIGenerator,
    Fichamento,
    FichamentoContent,
    ManifestOverride,
    TheoryVerdict,
)
from .pdf2md import check_gate
from .registry import load_articles

SCHEMA_HINT = """{
  "executive_summary": "string (~300 palavras)",
  "research_question": "string",
  "theories": [{"name": "...", "tradition": "...", "role": "...",
                "source_refs": ["p.3/L12"]}]
      // somente teorias relevantes FORA do pool de candidatos; [] se nenhuma,
  "theory_verdicts": []  // preenchido por chamada separada; responda [],
  "key_concepts": [{"concept": "...", "definition": "...", "quote": "trecho literal",
                    "source_refs": ["p.N"]}]  // exatamente 3 ou 4,
  "methodology": {"study_type": "teórico|empírico|...", "design": "...",
                  "sample_type": "...", "sample_size": int|null, "sector": "...",
                  "period": "...", "methods": ["..."],
                  "analysis_note": "...", "source_refs": ["p.N"]},
  "main_findings": [{"finding": "...", "type": "empirical|proposition|model",
                     "quote": "trecho literal", "source_refs": ["p.N"]}],
  "contribution": {"theoretical": "...", "practical": "..."}
}"""


def classify_theory_pool(
    article_id: str,
    round_: int,
    model: str,
    verdicts_version: str,
    temperature: float,
    md: str,
) -> tuple[list[TheoryVerdict], str | None]:
    """Second, independent call: the model assigns uses/discusses/
    does_not_use to each item of the candidate pool — the same closed task
    students perform, enabling per-item AI×human agreement."""
    from .candidates import VERDICT_SCHEMA_HINT, load_pool

    pool = load_pool(round_, article_id)
    if pool is None:
        return [], None
    cand = [
        {"item_id": i.item_id, "name": i.name, "tradition": i.tradition,
         "definition": i.definition}
        for i in pool.items if i.active
    ]
    if not cand:
        return [], None
    tpl = paths.prompt_path(verdicts_version).read_text()
    prompt = tpl.format(
        schema_hint=VERDICT_SCHEMA_HINT,
        candidates=json.dumps(cand, ensure_ascii=False, indent=1),
        document=md,
    )
    data, _ = _call_model(model, prompt, temperature)
    by_id = {i.item_id: i for i in pool.items}
    verdicts = [
        TheoryVerdict(
            item_id=v["item_id"],
            name=v.get("name") or by_id[v["item_id"]].name,
            verdict=v["verdict"],
            source_refs=v.get("source_refs", []),
            note=v.get("note", ""),
        )
        for v in data.get("verdicts", [])
        if v.get("item_id") in by_id
    ]
    return verdicts, verdicts_version


def generate_article(
    article_id: str,
    round_: int,
    model: str,
    prompt_version: str,
    temperature: float,
    verdicts_version: str | None = "1.0.0-theory-verdicts",
    force: bool = False,
    overwrite: bool = False,
) -> Fichamento | None:
    out = paths.fichamento_path(round_, article_id, "ai")
    if out.exists() and not overwrite:
        print(f"{article_id}: fichamento exists, skipping (use --overwrite)")
        return None

    manifest, problems = check_gate(article_id)
    if manifest is None:
        print(f"{article_id}: {problems[0]}")
        return None
    if problems and not force:
        for p in problems:
            print(f"{article_id}: GATE — {p}")
        return None
    if problems and force:
        manifest.overrides.append(
            ManifestOverride(
                reason="; ".join(problems),
                by="generate --force",
                at=datetime.now(timezone.utc),
            )
        )
        paths.manifest_path(article_id).write_text(
            manifest.model_dump_json(indent=2)
        )

    md = (paths.ROOT / manifest.md_path).read_text()
    prompt_template = paths.prompt_path(prompt_version).read_text()
    prompt = prompt_template.format(schema_hint=SCHEMA_HINT, document=md)

    t0 = time.time()
    data, meta = _call_model(model, prompt, temperature)
    try:
        content = FichamentoContent.model_validate(data)
    except Exception as e:
        # one repair retry: show the model its own validation error
        retry_prompt = (
            prompt
            + f"\n\nATENÇÃO: sua resposta anterior falhou na validação do "
              f"schema ({e}). Responda novamente APENAS o JSON corrigido."
        )
        data, meta2 = _call_model(model, retry_prompt, temperature)
        content = FichamentoContent.model_validate(data)
        meta = {k: (meta.get(k) or 0) + (meta2.get(k) or 0) or None for k in meta}

    used_verdicts_version = None
    if verdicts_version:
        verdicts, used_verdicts_version = classify_theory_pool(
            article_id, round_, model, verdicts_version, temperature, md
        )
        if verdicts:
            content.theory_verdicts = verdicts

    provider = model.split("/")[0] if "/" in model else "openai"
    fich = Fichamento(
        fichamento_id=f"F-R{round_}-{article_id}-AI",
        article_id=article_id,
        round=round_,  # type: ignore[arg-type]
        source="ai",
        generator=AIGenerator(
            provider=provider,
            model=model,
            prompt_version=prompt_version,
            temperature=temperature,
            generated_at=datetime.now(timezone.utc),
            input_tokens=meta["input_tokens"],
            output_tokens=meta["output_tokens"],
            latency_s=round(time.time() - t0, 2),
            md_sha256=manifest.md_sha256,
            forced=bool(problems),
            verdicts_prompt_version=used_verdicts_version,
        ),
        content=content,
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(fich.model_dump_json(indent=2))
    print(
        f"{article_id}: fichamento gerado ({model}, "
        f"{meta['output_tokens'] or '?'} tokens out)"
        + (" [FORCED]" if problems else "")
    )
    return fich


def generate_round(
    round_: int,
    model: str,
    prompt_version: str,
    temperature: float = 0.2,
    verdicts_version: str | None = "1.0.0-theory-verdicts",
    force: bool = False,
    overwrite: bool = False,
) -> None:
    articles = load_articles(round_)
    if not articles:
        print(f"no articles registered for round {round_}")
        return
    for a in articles:
        generate_article(
            a.article_id, round_, model, prompt_version,
            temperature, verdicts_version, force, overwrite,
        )
