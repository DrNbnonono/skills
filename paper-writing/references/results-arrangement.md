# Arranging the experiments

The evaluation is where the paper either earns its claim or is caught asserting it. This file is
about **order**: which experiment comes first, what each subsection must state, and how the section
maps back to the claims in the introduction.

## Measured shape (120 top-tier papers)

| Property | Value |
|---|---|
| Papers with a dedicated evaluation section | 78.3% |
| Evaluation sections per paper | median 1, max 2 |
| Paragraphs in the evaluation | median 24 (p90 41) |
| Introduction length for comparison | median 10 paragraphs, 1,032 words |

So the evaluation is roughly **two to three times the introduction**, and it is usually one section,
not several. A paper with five evaluation sections is usually a paper with five papers inside it.

### Evaluation subsections (60 papers, ar5iv section hierarchy)

| Measure | Value |
|---|---|
| Subsections per evaluation | median **4** (mean 4.4, max 11) |
| Has a setup subsection | 53.3% |
| ...and it comes first | 46.7% |
| Ends with a summary/discussion subsection | **5.0%** |
| Has a named ablation subsection | 13.3% |
| Has a named sensitivity subsection | 5.0% |
| Titles that are claim-specific rather than generic | **62%** |

The last row is the finding that matters. Most evaluation subsections are named after the specific
claim or condition they test ("Impact of phase differences", "Detection under compression"), not
after a generic function ("Setup", "Ablation", "Results"). The section is organised claim by claim;
the generic labels are a minority.

Two consequences:

- Do not force the generic vocabulary. A subsection called "Impact of X" is doing its job; one
  called "Additional experiments" is usually hiding an unmapped result.
- A closing "summary" subsection is rare (5%). The summary of what the evaluation established
  normally sits at the end of the **last** subsection or opens the discussion, not in its own
  heading.

Caveat: only papers whose evaluation contains subsections were counted; papers with a flat
evaluation section are not represented.

---

## 1. The mapping rule

**Every claim in the introduction gets exactly one evaluation subsection that answers it, and every
evaluation subsection answers exactly one introduction claim.**

Build the mapping before writing prose:

| Intro claim | Evaluation subsection | Display item | The number that settles it |
|---|---|---|---|
| | | | |

A claim with no subsection is a claim to delete. A subsection with no claim is an experiment to
delete (or to move to the appendix as a robustness check).

---

## 2. The default order

1. **Setup** (one subsection, short): what was run, on what, with which parameters, and what the
   reader should compare. State the hardware/software and the unit of measurement once; the reader
   needs it to interpret every later number.
2. **The headline result** — the claim the paper is named after. It goes first because a reader who
   stops after one subsection must still have the main finding.
3. **Supporting claims**, each in its own subsection, in the order the introduction listed them.
4. **Ablation** — only with a hypothesis ("if X causes the effect, removing X should reduce it").
   Without the hypothesis an ablation is a buffet, and reviewers read it as fishing.
5. **Sensitivity / robustness** — how the result moves when a knob moves. This is where the
   boundary of the claim is established.
6. **Threats to validity / failure cases** — what did not work, and why.

Two legitimate alternatives to this order:

- **Artifact-per-subsection** (one subsection per dataset or per system) when the reader's question
  is "does it generalise across X", not "does it do Y".
- **RQ-per-subsection** when the paper has two questions with different instruments; then each
  subsection repeats its own setup sentence.

---

## 3. What each subsection must contain

Four sentences of structure, in this order:

1. **The question** — what this subsection decides, phrased so it could fail.
2. **The design** — what was varied, what was held fixed, and why that isolates the effect.
3. **The evidence** — table or figure, with the specific column/panel named in the text.
4. **The interpretation** — what the number means for the claim, in words. Never leave this to the
   reader: "Table 3 shows 62%" is a report; "Table 3 shows that the patch seals only 62% of the
   paths a reader would infer, so half of the stated scope remains open" is an interpretation.

A subsection missing (4) is the single most common evaluation defect: the reader is handed numbers
and told to conclude.

---

## 4. Numbers: prose first, table second

- The headline number appears **in the sentence**, not only in the table. A reader skimming the
  section must meet the result in words.
- The table carries the detail: per-row values, variance, sample sizes.
- If a number appears in the abstract, the introduction, and a table, all three must match exactly;
  a mismatch is the fastest way to lose a reviewer's trust.

---

## 5. Failure modes

| Failure | Symptom | Fix |
|---|---|---|
| Results buffet | many tables, no claim per table | map each to an intro claim or move to appendix |
| Conclusion left implicit | section ends on a table | add the interpretation sentence |
| Ablation without hypothesis | "we also test without X" | state what would falsify the claim first |
| Only successes reported | every row passes | include a failing configuration or explain why none can |
| Setup repeated per subsection | same paragraph five times | state once, refer back |
| Claim stronger than the numbers | "significantly better" with no test | report the effect and the test, or drop "significantly" |

---

## 6. From a pile of results to a section

When the experiments are done but the section is not written:

1. List every result you have, one line each: what was run, what it shows.
2. Mark each with the intro claim it supports; unmarked results go to the appendix or the bin.
3. Order the marked results: headline first, then the order the introduction promises.
4. For each, write the four sentences of §3.
5. Check the reverse direction: every intro claim has a subsection.

`templates/results-inventory.md` is the worksheet for steps 1–2.
