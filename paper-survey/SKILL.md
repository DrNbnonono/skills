---
name: paper-survey
description: Run a pre-paper research survey (方向调研与可行性论证) for security/CS venues (S&P, USENIX Security, CCS, NDSS, journals, IEEE S&P Magazine). Use for 调研报告/前期调研/方向调研/选题论证/可行性分析/相关工作梳理/开题报告. Organises the survey into ten sections whose only job is to make the reader understand what was investigated and why the conclusion follows. No word limits, no mandatory tables: structure serves comprehension. Accuracy rules are strict (evidence grades, bounded negatives); form is not.
version: 1.2
---

# Paper survey (前期调研)

A survey report has one acceptance test:

> **Someone who did not do the survey can read it once and say: what was investigated, what is
> known, what is missing, whether it is worth doing, and what happens next.**

Everything in this skill serves that test. A report that satisfies every checklist but leaves the
reader unable to restate the argument has failed; a report with three sections and no tables that
makes the situation clear has passed.

## No quotas

- **Word count is not a limit.** A section is as long as it needs to be to answer its question.
  Do not pad to look thorough, do not compress to look efficient.
- **Tables, lists, and numbered artifacts are not mandatory.** They are tools: use one when it
  makes a comparison or a set of risks easier to see than prose. A clear paragraph beats a table
  that exists to satisfy a template.
- **The ten section names are a reading order, not a cage.** Keep the order (it is the argument's
  spine), but merge sub-points, rename sub-headings, and write prose where prose is clearer.
- **Do not manufacture content to fill a section.** If a section has little to say for this
  direction, say little and say why.

## Core principle

**The report's value is the decision it supports and the clarity with which it supports it.**

Three laws carry the accuracy; they are about claims, not about form:

- **Traceable.** Every factual claim has a source (link + venue/year), or is marked `[unverified]`.
- **Graded.** Evidence has four levels (E1 confirmed → E4 inferred); a candidate is never promoted
  to a confirmed result because the reasoning feels right.
- **Bounded.** "We did not find X in this search window on these venues" is a finding; "X does not
  exist" is an assertion you cannot support.

## The ten sections: what each must make clear

§1–§9 are the argument; §10 is the evidence index. A reader should be able to stop at §9 and
still find every source in §10.

| § | Section | The reader must be able to answer afterwards | Typical failure |
|---|---|---|---|
| 1 | 基本信息 | What is studied, by whom, over what period, at what stage, with what expected output | A background essay instead of a scope |
| 2 | 目的与背景 | Why this question exists, and what it must answer | No turn from "the field" to "the gap"; RQs that are topics |
| 3 | 范围与方法 | What is in, what is out, **how to search**, and how a claim will be judged | Scope only lists inclusions; method names without procedure |
| 4 | 相关工作 | Who is closest, what they settled, **their limitation**, and what can be borrowed | Strawmen; a row with no limitation and no takeaway |
| 5 | 现状总结 | What is settled and what is not, as judgments | Paper-by-paper summaries again |
| 6 | 空白与问题 | What existing work solved, where it falls short, what nobody has studied — and which gaps are real | "No one has studied X"; gaps too large to test |
| 7 | 可行性 | Data, difficulty, resources, time, risk — and what could stop us | Optimism without risk; risks without response |
| 8 | 初步思路 | How it would be done, in **more than one candidate**, and how success would be measured | Wish list; one approach presented as inevitable |
| 9 | 结论与建议 | Whether to continue, and the next step (立项 / 放弃 / 继续调研 / 与导师讨论) | Ending on "promising" |
| 10 | 参考文献与资料 | Every source used, including non-paper channels | Links without type or venue/year |

Per-section guidance — the questions to answer, what a convincing answer looks like, and the
questions to self-check — is in `references/section-constraints.md`. It is guidance, not a
completion form.

### Section 1 carries the survey's metadata

Add the four fields at the top; they answer "who is asking, over what window, on top of which
project document":

| 调研主题/方向 Topic/Direction | 调研人 Researcher | 起止时间 Duration | 项目内容文档 Project Doc |
|---|---|---|---|
| topic, may be broader than the project title | name | YYYY.MM – YYYY.MM | link to the project documentation |

### Four search methods worth naming in §3

1. **顺藤摸瓜 (citation chasing).** Start from the most recent 1–2 years of top-venue papers;
   their reference lists already cover most important prior work — trace backward.
2. **找综述 (Survey / SoK).** A survey or systematization gives the taxonomy and development
   line faster than scattered reading; use it for the map, then verify primary sources.
3. **横向对比 (side-by-side comparison).** Line up method, assumptions, data, and metrics
   (that is the §4 table); what is not solved becomes §6.
4. **多渠道 (multi-channel).** News, technical blogs, HN/Reddit/Zhihu, vendor advisories, and
   WeChat posts reveal recency and real-world impact that papers do not; they belong in §10
   with their type labelled.

### §10 is an evidence index, not only a bibliography

It is not limited to academic papers: news, blogs, forum threads, vendor advisories, and
WeChat posts all belong here. A table with type / title or outlet / link / note is the easiest
form; a plain list is acceptable if each entry still says what kind of source it is.

## What "readable" means here

The deliverable is judged by a reader, so build for the reader:

1. **The first 100 words say what this is.** Direction, decision, and the headline conclusion —
   before any background.
2. **Each section opens with its judgment, not with context.** The first sentence of §6 is the
   gap, not the history of the field.
3. **The argument is visible as a chain.** A reader can trace: background → scope → what is known
   → what is missing → what we would do → whether it is feasible → decision. Every section
   should connect to the previous one with a sentence the reader can point at.
4. **One term per concept, used everywhere.** If the report calls it "认证声明" in §2, it does not
   call it "认证结果字段" in §6 without saying they are the same.
5. **Comparisons are explicit.** "Where we differ" is a sentence with a subject and a dimension,
   not "is different".
6. **The reader's questions are anticipated.** If a claim will raise "but what about X?", answer
   it in the next sentence or in a short limitations note.
7. **No padding and no throat-clearing.** "随着……的发展" and "众所周知" are removable; they do not
   advance the decision.

A practical reader test before delivery: hand the report to someone who was not involved and ask
them to restate (a) the question, (b) the closest work, (c) the gap, (d) the recommendation. If
any of the four is wrong, the report is unclear, regardless of what it contains.

## Evidence grades (accuracy, unchanged)

| Grade | Meaning | Example |
|---|---|---|
| **E1 confirmed** | Official advisory / CVE / GHSA, merged fix, or a peer-reviewed result we reproduced | "GHSA-xxxx, 2026-11-11, CWE-346" |
| **E2 reproduced** | We ran it in a recorded environment | "3/3 configurations, `runs/…`" |
| **E3 candidate** | Consistent behavior, not yet confirmed upstream | "候选 MSL-099，待维护者回复" |
| **E4 inferred** | Analogy, source reasoning, or hypothesis | "如果实现遵循同一模式，则可能…" |

Never promote a grade silently. Wording rules, source format, and the ten accuracy traps are in
`references/evidence-and-claims.md`.

## Non-negotiables (all about claims, none about form)

1. **No source, no fact.** Unsourced statements are phrased as hypotheses or cut.
2. **Never write "first", "no one has", "fills a gap" without a stated search scope.**
3. **A known problem is not a gap.** §4 says what the closest work settled; §6 may claim only
   what that work cannot do, and must say why.
4. **Candidates stay candidates** until a maintainer, an advisory, or a reproducible experiment
   promotes them.
5. **Every number carries its denominator, window, and unit.**
6. **The date and the search protocol are part of the report.**
7. **Separate the three kinds of number** (discovery capability, real-world impact, defence) when
   the report reports results.
8. **The decision is a deliverable:** continue / narrow / stop, and what would change it.
9. **Ethics and access are part of feasibility.**
10. **Negative and inconclusive results stay visible.**
11. **Every source in the text appears in §10**, with its type (paper / survey / news / blog /
    forum / vendor advisory / WeChat post). A source that is only in the body is a dead link
    nobody can check.

## Workflow

- **Step 0 — Frame the decision.** What decision will this report support? What would make you
  narrow or stop? Write it down first (a paragraph is enough; `templates/survey-plan.md` is an
  optional prompt sheet, not a form to fill).
- **Step 1 — Fix the scope and the protocol.** In/out, venues, years, queries, and how a claim is
  graded. This is what makes later negative statements checkable.
- **Step 2 — Collect and grade.** One note per relevant work: link, venue/year, what it did, what
  it did not settle, and how confident we are.
- **Step 3 — Write the chain, not the inventory.** §2 background ends at the gap; §4 provides the
  evidence; §6 turns it into research problems; §8 answers them; §7 tests whether we can.
  Write §2 last, when the gap is finally clear.
- **Step 4 — Read for the reader.** Run the seven readability points above and the section
  self-check questions. Fix what a reader would stumble on, not what a template would flag.
- **Step 5 — Decide.** §9 states the decision, the next step, and the stop condition.
- **Step 6 — Optional mechanical check.** `scripts/check_survey.py` maps the report's structure
  and flags accuracy problems (unscoped overclaims) and a few clarity risks. It does not gate on
  length or on artifacts; treat its output as a second pair of eyes, not a grade.

## Deliverables

- The report, with date, researcher/window metadata, and search protocol.
- §10: every source used, typed (paper / survey / news / blog / forum / vendor advisory / WeChat).
- Whatever exhibits help the reader follow it (a comparison table, a risk table, a route table) —
  chosen, not mandatory.
- The decision and next steps.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Reading log instead of decision support | The reader cannot tell what to do after reading |
| Filling a template | Tables that exist to satisfy a checklist hide the argument |
| Padding for length / compressing for tidiness | Both trade clarity for appearance |
| "No one has studied X" | Unfalsifiable without a window; usually wrong |
| Sacrificing the closest work | A strawman makes the gap look bigger and collapses under review |
| Candidate promoted to confirmed | One wrong grade invalidates the report's credibility |
| Gaps too large to test | "Secure all email" is not a research problem |
| Plan with no milestone or stop condition | Optimism is not feasibility |
| One metric for three claims | Discovery, impact, and defence numbers measure different things |
| Background written first | It narrates what you expected to find, not what you found |
| Ending on "promising" | The deliverable is a decision, not a mood |

## Resource map

| File | Use |
|---|---|
| `references/section-constraints.md` | Per-section questions to answer, what a convincing answer looks like, self-check questions |
| `references/evidence-and-claims.md` | The E1–E4 ladder, wording rules, source format, accuracy traps |
| `references/related-work-and-gaps.md` | Search protocol, how to state the distance, the three-part gap, gap failure modes |
| `references/plan-and-feasibility.md` | Risk register, route with exit conditions, separated metric groups, go/narrow/stop |
| `templates/survey-plan.md` | Optional prompt sheet before searching |
| `templates/report-skeleton.md` | Optional skeleton: section prompts, not a form |
| `scripts/check_survey.py` | Structure map + accuracy/clarity warnings; no length gates |
