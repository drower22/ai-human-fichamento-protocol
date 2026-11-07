"""CLI entry point — `fichamento <command>`.

Commands:
  pdf2md        PDF -> line-marked markdown + ingestion manifest
  generate      AI fichamentos (litellm; gated on the manifest)
  import-human  wrap a student's content-JSON into a full fichamento
  blind         assign A/B positions, write private map + judge packets
  ingest        Google Forms CSV -> evaluation JSONs
  validate      validate all data artefacts against the schemas
  analyze       stats + report per round
  export-kg     nodes/edges JSONL for knowledge graphs
  schemas       regenerate schemas/*.schema.json from the models
"""

from __future__ import annotations

import argparse
import json
import sys

from . import paths


def main() -> None:
    ap = argparse.ArgumentParser(prog="fichamento")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pdf2md", help="PDF -> markdown com manifesto de ingestão")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--article", help="só um artigo (ex.: A03)")
    p.add_argument("--ocr-lang", default="por+eng")

    p = sub.add_parser("numbered-pdf",
                       help="PDF -> versão numerada (rótulos p.N Lnnn nas margens)")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--article", help="só um artigo (ex.: A03)")

    p = sub.add_parser("candidates", help="IA extrai pool de teorias candidatas")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--prompt-version", default="1.0.0-theory-pool")
    p.add_argument("--temperature", type=float, default=0.2)
    p.add_argument("--article", help="só um artigo")
    p.add_argument("--force", action="store_true")
    p.add_argument("--overwrite", action="store_true")

    p = sub.add_parser("generate", help="gera fichamentos de IA (com gate)")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--model", required=True,
                   help="string litellm, ex.: gpt-4o | claude-sonnet-4-5 | gemini/gemini-2.0-flash")
    p.add_argument("--prompt-version", required=True,
                   help="id do prompt = nome do arquivo, ex.: 1.0.0-baseline")
    p.add_argument("--verdicts-version", default="1.0.0-theory-verdicts",
                   help="prompt da classificação do pool; 'none' desativa")
    p.add_argument("--temperature", type=float, default=0.2)
    p.add_argument("--article", help="só um artigo")
    p.add_argument("--force", action="store_true",
                   help="registra override do gate no manifest")
    p.add_argument("--overwrite", action="store_true")

    p = sub.add_parser("import-human", help="importa fichamento de estudante")
    p.add_argument("--round", type=int, choices=[0, 1, 2], required=True,
                   help="0 = piloto")
    p.add_argument("--article", help="A01…A32; omita se o JSON já trouxer (ex.: PILOTO)")
    p.add_argument("--file", required=True,
                   help="JSON de conteúdo (template ou gerado pelo form HTML)")
    p.add_argument("--participant", help="S01…S{nn}; omita se o JSON já trouxer")
    p.add_argument("--minutes", type=int)
    p.add_argument("--overwrite", action="store_true")

    p = sub.add_parser("import-human-csv",
                       help="CSV do Forms (fichamento do estudante) -> JSONs")
    p.add_argument("--round", type=int, choices=[0, 1, 2], required=True,
                   help="0 = piloto")
    p.add_argument("--csv", required=True)
    p.add_argument("--map", help="student-column-map.json alternativo")
    p.add_argument("--pool", help="pool JSON p/ resolver nomes dos itens")

    p = sub.add_parser("assign", help="sorteia artigos→estudantes (grupos cruzados)")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--groups", help="groups.json (default: data/private/groups.json)")
    p.add_argument("--mode", choices=["groups", "per-student"], default="groups",
                   help="'groups' = cruzamento por grupo; 'per-student' = 1 artigo/aluno, só restrição orientador")

    p = sub.add_parser("blind", help="cegamento A/B + pacotes dos juízes")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--seed", type=int, default=42)

    p = sub.add_parser("ingest", help="CSV do Google Forms -> avaliações JSON")
    p.add_argument("--round", type=int, choices=[1, 2], required=True)
    p.add_argument("--csv", required=True)
    p.add_argument("--map", help="column-map.json alternativo")

    sub.add_parser("validate", help="valida todos os artefatos em data/")

    p = sub.add_parser("analyze", help="análise quantitativa")
    p.add_argument("--round", type=int, choices=[1, 2], action="append")
    p.add_argument("--all", action="store_true", help="ambas as rodadas")
    p.add_argument("--exclude-judge", action="append", default=[],
                   help="sensibilidade: descarta avaliações destes juízes (repetível)")

    p = sub.add_parser("export-kg", help="exporta nós/arestas JSONL")
    p.add_argument("--out", default=str(paths.REPORTS / "kg"))
    p.add_argument("--source", choices=["ai", "human", "both"], default="both")

    sub.add_parser("schemas", help="regenera schemas/*.schema.json")

    args = ap.parse_args()

    if args.cmd == "numbered-pdf":
        from .numberpdf import number_article
        from .registry import load_articles
        for a in load_articles(args.round):
            if args.article and a.article_id != args.article:
                continue
            number_article(a)
        return

    if args.cmd == "pdf2md":
        from .pdf2md import convert
        from .registry import load_articles
        arts = load_articles(args.round)
        for a in arts:
            if args.article and a.article_id != args.article:
                continue
            convert(a, ocr_lang=args.ocr_lang)

    elif args.cmd == "candidates":
        from .candidates import build_pool, build_round
        if args.article:
            build_pool(args.article, args.round, args.model,
                       args.prompt_version, args.temperature,
                       args.force, args.overwrite)
        else:
            build_round(args.round, args.model, args.prompt_version,
                        args.temperature, args.force, args.overwrite)

    elif args.cmd == "generate":
        from .generate import generate_article, generate_round
        vv = None if args.verdicts_version.lower() == "none" else args.verdicts_version
        if args.article:
            generate_article(args.article, args.round, args.model,
                             args.prompt_version, args.temperature,
                             vv, args.force, args.overwrite)
        else:
            generate_round(args.round, args.model, args.prompt_version,
                           args.temperature, vv, args.force, args.overwrite)

    elif args.cmd == "import-human":
        from .ingest import import_human
        import_human(args.round, args.article, args.file,
                     args.participant, args.minutes, args.overwrite)

    elif args.cmd == "import-human-csv":
        from .ingest import import_human_csv
        import_human_csv(args.round, args.csv, args.map, args.pool)

    elif args.cmd == "assign":
        from .assign import assign, assign_per_student
        if args.mode == "per-student":
            assign_per_student(args.round, args.seed, args.groups)
        else:
            assign(args.round, args.seed, args.groups)

    elif args.cmd == "blind":
        from .blind import create_blinding
        create_blinding(args.round, args.seed)

    elif args.cmd == "ingest":
        from .ingest import ingest_forms_csv
        ingest_forms_csv(args.round, args.csv, args.map)

    elif args.cmd == "validate":
        from .validate import validate_all
        sys.exit(validate_all())

    elif args.cmd == "analyze":
        from .analyze import analyze
        rounds = [1, 2] if args.all else (args.round or [])
        if not rounds:
            ap.error("informe --round N ou --all")
        analyze(rounds, tuple(args.exclude_judge))

    elif args.cmd == "export-kg":
        from .kg import export_kg
        srcs = ["ai", "human"] if args.source == "both" else [args.source]
        export_kg(args.out, srcs)

    elif args.cmd == "schemas":
        _write_schemas()


def _write_schemas() -> None:
    from .models import (ArticleEntry, BlindingMap, Evaluation, Fichamento,
                         IngestionManifest)
    for name, model in [
        ("article", ArticleEntry),
        ("ingestion-manifest", IngestionManifest),
        ("fichamento", Fichamento),
        ("evaluation", Evaluation),
        ("blinding-map", BlindingMap),
    ]:
        out = paths.SCHEMAS / f"{name}.schema.json"
        out.write_text(json.dumps(model.model_json_schema(), indent=2))
        print(f"wrote {out.relative_to(paths.ROOT)}")


if __name__ == "__main__":
    main()
