#!/usr/bin/env python3
"""Audita um fichamento contra o markdown numerado do artigo.

Para cada source_ref (p.N/Lnn): confere formato, se a linha existe na
página indicada e — quando há quote literal — se ela consta no trecho
referenciado (tolerando quebras de linha e hifenização).

Uso: scripts/verify_fichamento.py A01 [--round 1] [--source ai]
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fichamento import paths  # noqa: E402


def load_md(article_id):
    page_lines, cur, text = {}, None, {}
    for ln in paths.md_path(article_id).read_text().splitlines():
        m = re.match(r"<<p\.(\d+)", ln)
        if m:
            cur = int(m.group(1))
            page_lines[cur] = []
            continue
        m = re.match(r"L(\d+)\| ?(.*)", ln)
        if m and cur:
            page_lines[cur].append(int(m.group(1)))
            text[int(m.group(1))] = m.group(2)
    return page_lines, text


REF = re.compile(r"p\.(\d+)(?:/L(\d+)(?:-(\d+))?)?")


def main():
    args = sys.argv[1:]
    art = args[0]
    round_ = int(args[args.index("--round") + 1]) if "--round" in args else 1
    source = args[args.index("--source") + 1] if "--source" in args else "ai"

    page_lines, text = load_md(art)
    all_lines = sorted(text)
    print(f"{art}: {len(all_lines)} linhas L001..L{all_lines[-1]:03d} | "
          f"contíguas: {all_lines == list(range(1, len(all_lines) + 1))} | "
          f"{len(page_lines)} páginas")

    def span(ref):
        m = REF.fullmatch(ref)
        p = int(m.group(1))
        if not m.group(2):
            return p, page_lines[p]
        a, b = int(m.group(2)), int(m.group(3) or m.group(2))
        return p, list(range(a, b + 1))

    errs = n_refs = 0

    def check_ref(ref, where):
        nonlocal errs
        if not REF.fullmatch(ref):
            print(f"FORMATO INVÁLIDO {where}: {ref!r}")
            errs += 1
            return None
        p, ls = span(ref)
        bad = [n for n in ls if n not in page_lines.get(p, [])]
        if bad:
            print(f"LINHA FORA DA PÁGINA {where}: {ref} -> {bad[:4]}")
            errs += 1
            return None
        return ls

    def joined(lines):
        out = ""
        for n in lines:
            t = text[n].strip()
            out = (out[:-1] + t) if out.endswith("-") else ((out + " " + t) if out else t)
        return re.sub(r"\s+", " ", out)

    def check_quote(q, refs, where):
        nonlocal errs
        lines = []
        for r in refs:
            ls = check_ref(r, where)
            if ls:
                lines += ls
        if not q or not lines:
            return
        pool = joined(sorted(set(lines)))
        raw = "".join(text[n].strip() for n in sorted(set(lines))).replace("-", "")
        ok = (re.sub(r"\s+", " ", q) in pool
              or re.sub(r"[\s-]", "", q) in raw.replace(" ", ""))
        if not ok:
            print(f"QUOTE NÃO ENCONTRADA {where}: {q[:80]}")
            errs += 1

    path = paths.fichamento_path(round_, art, source)
    d = json.load(open(path))
    c = d["content"] if "content" in d else d

    for blob in (c.get("executive_summary", ""), c.get("research_question", ""),
                 (c.get("contribution") or {}).get("theoretical", ""),
                 (c.get("contribution") or {}).get("practical", ""),
                 (c.get("methodology") or {}).get("analysis_note", "")):
        for r in re.findall(r"p\.\d+/L\d+(?:-\d+)?", blob):
            check_ref(r, "inline")
            n_refs += 1

    for v in c.get("theory_verdicts", []):
        if v["verdict"] != "does_not_use" and not v["source_refs"]:
            print(f"VEREDITO SEM REF {v['item_id']}")
            errs += 1
        check_quote(v.get("quote", ""), v["source_refs"], f"veredito {v['item_id']}")
        n_refs += len(v["source_refs"])
    for k in c.get("key_concepts", []):
        check_quote(k.get("quote", ""), k["source_refs"], f"conceito {k['concept'][:20]}")
        n_refs += len(k["source_refs"])
    for f in c.get("main_findings", []):
        check_quote(f.get("quote", ""), f["source_refs"], f"achado {f['finding'][:25]}")
        n_refs += len(f["source_refs"])
    for r in (c.get("methodology") or {}).get("source_refs", []):
        check_ref(r, "metodologia")
        n_refs += 1

    print(f"refs: {n_refs} | erros: {errs} | {path.name}")
    return errs


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
