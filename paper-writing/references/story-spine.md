# The story spine

A research story is a line: **a question worth answering, turned by research into a warranted
understanding.** Five links, in this order. Each one has a characteristic failure, and the failure
shows up in a specific section.

> Where does the problem come from? → Why is it worth answering? → How is it answered? →
> How far does the evidence reach? → What do we know now that we did not?

---

## Why the line breaks (the diagnosis to make first)

Authors work in **work order**: first the experiment, then the analysis, then the meaning. Readers
read in **cause order**: first why, then how, then what follows. A paper written in work order
reads as a lab notebook: detailed, chronological, and impossible to care about.

So "I cannot tell a story" is usually not an expression problem. It is an ordering problem, and it
is fixed by supplying the links the author skipped — not by better sentences.

---

## Link 1 — Where does the problem come from?

The opening does not introduce a field; it **derives a question**. The most common break:

> "In recent years, X has attracted widespread attention."

This states that a field is popular. Nothing about popularity implies a question. The missing
inference has three steps, and all three must appear:

1. **What does the field need to decide?** A specific phenomenon to explain, a difficulty to
   resolve, a judgement practitioners must make.
2. **What does existing work already establish?** Organised by *claim*, not by paper: sources that
   support the same judgement go together; sources that disagree go together, with their
   conditions, methods and results contrasted.
3. **Where does the existing understanding fall short of that need?** Not "few studies exist", but
   "with what is known, we still cannot decide Z".

Then narrow: which object, under which conditions, to judge which relation, cause, or manifestation.

The paragraph should end in a question specific enough that the method follows from it.

**Test:** replace your first sentence with "X is popular, therefore…" — if the rest of the
paragraph still reads as a non sequitur, the derivation is missing.

---

## Link 2 — Why is it worth answering?

Importance is not "no one has studied this". That sentence reports a count. Importance connects the
question to **the judgement it unblocks**:

- If this question stays open, what can we still not decide?
- Once it is answered, which belief or decision changes?

Answering those two is the whole of "significance". They also police overclaiming: if the
introduction promises a large problem and the paper studies one component, the paragraph must say
why that component is the load-bearing one, and how far the work actually advances.

**Test:** delete the sentence "this is important" and check whether the two answers above are still
present. If they are not, the sentence was the only claim of importance, and it claims nothing.

---

## Link 3 — How is it answered?

Methods are not a record of actions; they are the reason the question becomes answerable.

| Record | Answer |
|---|---|
| "We measured three metrics and ran two conditions." | "To determine whether the change is caused by that factor, we held the rest fixed and varied only it." |
| "We used a dynamic testbed." | "Because the claim is about what is exploitable, the test must execute, so every unit was tested end to end." |
| "We collected 40 events." | "Forty events across four eras give enough per-era observations to compare medians, which is all the claim needs." |

Every non-obvious choice — this metric, this control, this corpus, this denominator — needs one
sentence of *why*. Without it the reader cannot judge whether the method answers the question, and a
method the reader cannot judge is a method the reader does not believe.

---

## Link 4 — How far does the evidence reach?

Two jobs: state what the data show, and state the inference from data to claim.

- Report the number, then **the judgement it supports**, in that order.
- Say what was not tested. The boundary belongs next to the claim, not only in the limitations
  section: a reader who discovers the boundary on page 12 feels misled even if the paper never lied.
- Distinguish "we did not observe" from "it does not happen". The first is a result; the second is a
  claim about the world that the evidence rarely licenses.

**Test:** cover the numbers and read only the interpretations. If the paragraph still makes a
checkable claim, the inference is written down. If it collapses into adjectives ("strong", "clear"),
the inference is missing.

---

## Link 5 — What do we know now?

The ending returns to the opening question and states the **change in knowledge**:

> Before: the boundary was believed to hold under condition A. Now: it holds under A but not under
> B, and the failure has a specific shape.

Not: "This work provides a reference for the field." That sentence reports no change.

The discussion places the answer back into the literature: what was known, what is now known, which
judgement that changes, and under which conditions the new claim holds — and where it does not.

**Test:** can a reader finish the discussion and say, in one sentence, what the field now knows that
it did not? If not, the contribution has not been stated at the level where it can be believed.

---

## The spine doubles as a research checklist

Read the spine against the work, not the draft. A link that cannot be written is usually a missing
piece of research, not a missing paragraph:

| Link that fails | Likely research gap |
|---|---|
| Cannot state the question in one sentence | the question was never fixed; the paper is a topic |
| Cannot say which judgement is blocked | the motivation is borrowed, not earned |
| Cannot justify a method choice | the choice was conventional, not reasoned |
| Cannot bound the claim | the evaluation did not vary the conditions that matter |
| Cannot state the change in knowledge | the result is a measurement without a consequence |

Fixing the writing will not fix those. Report them to the author as research gaps.

---

## Applying the spine to a paragraph

The same line works one level down. For each paragraph:

1. Which judgement must the reader hold after this paragraph?
2. What does the reader already know that this judgement builds on?
3. Which figure, number, or argument supplies it?

If (1) cannot be named, the paragraph is a container. If (3) is missing, the paragraph asserts
without support. If (2) is wrong, the paragraph is in the wrong place — see
`paper-prose-polish/references/structure-and-placement.md`.
