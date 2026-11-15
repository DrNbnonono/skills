# Section blueprints

What each section must accomplish, the measured convention where one exists (120 top-tier papers,
see `paper-prose-polish/references/structure-and-placement.md`), and the failure mode that shows up
most often.

Read a blueprint as a **job description**, not a template. The numbers are conventions; deviating is
allowed when the paper has a reason.

---

## Title

The finding, not the topic. A reader scanning a proceedings index should know what was established.

- Working shape: `<result>: <object and setting>` or `<question the paper answers>`.
- Avoid promising a mechanism the paper only correlates.
- Venue conventions differ: conferences accept long subtitles, magazines want 8–12 words
  (`paper-prose-polish/references/venue-profiles.md`).

**Failure:** a title that describes the field ("Towards Secure X") and could sit on any paper in it.

---

## Abstract

Four elements, last written. Full treatment in `abstract.md`.

---

## Introduction

**Job:** derive the question, show why it matters, state the answer and the evidence, list what the
paper contributes.

Five moves, in order:

1. **Stakes in one or two sentences** — the decision that defenders/users make with the artifact you
   study.
2. **The gap in existing understanding** — organised by claim, ending in "we still cannot decide Z".
3. **Why now** — the change that makes the question pressing (a trend, an incident, a new tool).
   Keep it factual; do not claim causation you do not test.
4. **What this paper does** — one paragraph: the question, the method, the answer, the boundary.
5. **Contributions** — a short list, each with its evidence. Three is usually right; ten is a sign
   the paper has no single question.

Measured on 120 papers:

| Property | Value |
|---|---|
| Introduction length | median **10 paragraphs / 1,032 words** (p90: 15 / 1,531) |
| Opens with boilerplate ("In recent years…", "With the rapid development…") | **1.7%** only |
| States a research question explicitly ("we ask / we study / our question") | 36.7% |
| Announces contributions in prose ("we make the following contributions") | 20.8% (bullet lists are invisible to this count, so the true rate is higher) |
| Ends with a roadmap ("the rest of this paper…") | **17.5%** |

Two readings. First, the boilerplate opening is nearly absent in accepted papers — 1.7%, not 30% —
which is the strongest evidence in this skill against opening with "in recent years". Second, a
roadmap is a minority convention and is the first paragraph to cut under a page limit.

**Failure:** a literature review in the introduction that duplicates §2. Numbers and case details
belong in one of the two, never both.

---

## Background / Related work

**Job:** give the reader the minimum technical context, then position the paper against the closest
work by **claim**, not by citation order.

- Group sources that support the same judgement; group sources that disagree and explain why
  (conditions, method, data).
- Close each group with what it cannot do — that is where your paper enters.
- Measured placement: **75%** put this before the design section; **15%** put it after the
  evaluation, when the comparison *is* the contribution.

**Failure:** a list of one-line summaries ("X did A [1]. Y did B [2].") that never says what the
field now believes.

---

## Threat model / assumptions

**Job:** state what the attacker can do, what the system assumes, and what is out of scope — before
any claim depends on it.

Measured: only **17.5%** have a dedicated section (median position: second section). Most papers
state assumptions inline where they are used. A dedicated section is warranted when several
sections share the same assumptions.

**Failure:** assumptions scattered such that a reviewer cannot tell whether the evaluation violates
one.

---

## Method / design

**Job:** make the question answerable, and justify each non-obvious choice.

For each component, the reader needs: what it is, why this way rather than the obvious alternative,
and what it costs. A design decision without an alternative considered reads as an accident.

**Failure:** a walkthrough of the implementation in the order it was built. Reorder by dependency:
what the reader must understand first.

---

## Evaluation

**Job:** support each claim with a measurement, and state the inference.

Rules:

1. **Claim → evidence → number.** Each subsection ends by saying what the numbers mean, not by
   leaving the reader to infer.
2. **Every claim in the introduction is tested somewhere.** A contribution with no corresponding
   measurement is a claim to delete.
3. **State the comparison baseline and why it is fair.**
4. **Report failures.** A table with no failing rows invites the question of whether the test can
   fail.
5. **Put the boundary in the same subsection** as the claim it limits.

Measured: **78.3%** of papers have a dedicated evaluation section (median 1, max 2), and it runs
**24 paragraphs** at the median (p90 41) — roughly two to three times the introduction. Paragraphs
run 75 words / 3 sentences (p90: 97 / 4), so the evaluation is a long section built from short
paragraphs, not a few long ones. A results subsection longer than a page without a display item is
usually prose doing a table's job. See `results-arrangement.md` for the order and the per-subsection
structure.

**Failure:** numbers reported, conclusion left implicit; or a conclusion asserted more strongly than
the numbers allow.

---

## Discussion

**Job:** place the answer back into the literature and state which judgement changes.

Structure: what was believed → what is now known → which decision changes → under which conditions
it holds.

**Failure:** repeating the results; or broad implications with no link to the measured conditions.

---

## Limitations

**Job:** state what the evidence cannot support, before a reviewer does it for you.

Measured: a standalone limitations section appears in **13%** of papers; most fold limitations into
the discussion, the evaluation, or the introduction's closing paragraph. A magazine expects a
"What we do not know" block.

**Failure:** limitations that are actually brags ("we only tested on 29 configurations"), or
limitations that contradict a claim made earlier without acknowledging it.

---

## Conclusion

**Job:** answer the question in one paragraph, restate the change in knowledge, and stop.

- No new claims, no new citations, no new numbers.
- Return to the question from the introduction, in the same words if possible.

**Failure:** a summary of sections ("Section 3 presented…") — that is a table of contents, not a
conclusion.

---

## Appendix

See `appendix-and-display-items.md`. In one line: the appendix holds what a specialist would check,
never the only evidence for a claim the paper makes.
