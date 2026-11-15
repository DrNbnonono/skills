# Body versus appendix, and display items

Two decisions that are cheapest to make once, at planning time, and most expensive to defer: which
claims get a display item, and where that display item lives.

---

## 1. The decision test

Ask these four questions of every table, figure, or extra experiment.

| Question | If yes | If no |
|---|---|---|
| Is the main claim believable without it? | appendix | body |
| Does the body text refer to it more than once? | body | appendix |
| Is it a variant that supports the same conclusion (another dataset, another baseline, a sweep, a robustness check)? | appendix | body |
| Would a reviewer who did not read it still accept the claim? | appendix | body |

The rule underneath: **the appendix holds what a specialist checks; the body holds what the argument
needs to be believed.** Never place the only evidence for a claim in the appendix — USENIX states
explicitly that reviewers are not required to read appendices, and that the paper must be
self-contained without them.

---

## 2. What typically goes where

| Body | Appendix |
|---|---|
| The one figure that carries the mental model | Full parameter sweeps, per-configuration tables |
| The table of the headline result | Additional baselines and their settings |
| The threat model / assumptions | Proofs, derivations, instrument text |
| One ablation that changes the interpretation | Robustness variants that confirm it does not |
| The headline number in a table or figure | Per-event or per-instance listings |
| The failure cases that bound the claim | The complete list of failures |

---

## 3. What was measured

`scripts/story_study.py`, 30 papers from the 120-paper corpus:

| Measure | Value |
|---|---|
| Display items per paper | 36 at the median — inflated: sub-figures counted separately |
| Display items in the appendix | **11.4%** of all items |
| Papers with at least one appendix item | 18 / 30 |

Read as an order of magnitude: **roughly one display item in ten lives in the appendix**, and about
half the papers put something there. The count is inflated by sub-figures, so do not treat 11.4% as
a target. The usable conclusion is that the appendix is a minority container, not a second paper.

---

## 4. Display items in the body

1. **One message per item.** If the caption needs "and", the item is two items.
2. **Every item is cited before it appears**, and the citing sentence says what to look at
   (`paper-prose-polish/references/floats-and-references.md`).
3. **Decide the style now**: type (bar / line / table), axis limits, units, color scheme, font
   size, caption voice. Style decided at planning time is free; style decided during polishing costs
   a day.
4. **Captions state the takeaway**, not the axes. "Recall falls to 3% under the literal reading" is a
   caption; "Recall by advisory source type" is a title.
5. **Plan the figure before the experiment that fills it.** The axes are a commitment to which
   quantity matters.

---

## 5. Appendix hygiene

- One page per topic, each appendix section with a sentence saying why it exists.
- Number the appendix items continuously with the body (`Table 4`, not `Table A1`) unless the venue
  dictates otherwise; readers cite them as tables either way.
- Never let the appendix contradict the body: a reviewer who reads both will trust the appendix and
  discount the paper.
- If the appendix is longer than the body, the paper is two papers.

---

## 6. Planning table (fill this before drafting)

| # | Item | Type | Claim it supports | Body / Appendix | Why |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

If a row has no claim in column 3, delete the row: an item without a claim is decoration, and
decoration is what makes a paper look padded.
