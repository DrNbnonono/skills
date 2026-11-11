# Production: from script to camera-ready

---

## 1. File layout (put the script next to the figure)

```
paper/
├── figs/
│   ├── fig1_cdf.pdf        # generated, committed
│   ├── fig1_cdf.png        # preview, committed for reviewers/GitHub
│   ├── fig1_cdf.py         # the script that generated it
│   └── data/fig1.csv       # the data (or a seed if synthetic)
└── sections/...
```

Rule: **a figure that cannot be regenerated is a liability.** Six months later, camera-ready
asks for a label change; the script turns that into a one-line edit instead of a redraw.

## 2. Export settings (matplotlib)

```python
import matplotlib as mpl
mpl.rcParams.update({
    "pdf.fonttype": 42,      # embed TrueType; IEEE PDF eXpress rejects Type 3
    "ps.fonttype": 42,
    "savefig.dpi": 300,      # raster only
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})
fig.savefig("figs/fig1_cdf.pdf")   # vector, for LaTeX
fig.savefig("figs/fig1_cdf.png")   # preview
```

- **PDF** for anything with text or lines: axes, annotations, CDFs, bars, timelines.
- **PNG at 300 dpi** only for photographs, screenshots, and raster heatmaps.
- **Never** export a screenshot of matplotlib at 72 dpi and scale it in LaTeX.

## 3. Check before inclusion

```bash
python scripts/check_figure.py figs/*.png --width-in 3.5 --preview
```

- 300 dpi and the intended width;
- grayscale and CVD previews read correctly;
- no clipped label at the edges (bbox tight should prevent it, but check the PDF).

For the PDF, open it and check at 100 %: fonts ≥ 7 pt, no missing glyphs (tofu boxes), no
rasterised text.

## 4. LaTeX inclusion

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figs/fig1_cdf.pdf}
  \caption{...}
  \label{fig:cdf}
\end{figure}
```

| Want | Use |
|---|---|
| Single column | `width=\columnwidth` |
| Double column | `width=\textwidth` |
| Exact print size | draw at that size, still include at `\columnwidth` |

Do not use `\resizebox`, `\scalebox`, or `height=` — they change the effective font size and
break the 7 pt guarantee. If the figure must be smaller, redraw it at the smaller size.

## 5. Fonts

- Use a font that exists on the build machine; `DejaVu Sans` ships with matplotlib and is
  safe, `Helvetica` may not be present on Linux CI.
- If the venue requires Times-like text, use `font.family: serif` and `font.serif:
  ["DejaVu Serif", "Times"]`; check the PDF after compiling.
- Embed fonts: `pdf.fonttype = 42`. Check with `pdffonts fig1.pdf` (all fonts should show
  `yes` in the `emb` column).

## 6. Anonymity (S&P, CCS, NDSS)

- Save the PDF **without** author metadata in the figure itself; matplotlib does not add
  author names by default, but check the PDF properties.
- No internal hostnames, no `/home/<name>/`, no institutional logo, no screenshot of an
  internal dashboard.
- File names should not contain the author's name (`fig1_cdf.pdf`, not
  `zhang_attack_v3.pdf`).

## 7. Camera-ready checklist

- [ ] Every figure referenced by `\ref` and discussed with a claim in the text
- [ ] Vector PDF for line art; 300 dpi for raster
- [ ] Fonts embedded; no Type 3; no tofu glyphs
- [ ] Fonts ≥ 7 pt at printed size
- [ ] Width = column width; no scaling in LaTeX
- [ ] Caption states the takeaway, unit, n, uncertainty
- [ ] Numbers match the table and the text
- [ ] Grayscale and CVD previews read correctly
- [ ] Script + data committed; figure reproducible
- [ ] Anonymity clean (for double-blind venues)
- [ ] No figure duplicates a table
- [ ] Total display items within the venue budget

## 8. Common build failures

| Symptom | Cause | Fix |
|---|---|---|
| Fuzzy text in the PDF | figure exported as PNG and scaled up | export PDF |
| Fonts rejected by PDF eXpress | Type 3 fonts from old matplotlib/PS output | `pdf.fonttype = 42`, re-export |
| Labels clipped at the edge | `bbox_inches` not tight | `savefig.bbox = "tight"`, `pad_inches = 0.02` |
| Text too small in print | drawn at 7 in, included at 3.5 in | redraw at printed width |
| Grayscale mush | colours similar in luminance | change marker/line style |
| Figure floats to the end of the paper | too large for one column | reduce height, use `[t]` |

## 9. Reproducibility

Keep the generator deterministic: fixed `numpy` seed, data file committed, style imported
from `scripts/figure_style.py` (not copy-pasted rcParams). Then a camera-ready edit is a
one-line change and a re-run, not a redraw.
