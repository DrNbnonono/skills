# Structure and placement

Language rules can be applied to a sentence in isolation. Placement cannot: where a paragraph
belongs depends on what the paper argues, and the same paragraph can be right in one paper and
wrong in another. So this file does **not** give rules for moving content. It gives:

1. measured conventions from 120 top-tier papers, so a deviation is visible as a deviation;
2. a placement checklist with confidence levels;
3. a protocol for raising a placement problem with the author, since the decision is theirs.

The governing principle: **structure is a discussion, not an edit.** Never move, merge, or delete
a paragraph without saying what the reader expects, what the paper does instead, and what the
move would cost.

---

## 1. Measured layout (120 papers, 1.49M words, 12,146 paragraphs)

Corpus: arXiv full text, top-level sections only, venue from the paper's comment field
(USENIX 58, CCS 30, NDSS 20, S&P 12). Section role detected from the heading text.

### 1.1 Which sections exist

| Role | Papers with it | Median position | Range |
|---|---|---|---|
| Related work / background | **87.5%** (105/120) | 1 | 1–9 |
| Design / approach / method | 59.2% (71/120) | 3 | 1–13 |
| Evaluation / results | **80.8%** (97/120) | 4 | 1–13 |
| Threat model / assumptions | **17.5%** (21/120) | 2 | 1–11 |
| Limitations (own section) | **13.3%** (16/120) | 6 | 5–11 |
| Ethics (own section) | 29.2% (35/120) | 8 | 3–11 |
| Conclusion | **90.8%** (109/120) | 7 | 4–13 |

Two readings matter here:

- A **dedicated limitations section is a minority form** (13/100 papers). Most papers fold
  limitations into the discussion, the evaluation, or the end of the introduction. A separate
  section is not wrong, but it is not the default either, and it costs a heading.
- A **threat model section is also a minority** (17.5%), concentrated in papers that attack a
  specific class of system. Measurement papers usually state assumptions inline, where they are
  used, rather than in a block. If a reviewer cannot find the assumptions, that is a placement
  problem, not a missing-section problem.

### 1.2 Where related work sits

| Placement | Share |
|---|---|
| Before the design section | **75.0%** |
| After the evaluation | 15.0% |
| No dedicated related-work section | 12.5% |

The convention is: related work early, before the reader has to judge novelty. The 15% that put
it after results are papers where the comparison is the contribution and reading it early would
spoil the argument. Either is defensible; what is not defensible is **both**, i.e. a short related
passage in the introduction and a longer one in section 2 that repeats the same studies.

### 1.3 Paragraph size

| Metric | Median | Mean | p90 |
|---|---|---|---|
| Words per paragraph | **75** | 78 | 97 |
| Sentences per paragraph | **3** | 3.5 | 4 |

A paragraph of 150+ words or 6+ sentences is in the top decile. That does not make it wrong, but
it means the reader has no resting point in the middle of a double column.

### 1.4 Introduction conventions

| Convention | Share | Note |
|---|---|---|
| Ends with a roadmap ("the rest of this paper is organized as follows") | **17.5%** | a minority form; often the first thing an editor cuts |
| Uses the word "contribution" | 38.3% | the list itself may be bulleted, which this corpus does not capture |

The roadmap result surprises most authors. It is not an error, but it is not the norm either, and
in a page-limited venue it is the cheapest paragraph to delete.

### 1.5 Redundant closure between paragraphs

Definition: the last sentence of a paragraph shares ≥2 content words with the first sentence of
the next paragraph **and** contains a forward marker (`below`, `the next section`, `we now`).
That is a paragraph closing by announcing the paragraph that follows.

| Measure | Corpus |
|---|---|
| Flagged paragraphs | 129 / 12,146 = **10.6 per 1,000** |
| Papers with at least one | 55.8% |

So roughly one paragraph in a hundred closes this way in published work; it happens, it is not
forbidden, and it becomes a problem when it is the *standard* way a paper ends paragraphs. Check
the draft's own rate rather than applying a rule.

---

## 2. Placement checklist

For each content type: the usual home, the evidence, and when to deviate. "Usual" means the
majority form; deviating is allowed when the paper has a reason.

| Content | Usual home | Evidence | Deviate when |
|---|---|---|---|
| The claim and its stakes | First 1–3 paragraphs of the introduction | universal | never |
| Related work | Section 2, before design | 75% | the comparison *is* the contribution (then after results) |
| Assumptions / attacker model | Inline where used, or a short section early | 17.5% have a section, median index 2 | the assumptions are numerous and shared by several sections |
| Method | After related work | median index 3 | an attack paper may start with the threat model |
| Evaluation | After method | median index 4 | a measurement paper may interleave method and results per RQ |
| Interpretation / implications | End of each results subsection, or a discussion section | common | — |
| Limitations | Inside the discussion, or the end of the evaluation | 13.3% use a standalone section | the venue expects a "what we do not know" block (magazines do) |
| Ethics / disclosure | A short block in the body, or a section before references | 29.2% | the venue mandates it (USENIX: own section) |
| Future work | End of conclusion | common | — |
| Definitions of coined terms | First use, or a glossary table | — | more than ~6 terms: use a table |

### 2.1 Signals that a paragraph is in the wrong place

Read the paragraph and ask these four questions. A "yes" is a candidate for a discussion, not an
automatic move.

1. **Does the reader lack a definition this paragraph needs?** → the paragraph is too early; the
   definition, or the paragraph, must move.
2. **Does this paragraph repeat something the reader met two sections ago?** → it is too late, or
   it is a duplicate; choose one home.
3. **Does the paragraph's first sentence depend on a result that appears later?** → too early.
4. **Would deleting it break the next paragraph's first sentence?** → it is load-bearing; do not
   move it without carrying the dependency.

### 2.2 Signals that a paragraph should not exist

- Its content is already stated in a table caption.
- It announces the next section ("we now turn to …") and the next section opens by saying the
  same thing.
- It is a list of two items written as prose.
- It exists only to introduce a figure that the figure's caption already introduces.

---

## 3. How to raise a placement issue

Structure changes are the author's call, because only the author knows what the paper is arguing.
The protocol:

1. **Name the expectation.** "Top-tier papers usually put related work before the method (75%);
   this paper puts it after the evaluation."
2. **Name the cost.** "A reader reaches the evaluation without knowing what was already known, so
   the novelty claim in §5 has no anchor."
3. **Offer two options with their costs.** "Move §2.3 before §3 (costs a transition paragraph), or
   add two sentences of positioning to the introduction (costs a paragraph of space)."
4. **Ask, and record the answer.** Never move text in the same round you raise the issue.

This is the same tiering as `SKILL.md` "Rewrite authority": placement is Tier 3.

---

## 4. Applying it to the draft in this repository

Measured on the draft (54 paragraphs, 5,949 words of prose):

| Metric | Draft | Corpus median | Reading |
|---|---|---|---|
| Words per paragraph | **112** (p90 179) | 75 (p90 97) | paragraphs carry ~50% more words than the norm |
| Sentences per paragraph | 3.0 (p90 6) | 3.0 (p90 4) | same median, heavier tail: the long paragraphs are 5–6 sentences |
| Roadmap sentence | present | 17.5% of papers | minority convention; cheapest paragraph to cut if space is tight |
| Related work before method | yes (§2.3 before §3) | 75% | matches the majority |
| Limitations as its own section | yes (§6) | 13.3% | minority in conferences, expected in magazines |
| Dedicated threat model | no | 17.5% | assumptions are inline in §3.1; acceptable for a measurement paper, but a reviewer may ask |

Two concrete actions, both for discussion rather than unilateral edit:

1. **Split the longest paragraphs.** The 230-word paragraph in §5 and the 224- and 220-word
   paragraphs in the appendix each carry 4–5 sentences of dense argument. Splitting at the point
   where the topic changes brings them to the corpus p90 (97 words) without deleting anything.
2. **Decide the roadmap's fate once.** If the venue is a magazine, delete it; if a conference and
   space is tight, it is the first cut. Do not keep it and also signpost at every section start.

---

## 5. Caveats

- Sections are top-level only; bulleted contribution lists inside the introduction are not
  captured by the `<p>`-based parse, so conclusions about "contributions" are weak (38.3% only
  says the word appears in a paragraph).
- Role detection is a heading regex; "Design" under a system name ("3 *OurSystem*") counts as
  other. The 59.2% figure is therefore a floor.
- The corpus is a convenience sample of arXiv HTML with venue labels from comment fields. Treat
  the percentages as orders of magnitude, not as a distribution of all accepted papers.
