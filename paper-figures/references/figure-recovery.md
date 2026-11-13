# Figure recovery: get a vector copy of a figure you already own

`scripts/figure_recovery.py` crops a figure out of a PDF as a **self-contained vector SVG**,
renders it back, and pixel-checks the result against the PDF. It is the tool for one situation:

> you have figure you are allowed to reuse (your own, or one with a compatible licence), and
> the source file is gone — only a PDF remains.

It is **not** a way to take a figure from someone else's paper.

---

## 1. Guardrails (read before running it)

- **Recover your own figures, or figures you have permission to reuse.** A published paper's
  figure is copyrighted unless its licence says otherwise (CC-BY, CC0, or a repo licence
  grants reuse with attribution; "all rights reserved" does not).
- **Never put a recovered figure into your submission.** Even when reuse is licensed, a paper
  must not present another paper's figure as its own. Recover it to study the encoding, then
  redraw it with `scripts/figure_style.py`.
- **Check the licence before adapting.** For CC-BY, credit the original and state the change;
  for anything else, ask the authors.
- **A raster figure is not a vector figure.** The probe reports `kind: raster`; do not trace it
  and call the result vector. Either redraw the plot from data or keep the image at 300 dpi and
  say so in the caption.
- **Keep the recovered files out of the paper's build.** Store them under `analysis/`, not
  `figs/`, so a recovered SVG cannot be shipped by accident.

## 2. Workflow

```bash
# 1. What is on the page, and where? (vector or raster, ink bbox)
python scripts/figure_recovery.py probe --pdf paper.pdf --page 3

# 2. Crop the figure (auto bbox = union of drawings/images; or pass the bbox in points)
python scripts/figure_recovery.py extract --pdf paper.pdf --page 3 \
    --bbox 54,120,300,260 --out analysis/recovered

# 3. Read the JSON: gate PASS when the normalised pixel difference is small
```

The extract step writes three files:

| File | Use |
|---|---|
| `<stem>.svg` | the vector figure, cropped to the bbox, self-contained |
| `<stem>.png` | 300 dpi raster of the same crop (preview, and the reference for the check) |
| `<stem>-diff.png` | reference / recovered / difference, side by side |

Exit code is 0 on a passing gate, 1 on a failing one, so a build or a batch script can stop.

## 3. Reading the QA numbers

| Field | Meaning | Gate |
|---|---|---|
| `mae_raw` | per-pixel MAE at 300 dpi — dominated by anti-aliasing | informational |
| `mae_norm` | MAE after downsampling to 900 px and a light blur — this is the real check | ≤ 2.0 |
| `struct_pct` | share of pixels differing by > 40/255 after normalisation | ≤ 2.0 % |
| `gate` | PASS/FAIL of the two above | — |

A faithful crop scores `mae_norm` around 1–2 and `struct_pct` 0.0. A failure usually means a
missing element, a shifted group, or a dropped mask — look at the diff image, not the number.

## 4. Text: fidelity or editability

| Mode | Flag | Result |
|---|---|---|
| Paths (default) | — | every glyph becomes a path: pixel-faithful, large file, text not editable |
| Text | `--text` | `<text>` elements survive: editable, but the viewer substitutes fonts, so glyphs can shift |

For a faithful copy use the default. For a figure you will restyle and re-typeset, `--text` is
usually the better starting point, checked against the diff.

## 5. Editing the recovered SVG

- **Inkscape / Illustrator / Figma**: open, ungroup, re-colour. Then apply
  `references/style-spec.md` if the figure is going into your own paper.
- **PowerPoint**: Insert → Pictures → SVG; right-click → Convert to Shape for native editing.
- **LaTeX**: `\includegraphics{fig.svg}` does not work directly; convert to PDF first
  (`inkscape --export-type=pdf`, or render with PyMuPDF at 300 dpi — but then it is raster).
  Prefer redrawing with `figure_style.py` for anything going into a paper.

## 6. Known limits

- MuPDF's SVG output may not reproduce soft masks, transparency groups, patterns, or ICC
  profiles exactly; the QA gate catches most of it, but always eyeball the diff.
- Very large pages (A0 posters) can be slow/memory-heavy; crop with `--bbox` first.
- Text as paths inflates the SVG (a full page of paths can be several MB); crop to the figure.
- Embedded raster images inside the figure are extracted as raster links; they do not become
  vector, and that is correct behaviour.

## 7. Prior art and differences

This script is our own implementation of the workflow popularised by
[`pdf-figure-vector`](https://github.com/tanzhouhu/pdf-figure-vector) (a Claude Code/Codex
skill that also emits editable PPTX and embeds font subsets, and drives a browser preview and
Chrome-based comparison). We did not copy its code; the differences are deliberate:

| | pdf-figure-vector | `figure_recovery.py` |
|---|---|---|
| Dependencies | Chrome, vtracer, fonttools | PyMuPDF, Pillow, numpy |
| Preview | auto-opens a browser | opt-in `--open` |
| Comparison | Chrome screenshots | PyMuPDF renders the SVG, headless |
| QA gate | MAE report | normalised MAE + structural share, exit code |
| PPTX output | yes, editable shapes + fonts | not emitted; use PowerPoint's SVG import |
| Raster input | traces with vtracer | reports `raster` and refuses to pretend |

If you need PPTX with editable text objects and font subsetting, use the upstream project and
follow its instructions; for a fast, headless, dependency-light recovery inside this skill, use
this script.
