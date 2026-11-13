# Changelog

## v1.1 — figure recovery (own figures only)

Integrates the workflow of [`pdf-figure-vector`](https://github.com/tanzhouhu/pdf-figure-vector)
into this skill, re-implemented to be headless and dependency-light, with an explicit copyright
guard. A user asked whether the skill could recover figures from a PDF; the answer is yes for
figures you own, and emphatically not for figures you do not.

### Added

- **`scripts/figure_recovery.py`** — three subcommands:
  - `probe` — is the figure native vector or raster, plus the ink bbox and counts;
  - `extract` — crop a figure to a self-contained SVG (cropped viewBox, optional editable
    text), render a 300 dpi PNG, and gate on a normalised pixel comparison;
  - `compare` — re-check an existing SVG against the PDF crop, writing a reference / recovered /
    difference image.
- **`references/figure-recovery.md`** — guardrails (copyright, licence, never ship a recovered
  figure), workflow, how to read the QA numbers (`mae_norm`, `struct_pct`), text-vs-paths
  trade-off, editing path (Inkscape/Illustrator/PowerPoint), known limits, and a differences
  table against the upstream project.

### Design decisions (vs the upstream project)

- **Headless**: PyMuPDF renders the SVG for the comparison, so no Chrome and no browser popup.
- **QA as a gate, not a vibe**: normalised MAE plus structural-difference share, exit code 1 on
  failure, so it can run in a build or a batch.
- **No fake vectorisation**: a raster figure is reported as raster and refused; tracing it and
  calling the result vector is the failure mode this skill exists to prevent.
- **No PPTX output**: python-pptx cannot embed SVG, and no converter is assumed. The documented
  editable path is PowerPoint's Insert → SVG → Convert to Shape.
- **No code copied**: the script is our own; the upstream project is credited as prior art and
  remains the choice for editable-text PPTX with font subsetting.

### Unchanged

The style system, examples, captions, accessibility, and production guidance from v1.0.

---

## v1.0 — initial release

Built from the figure practices of strong top-4 security/systems papers (S&P, USENIX Security,
CCS, NDSS), plus the general figure-guidance literature (Rougier et al. 2014 on figure design;
Crameri et al. 2020 on colour misuse; Okabe–Ito colour-universal design).

### Contents

- `SKILL.md` — the workflow: claim first → encoding → shared style → direct labels →
  print-safety → export → verify.
- `references/venue-figure-profiles.md` — column widths and caption rules per venue, what
  strong papers share, the rules that change between conference / magazine / journal.
- `references/encoding-guide.md` — claim-to-chart mapping, chart-by-chart rules, uncertainty,
  when a table wins, axis-integrity checklist.
- `references/style-spec.md` — every setting: sizes, Okabe–Ito hex codes, line weights, markers,
  grid, LaTeX inclusion.
- `references/captions.md` — the caption formula with bad/good pairs, panel captions, length by
  venue.
- `references/accessibility.md` — colour-blind and grayscale safety, second channel, alt text.
- `references/production.md` — vector export, embedded fonts, camera-ready checklist, common
  build failures.
- `references/anti-patterns.md` — 15 failure modes with the fix.
- `scripts/figure_style.py` — rcParams, palette, `new_fig`, `save`, `panel_label`,
  `annotate_end`.
- `scripts/make_examples.py` — generates every example (synthetic data, fixed seed).
- `scripts/check_figure.py` — size/dpi check, grayscale + deuteranopia previews, palette
  report, warnings when colours collapse.
- `examples/` — nine reference images + README explaining the rule each one demonstrates.
- `templates/figure-brief.md` — the one-page brief to fill before drawing.

### Design decisions

- **Examples are synthetic.** No figure is copied from a published paper; the repo stores what
  the style looks like, not other people's artwork.
- **Style is code.** The palette and rcParams live in `figure_style.py`, so a paper's figures
  cannot drift apart.
- **Print-safety is checked, not assumed.** `check_figure.py --preview` produces the grayscale
  and deuteranopia images a reviewer would see; the human step is looking at them.
