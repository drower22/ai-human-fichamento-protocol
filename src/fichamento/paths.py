"""Central path conventions — every module resolves files through here."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
ARTICLES = DATA / "articles"
PRIVATE = DATA / "private"
PROMPTS = ROOT / "prompts"
SCHEMAS = ROOT / "schemas"
PROTOCOL_FORMS = ROOT / "protocol" / "forms"
REPORTS = ROOT / "analysis" / "reports"

REGISTRY = ARTICLES / "registry.jsonl"


def md_path(article_id: str) -> Path:
    return ARTICLES / "markdown" / f"{article_id}.md"


def manifest_path(article_id: str) -> Path:
    return ARTICLES / "manifests" / f"{article_id}.ingestion.json"


def fichamento_dir(round_: int, source: str) -> Path:
    return DATA / "fichamentos" / f"round{round_}" / source


def fichamento_path(round_: int, article_id: str, source: str) -> Path:
    tag = "AI" if source == "ai" else "HUM"
    return fichamento_dir(round_, source) / f"F-R{round_}-{article_id}-{tag}.json"


def eval_dir(round_: int) -> Path:
    return DATA / "evaluations" / f"round{round_}"


def eval_path(round_: int, article_id: str, judge_id: str) -> Path:
    return eval_dir(round_) / f"E-R{round_}-{article_id}-{judge_id}.json"


def candidates_dir(round_: int) -> Path:
    return DATA / "candidates" / f"round{round_}"


def pool_path(round_: int, article_id: str) -> Path:
    return candidates_dir(round_) / f"{article_id}.candidates.json"


def pool_sheet_path(round_: int, article_id: str) -> Path:
    return candidates_dir(round_) / f"{article_id}.pool.md"


def blindmap_path(round_: int) -> Path:
    return PRIVATE / f"blinding-map-round{round_}.json"


def packets_dir(round_: int) -> Path:
    return PRIVATE / "judge-packets" / f"round{round_}"


def prompt_path(version: str) -> Path:
    """Prompt id IS the filename: 'v{version}.txt' (e.g. '1.0.0-baseline',
    '1.0.0-theory-pool', '1.0.0-theory-verdicts')."""
    p = PROMPTS / f"v{version}.txt"
    if p.exists():
        return p
    available = ", ".join(x.stem for x in sorted(PROMPTS.glob("v*.txt")))
    raise FileNotFoundError(
        f"prompt '{version}' not found. Available: {available}"
    )
