#!/usr/bin/env python
"""A first look at figure palettes in top-tier security papers.

For a sample of ar5iv pages, download the raster images embedded in figures and measure:
  - distinct hues carrying at least 5% of the coloured pixels (palette breadth)
  - whether a red/green pair is used (the most common colour-vision failure)
  - mean saturation of coloured pixels (how loud the palette is)
  - luminance spread (a proxy for whether the figure survives grayscale printing)

Usage: python figure_color_study.py [n_papers]
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
from PIL import Image

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
CORPUS = os.environ.get("PAPER_CORPUS", "corpus_v23.jsonl")


def fetch(url: str, timeout: int = 30) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout, context=CTX).read()


def analyse_image(blob: bytes) -> dict | None:
    try:
        im = Image.open(io.BytesIO(blob)).convert("RGB")
    except Exception:
        return None
    if min(im.size) < 120:
        return None
    im.thumbnail((600, 600))
    px = list(im.getdata())
    coloured, hues, lum = [], [0] * 12, []
    for r, g, b in px[::max(1, len(px) // 20000)]:
        mx, mn = max(r, g, b), min(r, g, b)
        lum.append(0.299 * r + 0.587 * g + 0.114 * b)
        if mx == 0 or (mx - mn) / mx < 0.25 or mx < 60:
            continue
        coloured.append((r, g, b))
        h = 0.0
        d = mx - mn
        if mx == r:
            h = (60 * ((g - b) / d)) % 360
        elif mx == g:
            h = 60 * ((b - r) / d) + 120
        else:
            h = 60 * ((r - g) / d) + 240
        hues[int(h // 30) % 12] += 1
    if not coloured:
        return {"coloured_share": 0.0, "hues": 0, "red_green": False, "sat": 0.0,
                "lum_std": round(statistics.pstdev(lum), 1)}
    total = len(coloured)
    shares = [h / total for h in hues]
    distinct = sum(1 for s in shares if s >= 0.05)
    red = shares[0] + shares[11]
    green = shares[2] + shares[3] + shares[4]
    sat = statistics.mean((max(c) - min(c)) / max(c) for c in coloured)
    return {"coloured_share": round(total / len(lum), 2), "hues": distinct,
            "red_green": red >= 0.05 and green >= 0.05, "sat": round(sat, 2),
            "lum_std": round(statistics.pstdev(lum), 1)}


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()]
    random.seed(3)
    sample = random.sample(rows, min(n * 2, len(rows)))
    results, papers = [], 0
    for r in sample:
        if papers >= n:
            break
        base = r["id"].split("v")[0]
        url = f"https://ar5iv.labs.arxiv.org/html/{base}"
        try:
            page = fetch(url, 40).decode("utf-8", "ignore")
        except Exception as e:
            print("skip page", base, repr(e)[:40])
            continue
        doc = LH.fromstring(page)
        imgs = doc.xpath("//figure[contains(@class,'ltx_figure')]//img/@src")
        imgs = [i for i in imgs if re.search(r"\.(png|jpg|jpeg)$", i, re.I)][:3]
        if not imgs:
            continue
        got = 0
        for src in imgs:
            full = urllib.parse.urljoin(url, src)
            try:
                m = analyse_image(fetch(full, 30))
            except Exception:
                continue
            if m:
                m["paper"] = base
                results.append(m)
                got += 1
        if got:
            papers += 1
            print(f"paper {papers}: {got} images", flush=True)

    if not results:
        print("no images analysed")
        return
    json.dump(results, open(r"E:\php2shell\writing\figure_colors.json", "w", encoding="utf-8"), indent=1)
    print(f"\nimages {len(results)} from {papers} papers")
    print(f"  distinct hues (>=5% each): median {statistics.median(x['hues'] for x in results):.0f}  "
          f"share with >=4: {100*sum(1 for x in results if x['hues']>=4)/len(results):.1f}%")
    print(f"  red+green pair: {100*sum(1 for x in results if x['red_green'])/len(results):.1f}%")
    print(f"  saturation: median {statistics.median(x['sat'] for x in results):.2f}")
    print(f"  luminance std: median {statistics.median(x['lum_std'] for x in results):.0f}")


if __name__ == "__main__":
    main()

