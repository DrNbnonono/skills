# Introduction anatomy, annotated

v1.0 of this skill asserted a five-link spine. v1.1 measured it. This file reports the annotation,
including where the annotators disagreed and what that disagreement means.

---

## 1. Method

- **Sample**: the first 100 papers of the 120-paper corpus (top-tier security venues).
- **Unit**: the introduction, split into numbered paragraphs.
- **Task**: mark where each of five moves occurs; `null` when absent
  (`intro_annot/instructions.md` in the working repository).
- **Annotators**: five independent agents, 20 papers each, no overlap.
- **Validation**: every range checked against paragraph counts; one extract was a whole-paper dump
  (114 paragraphs) and was excluded, leaving **99 papers**.

Limitations, stated up front: single annotation per paper (no double-coding, so no kappa); paragraph
extraction dropped paragraphs under 25 words, which shifts boundaries; five papers had truncated
source text (annotators flagged them in `notes`).

---

## 2. The spine exists, and it has an order

Median normalised position of each move within the introduction (0 = first paragraph, 1 = last):

| Move | Present | Median position | p10–p90 |
|---|---|---|---|
| Where the problem comes from | **100%** | **0.00** | 0.00–0.20 |
| Why it is worth answering | 76% | **0.12** | 0.00–0.33 |
| How it is answered | **100%** | **0.38** | 0.17–0.67 |
| How far the evidence reaches | **58%** | **0.62** | 0.25–1.00 |
| What we now know | 90% | **0.78** | 0.50–1.00 |

The order is monotone: problem → worth → how → boundary → change. The five-link spine is not a
stylistic preference; it is what the modal accepted introduction does.

Order violations are the exception: worth-answering before the problem (15% of papers that have
both), boundary before method (9%), change before boundary (17%).

**Composition**: 45% of introductions contain all five moves, 33% contain four, 20% contain three.
The mean is 4.2 of 5.

---

## 3. The two weak links

Two moves are frequently absent, and they are exactly the two reviewers complain about:

- **Why it is worth answering** — present in 76% of papers, but annotator agreement was poor
  (batch rates range from 25% to 100%). The disagreement is diagnostic: authors often state
  *severity* ("this is a critical threat") instead of *a blocked decision* ("until this is settled,
  we cannot tell whether a patch is complete"). Under the strict reading — a named judgement that
  the answer unblocks — only about a quarter of introductions qualify.
- **How far the evidence reaches** — present in 58%. The other 42% state scope only inside "we do X"
  sentences, or not at all. This is the boundary problem that resurfaces later as a reviewer's
  "the claim is overbroad".

The writing consequence: these two moves are the cheapest way to make an introduction look mature,
because most competitors skip them.

---

## 4. How introductions open

| Opening | Annotated share |
|---|---|
| A specific claim about the world | **63%** |
| A general trend statement ("X is increasingly…") | **36%** |
| Other | 1% |

An automated phrase match finds the *exact* clichés ("In recent years", "With the rapid
development") in only **1.7%** of these introductions. Both numbers are true and they mean different
things:

- The stock phrase is rare (1.7%).
- The general-trend opening is common (36%).

So the rule is not "never open with a trend" — a third of accepted papers do. The rule is: **if you
open with a trend, it must carry a specific, checkable assertion**, not just that the area is
growing. "Attacks on ML systems are increasingly common, and defenders have no way to tell which
patches close them" is a trend opening that earns its place; "In recent years, X has attracted
attention" does not.

---

## 5. Explicit research questions

| Method | Share |
|---|---|
| Annotated as stating the RQ explicitly | 24% |
| Regex match for "we ask / we study / our question" | 37% |

The gap is definitional: annotators required a sentence whose content *is* the question, while the
regex also catches "we study X" inside a method sentence. Report the range; do not claim a precise
number. Either way, **most introductions do not state the RQ as a question** — they derive it and
then describe what was done. A paper that does state it is in the minority, not in the wrong.

---

## 6. What to do with this

For a draft:

1. Locate each of the five moves. A move that cannot be found is the paragraph to write first.
2. Check the order. A boundary statement before the method suggests the introduction is defending
   before it has explained.
3. Check the two weak links specifically — they are absent in most competitor papers, so supplying
   them is cheap differentiation.
4. Do not chase the 45% "all five" figure as a target; 4 of 5 is the modal paper.

For the skill: this file replaces the earlier assertion-based description of the spine with an
empirical one. Where the two disagree, this file wins.
