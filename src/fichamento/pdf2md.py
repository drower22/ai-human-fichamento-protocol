"""PDF -> line-marked markdown with a verifiable ingestion manifest.

Output format (audited unit consumed by `fichamento generate`) — line
numbers are GLOBAL across the document (matches citation style
"linhas 161-180"); pages are marked as blocks::

    <!-- pdf2md article=A01 tool="pymupdf x.y" pdf_sha256=... pages=22 -->
    <<p.1>>
    L001| Journal of ...
    L002| ...
    <<p.5 method=ocr>>
    L161| ...

Coverage rule: every PDF page must appear as a block, tagged by method
(text / ocr / empty / manual). Pages OCR'd or empty are flagged
``needs_review`` — a human should eyeball them before trusting the
fichamento. ``coverage_complete`` means every page is accounted for.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone

import pymupdf

from . import paths
from .models import ArticleEntry, IngestionManifest, PageIngest

MIN_CHARS_PER_PAGE = 40  # below this a "text" page is treated as scanned

_ACUTE = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "ı": "í",
          "A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú"}
_UMLAUT = {"a": "ä", "o": "ö", "u": "ü", "A": "Ä", "O": "Ö", "U": "Ü"}


def _fix_text(t: str, font: str = "") -> str:
    """Corrige artefatos de encoding de fontes com cmap próprio —
    glifos que renderizam certo no papel mas saem como controles ou
    sinais na camada de texto (verificado visualmente por artigo):

    - ``\\xad`` soft hyphen de hifenização — some na junção;
    - ``\\x02``/``\\x03`` ligaduras ti/tt — o mapa é por FONTE
      (A12/Calibri: regular x02=ti x03=tt; Bold troca);
    - ``\\x14``+vogal acento agudo combinante, ``\\x18a`` å,
      ``~a``/``~o`` til combinante, ``€``+vogal trema (A14, fonte
      Emerald);
    - ``\\x07`` quebra fantasma em célula de tabela (A08);
    - controles restantes viram ``�`` para ficarem visíveis.
    """
    t = t.replace("\xad", "").replace("\x07", "")
    ti, tt = ("tt", "ti") if "Bold" in font else ("ti", "tt")
    t = t.replace("\x02", ti).replace("\x03", tt)
    t = re.sub(r"\x14([aeiouAEIOUı])", lambda m: _ACUTE[m.group(1)], t)
    t = t.replace("\x18a", "å")
    t = t.replace("~a", "ã").replace("~o", "õ")
    t = re.sub(r"€([aAoOuU])", lambda m: _UMLAUT[m.group(1)], t)
    t = t.replace("\t", " ").replace("\x0b", " ").replace("\x0c", " ")
    return re.sub(r"[\x00-\x08\x0e-\x1f]", "�", t)


# Transcrições manuais (conferidas no papel, pixel a pixel) para linhas
# cujo OCR embutido no PDF é ilegível — A04 é um scan EBSCO de 1978 com
# camada de texto ruidosa e página 1 com sobreposição dupla de scan.
# Chave: article_id -> {nº da linha global -> texto corrigido}.
_LINE_FIXES: dict[str, dict[int, str]] = {
    "A04": {
        2: "and Process¹",
        12: "fragmented theoretical treatment. Any attempt to examine "
            "organiza-",
        27: "[ilegível — sobreposição de scan]",
        32: "[ilegível — sobreposição de scan]",
        338: "more of a unit or small-batch technology (21).",
        447: "quality products, but Defenders also tend to ig-",
        491: "here as in the solution to the other two adaptive",
        557: "1.",
        632: "Costs and Benefits;",
        685: "er than to plan and control the operations of the",
        688: "pector's structure-process mechanisms must be",
        1058: "ronmental change and uncertainty, performing",
        1059: "poorly as a result, and then being reluctant to act",
        1276: "recognition. This model argued that impersonal",
        1280: "ance",
        1409: "permanent technology and structure. It seems",
        1488: 'Ansoff, H. Igor, and Richard Brandenburg. "A Language',
        1493: 'Technology-Based Business," Harvard Business Review,',
        **{n: "[ilegível — sobreposição de scan]" for n in range(49, 57)},
    }
}


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


def _gutter_x(items: list[tuple[str, "pymupdf.Rect", float]]) -> float | None:
    """X da calha central se a página tem 2 colunas, senão None.

    Histograma de cobertura: para cada fatia de 3pt do eixo-x conta
    quantas linhas a cruzam; a calha é o maior vão central quase sem
    cruzamentos (tolera títulos/cabeçalhos que atravessam a página).
    """
    n = len(items)
    if n < 20:
        return None
    lo = min(it[1].x0 for it in items)
    hi = max(it[1].x1 for it in items)
    if hi - lo < 150:
        return None
    nb = int((hi - lo) / 3)
    cover = [0] * nb
    for it in items:
        a = max(0, int((it[1].x0 - lo) / 3))
        b = min(nb - 1, int((it[1].x1 - lo) / 3))
        for i in range(a, b + 1):
            cover[i] += 1
    thresh = max(1, int(0.05 * n))
    best_len, best_range = 0, None
    run_start = None
    for i in range(nb):
        cx = lo + (i + 0.5) * 3
        central = lo + 0.35 * (hi - lo) <= cx <= lo + 0.75 * (hi - lo)
        if cover[i] <= thresh and central:
            if run_start is None:
                run_start = i
            if i - run_start + 1 > best_len:
                best_len, best_range = i - run_start + 1, (run_start, i)
        else:
            run_start = None
    if best_range is None or best_len * 3 < 6:  # calha >= 6pt
        return None
    a, b = best_range
    gx = lo + ((a + b + 1) / 2) * 3
    left = sum(1 for it in items if it[1].x1 <= gx)
    right = sum(1 for it in items if it[1].x0 >= gx)
    # >=8 linhas de cada lado E >=15% das linhas — evita falso positivo
    # em página de coluna única com faixa branca estranha
    if left < 8 or right < 8 or min(left, right) < 0.15 * n:
        return None
    return gx


def _band_gutter(items: list[tuple[str, "pymupdf.Rect", float]]):
    """Calhas por faixa vertical, para páginas MISTAS (tabela/título de
    largura total + corpo em 2 colunas). Janelas deslizantes de ~45
    linhas; cada linha usa a calha da janela mais próxima da sua
    baseline. Retorna função col(item)->0|1 ou None."""
    by_y = sorted(items, key=lambda it: it[2])
    n = len(by_y)
    W, S = 45, 15
    chunks = [by_y] if n < W else [by_y[s : s + W] for s in range(0, n - W + 1, S)]
    wins = []
    for chunk in chunks:
        gx = _gutter_x(chunk)
        if gx is not None:
            wins.append(((chunk[0][2] + chunk[-1][2]) / 2, gx))
    if not wins:
        return None

    def col(it):
        _, gx = min(wins, key=lambda w: abs(w[0] - it[2]))
        return 0 if it[1].x0 < gx else 1

    return col


def _columns_of(items: list[tuple[str, "pymupdf.Rect", float]]):
    """Função item->0 (coluna esquerda) | 1 (direita): calha global se
    existir, senão por faixas, senão tudo coluna única."""
    gx = _gutter_x(items)
    if gx is not None:
        return lambda it: 0 if it[1].x0 < gx else 1
    bf = _band_gutter(items)
    if bf is not None:
        return bf
    return lambda it: 0


def _page_lines(page: pymupdf.Page) -> list[tuple[str, pymupdf.Rect, float]]:
    """Text-layer lines of a page in VISUAL order (top→bottom, left→right).

    Returns ``(text, bbox, baseline_y)`` triples — ``baseline_y`` is the
    exact glyph baseline (span origin), needed to place margin labels
    precisely on the line. Sorting uses a 3pt vertical band so separate
    pieces of the same visual row (e.g. header title vs. page number)
    are ordered left→right instead of jumping. Two-column pages are
    detected by ``_gutter_x`` and ordered column-major (left column
    top→bottom, then right column) so ``Lnn`` runs down each column.

    Both the markdown and the line-numbered margin PDF must use this
    same ordering so that ``Lnn`` numbers always match.
    """
    out: list[tuple[str, pymupdf.Rect, float]] = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            t = _fix_text(
                "".join(
                    _fix_text(s["text"], s.get("font", ""))
                    if any(ord(c) in (2, 3) for c in s["text"])
                    else s["text"]
                    for s in line["spans"]
                )
            ).strip()
            if t:
                baseline = max(s["origin"][1] for s in line["spans"])
                out.append((t, pymupdf.Rect(line["bbox"]), baseline))
    col = _columns_of(out)
    out.sort(key=lambda l: (col(l), round(l[1].y0 / 3.0), l[1].x0))
    return out


def convert(article: ArticleEntry, ocr_lang: str = "por+eng") -> IngestionManifest:
    pdf = paths.ROOT / article.pdf_path
    if not pdf.exists():
        raise FileNotFoundError(f"{article.article_id}: {pdf} not found")

    doc = pymupdf.open(pdf)
    pages: list[PageIngest] = []
    blocks: list[str] = []
    ocr_used = False
    ln = 0  # global line counter across the whole document

    for i, page in enumerate(doc, start=1):
        lines = [t for t, _, _ in _page_lines(page)]
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
        for line in lines:
            ln += 1
            line = _LINE_FIXES.get(article.article_id, {}).get(ln, line)
            blocks.append(f"L{ln:03d}| {line}")
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
