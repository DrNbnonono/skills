# Anti-patterns

Each entry: what it looks like, why it fails, what to do instead. `examples/fig09_good_vs_bad.png`
shows two of them side by side.

---

## 1. The rainbow heatmap

`jet`, `hsv`, `rainbow`, or a hand-made 5-colour gradient over a continuous quantity.

**Why it fails.** Not perceptually ordered: equal value steps look unequal; the green/yellow
band creates a boundary that does not exist in the data; it turns to noise in grayscale and
misleads colour-blind readers.

**Instead.** `cividis` (default) or `viridis`; annotate values in the cells when there are
fewer than ~60.

## 2. The 3-D bar / pie / exploded pie

**Why it fails.** Perspective distorts lengths and angles; a slice at the back looks smaller;
shadows add pixels that encode nothing. `examples/fig09_good_vs_bad.png` (left) is the
deliberate demo.

**Instead.** Sorted horizontal bars with direct values; if parts of a whole matter, a stacked
bar or a small table.

## 3. Pie with more than three slices

**Why it fails.** Humans compare angles poorly; five slices are already guesswork.

**Instead.** Sorted bars, or a table if exact values matter.

## 4. The dual y-axis

Two quantities, two scales, one plot.

**Why it fails.** The reader will infer a correlation from the alignment of the curves, and
the alignment is a choice of scale. This is the most common "misleading figure" in reviews.

**Instead.** Two stacked panels sharing the x-axis, or normalise both series and say so.

## 5. Truncated y-axis on bars

**Why it fails.** A bar from 60 to 66 looks like a 10× difference. Reviewers notice, and it
costs more trust than the point gains.

**Instead.** Start at zero. If the differences are small, plot the difference directly (a
dumbbell or a delta plot) and show the CI.

## 6. The six-entry legend box

**Why it fails.** The reader has to match colours back and forth between plot and box; with
six entries nobody does it.

**Instead.** Direct labels at the line ends; or small multiples, one panel per series; or a
legend above the axes with two to four entries (`examples/fig01_cdf.png`).

## 7. Scaled-down figure (tiny fonts)

Draw at 7 in, include at `\columnwidth` (3.5 in).

**Why it fails.** Every font halves: 8 pt becomes 4 pt, i.e. grey noise. The figure cannot be
read at 100 % or in print.

**Instead.** Draw at the printed width. `new_fig(3.5, …)` in `figure_style.py`.

## 8. Caption that describes the axes

> "The x-axis shows days and the y-axis shows the fraction. The blue line is…"

**Why it fails.** The reader already sees the axes. The caption is the one place to state the
claim and the n.

**Instead.** First sentence = the claim; second = the encoding; third = n/CI/caveat. See
`captions.md`.

## 9. Figure that restates a table

**Why it fails.** It consumes a display item and adds no information; reviewers read it as
padding.

**Instead.** Keep whichever communicates the claim faster (usually the figure), and move the
exact values into the text or the appendix.

## 10. Unlabelled log axis

**Why it fails.** Slopes are not comparable; a reader who assumes linear axes misreads the
rate of change by an order of magnitude.

**Instead.** `ax.set_xscale("log")` plus "(log scale)" in the axis label and decade ticks.

## 11. Point estimate, no uncertainty

A single number per condition with no error bar, CI, or n.

**Why it fails.** It reads as a precise measurement; the reader cannot tell a difference from
noise.

**Instead.** CI band / error bar / individual points + n in the caption.

## 12. The screenshot figure

A screenshot of a terminal, a dashboard, or a table from a paper.

**Why it fails.** Not vector, not editable, not searchable, unreadable at 100 %, and often
contains identifying details (anonymity violation).

**Instead.** Re-create the information as a table or a vector plot; if a screenshot is
unavoidable, crop tightly, 300 dpi, and redact names/paths.

## 13. Decorative gridlines and fills

Heavy grids, zebra-striped backgrounds, gradient fills, drop shadows.

**Why it fails.** Data-ink ratio: ink that does not encode data competes with the data.

**Instead.** Horizontal grid only, light grey; no background fills; no shadow.

## 14. Colour as the only channel

Two series identical except for hue.

**Why it fails.** ~8 % of male reviewers are red–green colour blind; most reviewers may print
in grayscale.

**Instead.** Colour + marker shape + line style; check `--preview` output.

## 15. The missing reference

A figure that the text never discusses with a claim.

**Why it fails.** It signals the figure was drawn for the authors, not the reader. Reviewers
notice orphan figures in a display-item budget.

**Instead.** Reference it with a claim ("Figure 5 shows that the ratio crosses 1 in the AI
era"), or remove it.

---

## Quick removal test

For every figure, ask in order:

1. Can I delete it without losing a claim the text needs? → delete it.
2. Does it show one thing? → if not, split it.
3. Is the claim in the caption's first sentence? → if not, rewrite the caption.
4. Does it survive grayscale? → if not, add shape.
5. Is every number in it also in the table/text? → if not, reconcile.
