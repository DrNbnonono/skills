# Figures in the argument

A figure is not decoration and not a data dump: it is **a claim made visible**. This file covers the
planning decisions that belong to writing — which figure, which chart, which palette, which caption —
and hands execution (style module, export, grayscale checks) to `paper-figures`.

---

## 1. One figure, one claim

Before the figure exists, write its caption. If the caption needs "and", the figure is two figures.

| Caption that is a claim | Caption that is a label |
|---|---|
| "Recall falls to 3% under a literal reading of the advisory text." | "Recall by advisory source type." |
| "The ratio inverts after 2022: artifacts outgrow advisories." | "Artifact and advisory counts over time." |

The caption is the claim; the axes are the evidence. If you cannot write a claim-shaped caption, the
figure has no job.

---

## 2. Chart type follows the claim

| The claim is about | Use | Avoid |
|---|---|---|
| A comparison across categories | bar (horizontal if labels are long) | pie, 3-D bars |
| A trend over time | line, one line per series | stacked bars over many periods |
| A distribution or spread | CDF, box, violin | mean-only bars |
| A trade-off between two quantities | scatter, with the Pareto front marked | dual-axis lines |
| Composition of a total | stacked bar (few categories) | donut charts |
| A pipeline or mechanism | schematic diagram | a table pretending to be a picture |
| Coverage over a space (versions × paths) | matrix/heatmap with explicit cells | heatmap with continuous colormap and no legend |

---

## 3. Colour: what the corpus actually does

`scripts/figure_color_study.py` sampled **50 figures from 20 top-tier papers** (ar5iv raster images):

| Measure | Result |
|---|---|
| Distinct hues carrying ≥5% of coloured pixels | **median 2** |
| Figures with ≥4 distinct hues | 32% |
| Figures using a red **and** green pair | **18%** |
| Mean saturation of coloured pixels | 0.47 (moderate) |
| Luminance spread (grayscale proxy) | median std 55 |

Read this as a description, not a target. The usable lessons:

1. **Most figures are two-hue.** A four-hue palette is a choice, not a default; make it deliberately
   (four series, four conditions).
2. **Red/green is common and is the most common accessibility failure** (about one figure in five).
   If red and green must appear, separate them by luminance and line style, and never rely on the hue
   alone.
3. **Saturation around 0.5 prints better than 1.0.** Pure saturated fills turn into indistinguishable
   grey blocks in grayscale.
4. **Luminance separation is what survives printing.** Check the figure in grayscale before
   submission; a distinction that exists only in hue disappears in print.

For palettes, export settings, and the automated checks, use `paper-figures`.

---

## 4. Planning table

Fill before plotting; this is the writing-side handoff.

| # | Claim (caption draft) | Chart type | Series / categories | Palette + distinction | Grayscale-safe? | Body/Appendix |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

A row with an empty "claim" column should not be plotted.

---

## 5. Order and reference

- Figure order must follow the argument's order, not the order the experiments were run.
- Every figure is cited **before** it appears, and the citing sentence names the panel or axis
  (`paper-prose-polish/references/floats-and-references.md`).
- A figure that is never cited is a figure to delete, not to keep "for completeness".

---

## 6. Common defects

| Defect | Why it costs the reader | Fix |
|---|---|---|
| Axis starts at a non-zero value without saying so | exaggerates the effect | start at zero, or mark the break |
| No units | the number cannot be interpreted | label with units |
| Two y-axes | invites a false correlation | two panels side by side |
| Legend inside the plot area | covers data | move outside, or label lines directly |
| Error bars without saying what they are | ambiguous | state SD/SE/CI in the caption |
| Caption repeats the axis labels | wastes the one place that could state the claim | rewrite as a claim |
| Colour-only distinction | fails in grayscale and for colour-vision deficiency | add marker/line style |
