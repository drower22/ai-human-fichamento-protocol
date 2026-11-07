"""PDF numerado: página ampliada com o original embutido 1:1 e rótulos
`p.N Lnnn` na margem, na altura exata da baseline de cada linha.

Formato (espelha o artigo-piloto-numerado.pdf):
- página nova = original + 92pt à esquerda + 64pt à direita + 40pt de
  altura; o original entra via ``show_pdf_page`` em (92, 30) sem escala;
- rótulo ``p.N Lnnn`` na margem **esquerda** para linhas da coluna
  esquerda e na margem **direita** para linhas da coluna direita
  (detecção por página via ``pdf2md._gutter_x``);
- a numeração é global e usa a MESMA ordenação de ``_page_lines`` que
  gerou o markdown — L do PDF = L do .md, garantido por construção;
- páginas sem camada de texto (OCR no manifesto) são rotuladas via
  Tesseract TSV **somente** quando o texto bate 1:1 com as linhas do
  .md; em caso de divergência, recebem marca de página + aviso com o
  intervalo de linhas — a numeração nunca sai de sincronia.
"""

from __future__ import annotations

import csv
import io
import re
import subprocess

import pymupdf

from . import paths
from .models import ArticleEntry, IngestionManifest
from .pdf2md import _columns_of, _page_lines

M_LEFT = 92.0   # margem esquerda (rótulos da coluna esquerda)
M_RIGHT = 96.0  # margem direita (rótulos da coluna direita; 2 colunas)
M_TOP, M_BOT = 30.0, 10.0
LABEL_X_LEFT = 40.0
LABEL_SIZE = 6.5
PAGE_SIZE = 9.0
LABEL_PITCH = 7.2   # separação mínima vertical entre rótulos da mesma margem
LABEL_COL_W = 44.0  # largura de uma sub-coluna de rótulos na margem
LABEL_MAX_COLS = 2  # sub-colunas por margem (páginas muito densas)
LABEL_COLOR = (0.1, 0.2, 0.45)  # azul escuro


def _fit_column(ys: list[float], y_top: float, y_bot: float):
    """Posiciona rótulos de UMA margem; retorna [(sub_col, y, font)]
    alinhado a ``ys`` (que chega ordenado).

    1. 1 sub-coluna com anti-colisão a LABEL_PITCH (preserva baseline;
       só empurra quando linhas dividem a mesma altura);
    2. se estourar ``y_bot``: 2 sub-colunas **intercaladas** (índices
       pares à esq., ímpares à dir.) nas posições naturais — cada
       sub-coluna vê 1 rótulo a cada 2 linhas, o dobro do respiro;
    3. último recurso: passo uniforme comprimido por sub-coluna.
    """
    n = len(ys)
    res: list[tuple[int, float, float] | None] = [None] * n
    prev = None
    for i, y0 in enumerate(ys):
        yy = max(y0, y_top)
        if prev is not None and yy < prev + LABEL_PITCH:
            yy = prev + LABEL_PITCH
        prev = yy
        if yy > y_bot:
            break
        res[i] = (0, yy, LABEL_SIZE)
    if res[-1] is not None:
        return res  # type: ignore[return-value]

    res = [None] * n
    for j in range(LABEL_MAX_COLS):
        idxs = list(range(j, n, LABEL_MAX_COLS))
        gaps = [ys[b] - ys[a] for a, b in zip(idxs, idxs[1:])]
        min_gap = min(gaps) if gaps else 99.0
        font = min(LABEL_SIZE, min_gap - 0.4)
        if font >= 3.4:
            for i in idxs:
                res[i] = (j, ys[i], font)
        else:
            pitch = max(3.2, (y_bot - y_top) / len(idxs))
            for k, i in enumerate(idxs):
                res[i] = (j, y_top + k * pitch,
                          max(3.0, min(LABEL_SIZE, pitch - 0.7)))
    return res  # type: ignore[return-value]


def _draw_labels(newp, pending, x_right: float, y_bot: float) -> None:
    """``pending``: [(lado, y, label)] com lado "L" (margem esquerda) ou
    "R" (margem direita, base ``x_right``). Agrupa por margem, ajusta
    sub-colunas/passo e desenha. Com 1 sub-coluna mantém o x habitual;
    com 2, usa a margem inteira (esq: x=4/48, dir: x_right/x_right+44)."""
    groups: dict[str, list[tuple[float, str]]] = {}
    for side, y, label in pending:
        groups.setdefault(side, []).append((y, label))
    for side, items in groups.items():
        items.sort()
        ys = [y for y, _ in items]
        placed = _fit_column(ys, M_TOP + 2, y_bot)
        ncols = max(j for j, _, _ in placed) + 1
        for (j, yy, size), (_, label) in zip(placed, items):
            if side == "L":
                xx = LABEL_X_LEFT if ncols == 1 else 4.0 + j * LABEL_COL_W
            else:
                xx = x_right + j * LABEL_COL_W
            newp.insert_text(
                pymupdf.Point(xx, yy), label,
                fontsize=size, fontname="helv", color=LABEL_COLOR,
            )


def _norm(s: str) -> str:
    return re.sub(r"[^0-9A-Za-zÀ-ÿ]", "", s).lower()


def _ocr_lines(page: pymupdf.Page, lang: str = "por+eng"):
    """Linhas OCR com geometria via Tesseract TSV — para páginas sem
    camada de texto. Retorna [(texto, Rect, baseline)] na ordem de
    leitura do Tesseract, em coordenadas da página."""
    dpi = 300
    pix = page.get_pixmap(dpi=dpi)
    proc = subprocess.run(
        ["tesseract", "stdin", "stdout", "-l", lang, "tsv"],
        input=pix.tobytes("png"), capture_output=True,
    )
    scale = page.rect.width / pix.width
    rows = csv.DictReader(io.StringIO(proc.stdout.decode()), delimiter="\t")
    groups: dict[tuple, list[dict]] = {}
    for r in rows:
        if (r.get("text") or "").strip():
            k = (r["block_num"], r["par_num"], r["line_num"])
            groups.setdefault(k, []).append(r)
    out = []
    for ws in groups.values():
        x0 = min(int(w["left"]) for w in ws) * scale
        y0 = min(int(w["top"]) for w in ws) * scale
        x1 = max(int(w["left"]) + int(w["width"]) for w in ws) * scale
        y1 = max(int(w["top"]) + int(w["height"]) for w in ws) * scale
        out.append((" ".join(w["text"] for w in ws),
                    pymupdf.Rect(x0, y0, x1, y1), y1 - (y1 - y0) * 0.2))
    return out


def _md_page_lines(article_id: str, page_no: int) -> list[str]:
    """Linhas de texto que o MD registrou para a página (sem o `Lnnn|`)."""
    md = paths.md_path(article_id)
    if not md.exists():
        return []
    m = re.search(
        rf"<<p\.{page_no}[^>]*>>(.*?)(?=<<p\.|\Z)", md.read_text(), re.S
    )
    if not m:
        return []
    return [ln.split("|", 1)[1].strip()
            for ln in m.group(1).splitlines() if "|" in ln]


def number_article(article: ArticleEntry) -> int:
    """Gera data/articles/pdfs/{id}-numerado.pdf. Retorna nº de linhas."""
    src = paths.ROOT / article.pdf_path
    if not src.exists():
        raise FileNotFoundError(f"{article.article_id}: {src} not found")
    mpath = paths.manifest_path(article.article_id)
    if not mpath.exists():
        raise FileNotFoundError(
            f"{article.article_id}: manifesto ausente — rode `pdf2md` antes"
        )
    manifest = IngestionManifest.model_validate_json(mpath.read_text())
    n_lines_by_page = {p.page: p.n_lines for p in manifest.pages}
    method_by_page = {p.page: p.method for p in manifest.pages}

    in_doc = pymupdf.open(src)
    out = pymupdf.open()
    ln = 0
    for i, page in enumerate(in_doc, start=1):
        ow, oh = page.rect.width, page.rect.height
        newp = out.new_page(width=ow + M_LEFT + M_RIGHT,
                            height=oh + M_TOP + M_BOT)
        newp.show_pdf_page(
            pymupdf.Rect(M_LEFT, M_TOP, M_LEFT + ow, M_TOP + oh), in_doc, i - 1
        )
        # marca de página no topo da margem esquerda
        newp.insert_text(
            pymupdf.Point(24, 22), f"p.{i}",
            fontsize=PAGE_SIZE, fontname="hebo", color=LABEL_COLOR,
        )
        if method_by_page.get(i) != "text":
            # página OCR/vazia: as linhas existem no MD mas vêm do
            # tesseract. Tenta rotulá-las via TSV — só desenha se o
            # texto bater 1:1 com o MD (paridade nunca é sacrificada);
            # senão avança o contador e avisa, senão os L das páginas
            # seguintes sairiam de sincronia com o MD.
            first, n = ln + 1, n_lines_by_page.get(i, 0)
            md_lines = _md_page_lines(article.article_id, i)
            ocr = _ocr_lines(page) if n else []
            if md_lines and len(ocr) == n and all(
                _norm(a) == _norm(t) for a, (t, _, _) in zip(md_lines, ocr)
            ):
                pending = []
                for text, bbox, base in ocr:
                    ln += 1
                    pending.append(("L", M_TOP + base, f"p.{i} L{ln:03d}"))
                _draw_labels(newp, pending, M_LEFT + ow + 6, M_TOP + oh - 4)
                continue
            ln += n
            newp.insert_text(
                pymupdf.Point(24, 32),
                f"(sem camada de texto — L{first:03d}–L{ln:03d} no .md)",
                fontsize=5.5, fontname="helv", color=LABEL_COLOR,
            )
            continue
        lines = _page_lines(page)
        col = _columns_of(lines)
        pending = []
        for text, bbox, base in lines:
            ln += 1
            side = "R" if col((text, bbox, base)) else "L"
            pending.append((side, M_TOP + base, f"p.{i} L{ln:03d}"))
        _draw_labels(newp, pending, M_LEFT + ow + 6, M_TOP + oh - 4)
    out_path = paths.numbered_pdf_path(article.article_id)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, deflate=True, garbage=3)
    n_pages = in_doc.page_count
    out.close(); in_doc.close()
    print(f"{article.article_id}-numerado.pdf: {n_pages} páginas, {ln} linhas rotuladas")
    return ln
