# What goes in the appendix

## Measured shape (120 top-tier papers)

| Property | Value |
|---|---|
| Papers with an appendix | **60.8%** (73/120) |
| Appendix sections per paper with one | 251 / 73 = **3.4** |
| Display items in the appendix | **10.9%** of all items (25-paper sample, top-level items only) |

Topic frequency over the 251 appendix sections (titles can match more than one topic, so the column does not sum to 251):

| Topic | Sections |
|---|---|
| Parameters, settings, implementation details | 16 |
| Additional results / experiments | 11 |
| Proofs, theorems, derivations | 11 |
| Full protocol, questionnaire, instrument, prompts | 10 |
| Artifacts, code, reproducibility | 5 |
| Datasets, collection procedure | 5 |
| Ablations | 4 |
| Ethics, disclosure | 4 |
| Robustness / sensitivity | 2 |

Read the ranking, not the absolute counts: the appendix is dominated by **details a specialist would
check** — settings, extra experiments, proofs, instruments — not by new claims.

---

## 1. The rule

**The appendix holds what a specialist checks; the body holds what the argument needs to be
believed.** Corollaries:

- Never put the only evidence for a claim in the appendix. USENIX states that reviewers are not
  required to read appendices, and that the paper must be self-contained without them.
- Every appendix section is referenced at least once in the body, with what to look for.
- If the appendix is longer than the body, the paper is two papers.

---

## 2. What belongs, in the order it usually appears

1. **Proofs and derivations** — anything that interrupts the argument but is needed for trust.
2. **Additional results** — the same claim under more datasets, seeds, or baselines.
3. **Parameters and implementation details** — enough to reproduce, too much to read.
4. **Datasets and collection** — inclusion criteria, annotation protocol, licensing.
5. **Ablations and sensitivity** — the full grid behind the one row in the body.
6. **Instruments** — questionnaires, prompts, interview guides, exact wording.
7. **Artifacts, ethics, disclosure** — code/data availability, coordination status, IRB.

This order matches the frequency data above and moves from "needed for trust" to "needed for
compliance".

---

## 3. What does not belong

- The threat model or assumptions (the reader needs them before the method).
- The main result table.
- A second, better-evaluated version of the system. If it is better, it belongs in the body and the
  body's claim must change.
- Reviewer defence written as an attack ("in case the reviewer asks…"). Answer in the body, once.
- Anything the body never cites.

---

## 4. Appendix hygiene

- **One topic per appendix section**, titled with the topic, not "Appendix A".
- **Count continuously** with the body (`Table 4`), unless the venue dictates otherwise.
- **No contradictions with the body.** A reviewer who reads both will trust the appendix and discount
  the paper.
- **Keep the appendix under the page budget**: some venues count it, some do not; check before
  filling it.

---

## 5. Decision checklist

For each candidate appendix item:

- [ ] It is not the only evidence for a body claim.
- [ ] The body references it.
- [ ] It has one topic.
- [ ] It does not contradict the body.
- [ ] It is worth the page.

If the fifth box is doubtful, delete it: an appendix is not a bin for work that did not fit the
argument.
