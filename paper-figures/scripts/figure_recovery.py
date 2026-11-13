#!/usr/bin/env python3
"""Recover a figure from a PDF as a self-contained vector SVG, with a pixel check.

Purpose: get a clean vector copy of a figure you already own (or have permission to reuse) --
e.g. you lost the source of your own figure, or you are studying how a published figure was
built. It is **not** a way to lift someone else's figure into your paper: see
`references/figure-recovery.md` and the copyright guard in `SKILL.md`.

Design choices vs the original pdf-figure-vector project (github.com/tanzhouhu/pdf-figure-vector):
  * no Chrome dependency: PyMuPDF renders the SVG for the pixel comparison, so it runs headless;
  * no automatic browser popup: `--open` is opt-in;
  * deterministic JSON summary + a MAE gate, so it can run in a build;
  * refuses to pretend a raster figure is vector (the probe reports it).

Usage
-----
    python figure_recovery.py probe   --pdf paper.pdf --page 3
    python figure_recovery.py extract --pdf paper.pdf --page 3 --out figs/recovered
    python figure_recovery.py extract --pdf paper.pdf --page 3 --bbox 54,120,300,260 --text
    python figure_recovery.py compare --pdf paper.pdf --page 3 --bbox 54,120,300,260 --svg fig.svg

Dependencies: pymupdf, pillow, numpy (all common; check with `python -c "import fitz"`).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
from PIL import Image

SVG_ROOT_RE = re.compile(r"<svg\b[^>]*>", re.S)
ATTR_RE = re.compile(r'(\w[\w:-]*)="([^"]*)"')


def page_of(pdf: str, page_no: int) -> fitz.Page:
    doc = fitz.open(pdf)
    if not 1 <= page_no <= doc.page_count:
        raise SystemExit(f"page {page_no} out of range (1..{doc.page_count})")
    return doc[page_no - 1]


def ink_bbox(page: fitz.Page) -> tuple[float, float, float, float] | None:
    """Union bbox of vector drawings and placed images on the page."""
    rects = []
    for d in page.get_drawings():
        if d.get("rect"):
            rects.append(fitz.Rect(d["rect"]))
    for info in page.get_images(full=True):
        try:
            rects.extend(page.get_image_rects(info[0]))
        except Exception:
            pass
    if not rects:
        return None
    box = rects[0]
    for r in rects[1:]:
        box |= r
    return (box.x0, box.y0, box.x1, box.y1)


def classify(page: fitz.Page) -> dict:
    drawings = page.get_drawings()
    images = page.get_images(full=True)
    box = ink_bbox(page)
    if drawings and images:
        kind = "mixed"
    elif drawings:
        kind = "vector"
    elif images:
        kind = "raster"
    else:
        kind = "none"
    return {
        "page_size_pt": [round(page.rect.width, 2), round(page.rect.height, 2)],
        "drawings": len(drawings),
        "images": len(images),
        "kind": kind,
        "ink_bbox_pt": [round(v, 2) for v in box] if box else None,
    }


def crop_svg(svg: str, bbox: tuple[float, float, float, float]) -> str:
    """Re-root the page SVG on a bbox (PDF points). Content coordinates are already page-space."""
    m = SVG_ROOT_RE.search(svg)
    if not m:
        raise SystemExit("could not find <svg> root in extracted SVG")
    tag = m.group(0)
    attrs = dict(ATTR_RE.findall(tag))
    width = attrs.get("width", "0")
    x0, y0, x1, y1 = bbox
    w, h = x1 - x0, y1 - y0
    new_tag = re.sub(r'\s(width|height|viewBox)="[^"]*"', "", tag)
    new_tag = new_tag[:-1] + (
        f' width="{w:.3f}" height="{h:.3f}" viewBox="{x0:.3f} {y0:.3f} {w:.3f} {h:.3f}">'
    )
    return svg[: m.start()] + new_tag + svg[m.end():]


def render_pdf(page: fitz.Page, bbox, dpi: int) -> Image.Image:
    pix = page.get_pixmap(clip=fitz.Rect(*bbox), dpi=dpi, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def render_svg(svg_path: Path, bbox, dpi: int) -> Image.Image:
    doc = fitz.open(str(svg_path))
    try:
        pix = doc[0].get_pixmap(dpi=dpi, alpha=False)
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    finally:
        doc.close()


def mae(a: Image.Image, b: Image.Image) -> tuple[float, Image.Image]:
    if a.size != b.size:
        b = b.resize(a.size)
    aa = np.asarray(a, dtype=np.float32)
    bb = np.asarray(b, dtype=np.float32)
    diff = np.abs(aa - bb)
    score = float(diff.mean())
    heat = Image.fromarray(np.clip(diff.mean(axis=2) * 3, 0, 255).astype(np.uint8))
    return score, heat


def qa(ref: Image.Image, got: Image.Image, max_mae: float) -> dict:
    """Compare the vector copy with the PDF crop.

    Raw per-pixel MAE is dominated by ~1 px anti-aliasing differences between two rasterisers,
    so the gate uses a normalised copy: both images are downsampled to 900 px wide and lightly
    blurred, which removes edge noise while keeping missing/misplaced content visible.
    """
    from PIL import ImageFilter

    raw, heat = mae(ref, got)

    def norm(im: Image.Image) -> Image.Image:
        w = 900
        h = max(1, round(im.height * w / im.width))
        return im.resize((w, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.0))

    a, b = norm(ref), norm(got)
    aa = np.asarray(a, dtype=np.float32)
    bb = np.asarray(b, dtype=np.float32)
    score = float(np.abs(aa - bb).mean())
    struct = float((np.abs(aa - bb).max(axis=2) > 40).mean() * 100)
    return {
        "mae_raw": round(raw, 2),
        "mae_norm": round(score, 2),
        "struct_pct": round(struct, 2),
        "gate": "PASS" if (score <= max_mae and struct <= 2.0) else "FAIL",
        "max_mae_norm": max_mae,
        "heat": heat,
    }


def side_by_side(a: Image.Image, b: Image.Image, heat: Image.Image) -> Image.Image:
    h = max(a.height, b.height, heat.height)
    w = a.width + b.width + heat.width + 16
    canvas = Image.new("RGB", (w, h), "white")
    x = 0
    for img in (a, b, heat.convert("RGB")):
        canvas.paste(img, (x, 0))
        x += img.width + 8
    return canvas


def cmd_probe(args) -> int:
    page = page_of(args.pdf, args.page)
    info = classify(page)
    info.update({"pdf": str(args.pdf), "page": args.page})
    print(json.dumps(info, indent=2))
    if info["kind"] == "raster":
        print("\nNOTE: raster figure. Do not vectorise it and call the result 'vector'; either "
              "redraw it with scripts/figure_style.py or keep it as a 300 dpi image.")
    return 0


def resolve_bbox(args, page) -> tuple[float, float, float, float]:
    if args.bbox and args.bbox != "auto":
        vals = [float(v) for v in re.split(r"[,\s]+", args.bbox.strip()) if v]
        if len(vals) != 4:
            raise SystemExit("--bbox needs four numbers: x0,y0,x1,y1 (PDF points)")
        box = tuple(vals)
    else:
        box = ink_bbox(page)
        if not box:
            raise SystemExit("no drawings or images on this page; pass --bbox manually")
    pad = args.pad
    return (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)


def cmd_extract(args) -> int:
    page = page_of(args.pdf, args.page)
    bbox = resolve_bbox(args, page)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{Path(args.pdf).stem}-p{args.page}"
    svg_path = out_dir / f"{stem}.svg"
    png_path = out_dir / f"{stem}.png"
    svg = page.get_svg_image(text_as_path=not args.text)
    svg_path.write_text(crop_svg(svg, bbox), encoding="utf-8")
    render_pdf(page, bbox, args.dpi).save(png_path)
    info = {
        "pdf": str(args.pdf), "page": args.page,
        "bbox_pt": [round(v, 2) for v in bbox],
        "svg": str(svg_path), "png": str(png_path),
        "svg_bytes": svg_path.stat().st_size,
        "text_mode": "text" if args.text else "paths",
    }
    if not args.no_compare:
        ref = render_pdf(page, bbox, args.dpi)
        got = render_svg(svg_path, bbox, args.dpi)
        result = qa(ref, got, args.max_mae)
        diff_path = out_dir / f"{stem}-diff.png"
        side_by_side(ref, got, result["heat"]).save(diff_path)
        result.pop("heat")
        info.update(result)
        info["diff"] = str(diff_path)
    print(json.dumps(info, indent=2))
    if args.open and info.get("svg"):
        import webbrowser
        webbrowser.open(svg_path.resolve().as_uri())
    return 0 if info.get("gate", "PASS") == "PASS" else 1


def cmd_compare(args) -> int:
    page = page_of(args.pdf, args.page)
    bbox = resolve_bbox(args, page)
    ref = render_pdf(page, bbox, args.dpi)
    got = render_svg(Path(args.svg), bbox, args.dpi)
    result = qa(ref, got, args.max_mae)
    out = Path(args.svg).with_name(Path(args.svg).stem + "-diff.png")
    side_by_side(ref, got, result["heat"]).save(out)
    result.pop("heat")
    result.update({"svg": str(args.svg), "diff": str(out)})
    print(json.dumps(result, indent=2))
    return 0 if result["gate"] == "PASS" else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("probe", help="is the figure vector or raster? bbox and counts")
    p.add_argument("--pdf", required=True)
    p.add_argument("--page", type=int, required=True)
    p.set_defaults(fn=cmd_probe)

    e = sub.add_parser("extract", help="crop the figure to a self-contained SVG + PNG, and compare")
    e.add_argument("--pdf", required=True)
    e.add_argument("--page", type=int, required=True)
    e.add_argument("--bbox", default="auto", help="x0,y0,x1,y1 in PDF points, or 'auto'")
    e.add_argument("--pad", type=float, default=4.0, help="padding around the ink bbox (pt)")
    e.add_argument("--out", default="recovered")
    e.add_argument("--dpi", type=int, default=300)
    e.add_argument("--text", action="store_true", help="keep editable <text> (may shift glyphs)")
    e.add_argument("--no-compare", action="store_true")
    e.add_argument("--max-mae", type=float, default=2.0, help="normalised MAE gate (0-255 scale)")
    e.add_argument("--open", action="store_true", help="open the SVG in the default viewer")
    e.set_defaults(fn=cmd_extract)

    c = sub.add_parser("compare", help="pixel-compare an existing SVG against the PDF crop")
    c.add_argument("--pdf", required=True)
    c.add_argument("--page", type=int, required=True)
    c.add_argument("--bbox", default="auto")
    c.add_argument("--pad", type=float, default=4.0)
    c.add_argument("--svg", required=True)
    c.add_argument("--dpi", type=int, default=300)
    c.add_argument("--max-mae", type=float, default=2.0)
    c.set_defaults(fn=cmd_compare)

    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
