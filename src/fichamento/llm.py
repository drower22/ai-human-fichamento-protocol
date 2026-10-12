"""Shared litellm helpers — model call + robust JSON extraction."""

from __future__ import annotations

import json
import re

import litellm


def extract_json(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if not m:
            raise ValueError("model output contains no JSON object")
        return json.loads(m.group(0))


def call_model(model: str, prompt: str, temperature: float) -> tuple[dict, dict]:
    """Returns (parsed_json, usage_meta). Retries without json-mode if the
    provider rejects response_format."""
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
    return extract_json(resp.choices[0].message.content), meta
