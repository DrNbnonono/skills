# Rubric

The operational layer: how to judge one sentence, what to call the defect, how far to go,
and what to record.

---

## 1. Five questions (≈30 seconds per sentence)

**Q0 — First read (the gate).** Read the sentence once, at speed, as the reader model in
`SKILL.md`: an expert whose first language is not English. Did you get the claim without
backtracking, without decoding a phrase, and without translating a clause? If not, the
sentence fails regardless of grammar — see `comprehension-gate.md` for the stall codes
(S1–S8). Q0 is checked first and overrides a "pass" on Q1–Q4.

**Q1 — Agent.** After one read, can you say who (or what system) did what to whom?
If not, the agent was deleted. This is the most frequent defect in non-native academic prose.

**Q2 — Breath.** Can you read it without backtracking, and still hold the subject at the
period? If not, it is too long or the insertion is too deep.

**Q3 — Restatement.** Can you say it as one plain sentence in the author's first language?
If the restatement needs two or more "and / while / but", the sentence carries three or more
information units: split it.

**Q4 — Deletion.** Delete every dash, parenthesis, and `, which` clause. Does the main clause
still stand and still make the point?
- Still stands → the insertion is an aside; at most one per paragraph.
- Collapses → **the argument was placed inside the aside**; promote it to the main clause.
- No main clause at all → the sentence is a fragment carrying a claim (see A7).

Any failed question → the sentence enters revision. All five pass → **KEEP and do not touch**.

---

## 2. Defect codes

| Code | Name | Detection signal | Rule |
|---|---|---|---|
| **A1** | Agent lost | Passive without `by`; `was combined / were tested / is shown` | L7, L2 |
| **A2** | Nominalisation stack | ≥3 of `-tion/-ment/-ance/-ity/-ness` in one sentence; verb slot occupied by a noun | L3 |
| **A3** | Subject–verb gap | ≥8 words between subject and verb, often a parenthesis | L5 |
| **A4** | Long tail | >35 words, or two stacked clauses after the object | L6, L1 |
| **A5** | Bare `This` | Sentence-initial `This is / These are` with no noun | L9 |
| **A6** | Loose `which` | `, which` used for cause, or antecedent not adjacent | L8 |
| **A7** | Fragment | Noun phrase or verbless label used as a sentence | L1 (magazine layout exempts run-in heads) |
| **A8** | Argument in an aside | Main clause collapses when the insertion is deleted; ≥2 dashes in a paragraph | L10 |
| **A9** | Term drift | Same concept under two spellings; abbreviation never expanded | L12 |
| **A10** | Hedge pile | ≥2 of `rather than / not … but / we do not claim / may` in one sentence | §paragraph |
| **A11** | List in prose | Colon followed by ≥4 items, each with its own modifier | L1 |
| **A12** | Dangling number | Percentage or ratio without numerator, denominator, or comparison | L11 |
| **A13** | Opaque to L2 reader | Idiom, phrasal verb, culture reference, or non-transparent word in a sentence that carries a claim (`hold up`, `shed light on`, `notwithstanding`) | L15, `vocabulary.md` |
| **A14** | Referent lost | `this` / `it` / `the former` with a distant or ambiguous antecedent; two competing nouns before the pronoun | L16 |
| **A15** | Clause stack | ≥3 subordinate clauses (`because/although/while/which/that/if`) or ≥2 parenthetical insertions in one sentence | L14, S3 |
| **A16** | Misordered information | Claim placed after its evidence, or old information in the stress position; conclusion buried in a trailing clause | L4, S8 |
| **A17** | Negation stack | >=2 negators in one sentence; a sentence opening `Not / Never / No / Neither / Unlike`; `we do not ...` describing the author's own stance; a negator plus a negative prefix (`not uncommon`) | L18 |
| **A18** | Unanchored quantifier / label summary | `both`, `the two`, `the second` before the pair is introduced; a closing sentence that restates the section's labels (`accuracy and pace`) instead of naming measured objects | L19 |
| **A19** | Author-framing hedge | Sentence about the paper's own epistemic status: `that is an empirical question`, `not a premise`, `we treat X as an empirical question`; excludes `X remains an open question whether ...` (subject is the phenomenon) | L20 |
| **A20** | Orphan split / seam break | A split whose second sentence starts with `This / It / They / That` with no antecedent in its own sentence; a `because / so / although` that vanished in the split; a restriction detached from its claim (`, but only for ...`) | L21, L22, `coherence.md` |
| **A21** | Choppy run / sentence salad | Three or more consecutive sentences under ~12 words, or a paragraph whose sentences all open the same way; the signature of a metric-driven split pass | L23, `--flow` |

---

A17 has a fixed rewriting direction: **almost always recast to the positive**. Keep the
negation only when the sentence contrasts a *named* alternative, or states a genuine
impossibility that bounds the claim.

| Negative form | Positive recast |
|---|---|
| "That is an empirical question, not a premise." | "The premise is narrower: ..." |
| "This is not to say that every advisory is wrong." | "Most advisories are right; the errors concentrate in one claim." |
| "We cannot rule out that the trend is confounded." | "The data are consistent with a confounded trend." |
| "not uncommon" | "common" |
| "We deliberately do not assume that AI accelerates this." | "Whether AI accelerates this is what RQ2 measures." |

Norm: top-tier papers average 4.6 negators per 1,000 words and 0.8% sentences with two or
more; see `sentence-rules.md` L18 for the corpora.

---

## 3. Six verdicts

| Verdict | Meaning | Action | Expected share |
|---|---|---|---|
| **KEEP** | Passes all five questions | Nothing | ~40% |
| **TRIM** | Correct, but padded with adjectives, hedges, or a redundant clause | Delete words; keep structure | ~20% |
| **SPLIT** | Content correct, too long **and a legal seam exists** | Cut at the seam into 2–3 sentences; run the R/L/T tests | ~20% |
| **MERGE** | Sentences are each fine, but the paragraph has chopped into stubs | Join two adjacent sentences that share a subject or a referent | ~5% |
| **RECAST** | Content correct, unreadable because of subject or order | Change the subject, move the verb forward, put the conclusion last | ~10% |
| **REWRITE** | **Meaning itself is unclear** | Stop and ask the author; do not guess | ~5% |
| **DELETE** | Nothing to preserve: filler, duplicate, dangling quantifier, or a summary already given by the next section | Remove it; record what was removed and why nothing is lost | ~5% |

SPLIT carries a condition the other verdicts do not: **a legal seam must exist**
(`coherence.md` §4). If no seam exists, the sentence is not too long — it is too dense, and
TRIM or RECAST is the correct verdict. Splitting through a joint is how a metric pass produces
A20 and A21.

**KEEP is the expected majority verdict, and a round may be almost all KEEP.** The gate is a
reader-stall detector, not a quota. If a paragraph already passes all five questions, record
"no change" and move on; manufacturing an edit to look productive is itself a defect (see
`SKILL.md` non-negotiable 10).

REWRITE exists because some unreadable sentences are unreadable for a reason grammar cannot
fix: the author has not decided what the sentence asserts. Ask, batch the questions, continue.

---

## 4. Eight surgery moves (try in this order)

1. **Add `we`** — passive → `We <verb>`. Rescues most method sentences.
2. **Turn the noun back into a verb** — `the validation of X` → `we validate X`.
3. **Cut at the semicolon** — `;` almost always becomes a period.
4. **Relocate the insertion** — argument to the main clause, example to the end or brackets.
5. **Move the conclusion to the end** — out of the `which` clause, into its own sentence.
6. **Replace `which`** — cause → `so / because`; addition → `and`; example → `for example`.
7. **Land the number** — `68% of gaps` → `in 68 of the 123 gaps we coded`.
8. **Merge two stubs** — when a split has left two short sentences that share a subject or a
   pronoun chain, join them (`coherence.md` §5). A one-line sentence with no independent claim
   is a fragment pretending to be a paragraph.

---

## 5. Record format

```markdown
| # | Location | Original (truncated) | Code | Verdict | Rewrite | Where the reader stalls | Seam R/L/T |
|---|----------|----------------------|------|---------|---------|-------------------------|------------|
| 1 | abstract:2 | To assess … was combined with … | A1,A3 | RECAST | We test … and we pair … | passive plus a 15-word subject; the verb arrives at word 21 and no agent is named | n/a |
| 2 | rq1:12 | …seals four of nine paths, but only where… | A4 | TRIM | (kept whole; 6 words trimmed) | 46 words, but the trailing clause is the claim's scope | split rejected: would detach restriction |
```

The stall column must name a **reader failure** ("the verb arrives at word 21"), never a taste
judgement ("smoother", "more native"). The seam column is `n/a` for non-splits; for a SPLIT or
MERGE, record `R/L/T` and note any repair (`R: pronoun named`, `L: "so" moved to sentence start`).

---

## 6. Walkthrough

Original (52 words):

> A fixed embargo window that was defensible under earlier rediscovery dynamics is not
> automatically still defensible now; a more principled, risk-adjusted approach to setting
> and revisiting embargo windows---and a post-release review rule that checks whether a
> release was, in retrospect, complete---is one direction we explore in the appendix.

**Q1** The subject is *a window is not defensible*: an object is doing the judging. Nobody
decides anything. → fail (A1, A2)
**Q2** 52 words, one semicolon carrying two propositions, a 20-word dash insertion. → fail (A4, A8)
**Q3** Restating needs three connectors: "…and therefore…, which includes…, and that is in the
appendix". → fail
**Q4** Delete the dashes: "a more principled approach … is one direction we explore" dangles —
explore what? → fail

**Verdict**: SPLIT + RECAST.

> An embargo window that made sense under earlier rediscovery dynamics is not automatically
> defensible now. Coordinators need a risk-adjusted way to set the window and to revisit it
> later. The appendix takes one step in that direction: a post-release rule that asks, after
> the fact, whether the release was complete.

Seam check after the split: **R** — "that direction" has an antecedent in its own sentence
("a risk-adjusted way"); **L** — the original semicolon carried no connector, so none was lost;
**T** — "The appendix" is given by the previous sentence's stress ("one step in that direction").
Had the target been a metric rather than a legal seam, the dash content would have been cut
into a fourth sentence and lost its antecedent.

What changed: the abstract subject became a human decision ("made sense"); the semicolon
became three sentences; the dash content became the third sentence's main clause; the dangling
"one direction we explore" became a subject with a verb ("The appendix takes one step"). No
number or claim was altered.

---

## 7. Prohibitions

- Do not alter numbers or the strength of a claim. If strength must change, list it and ask.
- Do not replace `we` with `this paper` throughout; `we` is standard and preferred.
- Do not upgrade plain verbs (`use` → `utilize`, `show` → `demonstrate`, `find` → `ascertain`).
- Do not restructure sections during the sentence pass; log structural findings separately.
- **Do not split to move a metric.** Name the seam first; if there is no legal seam, the fix is
  TRIM or RECAST, and the metric may be missed with a recorded reason (`coherence.md` §1).
- **Do not repair cohesion by adding connectives everywhere.** Glue above ~18 % of sentences is
  its own defect (A21); let order carry the logic where it can.
- **Do not merge across a paragraph boundary.** Paragraphs are claims; merging two of them
  changes the argument, which is Tier 3.
