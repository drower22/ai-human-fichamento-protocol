"""Generate AI fichamentos via litellm (multi-provider).

Gate: only runs when the ingestion manifest proves complete coverage and
the markdown checksum still matches. ``--force`` records an override in
the manifest and flags the resulting fichamento (``generator.forced``).
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone

import litellm

from . import paths
from .models import (
    AIGenerator,
    Fichamento,
    FichamentoContent,
    ManifestOverride,
)
from .pdf2md import check_gate
from .registry import load_articles

SCHEMA_HINT = """{
  "executive_summary": "string (~300 palavras)",
  "research_question": "string",
  "theories": [{"name": "...", "tradition": "...", "role": "...", "source_refs": ["p.3/L12"]}],
  "key_concepts": [{"concept": "...", "definition": "...", "source_refs": ["p.N"]}]  // exatamente 3 ou 4,
  "methodology": {"design": "...", "sample_size": int|null, "sector": "...",
                  "period": "...", "methods": ["..."], "source_refs": ["p.N"]},
  "main_findings": [{"finding": "...", "type": "empirical|proposition|model",
                     "source_refs": ["p.N"]}],
  "contribution": {"theoretical": "...", "practical": "..."}
}"""


def _extract_json(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if not m:
            raise ValueError("model output contains no JSON object")
        return json.loads(m.group(0))


def _call_model(model: str, prompt: str, temperature: float) -> tuple[dict, dict]:
    kwargs = dict(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    try:
        resp = litellm.completion(**kwargs, response_format={"type": "json_object"})
    except Exception:
        resp = litellm.completion(**kwargs)
    usage = getattr(resp, "usage", None)
    meta = {
        "input_tokens": getattr(usage, "prompt_tokens", None),
        "output_tokens": getattr(usage, "completion_tokens", None),
    }
    return _extract_json(resp.choices[0].message.content), meta


def generate_article(
    article_id: str,
    round_: int,
    model: str,
    prompt_version: str,
    temperature: float,
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
            temperature, force, overwrite,
        )
