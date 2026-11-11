#!/usr/bin/env python3
"""Check a figure before it goes into the paper.

Automated (reliable):
  * pixel size, dpi, and effective print width at 300 dpi,
  * grayscale and deuteranopia preview files, so a human can look at the print version,
  * a rough palette report: which chromatic inks the figure uses,
  * a warning when two chromatic inks collapse in grayscale or under deuteranopia.

Not automated (human, see references/captions.md and anti-patterns.md):
  * font size inside a vector PDF,
  * whether the caption states the takeaway,
  * whether the figure carries exactly one message.

Usage
-----
    python check_figure.py examples/fig01_cdf.png
    python check_figure.py fig/*.png --width-in 3.5
    python check_figure.py fig/fig3.pdf            # reports vector info only
    python check_figure.py fig/fig1.pdf --preview  # writes *_gray.png and *_cvd.png

Exit code 1 when a hard check fails (dpi, missing file), so it can gate a build.
Warnings do not fail the build.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# Machado et al. 2009, severity 1.0
DEUTERANOPIA = np.array([
    [0.367322, 0.860646, -0.227968],
    [0.280085, 0.672501, 0.047413],
    [-0.011820, 0.042940, 0.968881],
])


def luminance(rgb: np.ndarray) -> float:
    return float(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])


def cluster_ink(im: Image.Image, k: int = 6) -> list[tuple[tuple[int, int, int], float]]:
    """Cluster the non-white ink pixels; returns (colour, share) pairs."""
    arr = np.asarray(im.convert("RGB").resize((220, 220))).reshape(-1, 3).astype(float)
    arr = arr[arr.min(axis=1) < 170]
    if len(arr) < 100:
        return []
    rng = np.random.default_rng(0)
    k = min(k, len(arr))
    centers = arr[rng.choice(len(arr), k, replace=False)].copy()
    labels = np.zeros(len(arr), dtype=int)
    for _ in range(30):
        d = ((arr[:, None, :] - centers[None, :, :]) ** 2).sum(-1)
        labels = d.argmin(1)
        for j in range(k):
            sel = labels == j
            if sel.any():
                centers[j] = arr[sel].mean(0)
    counts = np.bincount(labels, minlength=k)
    return [
        (tuple(int(round(v)) for v in centers[j]), counts[j] / len(arr))
        for j in np.argsort(counts)[::-1]
    ]


def apply_deuteranopia(im: Image.Image) -> Image.Image:
    arr = np.asarray(im.convert("RGB")).astype(float) @ DEUTERANOPIA.T
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))


def check(path: Path, width_in: float, preview: bool, outdir: Path | None) -> bool:
    print(f"\n=== {path.name} ===")
    if path.suffix.lower() == ".pdf":
        print(f"  info  vector PDF, {path.stat().st_size / 1024:.0f} KB. "
              f"Verify embedded fonts and that font sizes are >= 7 pt at print scale.")
        return True

    im = Image.open(path).convert("RGB")
    w, h = im.size
    dpi = float(im.info.get("dpi", (300, 300))[0] or 300)
    inches = w / dpi
    hard_ok = True
    print(f"  size   {w}x{h} px at {dpi:.0f} dpi -> {inches:.2f} in wide")
    if dpi < 250:
        print(f"  FAIL   dpi {dpi:.0f} < 250; use 300 dpi for raster figures")
        hard_ok = False
    elif abs(inches - width_in) > 0.35:
        print(f"  note   width differs from the {width_in} in target. With a tight bounding "
              f"box that is normal; make sure the source figure was set to the printed width "
              f"so the fonts are not scaled down.")

    inks = cluster_ink(im)
    chromatic = [c for c, share in inks if max(c) - min(c) >= 25]
    achromatic = [c for c, share in inks if max(c) - min(c) < 25]
    if chromatic:
        print("  palette (chromatic): "
              + ", ".join("#%02x%02x%02x" % c for c in chromatic[:6]))
    if achromatic:
        print("  palette (ink/gray): "
              + ", ".join("#%02x%02x%02x" % c for c in achromatic[:3]))

    if len(chromatic) >= 2:
        lum = sorted(luminance(np.array(c, dtype=float)) for c in chromatic)
        gap = min(b - a for a, b in zip(lum, lum[1:]))
        print(f"  gray   smallest luminance gap between chromatic inks: {gap:.0f}/255")
        if gap < 18:
            print("  WARN   two chromatic inks have nearly the same brightness; "
                  "add a marker or linestyle difference so the figure survives grayscale print")
        sim = np.clip(
            np.array([DEUTERANOPIA @ np.array(c, dtype=float) for c in chromatic]), 0, 255
        )
        d = min(
            float(np.linalg.norm(sim[i] - sim[j]))
            for i in range(len(sim)) for j in range(i + 1, len(sim))
        )
        print(f"  CVD    smallest deuteranopia distance between chromatic inks: {d:.0f}/441")
        if d < 45:
            print("  WARN   two inks collapse under deuteranopia; use the Okabe-Ito palette "
                  "and encode the series by shape as well")

    if preview:
        stem = path.with_suffix("")
        g = stem.parent / (stem.name + "_gray.png")
        cvd = stem.parent / (stem.name + "_cvd.png")
        im.convert("L").convert("RGB").save(g)
        apply_deuteranopia(im).save(cvd)
        print(f"  wrote  {g.name}, {cvd.name}  (look at both before submitting)")

    print("  RESULT:", "PASS" if hard_ok else "FAIL")
    return hard_ok


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--width-in", type=float, default=3.5,
                    help="intended print width in inches (3.5 single column, 7.16 double)")
    ap.add_argument("--preview", action="store_true",
                    help="write grayscale and deuteranopia previews next to each figure")
    ap.add_argument("--outdir", default=None, help="write previews here instead")
    args = ap.parse_args()
    outdir = Path(args.outdir) if args.outdir else None

    # Expand globs here: Windows shells pass "examples/*.png" through literally.
    paths: list[Path] = []
    for p in args.paths:
        hits = sorted(Path().glob(p)) if any(ch in p for ch in "*?[") else [Path(p)]
        paths.extend(hits if hits else [Path(p)])

    results = []
    for path in paths:
        if not path.exists():
            print(f"missing: {path}")
            results.append(False)
            continue
        results.append(check(path, args.width_in, args.preview, outdir))
    print(f"\n{sum(results)}/{len(results)} figures passed")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
