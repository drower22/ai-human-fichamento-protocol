#!/usr/bin/env python3
"""Gera índice de evidências por artigo: onde cada item do pool de teorias
é mencionado no markdown numerado. Artefato de preparação — não substitui
a leitura integral; serve para localizar rapidamente os trechos dos
vereditos durante a geração dos fichamentos de IA.

Saída: data/prep/{article}.evidence.txt
Uso: scripts/evidence_index.py [A01 A02 ...]  (sem args = todos da R1/R2)
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fichamento import paths  # noqa: E402
from fichamento.candidates import load_pool  # noqa: E402
from fichamento.registry import load_articles  # noqa: E402

STOP = {"teoria", "theory", "aplicada", "applied", "perspectiva", "perspective",
        "organizacional", "organizational", "estratégia", "strategy", "sobre",
        "para", "como", "com", "das", "dos", "uma", "the", "and", "de", "da",
        "do", "a", "o", "e", "em", "à", "ao", "ou", "na", "no", "ética",
        "ethics", "kantiana", "deontologia"}


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def stems(name):
    """Radicais de busca a partir do nome do item (palavras >=5 letras)."""
    out = set()
    for w in re.findall(r"[A-Za-zÀ-ÿ-]{4,}", name):
        w = norm(w)
        if w in STOP:
            continue
        out.add(re.escape(w[:6]))  # radical: prefixo de 6 letras
    return out


def main():
    arts = sys.argv[1:] or [a.article_id for a in load_articles(1)]
    prep = paths.DATA / "prep"
    prep.mkdir(exist_ok=True)
    for art in arts:
        md = paths.md_path(art).read_text().splitlines()
        lines = [(m.group(1), m.group(2))
                 for ln in md if (m := re.match(r"(L\d+)\| ?(.*)", ln))]
        # mapa L -> página
        page_of, cur = {}, None
        for ln in md:
            if (m := re.match(r"<<p\.(\d+)", ln)):
                cur = int(m.group(1))
            elif (m := re.match(r"L(\d+)\|", ln)) and cur:
                page_of[int(m.group(1))] = cur

        pool = load_pool(1, art) or load_pool(2, art)
        out = [f"# Índice de evidências — {art} ({len(lines)} linhas)", ""]
        for it in (pool.items if pool else []):
            pats = stems(it.name) or {re.escape(norm(it.name)[:8])}
            hits = [lid for lid, txt in lines
                    if any(re.search(p, norm(txt)) for p in pats)]
            if not it.active:
                continue
            refs = ", ".join(f"{lid}(p.{page_of[int(lid[1:])]})" for lid in hits) or "—"
            out.append(f"{it.item_id} {it.name}")
            out.append(f"  radical: {' | '.join(sorted(pats))}")
            out.append(f"  {refs}")
            out.append("")
        (prep / f"{art}.evidence.txt").write_text("\n".join(out))
        print(f"{art}: indexado ({len(lines)} linhas)")


if __name__ == "__main__":
    main()
