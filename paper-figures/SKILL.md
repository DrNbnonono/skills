---
name: paper-figures
description: Design, draw, and verify figures for security/systems papers (IEEE S&P, USENIX Security, CCS, NDSS, journals, IEEE S&P Magazine), in the style of strong top-4 papers. Use for 画图/作图/图表设计/论文配图, choosing the right chart for a claim, making a figure print-safe, writing captions that state the takeaway, or converting a matplotlib figure into a camera-ready vector PDF. Optionally recovers your own figures from a PDF as self-contained vector SVG with a pixel QA gate (never for other people's figures). Ships runnable examples with synthetic data (examples/), a matplotlib style module (scripts/figure_style.py), a generator (scripts/make_examples.py), and pre-submission checkers (scripts/check_figure.py, scripts/figure_recovery.py).
version: 1.1
---

# Paper figures

A figure is an argument made visible. It earns its place when a reader who looks at it for
five seconds, before reading the caption, can state the claim it makes. Everything in this
skill serves that test.

The style it encodes is the one strong papers at S&P, USENIX Security, CCS, and NDSS share:
small, vector, two-column-width figures; few display items; direct labels; print-safe colour;
captions that state the takeaway rather than describing the axes.

## Core principle

**One figure = one claim = one message in the caption.**

If two claims need showing, draw two panels or two figures. A figure that shows three things
is read as none of them.

## Non-negotiables

1. **One message per figure.** The caption's first sentence states it; the graphic supports it.
2. **Draw at printed size.** A single-column figure is 3.5 in wide (IEEE), 3.33 in (ACM
   sigconf), 3.4 in (USENIX). Never draw big and scale down in LaTeX: the fonts shrink below
   the 7 pt floor.
3. **Vector output** (`.pdf` from matplotlib) for anything with text or lines. 300 dpi raster
   only for photographs and screenshots.
4. **Fonts ≥ 7 pt at print size**; axis labels 8 pt, tick labels 7 pt.
5. **Print-safe colour**: Okabe–Ito palette, nothing distinguished by colour alone, and the
   figure must survive grayscale (`scripts/check_figure.py --preview`).
6. **No misleading axes**: bar charts start at zero; log scales are labelled; no truncated
   y-axis to dramatise a difference; no dual y-axes without an explicit, stated reason.
7. **Show uncertainty** where the claim is quantitative: CI bands, error bars, or n in the
   caption. A point estimate without a denominator is not a result.
8. **The caption states what to notice**, then the units, then n. It is not a list of colours.
9. **No chartjunk**: no 3-D, no shadows, no gradients as decoration, no rainbow maps, no
   background fills, no gridlines that fight the data.
10. **Reproducible**: the script that generated the figure lives next to it in the repo, with
    the data file or a seed. A figure no one can regenerate is a liability at camera-ready.
11. **Never lift a figure.** A figure from another paper is copyrighted unless its licence says
    otherwise, and presenting it as yours is plagiarism. `scripts/figure_recovery.py` exists to
    recover **your own** figures (or licensed ones, with attribution) from a PDF — not to
    harvest other people's. Recovered files live under `analysis/`, never in `figs/`.

## Step 0 — Decide the claim first

Write one sentence, in words, that the figure must make self-evident:

> "Public exploit code now appears faster than advisories: the 30-day artifact-to-advisory
> ratio rose from 0.63 to 1.83 across four eras."

If you cannot write that sentence without "and", you have two figures.

Fill `templates/figure-brief.md` before touching matplotlib. It takes two minutes and prevents
the most common rework: a beautiful figure that shows the wrong quantity.

## Step 1 — Choose the encoding from the claim

Read `references/encoding-guide.md`. The short version:

| Claim type | Encoding | Avoid |
|---|---|---|
| Distribution / how fast | CDF (step), violin, box, strip | bar of means with no spread |
| Paired comparison | dumbbell, slope, paired dots | two floating bars |
| Composition over time | stacked area, small multiples | pie, 3-D pie |
| Ranking | sorted horizontal bars, dot plot | unordered bars, rainbow |
| Two-variable trade-off | scatter + Pareto frontier | bubble with unreadable sizes |
| Matrix / coverage | heatmap with a perceptually uniform map, in-cell values | rainbow heatmap without values |
| Process / timeline | swimlane, timeline, sequence diagram | a table of dates in prose |
| Taxonomy / decision | labelled tree, matrix of populated cells | nested bullet text |

## Step 2 — Draw with the shared style

```python
import sys; sys.path.insert(0, "scripts")
from figure_style import apply_style, new_fig, save, SERIES, panel_label

apply_style()                       # 8 pt base, Okabe–Ito, print-safe rcParams
fig, ax = new_fig(3.5, 2.3)         # single column, correct aspect
ax.plot(x, y, color=SERIES[0], label="Pre-AI")
save(fig, "figs/fig1_cdf")          # writes .pdf (for LaTeX) + .png (preview)
```

Adjust the style **globally**, never per figure: two figures in one paper with different
fonts or line weights read as two different papers.

`references/style-spec.md` lists every setting and why it is set that way.

## Step 3 — Label directly, caption last

- Put the series name at the end of its line, or on the plot, rather than in a legend box.
  Use a legend only when direct labels would collide (see `examples/fig01_cdf.png`).
- Panel labels **A**, **B**, **C** in bold at the top-left, referenced from the caption.
- Axis labels: quantity + unit + scale (`Days since disclosure (log scale)`).
- Then write the caption with `references/captions.md`: takeaway → what the axes show →
  units/n/CI → the one caveat a reader must not miss.

## Step 4 — Make it print-safe

- Palette: `SERIES` in `scripts/figure_style.py` (Okabe–Ito). Sequential data: `cividis`,
  never `jet`. Diverging: `RdBu_r`, only around a meaningful zero.
- Encode by shape too: markers and line styles vary with series, so the figure survives
  grayscale printing and colour-blind reviewers.
- Run the checker:

```bash
python scripts/check_figure.py figs/fig1_cdf.png --preview
```

It reports size/dpi, the chromatic palette, the grayscale and deuteranopia separation, and
writes `fig1_cdf_gray.png` / `fig1_cdf_cvd.png`. **Look at both.**

`references/accessibility.md` covers the details (contrast, CVD, alt text).

## Step 5 — Export and include

- Export vector PDF with embedded TrueType fonts (`pdf.fonttype = 42`, already set).
- Include at the printed width: `\includegraphics[width=\columnwidth]{figs/fig1_cdf.pdf}`.
- Check the compiled PDF at 100 %: no text below 7 pt, no clipped labels, no figure taller
  than half a column unless it is the paper's main conceptual figure.
- `references/production.md` covers LaTeX inclusion, font embedding, and file layout.

## Step 6 — Verify like a reviewer

1. **Five-second test**: show the figure alone to someone; can they state the claim?
2. **Caption test**: the first sentence should be the claim, not "Figure 3 shows…".
3. **Grayscale test**: both previews read correctly.
4. **Zoom test**: at 100 % of the compiled PDF, every label is legible.
5. **Integrity test**: the numbers in the figure match the table and the text; the axis is
   not truncated; error bars are defined in the caption.
6. **Reuse test**: delete the PNG; does the script regenerate it byte-comparably? It should.

## Optional: recover a vector copy of an existing figure

Use this only for **your own** figure (source lost, PDF remains) or a licensed one you are
adapting with attribution — never to lift a figure from another paper (non-negotiable 11).

```bash
python scripts/figure_recovery.py probe   --pdf paper.pdf --page 3
python scripts/figure_recovery.py extract --pdf paper.pdf --page 3 --bbox 54,120,300,260 \
                                          --out analysis/recovered
```

- `probe` says whether the figure is native vector or raster. If it is raster, do **not** trace
  it and call it vector: redraw from data, or keep the image at 300 dpi.
- `extract` writes a self-contained SVG, a 300 dpi PNG, and a reference/recovered/difference
  image, and gates on a normalised pixel comparison (exit code 1 on failure).
- A recovered figure is for slides, archaeology, or study; anything going into the paper should
  still be redrawn with `scripts/figure_style.py`.

Requires PyMuPDF, Pillow, and numpy for this optional step only; the rest of the skill needs
matplotlib. Full workflow, guardrails, text-mode trade-offs, and known limits:
`references/figure-recovery.md`.

## Display-item budget

| Venue class | Total display items | Notes |
|---|---|---|
| Top-4 conference | 6–10 | One conceptual figure, one timeline, results tables; every item referenced in text |
| Magazine | 4–6 | One message per item; sidebars instead of appendices |
| Journal | 8–12 | More room, same rules |

If a figure is not referenced with a claim in the text ("Figure 5 shows that X"), remove it or
rewrite the sentence.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Rainbow/jet colormap | Not perceptually ordered; misleading values; unreadable in grayscale |
| 3-D or shadowed bars/pies | Decoration that distorts the comparison |
| Pie with >3 slices | Humans compare angles badly; use sorted bars |
| Dual y-axis | Invites a correlation claim the data does not support; use two panels |
| Truncated y-axis on bars | Exaggerates differences; a reviewer will notice |
| Legend box with 6 entries | Forces colour-matching; use direct labels or small multiples |
| Tiny text scaled down in LaTeX | Fonts fall below 7 pt; the figure becomes gray noise |
| Caption that lists colours | "The blue line shows…" tells the reader nothing they cannot see |
| Screenshot of a table | Not vector, not editable, not accessible |
| Figure that restates a table | Waste of a display item; keep the one that supports the claim |
| Unlabelled log axis | The reader cannot compare slopes across decades |
| Missing n / error bars | A point estimate without uncertainty is not evidence |

## Resource map

| File | Use |
|---|---|
| `references/venue-figure-profiles.md` | What the top-4 venues expect, column widths, caption/placement rules |
| `references/encoding-guide.md` | Claim → chart mapping, log scales, uncertainty, when a table wins |
| `references/style-spec.md` | Every matplotlib setting with its reason; palette hex codes |
| `references/captions.md` | Caption formula and before/after examples |
| `references/accessibility.md` | Colour-blind and grayscale safety, contrast, alt text |
| `references/production.md` | Export, LaTeX inclusion, fonts, file layout, reproducibility |
| `references/figure-recovery.md` | Recover a vector copy of a figure you own (or are licensed to reuse): guardrails, workflow, QA gate, limits |
| `references/anti-patterns.md` | What to remove, with the example that shows it |
| `scripts/figure_style.py` | rcParams, Okabe–Ito palette, `new_fig`, `save`, `panel_label` |
| `scripts/check_figure.py` | Size/dpi check, grayscale and deuteranopia previews, palette report |
| `scripts/figure_recovery.py` | Optional: PDF figure → self-contained SVG + pixel QA (PyMuPDF; own figures only) |
| `scripts/make_examples.py` | Generates every example figure (synthetic data) |
| `examples/` | Reference images: what good looks like, plus a bad-vs-good pair |
| `templates/figure-brief.md` | One-page brief before drawing |
