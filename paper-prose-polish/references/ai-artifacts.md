# AI-writing artifacts, and what the corpus actually shows

Generated prose and human prose fail differently. This file separates the artifacts that have a
**measurable corpus signature** from the ones that only appear as local incoherence. Writing a
rule without evidence is how a style guide turns into superstition, so each item below states
how it was checked and what the check found.

Corpora used throughout: 16 top-tier security papers (250,324 words, arXiv full text, venue
named in the paper's comment field), one complete issue of IEEE S&P Magazine (64,197 words),
and the non-native draft used in the worked example (6,480 words).

---

## 1. Artifacts with a measured signature

### 1.1 Negation stacking (real, and large)

| Metric | 16 papers | Magazine | Draft |
|---|---|---|---|
| Negators per 1,000 words | 4.6 (2.6–7.1) | 4.6 | **9.7** |
| Sentences with ≥2 negators | 0.8% | 0.8% | **5.7%** |
| Contrast markers per 1,000 | 0.66 | 0.50 | **3.7** |
| "we do not / we cannot" per 1,000 | 0.14 | 0.00 | **0.90** |

Two independent corpora land on the same number, so the norm is not an artifact of the sample.
Rule: `sentence-rules.md` L18, code A17.

---

## 2. Suspicious, but **not** a defect: meta-discourse

The hypothesis that generated prose over-narrates itself ("this paper measures …", "we measure
both …") does not survive measurement:

| Metric | 16 papers | Magazine | Draft |
|---|---|---|---|
| Meta-discourse per 1,000 words | 0.77 (0.13–1.18) | 0.48 | 0.91 |
| Share of sentences containing meta-discourse | 1.65% | 1.2% | 2.6% |
| "both X and Y" per 1,000 words | 0.45 | 0.56 | 0.15 |

The draft sits **inside** the published range. Real papers signpost at almost exactly the same
rate. **Do not add a rule that deletes signposts.** A rule of that kind would damage correct
prose, and it would flag a 0.91 against a 1.18 maximum — i.e. it would fire on papers that were
accepted.

What survives is narrower and local, in section 3.

---

## 3. Artifacts with no density signal — local only

These cannot be caught by a counter, because they depend on what the preceding sentence said.
They are caught by the five questions and named here so the failure is recognised.

### 3.1 The quantifier points forwards (A18)

> We measure both: accuracy and pace.

A quantifier (`both`, `the two`, `the second`, `these three`) presupposes that the reader has
already stored the set. Here the set is announced *after* the quantifier, so the reader holds a
dangling "both" and then receives two abstract labels to attach to it.

Corpus check: the magazine uses `both` 5 times in one issue, every time pointing backwards to an
established pair (NSF/EU, advocates/opponents, teaching/service). Forward-announcing `both:`
appears **zero** times. The construction is not ungrammatical; it is simply never used by
published authors in this position.

Fix: put the pair first, or drop the quantifier ("We check the documents against dynamic
exploitation, and we time the ecosystem's response"), or delete the sentence and let the
research-question list that follows do the work.

### 3.2 Label nouns instead of measured objects

`accuracy` and `pace` are the section's labels, not quantities. You do not measure "accuracy";
you measure recall against a validated set, or time-to-advisory against a disclosure date.
Generated text reaches for the label because the label was produced alongside the outline.

Test: replace the label with what the instrument produced. If the sentence becomes a real
sentence, the original was a label.

### 3.3 Redundant closure

A paragraph's last sentence that announces what the next section will contain duplicates the
next section's first sentence. Published prose does this at section boundaries, rarely at the
end of a body paragraph. If the following block is a list of research questions, the closing
summary is read twice in ten seconds.

### 3.4 Meta-hedge in place of a claim (measured in v2.3)

> We treat AI's role in that acceleration as an empirical question.

This is a statement about the author's method, not about the world. Measured on 120 top-tier
papers (64,889 sentences): **zero** occurrences of the author-framing form; one in the draft.
Rule: `sentence-rules.md` L20, code A19. The look-alike `X remains an open question whether ...`
is legitimate (its subject is the phenomenon) and was excluded by the strict detector.

### 3.5 `And` at sentence start - retracted as a defect (v2.3)

Measured: 1.0 per 1,000 sentences in 120 papers, **10.1 per 1,000 in a magazine issue**. It is a
register marker, not an error. The earlier version of this file called it "paragraph-flattening";
the data do not support that. Flag it only when consecutive sentences or paragraph openings begin
this way.

---

## 4. How to extend this file

1. Propose the artifact as a **hypothesis**, not a rule.
2. Measure it on at least two corpora plus the draft. Report words, n, mean, range.
3. If the draft is inside the published range, write **nothing** — record the null result here
   instead (section 2 is that record for meta-discourse).
4. If the draft is outside the range, write the rule with the numbers and a counter-example from
   published prose.
5. Keep the null results. They are the reason the skill does not accumulate rules that fire on
   accepted papers.
