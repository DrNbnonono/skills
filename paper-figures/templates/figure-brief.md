# Figure brief — fill before drawing

Copy this file next to the figure script and fill it in. Two minutes here prevents the most
common rework: a well-drawn figure that shows the wrong quantity.

---

**Figure id:** `fig<N>_<short_name>`
**Section it supports:** §___
**Will appear:** single column / double column / sidebar

## 1. The claim (one sentence, with the number)

> e.g. "Public exploit code now appears faster than advisory text: the 30-day
> artifact-to-advisory ratio rose from 0.63 (Pre-AI) to 1.83 (AI)."

If you need "and" to state it, you need two figures.

## 2. What the reader must notice in five seconds

One sentence, written from the reader's point of view:

> e.g. "The green curve is far to the left of the black one."

## 3. Data and denominator

- Data file / query:
- n (per group):
- Unit of observation:
- Uncertainty shown (CI / error bar / none, and why):
- Exclusions:

## 4. Encoding

| Element | Choice |
|---|---|
| Chart type (encoding-guide §1) | CDF / dumbbell / swimlane / heatmap / scatter / bars / small multiples |
| x-axis | quantity + unit + scale |
| y-axis | quantity + unit + scale |
| Series | 3–5, with colour + marker + line style |
| Colour palette | Okabe–Ito `SERIES` (default) |
| Scale | linear / log (justify) |

## 5. Size and output

- Drawn at: 3.5 in × ___ in (single column) / 7.16 in (double)
- Files: `figs/fig<N>_<name>.py`, `.pdf`, `.png`
- Included as: `\includegraphics[width=\columnwidth]{...}`

## 6. Caption draft (takeaway first)

> Sentence 1: the claim.
> Sentence 2: what is plotted, units, scale.
> Sentence 3: n, uncertainty, one caveat.

## 7. Checks before marking done

- [ ] Five-second test passed with a colleague
- [ ] Caption first sentence survives without the figure
- [ ] Numbers match text and table
- [ ] Grayscale preview read (`check_figure.py --preview`)
- [ ] CVD preview read
- [ ] Fonts ≥ 7 pt at print size
- [ ] Figure referenced in the text with a claim
- [ ] Script committed with the figure
