# Changelog

## v1.2 — the ten-section template, integrated as guidance

The author supplied a ten-section template they find clear. This release folds its content into
the skill while keeping v1.1's rule that form is not a quota: the template supplies the sections'
metadata, the search methods, and the table columns; it does not add length limits or mandatory
exhibits.

### Added

- **§1 metadata**: 调研主题/方向, 调研人, 起止时间, and the link to the project content document.
  A survey without "who/when" cannot be assessed later.
- **§3 four search methods**: 顺藤摸瓜 (citation chasing), 找综述 (Survey/SoK), 横向对比
  (side-by-side comparison), 多渠道 (news/blogs/forums/vendor advisories/WeChat). These are the
  practical advice the template carries, and they are now part of the method section's guidance.
- **§4 five-column comparison**: 论文/工具 | 来源（venue/年份） | 核心思路 | 局限性/差距 | 可借鉴点.
  Limitation and takeaway are called out as the load-bearing columns — a row without them is a
  citation, not a survey.
- **§6 structure**: solve (已解决) / falls-short (不够好) / unstudied (尚未研究), building directly
  on the §4 comparison. These are potential entry points.
- **§7 five feasibility dimensions**: data availability, technical difficulty, resources/tools,
  time cost, and risk — each with assessment and risk/mitigation.
- **§8 candidate approaches**: more than one plausible route, compared; one approach presented as
  inevitable is now a named failure mode.
- **§9 four outcomes**: 立项 / 放弃 / 继续调研 / 与导师讨论 (or a close equivalent), instead of only
  continue/narrow/stop.
- **§10 参考文献与资料**: every source, typed (paper / survey / news / blog / forum / vendor
  advisory / WeChat), with link and note. Multi-channel evidence is explicitly welcome.

### Changed

- `SKILL.md` is now "ten sections": §1–§9 are the argument, §10 is the evidence index.
- `scripts/check_survey.py`: §10 is recommended (missing → warning, not failure); §1 metadata
  missing → warning; §9 decision recognises the four outcomes; §10 reports links and typed entries.
- Templates updated to the ten-section skeleton and metadata header.

### Unchanged

- **No word limits, no mandatory tables.** The new table columns are recommended forms; prose with
  the same facts is still acceptable.
- Accuracy rules (E1–E4, bounded negatives, denominators) and the decision requirement.

### Calibration

- Reference report (predates this template): PASS; warnings are exactly the two new fields it does
  not have — no §10 and no researcher/duration metadata.
- Prose-only report: PASS with warnings (no table, no links).

---

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
