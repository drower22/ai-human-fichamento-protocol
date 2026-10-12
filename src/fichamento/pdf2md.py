"""PDF -> line-marked markdown with a verifiable ingestion manifest.

Output format (audited unit consumed by `fichamento generate`)::

    <!-- pdf2md article=A01 tool="pymupdf x.y" pdf_sha256=... pages=22 -->
    <<p.1>>
    L01| Journal of ...
    <<p.5 method=ocr>>
    L01| ...

Coverage rule: every PDF page must appear as a block, tagged by method
(text / ocr / empty / manual). Pages OCR'd or empty are flagged
``needs_review`` — a human should eyeball them before trusting the
fichamento. ``coverage_complete`` means every page is accounted for.
"""

from __future__ import annotations

import hashlib
import subprocess
from datetime import datetime, timezone

import pymupdf

from . import paths
from .models import ArticleEntry, IngestionManifest, PageIngest

MIN_CHARS_PER_PAGE = 40  # below this a "text" page is treated as scanned


def _sha256(path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _ocr_page(page: pymupdf.Page, lang: str) -> str:
    pix = page.get_pixmap(dpi=300)
    proc = subprocess.run(
        ["tesseract", "stdin", "stdout", "-l", lang],
        input=pix.tobytes("png"),
        capture_output=True,
    )
    return proc.stdout.decode("utf-8", errors="replace")


def _lines(text: str) -> list[str]:
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def convert(article: ArticleEntry, ocr_lang: str = "por+eng") -> IngestionManifest:
    pdf = paths.ROOT / article.pdf_path
    if not pdf.exists():
        raise FileNotFoundError(f"{article.article_id}: {pdf} not found")

    doc = pymupdf.open(pdf)
    pages: list[PageIngest] = []
    blocks: list[str] = []
    ocr_used = False

    for i, page in enumerate(doc, start=1):
        text = page.get_text("text")
        lines = _lines(text)
        method: str = "text"
        warnings: list[str] = []
        needs_review = False

        if sum(len(ln) for ln in lines) < MIN_CHARS_PER_PAGE:
            ocr_text = _ocr_page(page, ocr_lang)
            ocr_lines = _lines(ocr_text)
            if sum(len(ln) for ln in ocr_lines) >= MIN_CHARS_PER_PAGE:
                lines, method, ocr_used = ocr_lines, "ocr", True
                needs_review = True
                warnings.append("no text layer; OCR applied — verify visually")
            elif not lines and not ocr_lines:
                method, needs_review = "empty", True
                warnings.append("no extractable text — blank page? verify")
            else:
                needs_review = True
                warnings.append("little text extracted — check for scanned content")

        tag = f"<<p.{i}>>" if method == "text" else f"<<p.{i} method={method}>>"
        blocks.append(tag)
        blocks.extend(f"L{n:02d}| {ln}" for n, ln in enumerate(lines, 1))
        pages.append(
            PageIngest(
                page=i,
                n_lines=len(lines),
                n_chars=sum(len(ln) for ln in lines),
                method=method,  # type: ignore[arg-type]
                needs_review=needs_review,
                warnings=warnings,
            )
        )

    header = (
        f"<!-- pdf2md article={article.article_id} "
        f'tool="pymupdf {pymupdf.__version__}" pages={doc.page_count} -->'
    )
    md = header + "\n" + "\n".join(blocks) + "\n"

    out_md = paths.md_path(article.article_id)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md)

    flagged = [p.page for p in pages if p.needs_review]
    manifest = IngestionManifest(
        article_id=article.article_id,
        pdf_path=article.pdf_path,
        pdf_sha256=_sha256(pdf),
        md_path=str(out_md.relative_to(paths.ROOT)),
        md_sha256=_sha256(out_md),
        tool=f"pymupdf {pymupdf.__version__}",
        ocr_tool=_tesseract_version() if ocr_used else None,
        pages_pdf=doc.page_count,
        pages_extracted=len(pages),
        est_tokens=sum(p.n_chars for p in pages) // 4,
        pages=pages,
        coverage_complete=len(pages) == doc.page_count,
        created_at=datetime.now(timezone.utc),
    )
    doc.close()

    mpath = paths.manifest_path(article.article_id)
    mpath.parent.mkdir(parents=True, exist_ok=True)
    mpath.write_text(manifest.model_dump_json(indent=2))

    print(
        f"{article.article_id}: {manifest.pages_extracted}/{manifest.pages_pdf} pages, "
        f"~{manifest.est_tokens} tokens"
        + (f" | needs_review pages: {flagged}" if flagged else "")
    )
    return manifest


def _tesseract_version() -> str | None:
    try:
        out = subprocess.run(
            ["tesseract", "--version"], capture_output=True, text=True
        )
        return out.stdout.splitlines()[0].strip() if out.stdout else "tesseract"
    except FileNotFoundError:
        return None


def check_gate(article_id: str) -> tuple[IngestionManifest | None, list[str]]:
    """Gate for `generate`: (manifest, problems). Empty problems => ok."""
    problems: list[str] = []
    mpath = paths.manifest_path(article_id)
    if not mpath.exists():
        return None, [f"no ingestion manifest — run `fichamento pdf2md` first"]
    manifest = IngestionManifest.model_validate_json(mpath.read_text())
    md = paths.ROOT / manifest.md_path
    if not md.exists():
        problems.append(f"{manifest.md_path} missing")
    elif _sha256(md) != manifest.md_sha256:
        problems.append(
            "markdown changed after ingestion (sha256 mismatch) — "
            "re-run pdf2md or record an override"
        )
    if not manifest.coverage_complete and not manifest.overrides:
        problems.append("coverage incomplete and no override recorded")
    flagged = [p.page for p in manifest.pages if p.needs_review]
    if flagged and not manifest.overrides:
        problems.append(f"pages pending human review: {flagged}")
    return manifest, problems
