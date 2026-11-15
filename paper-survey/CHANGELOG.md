# Changelog

## v1.1 — remove the quotas; keep the clarity

v1.0 turned a good report into a compliance form: length ranges per section, and a list of
"required artifacts" that a section had to produce. That is the wrong direction. The report's job
is to let a reader understand what was surveyed and why the conclusion follows; word counts and
mandatory tables are proxies that can be satisfied while the argument stays unclear.

### Changed

- **No word limits.** All per-section length ranges are gone. A section is as long as its question
  needs; the checker reports size only as orientation, with no pass/fail.
- **No mandatory artifacts.** Tables, risk matrices, routes, and numbered lists are recommended as
  tools when they clarify a comparison, and explicitly optional. A three-paragraph section with no
  table can be complete.
- **Section guide rewritten** (`references/section-constraints.md`): each section now lists the
  questions the reader must be able to answer, what a convincing answer looks like, the failure
  mode, and self-check questions — no "must contain" lists, no ranges.
- **Checker rewritten** (`scripts/check_survey.py`): it now produces a structure map (sections,
  units, tables, links) and flags (a) accuracy problems — unscoped "首次/填补空白/尚无" are still
  failures — and (b) readability risks as warnings: a heading-only section, gaps missing a beat, a
  recommendation without a next step. Missing tables are warnings, not failures.
- **Templates labelled optional**, and the report skeleton says to delete anything that does not
  help the reader.

### Added

- **"What readable means here"** in `SKILL.md`: first 100 words state the object/decision/headline;
  each section opens with its judgment; the chain background → scope → known → missing → plan →
  feasibility → decision is traceable; one term per concept; comparisons name a dimension; no
  padding. Plus the reader test: ask someone uninvolved to restate question, closest work, gap,
  recommendation.

### Unchanged

The accuracy rules (E1–E4 grades, bounded negatives, denominators, "a known problem is not a
gap") and the decision requirement in §9. Those are about claims, not form.

### Calibration

- Reference report (the author's 9-section survey): PASS, 0 fail / 0 warn.
- A thin report with the same headings but no content: FAIL on unscoped overclaims, warnings for
  near-empty sections, missing comparison, missing next step.
- A prose-only report (no tables, one page) passes with warnings at most — by design.

---

## v1.0 — pre-paper research survey (9 sections, graded evidence)

The skill covers the stage before `paper-writing`: deciding whether a direction is worth a paper,
what exactly is missing, and whether it can be done.

### Added

- Nine-section frame, recommended writing order, ten non-negotiables (traceability, grading,
  bounded negatives, no fake gaps, separated metrics).
- `references/evidence-and-claims.md`: E1–E4 ladder, promotion rules, scope formulas, source
  record format, ten accuracy traps.
- `references/related-work-and-gaps.md`: search protocol, three-distance comparison, three-part
  gaps, gap failure modes.
- `references/plan-and-feasibility.md`: risk register, staged route, separated metric groups,
  go/narrow/stop criteria.
- Templates: pre-search plan, report skeleton.
- `scripts/check_survey.py`.
