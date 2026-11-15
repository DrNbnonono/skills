#!/usr/bin/env python
"""One fetch pass that fixes three denominators and extracts figure-type features.

1. Display items: count only TOP-LEVEL figures/tables (sub-figures are nested), so "floats per
   paper" stops being inflated, and count how many sit in the appendix.
2. Hue sensitivity: recompute palette breadth at 3% / 5% / 10% of coloured pixels.
3. Figure-type features for a later classifier: background fraction, edge density, long straight
   runs (bars/frames), connected components (scatter dots vs solid bars), colour count.

Saves images to writing/figs/ so they can be labelled by eye.

Usage: python figure_features.py [n_papers]
"""
from __future__ import annotations

import io
import json
import os
import random
import re
import ssl
import statistics
import sys
import urllib.parse
import urllib.request

from lxml import html as LH
from PIL import Image, ImageChops, ImageFilter

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
CORPUS = os.environ.get("PAPER_CORPUS", "corpus_v23.jsonl")
FIGDIR = os.environ.get("PAPER_FIGS", "figs")


def fetch(url: str, timeout: int = 40) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout, context=CTX).read()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def is_top_level(el) -> bool:
    p = el.getparent()
    while p is not None:
        if isinstance(p.tag, str) and p.tag == "figure":
            cls = p.get("class") or ""
            if "ltx_figure" in cls or "ltx_table" in cls:
                return False
        p = p.getparent()
    return True


def count_display_items(doc) -> dict:
    total = app = 0
    for sec in doc.xpath("//section"):
        title = norm(" ".join(sec.xpath("./h2//text()")))
        figs = [f for f in sec.xpath(".//figure")
                if ("ltx_figure" in (f.get("class") or "") or "ltx_table" in (f.get("class") or ""))
                and is_top_level(f)]
        # avoid double counting nested sections: only count figures whose nearest section is this one
        own = []
        for f in figs:
            owner = f.xpath("ancestor::section[1]")
            if owner and owner[0] is sec:
                own.append(f)
        if not own:
            continue
        total += len(own)
        if re.search(r"appendix", title, re.I):
            app += len(own)
    return {"total": total, "appendix": app}


def hue_stats(im: Image.Image) -> dict:
    im = im.convert("RGB")
    im.thumbnail((600, 600))
    px = list(im.getdata())[:: max(1, len(im.getdata()) // 20000)]
    hues = [0] * 12
    coloured = 0
    for r, g, b in px:
        mx, mn = max(r, g, b), min(r, g, b)
        if mx == 0 or mx < 60 or (mx - mn) / mx < 0.25:
            continue
        coloured += 1
        d = mx - mn
        if mx == r:
            h = (60 * ((g - b) / d)) % 360
        elif mx == g:
            h = 60 * ((b - r) / d) + 120
        else:
            h = 60 * ((r - g) / d) + 240
        hues[int(h // 30) % 12] += 1
    if not coloured:
        return {"hues3": 0, "hues5": 0, "hues10": 0}
    shares = [h / coloured for h in hues]
    return {"hues3": sum(s >= 0.03 for s in shares),
            "hues5": sum(s >= 0.05 for s in shares),
            "hues10": sum(s >= 0.10 for s in shares)}


def features(im: Image.Image) -> dict:
    im = im.convert("L").resize((400, 300))
    px = list(im.getdata())
    w, h = im.size
    bg = sum(1 for v in px if v > 235) / len(px)
    edge = im.filter(ImageFilter.FIND_EDGES)
    ep = list(edge.getdata())
    edge_density = sum(1 for v in ep if v > 60) / len(ep)

    # long straight runs: a row (col) whose dark pixels span >=30% of the width (height)
    dark_rows = 0
    for y in range(h):
        row = px[y * w:(y + 1) * w]
        dark = [1 if v < 120 else 0 for v in row]
        run = best = 0
        for d in dark:
            run = run + 1 if d else 0
            best = max(best, run)
        if best >= 0.3 * w:
            dark_rows += 1
    dark_cols = 0
    for x in range(w):
        col = [px[y * w + x] for y in range(h)]
        dark = [1 if v < 120 else 0 for v in col]
        run = best = 0
        for d in dark:
            run = run + 1 if d else 0
            best = max(best, run)
        if best >= 0.3 * h:
            dark_cols += 1
    return {"bg": round(bg, 2), "edge": round(edge_density, 3),
            "h_runs": dark_rows, "v_runs": dark_cols}


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    os.makedirs(FIGDIR, exist_ok=True)
    rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()]
    random.seed(3)
    sample = random.sample(rows, min(n * 2, len(rows)))
    display, figs, got = [], [], 0

    for r in sample:
        if got >= n:
            break
        base = r["id"].split("v")[0]
        url = f"https://ar5iv.labs.arxiv.org/html/{base}"
        try:
            page = fetch(url).decode("utf-8", "ignore")
        except Exception as e:
            print("skip page", base, repr(e)[:40])
            continue
        doc = LH.fromstring(page)
        d = count_display_items(doc)
        if d["total"] >= 3:
            display.append({"id": r["id"], **d})
            got += 1
        srcs = [s for s in doc.xpath("//figure[contains(@class,'ltx_figure')]//img/@src")
                if re.search(r"\.(png|jpg|jpeg)$", s, re.I)][:3]
        for i, src in enumerate(srcs):
            try:
                blob = fetch(urllib.parse.urljoin(url, src), 30)
                im = Image.open(io.BytesIO(blob))
                if min(im.size) < 140:
                    continue
                rec = {"paper": base, "i": i, **hue_stats(im), **features(im)}
                fn = os.path.join(FIGDIR, f"{base}_{i}.png")
                im.convert("RGB").save(fn)
                rec["file"] = os.path.basename(fn)
                figs.append(rec)
            except Exception:
                continue
        if got % 5 == 0:
            print(f"{got} papers, {len(figs)} figures", flush=True)

    json.dump({"display": display, "figures": figs},
              open(r"E:\php2shell\writing\figure_features.json", "w", encoding="utf-8"), indent=1)

    if display:
        tot = sum(d["total"] for d in display)
        app = sum(d["appendix"] for d in display)
        print(f"\ndisplay items: papers {len(display)}  items {tot}  per paper median "
              f"{statistics.median([d['total'] for d in display]):.0f}  in appendix {100*app/max(tot,1):.1f}%")
        print(f"papers with appendix items: {sum(1 for d in display if d['appendix'])}/{len(display)}")
    if figs:
        for k in ("hues3", "hues5", "hues10"):
            vals = [f[k] for f in figs]
            print(f"  {k}: median {statistics.median(vals):.0f}  "
                  f"share>=4: {100*sum(1 for v in vals if v>=4)/len(vals):.0f}%")
        print(f"  figures saved: {len(figs)}")


if __name__ == "__main__":
    main()

