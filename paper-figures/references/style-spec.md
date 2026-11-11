# Style specification

Every value below is set once in `scripts/figure_style.py` and applies to every figure in the
paper. Change it there, not per figure: two figures with different fonts or line weights read
as two different papers.

---

## 1. Size

| Item | Value | Reason |
|---|---|---|
| Single-column width | 3.5 in (IEEE), 3.33 in (ACM), 3.4 in (USENIX) | Prints at `\columnwidth` without scaling |
| Double-column width | 7.16 in (IEEE), 7.0 in (ACM/USENIX) | Conceptual figure or multi-panel main result |
| Default height | 2.0–2.6 in single column | Half a column; leaves room for the caption |
| Aspect | 1.3–1.7 wide : 1 tall | Reads well in two-column layout |
| Base font | 8 pt | 7 pt tick/label floor at print |
| Tick labels | 7 pt | Legible at 100 % of a printed page |
| dpi (PNG preview) | 300 | Venue requirement for raster |
| Output | PDF (vector) + PNG (preview) | PDF for LaTeX, PNG for GitHub/slides |

## 2. Palette (Okabe–Ito, colour-universal design)

| Name | Hex | Use |
|---|---|---|
| black | `#000000` | first series, single-series plots, text |
| orange | `#E69F00` | 5th series |
| sky | `#56B4E9` | 7th series, fills |
| green | `#009E73` | 4th series, "good/after" |
| yellow | `#F0E442` | highlight only (low contrast on white) |
| blue | `#0072B2` | 2nd series |
| vermillion | `#D55E00` | 3rd series, "before/claim" |
| purple | `#CC79A7` | 6th series |

Rules:

- **Series order** is `black, blue, vermillion, green, orange, purple, sky` (`SERIES`).
- **Sequential** data: `cividis` (perceptually uniform, grayscale-safe). Never `jet`, `hsv`,
  `rainbow`.
- **Diverging** data: `RdBu_r`, only around a meaningful zero.
- **Two-tone** comparisons (claim vs observed): `PAIR = [black, vermillion]` — distinguishable
  by lightness as well as hue.
- Yellow on white is low contrast; use it as a highlight fill, never as a thin line.

## 3. Lines, markers, fills

| Item | Value | Reason |
|---|---|---|
| Line width | 1.2 pt | Visible in print; 0.8 looks grey, 2.0 looks clumsy |
| Marker size | 3.5 pt | Small enough not to obscure data, large enough to see shape |
| Marker edge | 0.8 pt, darker than fill | Separates overlapping points |
| Error bar cap | 2 pt | Readable but not a cross |
| Fill alpha | 0.15–0.25 | CI bands visible, not overpowering |
| Grid | horizontal only, `#DDDDDD`, 0.5 pt | Guides the eye without competing |
| Spines | left + bottom only, 0.6 pt, `#333333` | Tufte-lite |
| Ticks | outward, 2.5 pt, 0.6 pt wide | Less ink than inward+grid |

## 4. Text

- Axis label: quantity + unit + scale, e.g. `Days since disclosure (log scale)`.
- No title inside the figure. The caption is the title. (Magazine exceptions: panel titles.)
- Use sentence case for labels, not Title Case.
- No periods at the end of axis labels or legend entries.
- Abbreviations: expand in the caption at first use.
- Direct labels at the end of curves beat a legend box. Use a legend when labels would
  collide (see `examples/fig01_cdf.png`, where a horizontal legend above the axes is cleaner
  than four colliding end labels).

## 5. Annotations

- Panel labels: bold `A`, `B`, `C` at the top-left, 8 pt, referenced from the caption.
- Annotation text: 7 pt, dark grey (`#222222`), one short clause.
- Leader lines: 0.5 pt, `#888888`. Never an arrow to every point.
- Highlight the one point that carries the claim; leave the rest unannotated.

## 6. matplotlib rcParams (the actual settings)

`apply_style()` in `scripts/figure_style.py` sets, among others:

```python
font.size = 8;  axes.labelsize = 8;  xtick.labelsize = 7;  ytick.labelsize = 7
lines.linewidth = 1.2;  lines.markersize = 3.5
axes.spines.top = False;  axes.spines.right = False
axes.grid = True;  axes.grid.axis = "y";  grid.color = "#DDDDDD"
legend.frameon = False
pdf.fonttype = 42          # embed TrueType, not Type 3 (IEEE requirement)
savefig.dpi = 300
```

Do not set `constrained_layout` and `tight_layout` together; choose one. The examples use
`fig.subplots_adjust`, which is predictable at fixed print size.

## 7. LaTeX side

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figs/fig1_cdf.pdf}
  \caption{Public exploit code now arrives faster than advisory text. Median days to the
  first public PoC fall from 19 (Pre-AI) to 3 (AI); the CDF is over 40 events per era
  (log-scaled x-axis).}
  \label{fig:cdf}
\end{figure}
```

- IEEE: figure captions go **below** the figure; table captions **above** the table.
- Keep `\label` after `\caption` so `\ref` numbers resolve.
- `width=\columnwidth` for single column, `width=\textwidth` for double column.
- Do not use `\resizebox`, `\scalebox`, or `height=` unless the figure was drawn for that
  size; scaling breaks the font-size guarantee.
