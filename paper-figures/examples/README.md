# Examples

What good looks like. Every image here is generated from **synthetic data** by
`scripts/make_examples.py` — nothing is copied from a published paper, and the numbers are
illustrative, not results.

Regenerate all of them:

```bash
python scripts/make_examples.py
```

Each figure is drawn at 3.5 in (single column) with fonts set at print size, using
`scripts/figure_style.py`.

---

## fig01_cdf.png — distribution comparison over time

**Claim shown:** public exploit code appears sooner in later eras (median 19 → 3 days).
**Encoding:** step CDF, log x-axis, four eras.
**Rules demonstrated:** step CDF, log axis labelled "(log scale)", decade ticks, horizontal
legend above the axes when end-labels would collide, light horizontal grid, no top/right spines.
**LaTeX usage:** single column, `width=\columnwidth`.

## fig02_dumbbell.png — paired comparison

**Claim shown:** the literal reading of an advisory hides most of the covered surface; the gap
between the two lenses is the finding.
**Encoding:** dumbbell (one line per item, dot at each lens), values labelled at both ends.
**Rules demonstrated:** paired encoding instead of grouped bars; direct value labels; no legend
box inside the plot; sorted by magnitude from top to bottom.

## fig03_swimlane.png — timeline

**Claim shown:** three independent reports, a leak, an accelerated release, a follow-on CVE.
**Encoding:** three lanes (finders / vendor / public), time on x, labelled events.
**Rules demonstrated:** one lane per actor; the release date as a single vertical rule; short
labels; the caption carries the narrative.

## fig04_taxonomy.png — typology with only populated cells

**Claim shown:** gaps concentrate in two cells; four cells never occur.
**Encoding:** labelled grid, rounded boxes only where counts exist.
**Rules demonstrated:** the absence of a cell is part of the message; counts are large and
central; stage and driver labels on the axes instead of a legend.

## fig05_heatmap.png — matrix

**Claim shown:** exploitability is configured by chain and version; some cells do not exist.
**Encoding:** matrix, `cividis`, in-cell values, grey "—" for undefined cells.
**Rules demonstrated:** perceptually uniform map; values written in cells; inapplicable cells
distinguished from zeros; colourbar labelled with units.

## fig06_pareto.png — trade-off

**Claim shown:** faster PoC publication goes with more artifacts; one point is not dominated.
**Encoding:** scatter, era colours, Pareto frontier as a dashed step line.
**Rules demonstrated:** log x-axis labelled; frontier drawn and named; 1–3 annotations, not all
points; legend only because direct labels would overlap.

## fig07_smallmultiples.png — same measurement per era

**Claim shown:** artifacts overtake advisories in the last era.
**Encoding:** 2×2 small multiples, shared axes, panel labels A–D.
**Rules demonstrated:** shared limits so comparison is visual; one shared y label; panel labels;
consistent colours across panels.

## fig08_palette.png — the palette and its two previews

**Content:** Okabe–Ito swatches with hex codes, then the same swatches in grayscale and under
deuteranopia simulation.
**Rules demonstrated:** the palette; that colour survives grayscale and CVD; where to get the
hex values (`figure_style.OKABE_ITO`).

## fig09_good_vs_bad.png — the anti-pattern pair

**Left (avoid):** rainbow pie, exploded slices, shadow, 4.5 pt text.
**Right (prefer):** sorted horizontal bars, one colour, direct values, 7 pt text.
**Also:** `fig09_good_vs_bad_grayscale.png` is the same figure converted to grayscale — the pie
becomes indistinguishable wedges, the bars stay readable. That is the print-safety test.

---

## How to use these as references

1. Read the caption of the figure and the claim in this README side by side: the caption should
   be able to stand alone.
2. Run `python scripts/check_figure.py examples/<file>.png --preview` and look at the
   grayscale/CVD outputs.
3. Copy the closest example as a starting point, then change the data — not the style.
