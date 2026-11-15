---
name: paper-survey
description: Plan and run a pre-paper research survey (方向调研与可行性论证) for security/CS venues (S&P, USENIX Security, CCS, NDSS, journals, IEEE S&P Magazine). Use for 调研报告/前期调研/方向调研/选题论证/可行性分析/相关工作梳理/开题报告. Produces a nine-section report whose sections are constrained by content, evidence grade, and length, and whose last section is a go/no-go recommendation. Every claim carries a source or an explicit "unverified" mark; "not found in this search" is never written as "does not exist". Not for sentence polishing (paper-prose-polish), figure design (paper-figures), or paper structure (paper-writing).
version: 1.0
---

# Paper survey (前期调研)

A survey report is not a literature list and not a draft of the paper's related-work
section. It answers three decisions:

1. **Is this direction worth a paper?** (or: which sub-question of it is?)
2. **What exactly is missing, stated so that it can be checked?**
3. **Can we do it with the evidence, access, and time we have?**

If the report does not help someone make those three decisions, it is a reading log.

## Core principle

**The report's value is the decision it supports, not the number of papers it cites.**

Three laws follow:

- **Traceable.** Every factual claim has a source (link + venue/year), or is marked
  `[unverified]`. A claim you cannot source is a hypothesis, and must be written as one.
- **Graded.** Evidence has four levels (E1 confirmed → E4 inferred). A candidate is never
  promoted to a confirmed vulnerability because the plot looks right; a single anomaly is never
  a bug; "no paper found" is never "no paper exists".
- **Bounded.** Every negative or "first" claim names its search window, databases, and query
  scope. "In the papers we searched (S&P/USENIX/CCS/NDSS, 2018–2025), we did not find X" is a
  finding; "X has never been studied" is an unverified assertion.

## When this applies

- Before starting a paper: choosing the direction, the RQ, and the contribution.
- Before a thesis proposal / 开题: the same nine sections are required.
- When a draft is stuck: the report shows whether the gap is real or the paper is thin.
- When joining a project: the fastest honest way to learn what the group already established.

Not for: producing a camera-ready survey paper (that is a paper, with its own reviewing
standard); sentence-level revision (`paper-prose-polish`); figure design (`paper-figures`);
section planning once the direction is settled (`paper-writing`).

## The nine sections (fixed order)

| § | Section | Its one job | Required artifact | Most common failure |
|---|---|---|---|---|
| 1 | 基本信息 Basic Information | Fix the direction, the subject, the goal, the expected outputs, and the stage | 5 labeled fields + expected-output list | Writing a background essay instead of a scope statement |
| 2 | 目的与背景 Purpose & Background | Explain why this question exists and what it must answer | Background narrative + RQ1–RQn, each with a scope sentence | RQs that are topics, not questions |
| 3 | 范围与方法 Scope & Method | Say what is in, what is out, how evidence is gathered, and how a claim is judged | Inclusion/exclusion table + method list + evidence-grading rule | No exclusion list, so the boundary is invisible |
| 4 | 相关工作 Related Work Survey | Place the closest work, one row each, with what it did and why this differs | Comparison table: work / what it did / distance to us | Strawmen; no "distance" column; links without venue/year |
| 5 | 现状总结 State-of-the-Art Summary | State what is settled, in judgments rather than summaries | 3–5 judgments, each with evidence and a boundary note | Listing papers again |
| 6 | 空白与问题 Gaps & Open Problems | Turn the gap into a checkable research problem | Each Gap: 已有问题 / 研究空白 / 拟解决问题 | "No one has studied X" with no evidence; gaps too large to test |
| 7 | 可行性 Feasibility | Separate "can we" from "is it risky" | Capability list + feasibility/risk table + risk responses | Optimism with no risk, or risks with no response |
| 8 | 初步思路 Candidate Approaches | Say how it would be done, and how success would be measured | Core idea sentence + modules + P0–Pn route + separate metric groups | A wish list with no milestones, or one mixed metric |
| 9 | 结论与建议 Conclusion & Recommendation | Give the decision and the next step, with a stop condition | Conclusion + short/mid/long plan + final positioning + core question | Ending on "promising" with no next action |

Full per-section constraints (must contain, must not contain, length range, checklist):
`references/section-constraints.md`.

## Recommended writing order

The report reads 1→9, but writing it in that order wastes work. Write in this order:

1. **§1** (direction, goal, expected outputs) — the anchor.
2. **§3** (scope, method, evidence rule) — it determines what you are allowed to claim.
3. **§4** (related work table) — the evidence base.
4. **§6** (gaps) — the judgment the table supports.
5. **§5** (state of the art) — the summary of §4 + §6.
6. **§8** (approaches) — what follows from §6.
7. **§7** (feasibility) — the honest test of §8.
8. **§9** (recommendation) — the decision.
9. **§2** (purpose & background) — written last, because the background narrative that makes
   §6 inevitable is only visible after §4–§6 exist.
10. **Full pass** — numbers, terms, and cross-references checked together.

## Evidence grades

Use these four labels in the report wherever a claim's status matters (details and wording
rules: `references/evidence-and-claims.md`).

| Grade | Meaning | Example |
|---|---|---|
| **E1 confirmed** | Official advisory / CVE / GHSA, merged fix, or a peer-reviewed result we reproduced | "GHSA-xxxx, published 2026-11-11, CWE-346" |
| **E2 reproduced** | We ran it in a recorded environment | "our lab run, 3/3 configurations, logs in `runs/…`" |
| **E3 candidate** | Consistent behavior, not yet confirmed upstream | "candidate MSL-099, awaiting maintainer reply" |
| **E4 inferred** | Analogy, model reasoning, or a hypothesis | "if the parser follows the same pattern, it would…" |

Never promote a grade silently. A sentence that changes grade is a claim change (Tier 3).

## Non-negotiables

1. **No source, no fact.** Unsourced statements are written as hypotheses or cut.
2. **Never say "first", "no one has", "fills a gap" without a stated search scope** and a
   checked search. Say "we did not find, in this window, on these venues".
3. **A known problem is not a gap.** §4 must state what the closest work already does; §6 may
   only claim what that work cannot do, and must say why.
4. **Candidates stay candidates.** A candidate vulnerability/result is labeled E3 until a
   maintainer, an advisory, or a reproducible experiment promotes it.
5. **Every number carries its denominator.** Percentages need n; medians need the sample;
   counts need the window.
6. **Date and search protocol are part of the report**, not metadata: the date, the databases,
   the venues, the years, and the query terms.
7. **Separate the three kinds of number** in §8: discovery capability, real-world impact, and
   defence effectiveness. Mixing them is the most common way to inflate a result.
8. **The decision is a deliverable.** §9 says continue / narrow / stop, and states what evidence
   would change the decision.
9. **Ethics and access are part of feasibility.** No unauthorized testing, no scraping private
   data, no over-claiming access you do not have.
10. **A negative result stays visible.** "Not found", "not reproducible", "inconclusive" are
    kept in the report, because they are why the plan is shaped the way it is.

## Workflow

```bash
python scripts/check_survey.py report.md          # structure + evidence + overclaim checks
python scripts/check_survey.py report.md --json    # machine-readable summary
```

- **Step 0 — Frame the decision.** Write the go/no-go question and the candidate sub-questions.
  Fill `templates/survey-plan.md` before searching.
- **Step 1 — Fix the scope and the protocol.** Inclusion/exclusion, venues, years, query terms,
  evidence-grading rule. Without this, §4 has no denominator.
- **Step 2 — Collect and grade.** One row per relevant work: link, venue/year, what it did,
  what it did not do, grade of our belief about it.
- **Step 3 — Write §4 and §6 together.** The distance column in §4 is the raw material of each
  Gap; a Gap with no row in §4 is unsupported.
- **Step 4 — State the art (§5), then the plan (§8), then the honest test (§7).**
- **Step 5 — Decide (§9).** Continue / narrow / stop, short vs long plan, and the core question
  the future paper must answer.
- **Step 6 — Write §2 last**, so the background makes the gap inevitable.
- **Step 7 — Self-check** with `scripts/check_survey.py`, then read the whole report once as the
  person who has to approve the project.

## Deliverables

1. The nine-section report (markdown or LaTeX), with date and search protocol.
2. The related-work table with a distance column, every row sourced.
3. The gap list, each gap in the three-part form and checkable.
4. The feasibility/risk table with responses and a stop condition.
5. The recommendation with short/mid/long next steps.
6. A one-page appendix: search queries, inclusion/exclusion decisions, and the evidence that did
   not fit.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Reading log instead of decision support | The reader cannot tell what to do after reading |
| "No one has studied X" | Unfalsifiable without a search window; usually wrong |
| Sacrificing the closest work | A strawman makes the gap look bigger and collapses under review |
| Candidate promoted to confirmed | One wrong grade invalidates the whole report's credibility |
| Gaps that are too large to test | "Secure all email" is not a research problem |
| A plan with no milestones or stop condition | Optimism is not feasibility |
| One metric for three claims | Discovery, impact, and defence numbers measure different things |
| Background written first | It narrates what you expected to find, not what you found |
| No date / no queries | The report cannot be re-verified, so it ages badly |
| Ending with "promising" | The deliverable is a decision, not a mood |

## Resource map

| File | Use |
|---|---|
| `references/section-constraints.md` | The nine sections: must contain, must not contain, length, checklist |
| `references/evidence-and-claims.md` | The E1–E4 ladder, wording rules, source format, scope statements |
| `references/related-work-and-gaps.md` | Search protocol, comparison table, three-part gaps, gap failure modes |
| `references/plan-and-feasibility.md` | Feasibility/risk tables, P0–Pn route, separated metric groups, stop conditions |
| `templates/survey-plan.md` | Pre-search questionnaire: decision, scope, protocol, evidence list |
| `templates/report-skeleton.md` | Nine-section skeleton with prompts and required tables |
| `scripts/check_survey.py` | Structure/evidence/overclaim checker with PASS/WARN/FAIL and `--json` |
