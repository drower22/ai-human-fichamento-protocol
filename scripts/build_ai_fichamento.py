#!/usr/bin/env python3
"""Monta o fichamento de IA de um artigo a partir de um spec escrito após a
leitura integral (data/prep/specs/{ID}.py) e valida contra o schema.

Uso: scripts/build_ai_fichamento.py A02 [--round 1]
O spec define: SUMMARY, RESEARCH_QUESTION, VERDICTS (tuplas id, verdict,
refs, quote, note), KEY_CONCEPTS, METHODOLOGY, FINDINGS, CONTRIBUTION.
"""
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fichamento import paths  # noqa: E402
from fichamento.models import AIGenerator, Fichamento, FichamentoContent  # noqa: E402

MODEL = "claude-sonnet-5.5-medium (execução assistida, sem API)"
MODEL_API = "claude-sonnet-5.5-medium"


def _opt(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default


def main():
    art = sys.argv[1]
    rnd = int(_opt("--round", 1))
    prompt_version = _opt("--prompt-version", "1.0.0-baseline" if rnd == 1 else "1.1.0-calibrated")
    verdicts_version = _opt("--verdicts-version", "1.0.0-theory-verdicts" if rnd == 1 else "1.1.0-theory-verdicts")
    model = MODEL if rnd == 1 else f"{MODEL_API} (execução assistida; spec de leitura integral, sem API)"
    spec_path = paths.DATA / "prep" / "specs" / f"{art}.py"
    spec = importlib.util.spec_from_file_location("spec", spec_path)
    s = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s)

    pool = json.loads((paths.candidates_dir(rnd) / f"{art}.candidates.json").read_text())
    names = {i["item_id"]: i["name"] for i in pool["items"] if i.get("active", True)}
    manifest = json.loads(paths.manifest_path(art).read_text())

    verdicts = [dict(item_id=i, name=names[i], verdict=v, source_refs=r, quote=q, note=n)
                for i, v, r, q, n in s.VERDICTS]
    missing = set(names) - {v["item_id"] for v in verdicts}
    assert not missing, f"itens do pool sem veredito: {missing}"

    content = FichamentoContent.model_validate(dict(
        executive_summary=s.SUMMARY, research_question=s.RESEARCH_QUESTION, theories=[],
        theory_verdicts=verdicts, key_concepts=s.KEY_CONCEPTS, methodology=s.METHODOLOGY,
        main_findings=s.FINDINGS, contribution=s.CONTRIBUTION))

    fich = Fichamento(
        fichamento_id=f"F-R{rnd}-{art}-AI", article_id=art, round=rnd, source="ai",
        generator=AIGenerator(
            provider="anthropic", model=model, prompt_version=prompt_version,
            temperature=None, generated_at=datetime.now(timezone.utc),
            md_sha256=manifest["md_sha256"], forced=False,
            verdicts_prompt_version=verdicts_version),
        content=content)
    out = paths.fichamento_path(rnd, art, "ai")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(fich.model_dump_json(indent=2))
    print("ok", out.name, "| resumo palavras:", len(s.SUMMARY.split()))


if __name__ == "__main__":
    main()
