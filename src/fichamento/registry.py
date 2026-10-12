"""Load and validate the article registry."""

from __future__ import annotations

import json

from . import paths
from .models import ArticleEntry


def load_articles(round_: int | None = None) -> list[ArticleEntry]:
    if not paths.REGISTRY.exists():
        raise FileNotFoundError(
            f"{paths.REGISTRY} not found — register articles first "
            "(see data/README.md)"
        )
    articles: list[ArticleEntry] = []
    for i, line in enumerate(paths.REGISTRY.read_text().splitlines(), 1):
        if not line.strip():
            continue
        articles.append(ArticleEntry.model_validate(json.loads(line)))
    if round_ is not None:
        articles = [a for a in articles if a.round == round_]
    return articles
