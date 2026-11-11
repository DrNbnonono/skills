# Changelog

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
