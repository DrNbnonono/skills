# Venue figure profiles (top-4 security/systems, journals, magazine)

Figures are judged by the same reader who judges the prose: a reviewer skimming, often
printing the paper. What changes by venue is the page geometry and the display-item budget,
not the standard.

Confidence labels: **[official]** = stated in the venue's author instructions; **[template]** =
derived from the template's measured geometry; **[observed]** = consistent across accepted
papers, not a rule.

---

## 1. Geometry (the numbers that actually constrain you)

| Venue | Template | Single column | Double column | Caption position |
|---|---|---|---|---|
| IEEE S&P | IEEEtran, `compsoc` | 3.5 in | 7.16 in | below figure |
| NDSS | IEEEtran | 3.5 in | 7.16 in | below figure |
| ACM CCS | `acmart`, sigconf | 3.33 in | 7.0 in | below figure |
| USENIX Security | USENIX template | 3.4 in | 7.0 in | below figure |
| IEEE/ACM journals | their template | ~3.5 in | ~7.16 in | below figure |
| IEEE S&P Magazine | publisher typesets | ~3.4 in | 7.0 in | below figure, publisher's style |

**[template]** These are the usable text widths, not the paper size. A figure set to 3.5 in
and included with `width=\columnwidth` prints at exactly the size you drew it; a figure drawn
at 7 in and included at `width=\columnwidth` has its fonts halved.

**Practical rule:** draw at the width it will be printed (`new_fig(3.5, …)`), keep
`\includegraphics[width=\columnwidth]`, and never scale down.

## 2. Raster resolution and vector rules

- **[official]** IEEE asks for 300 dpi for raster art (600 dpi for line art), and prefers
  vector. USENIX and ACM accept PDF/EPS vector.
- **[official]** Fonts must be embedded; Type 3 fonts are rejected by IEEE PDF eXpress.
  Matplotlib: `pdf.fonttype = 42` (set in `figure_style.apply_style()`).
- **[observed]** Any photo, screenshot, or heatmap exported as PNG should be 300 dpi at final
  width. Everything with lines and text is a PDF.

## 3. What strong top-4 figures share [observed]

1. **One conceptual figure early.** A system/attack overview in the first 2–3 pages that a
   reviewer can read without the text. It earns the space; it is usually the most-cited figure
   in later papers.
2. **Results as compact plots or dense tables, not dashboards.** One claim per item.
3. **Direct labels, not legend boxes.** Series names at the line ends; panel labels A/B/C.
4. **Grayscale-safe.** Many reviewers print. Colour encodes the category, but shape/position
   also does.
5. **Captions that state the takeaway first**, then the units and n.
6. **Small footprint.** Most figures are one column, ~2.0–2.6 in tall. A full-width figure is
   reserved for the conceptual diagram or a multi-panel main result.
7. **No chartjunk.** No 3-D, no gradients, no shadow, no decorative icons, no rainbow maps.

## 4. Rules that change by venue

| Rule | Top-4 conference | Magazine | Journal |
|---|---|---|---|
| Anonymity | S&P/CCS/NDSS: anonymous — no identifying artifacts in figures (no internal hostnames, no author paths) | Single-blind: real names, real affiliations | Author names allowed |
| Display items | 6–10 | 4–6 | 8–12 |
| Colour | Assume print reproduces in grayscale | Assume the same; colour online only | Same |
| Caption length | 2–4 sentences, self-contained | 2–3 sentences, takeaway first, no jargon | 3–5 sentences |
| Vector requirement | Yes | Publisher will re-typeset; supply vector + source | Yes |
| Appendix figures | Allowed | No appendices — a sidebar instead | Allowed |

**Anonymity trap (S&P/CCS/NDSS).** Figure metadata, file paths, and screenshots can deanonymise
a submission: strip `Author` from the PDF metadata (`matplotlib` sets it from
`savefig.metadata` only if you configure it), remove usernames from screenshot paths, and do
not put an institutional logo in a figure.

## 5. How reviewers actually look at a figure [observed]

1. Read the caption first. If the caption does not state a claim, the figure is skipped.
2. Check the axes: units, scale, zero baseline, log label.
3. Check that the numbers match the text and table.
4. Check uncertainty: is there a CI, error bar, or n?
5. Only then look at the visual pattern.

This order is why the caption and the axes come before aesthetics in this skill.

---

Sources (check current-year instructions before relying on any of these):

- IEEE author center, graphics and tables: <https://journals.ieeeauthorcenter.ieee.org/>
- ACM primary article template (sigconf): <https://www.acm.org/publications/proceedings-template>
- USENIX Security submission instructions: <https://www.usenix.org/conference/usenixsecurity25>
- VUSEC writing checklist (figures and tables section):
  <https://download.vusec.net/resources/thesis/guidelines/PaperWritingChecklist.pdf>
- Rougier, Droettboom, Bourne, "Ten Simple Rules for Better Figures", PLOS Comput Biol 2014:
  <https://doi.org/10.1371/journal.pcbi.1003833>
- Crameri, Shephard, Heron, "The misuse of colour in science communication", Nat Commun 2020:
  <https://doi.org/10.1038/s41467-020-19160-7>
