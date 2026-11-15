---
name: paper-writing
description: Plan and draft a research paper from the research question outward, for security/CS venues (S&P, USENIX Security, CCS, NDSS, journals, IEEE S&P Magazine). Use when starting a paper, choosing its structure, deciding what each section must claim, allocating figures and tables between body and appendix, or writing the abstract last. Use for 论文写作/搭框架/定RQ/章节规划/摘要怎么写. Not for sentence-level revision (paper-prose-polish) or figure design (paper-figures).
version: 1.0
---

# Paper writing

A paper is an argument with evidence, not a record of what was done. The reader did not run the
experiments, does not know why they were run, and will decide whether to believe the result in the
first two pages. This skill builds the paper in that order: question → argument → evidence →
sections → sentences (the last handled by `paper-prose-polish`).

## The one rule

**Nothing goes into the paper that does not answer the research question.** Every section, table,
figure, and paragraph has a job: to move the reader one step closer to believing the answer. If
something cannot state its job in one sentence, it is either not needed or not yet understood.

## When this applies

- Starting a paper, or restarting one that has lost its shape.
- Choosing between "one shared method, several RQs" and "one chapter per RQ".
- Deciding what belongs in the body and what belongs in the appendix.
- Writing the abstract, which comes last and is judged first.
- A draft that has all the material but reads as a lab notebook.

Not for: revising sentences (`paper-prose-polish`), designing figures (`paper-figures`).

## Step 0 — The research question

Write the question as one sentence a reader could disagree with:

> We ask whether public advisories describe the vulnerability that actually exists.

Test it:

| Test | Failing form | Working form |
|---|---|---|
| Could a knowledgeable reader answer it differently? | "We study PHP security." | "Do advisories understate exploitable paths?" |
| Does it name an object and a judgement? | "Python is popular." | "Can a single affected-version range describe a five-chain family?" |
| Is the answer not already known? | "Patches sometimes miss variants." | "How often, and in which claim?" |
| Is it answerable with the evidence you can get? | "Is disclosure broken?" | "What fraction of coded claims conflict with dynamic tests?" |

One paper answers one question. Two questions are two papers, or one question with two parts that
share a method.

## Step 1 — Venue and skeleton

Read `references/section-blueprints.md` for what each section must do, and
`paper-prose-polish/references/venue-profiles.md` for per-venue hard constraints (template, page
budget, anonymity, ethics section, CVE identifiers).

Choose one of two skeletons and record why:

| Skeleton | Shape | Use when |
|---|---|---|
| **Method-first** | Intro → background → method → one evaluation → discussion | one method produces several results; RQs share instrumentation |
| **RQ-chapters** | Intro → background → (RQ1 method + result) → (RQ2 method + result) → discussion | the RQs need different methods or different datasets |

Measured layout in 120 top-tier papers: related work before the design section in 75% (after the
evaluation in 15%); a dedicated limitations section in 13%; a threat-model section in 17.5%. These
are conventions, not rules — but a deviation should be a decision, not an accident.

## Step 2 — The story spine

Every paper answers five questions in order. Write one sentence for each before drafting anything
(`references/story-spine.md` explains why each link fails):

1. **Where does the problem come from?** Not "X is important", but the specific judgement the
   field cannot make today.
2. **Why is it worth answering?** What decision changes if the answer is one way rather than the
   other.
3. **How is it answered?** The method, stated as the reason for each choice, not a list of steps.
4. **How far does the evidence go?** Which conditions were tested, which were not.
5. **What do we know now that we did not?** The change in knowledge, with its boundary.

The five sentences are the paper's spine. If any one is missing, the corresponding section will
read as filler no matter how well it is written.

## Step 3 — Section plan

For each section, write three lines before drafting it:

```
§N claim:    <the one judgement this section establishes>
   evidence: <the table, figure, or argument that supports it>
   reader:   <what the reader must already know to follow it>
```

A section whose claim cannot be written is a section that has not been thought through. A section
whose claim is not needed by the next section is a section to cut.

## Step 4 — Terminology and display items

**Terminology lock.** One canonical form per concept, with its definition and the variants that are
banned. Coined terms are the first thing to drift; a glossary table in the plan pays for itself by
the third section (`templates/paper-plan.md` section 5).

**Display items.** Plan every figure and table before drafting, and assign each one to the body or
the appendix (`references/appendix-and-display-items.md`). Decide the style now, not during
polishing: a figure's message, its axes, and its caption belong to the argument.

## Step 5 — Write in the order that survives revision

1. **Introduction and background first.** They fix the vocabulary and the claim; if the middle
   changes later, these two sections absorb the change.
2. **Middle sections next, iteratively.** Each one is written against a result that exists. When a
   result is missing, run the experiment — do not write around the hole; a paragraph that describes
   an experiment that was never run is the most expensive kind of debt.
3. **Abstract last.** It is the only part every reviewer reads, and it can only be written once the
   claims are final (`references/abstract.md`).
4. **Title last of all**, constrained by the venue's title conventions.

Draft order is not reading order. The reader meets: title → abstract → introduction → figures.

## Step 6 — Compliance pass

Before submission, verify against the venue's own text: template and page limit, anonymity rules
(including identifiers in the text), ethics section, artifact availability, figure legibility in
grayscale, and reference style. Compliance failures are desk-reject risks, not style notes.

## What to hand the agent

Fill `templates/paper-plan.md`. It asks for the RQ, the skeleton choice, the per-section claim, the
terminology, the display-item allocation, and the open questions. Anything you cannot answer, write
`?` — the `?` marks are the agenda for the next discussion, and they are more useful than a
plausible guess.

## Non-negotiables

1. **No drafting before Step 2.** A section written before the spine exists will be rewritten.
2. **Every section states a claim.** "This section describes the dataset" is not a claim.
3. **Never claim more than the evidence covers.** The boundary belongs in the same paragraph as
   the claim, not only in the limitations section.
4. **Do not write an experiment that was not run.** Mark the gap and run it.
5. **Figures and tables are planned, not added later.** An unplanned display item usually means the
   claim was not planned either.
6. **The abstract reports results, not the table of contents.** See `references/abstract.md`.
7. **When the story does not close, the research is incomplete, not the writing.** A gap in the
   spine is a finding about the work.

## Resource map

| File | Use |
|---|---|
| `references/story-spine.md` | The five links, why each fails, and the repair |
| `references/section-blueprints.md` | Per-section job, measured conventions, common failures |
| `references/abstract.md` | Four elements, three properties, four failure modes, field differences |
| `references/appendix-and-display-items.md` | Body vs appendix decision rules, with measured split |
| `templates/paper-plan.md` | The author questionnaire to fill before drafting |
| `scripts/story_study.py` | Reproduces the abstract and appendix measurements |
