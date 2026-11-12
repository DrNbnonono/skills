# Diagnosis playbook

How to measure a draft, how to read the numbers, and how to report them so the author acts
on them.

---

## 1. Why measure first

Two failure modes are avoided by a baseline: revising by impression (endless, unverifiable),
and revising everything (destroys precision and the author's voice). A measurement converts
"this reads strangely" into "one sentence in four exceeds 45 words, and 26% are passive".

---

## 2. Procedure

1. **Extract prose only.** Strip comments, tables, figures, `\input`, `\cite`, `\ref`, `\label`,
   and math placeholders. Keep headings out of the sentence stream but keep them as boundaries.
2. **Split sentences.** A period/question/exclamation followed by whitespace and a capital
   letter, bracket, or quote. Watch for two artefacts:
   - sentences ending in math or a citation, where the next sentence starts lowercase after
     macro removal (this fuses two sentences and inflates the maximum);
   - headings glued to the following paragraph.
   Verify by printing the ten longest sentences and inspecting them by hand. If a "sentence"
   spans two ideas joined by a lowercase word, the splitter is wrong, not the author.
3. **Compute** per file and in total: sentence count, word count, mean, median, p90, max,
   counts over 35 and over 45 words, passive rate, nominalisation density, dash count,
   `This + be` count.
4. **Print the worst ten** and read them. Numbers locate the problem; reading confirms it.
5. **Save the baseline** as JSON so later rounds use the identical measurement.

`scripts/lint_prose.py` implements steps 1–5 for `.tex` and `.md`.

---

## 3. Thresholds by venue class

| Metric | Conference draft (target) | Magazine draft (target) | Red flag |
|---|---|---|---|
| Mean sentence length | ≤25 words | ≤22–25 words | >30 |
| p90 sentence length | ≤38 | ≤32 | >45 |
| Sentences >45 words | ≤2.5 per 100 | ≤1.5 per 100 | >5 per 100 (≈10% of sentences) |
| Passive rate | ≤18% | ≤12% | >30% in method, limitation, or conclusion sections |
| Nominalisations per sentence | ≤1.6 | ≤1.4 | >2.2 |
| Dashes (`---`) per 1,000 words | ≤2 | ≤2 | >5 |
| Sentences opening with `We` in the abstract | ≥3 | ≥2 | 0 |
| Unfinished markers (`\todo`, `[TBD]`, `XXX`) | 0 | 0 | any |

Calibration data: a full issue of IEEE S&P Magazine (Vol. 15 No. 5, 2017; 100 pages,
419k characters, noise included) measures **2,658 sentences, mean 23.5 words, median 20.0**.
Use it as an order of magnitude, not a target.

### 3.1 L2 blocker thresholds (v2)

These are the metrics that predict first-read failure. The linter computes them; `--gate`
prints pass/fail.

| Metric | Conference target | Magazine target | Red flag | Why it matters |
|---|---|---|---|---|
| Words before the main verb | ≤10 | ≤10 | >14 | The reader cannot hold a subject longer than that |
| Subordinate clauses per sentence | ≤2 | ≤2 | >3 | Three clauses is where backtracking starts |
| Parenthetical insertions per sentence | ≤1 | ≤1 | ≥2 | Each one suspends the main clause |
| Idioms / phrasal verbs per 1,000 words | ≤2 | ≤2 | >5 | Opaque to readers who do not share them |
| Non-transparent formal words per 1,000 words | ≤5 | ≤3 | >10 | `utilize`, `aforementioned`, `henceforth` |
| Abstract / method sentences with 2+ new terms | 0 | 0 | any | Working-memory overload for an L2 reader |
| Stalls per 100 words (first-read gate) | ≤3 | ≤1 | ≥4 | The aggregate comprehension measure |

A draft can pass every length threshold and still fail the gate: 20-word sentences with two
idioms each are short and opaque. Check the L2 blockers before declaring the pass finished.

---

### 3.2 Negation calibration (v2.1)

Same counter, three corpora:

| Corpus | Words | Negators /1k | >=2-negator sentences | Contrast /1k | "we do not" /1k |
|---|---|---|---|---|---|
| 16 top-tier security papers (arXiv HTML, venue named in comments) | 250,316 | **4.6** (2.6-7.1) | **0.8%** (0.1-1.7) | 0.66 | 0.14 |
| IEEE S&P Magazine, one full issue | 64,197 | **4.6** | **0.8%** | 0.50 | 0.00 |
| A non-native draft (same paper as the worked example) | 6,480 | **9.7** | **5.7%** | 3.70 | 0.90 |

The draft is beyond the maximum of every sampled paper on every negation metric. That is the
signature of defensive framing (L18 / A17), not a stylistic preference. Two corpora agreeing at
4.6 and 0.8% is the reason the gate uses 6 and 1.5% rather than a stricter cutoff.

Method note: the conference corpus is 16 arXiv papers whose comment field names USENIX
Security, IEEE S&P, ACM CCS, or NDSS; HTML full text was fetched and stripped, body plus
references included. It is a convenience sample, adequate for an order of magnitude and for the
observation that two independent corpora land on the same number.

## 4. Reading the numbers

| Pattern | Interpretation | First action |
|---|---|---|
| Mean >30, p90 >50 | Sentences are carrying two or three claims each | SPLIT the >45 group; that alone moves the mean several points |
| Max much larger than p90 | A few 90+ word sentences, usually enumerations | Split or convert to a list |
| Passive >30% in one section only | That section hides the agent — usually methods or limitations | Recast with `we`; check that nothing became unreproducible |
| Passive high in the conclusion | The paper is hedging at the moment it should be assertive | Convert to active, keep the claim strength |
| Nominalisations >2.2 | Verbs are locked inside nouns | L3 pass, sentence by sentence |
| Abstract: 0 `We` sentences | The abstract describes results as if they occurred without an agent | Rewrite the abstract (do it last, once terminology is settled) |
| Dashes >5 per 1,000 words | Argument is being smuggled into asides | Q4 audit: delete each dash and test the main clause |
| Section mean >45 | Usually the appendix and the conclusion: the two places reviewers check rigour | Treat as a priority, not an afterthought |
| Negators >8/1k **and** >=2-negator sentences >3% | Defensive framing: the paper spends sentences on what it does not claim | L18 pass: recast to positive, keep only contrasts with named alternatives |

---

## 5. Reporting

Present, in this order:

1. **One sentence of conclusion** — what the numbers mean for the reader
   (e.g. "the content is there; the agent is missing").
2. **A table** with per-file and total metrics, with the worst cells marked.
3. **Three headline findings**, each tied to a measured value and a consequence.
4. **Systemic issues**, ranked P0 (submission-blocking: unfinished markers, missing
   statistics, anonymity violations, wrong template) → P1 (structure, over-claiming) →
   P2 (terminology) → P3 (rhythm).
5. **Worked examples**: 8–10 sentences, before → diagnosis → after, chosen to cover the
   most common codes rather than the worst sentences.
6. **Questions for the author** — the REWRITE batch.

Do not lead with counts. Lead with the consequence, then the evidence.

---

## 6. Pitfalls

- **Trusting the splitter.** Always eyeball the longest ten. A merged pair of sentences
  produces a fake 100-word outlier and an inflated maximum.
- **Counting headings and captions.** They are short and drag the mean down; keep them out.
- **Treating the passive rate as a score.** A passive sentence with a known agent in the
  stress position is correct English. Judge per sentence, use the rate only as a trend.
- **Optimising the mean.** Deleting information to shorten sentences is the most common way
  to make a paper worse while the metrics improve. Prefer adding a sentence to cutting content.
- **Revising the abstract first.** Terminology and claim strength are settled in the body;
  an abstract rewritten before that has to be redone.
