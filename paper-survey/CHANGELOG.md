# Changelog

## v1.0 — pre-paper research survey (9 sections, graded evidence)

The skill covers the stage before `paper-writing`: deciding whether a direction is worth a paper,
what exactly is missing, and whether it can be done. It is calibrated against a report the author
judged good, and its checker passes that report with zero failures and zero warnings.

### Added

- **`SKILL.md`** — the nine-section frame, the decision the report must support (continue / narrow
  / stop), recommended writing order (§1 → §3 → §4 → §6 → §5 → §8 → §7 → §9 → §2 → pass), and
  ten non-negotiables (traceability, grading, bounded negatives, no fake gaps, separated metrics).
- **`references/section-constraints.md`** — per-section job, required artifacts, forbidden
  content, length range, checklist. Length ranges are calibrated on a 9,157-unit report judged
  good (e.g. §6 gaps 1,717 units, §4 related work 1,153).
- **`references/evidence-and-claims.md`** — the E1–E4 ladder (confirmed / reproduced / candidate /
  inferred), promotion rules, scope formulas for negative and "first" claims, source record
  format, ten accuracy traps.
- **`references/related-work-and-gaps.md`** — reproducible search protocol (databases, venues,
  window, queries, inclusion, snowballing, stop rule), the three-distance comparison table
  (object / method / evidence), the three-part gap (已有问题 / 研究空白 / 拟解决问题), gap failure
  modes, and the work→gap→module→metric mapping.
- **`references/plan-and-feasibility.md`** — capability list, feasibility/risk tables, risk
  register with trigger/response/stop condition, module spec, P0–Pn route with exit conditions,
  three separated metric groups, and go/narrow/stop criteria.
- **`templates/survey-plan.md`** — pre-search questionnaire (decision, assets, protocol, evidence
  list, nearest work, risks).
- **`templates/report-skeleton.md`** — the nine headings with prompts and required tables.
- **`scripts/check_survey.py`** — mechanical checks: sections present/ordered, per-section length,
  related-work table size/links/distance column, three-part gaps (≥3), feasibility table and risk
  responses, next steps, RQ count, date, search protocol, evidence grades, and unscoped overclaim
  wording ("首次/填补空白/尚无…"). `--json` and `--strict`; exit 1 on FAIL.

### Calibration

Run on the reference report (9 sections, 9,157 units, 9 sources, 9-row comparison table, 5 gaps,
4 risks): **PASS, 0 fail / 0 warn**. Run on a deliberately thin report of the same headings:
**5 fail / 18 warn** — missing tables, no three-part gaps, no next steps, unscoped "首次/填补空白".

The reference report itself is not shipped (it is the author's research material); the ranges and
checks are what carry its standard.

### Not covered

- Turning the report into a paper (that is `paper-writing`).
- Language-level revision (`paper-prose-polish`).
- Figures (`paper-figures`).
- Deciding whether the *search* was adequate — the checker verifies that a protocol is recorded,
  not that it was good.
