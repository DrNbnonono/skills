# Encoding guide: claim → chart

Choose the chart from the claim, not from the data shape. This file maps the claims that
appear in security/systems papers to the encodings that make them visible.

---

## 1. The mapping

| The claim in one sentence | Encoding | Why | Example |
|---|---|---|---|
| "X is faster/slower than Y" | CDF (step), survival curve | Shows the whole distribution, not a mean; log x for heavy tails | `examples/fig01_cdf.png` |
| "The gap between claim and reality is large" | dumbbell / paired dots | Makes the two values and the gap readable in one glance | `examples/fig02_dumbbell.png` |
| "The disclosure happened in this order" | swimlane / timeline | Ordering is the message; positions carry meaning | `examples/fig03_swimlane.png` |
| "Gaps fall into these categories, and only some cells are populated" | labelled grid, populated cells only | The empty cells are part of the finding | `examples/fig04_taxonomy.png` |
| "Coverage depends on two dimensions" | heatmap with in-cell values | Matrix structure is the message; values keep it honest | `examples/fig05_heatmap.png` |
| "There is a trade-off; these points are not dominated" | scatter + Pareto frontier | Frontier makes the trade-off explicit | `examples/fig06_pareto.png` |
| "The same pattern holds in every era/group" | small multiples, shared axes | Comparison is vertical; shared axes prevent misreading | `examples/fig07_smallmultiples.png` |
| "These five items rank like this" | sorted horizontal bars, direct values | Length is the most accurate visual channel | `examples/fig09_good_vs_bad.png` |
| "The distribution is skewed / has outliers" | strip plot + box, or violin with n | Mean bars would hide it | — |
| "A and B co-vary" | scatter with fit and CI | Shows spread and trend together | — |
| "Composition changes over time" | stacked area or 100 % stacked bar | Part-whole over a time axis | — |
| "Two variables change together over years, with events marked" | line + annotated event markers | Narrative and trend in one frame | — |

## 2. Chart-by-chart rules

### CDF (cumulative distribution)

- Use a **step** CDF, not a smoothed line: the data are empirical.
- Log x is right when values span decades (days to first PoC: 1–365). Label the axis
  "(log scale)" and put ticks at decades.
- Mark the median with a tick or a dot; the median is the sentence you will write.
- Compare 3–5 groups. More curves on one axes is unreadable; use small multiples.

### Dumbbell / paired dots

- One row per item, two dots per row, a light connector.
- Label both values; the gap is the claim.
- Do not use grouped bars for two values per item: bars start at zero and the gap disappears
  when both values are large.

### Heatmap

- Use a perceptually uniform sequential map (`cividis`); never `jet`/rainbow.
- Write the value in each cell if there are fewer than ~60 cells; the colour is a hint, the
  number is the evidence.
- Mark inapplicable cells explicitly (e.g. `—` on a light background); an empty cell and a
  zero are different statements.
- Diverging maps only when zero is meaningful and the sign matters.

### Timeline / swimlane

- One lane per actor (finders, vendor, public); time on x.
- Label events in the lane where the action happened, not in a legend.
- Mark the release date with a vertical line; that line is usually the story.
- Keep labels short; the caption carries the narrative.

### Scatter / Pareto

- Axis = the two quantities in the claim; log only when the range demands it.
- Draw the frontier if you claim a trade-off; state in the caption what "better" means
  (fewer days, more artifacts, lower cost).
- Annotate 1–3 points, not all of them.

### Small multiples

- Same axes limits and ticks in every panel; the comparison must be visual, not numeric.
- Title each panel with the group name, label panels A–D only if the caption refers to them.
- One shared y-axis label, not one per panel.

### Bars

- Start at zero. Always.
- Sort by value unless the order is meaningful (e.g. chain A–E).
- Horizontal bars when labels are long; direct value labels instead of a gridline dance.

## 3. Uncertainty: what to show

| Situation | Show |
|---|---|
| Median over n events | CI band, or error bars, with n in the caption |
| Proportion | CI (Wilson/Clopper–Pearson), or the count and denominator |
| Point estimate from a small sample | The individual points (strip) plus the summary |
| Model fit | Fit line + CI band + data |
| Comparison of two proportions | Two CIs, or a difference with its CI |

A figure that shows a point estimate with no uncertainty and no n is read as a stronger claim
than the data support. Reviewers know this.

## 4. When a table wins

A table beats a figure when:

- the reader needs exact values (completeness percentages, counts, p-values);
- there are many dimensions (event × stage × driver);
- n is small and the pattern is verbal, not visual;
- the claim is a list, not a comparison.

Keep tables dense but readable: no vertical rules, a single horizontal rule above and below,
caption above the table (IEEE style), numbers right-aligned, units in the column header.

## 5. Axis integrity checklist

- Bar charts start at zero; line charts may start elsewhere only if the caption says so.
- Log axes are labelled "(log scale)" with decade ticks.
- No dual y-axis. If two quantities must share an x, use two stacked panels.
- Units on every axis, including ratios ("%" or "×").
- Consistent denominators across panels.
- The same colour means the same thing in every figure of the paper.
