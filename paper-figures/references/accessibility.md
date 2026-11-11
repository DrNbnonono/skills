# Accessibility and print safety

Two readers you must assume: one printing the PDF in black and white, one who is red–green
colour blind (about 8 % of men). Neither is exotic, and both are in a program committee.

The test is not "is it pretty in colour" but "does it still carry the claim when colour is
removed".

---

## 1. Colour encoding rules

1. **Never encode a distinction by colour alone.** Pair colour with position, shape, line
   style, or a direct label. Then removing colour removes nothing.
2. **Use the Okabe–Ito palette** (`SERIES` in `scripts/figure_style.py`). It is designed for
   deuteranopia and protanopia and remains distinguishable in grayscale for most pairs.
3. **Avoid red/green semantics** (pass/fail, before/after) unless shape also differs.
4. **Sequential data**: use a perceptually uniform map (`cividis`). `jet`/rainbow creates
   false boundaries and turns to mush in grayscale.
5. **Diverging data**: `RdBu_r` only when zero is meaningful and the sign is the message.
6. **Contrast**: text and thin lines need ≥ 3:1 against the background; on white paper, avoid
   `yellow` and `sky` as thin lines (they are light). Use them as fills.

## 2. The grayscale test (do this every time)

```bash
python scripts/check_figure.py figs/fig3.pdf --preview   # writes fig3_gray.png
```

Look at the grayscale preview:

- Can you still tell the series apart?
- Are the CI bands still visible?
- Does any annotation disappear into the background?
- Is the highlighted point still highlighted?

If not, add a marker shape or line style difference — do not just darken the colours.

`examples/fig09_good_vs_bad_grayscale.png` shows the failure mode: a rainbow pie becomes
indistinguishable grey wedges, while the sorted bars remain readable.

## 3. The colour-blindness test

`--preview` also writes `<name>_cvd.png` (deuteranopia simulation, Machado et al. 2009). Check:

- Two series that were distinct in colour are still distinct in the preview.
- No information is carried by a hue difference alone.
- Heatmaps remain ordered (this is why perceptually uniform maps matter).

The checker also reports the minimum separation between the figure's chromatic inks; a value
below ~45/441 means two colours collapse.

## 4. Line styles and markers as the second channel

Use enough distinct combinations that four series are readable without colour:

| Series | Colour | Line | Marker |
|---|---|---|---|
| 1 | black | solid | ● |
| 2 | blue | dashed | ■ |
| 3 | vermillion | dash-dot | ▲ |
| 4 | green | dotted | ◆ |

For bars, hatch patterns are a last resort: they add visual noise. Prefer direct labels.

## 5. Text accessibility

- Minimum 7 pt at print size; 8 pt for axis labels.
- No text over a busy fill; put the label on the outside with a leader line.
- Avoid abbreviations in axis labels; expand them in the caption.
- Use sentence case, not all caps (all caps is slower to read and wider).

## 6. Alt text (for the arXiv/HTML version)

A figure in an HTML version needs an alternative text equal to its caption's claim, not a
description of pixels:

> `alt="CDF of days to first public exploit code by era; medians fall from 19 days (Pre-AI)
> to 3 days (AI)."`

## 7. Checklist

- [ ] Okabe–Ito or another CVD-safe palette
- [ ] Grayscale preview read and understood
- [ ] Deuteranopia preview read and understood
- [ ] Second channel (shape/line/label) for every colour distinction
- [ ] Sequences use `cividis`, not a rainbow
- [ ] Text ≥ 7 pt, contrast sufficient
- [ ] Alt text written for the HTML version
