# Local artifacts: what 120 papers actually do

Word-frequency counters cannot see defects that depend on position: a quantifier that points
forward, a sentence that comments on the paper's own epistemic status, a closing line that
restates the section's labels. This file measures five such artifacts by **annotation**, and
records the ones that turned out not to be defects.

The rule of this file: **a hypothesis is not a rule.** An artifact earns a rule only when two
independent corpora plus the draft separate, and the detector's precision survives a manual read.

---

## 1. Corpora

| Corpus | Papers | Words | Sentences | Stratification |
|---|---|---|---|---|
| Top-tier security papers | **120** | 1,489,207 | 64,889 | USENIX 58, CCS 30, NDSS 20, S&P 12; introduction 120 papers (165,399 w), evaluation/results 73 papers (204,398 w) |
| IEEE S&P Magazine, one issue | — | 64,197 | 2,566 | whole issue |
| The draft under revision | — | 6,480 | 193 | whole paper |

Corpus construction: arXiv full text (LaTeXML HTML), segmented into top-level sections and
labelled introduction / related / results / conclusion by heading text. Venue comes from the
paper's comment field. Reproduce with `build_corpus_v23.py` and `annotate_local.py` (§6).

**Unit of measurement is per 1,000 sentences**, not per 1,000 words: a local artifact is a
sentence property, and papers with long reference lists would otherwise dilute the rate.

---

## 2. Results

| Artifact | Corpus (120 papers) | Intro stratum | Results stratum | Magazine | Draft |
|---|---|---|---|---|---|
| **D1** quantifier + colon (`both: X and Y`) — **strict** | **0** | 0 | 0 | **0** | 0 (see note) |
| D1 — loose variant (any quantifier before a colon) | 9 (0.1) | 1 (0.2) | 1 (0.1) | 0 | 2 (10.4) |
| **D2** label summary (sentence-final colon + `X and Y`) | 179 (2.8) | 14 (2.2) | 10 (1.2) | 4 (1.6) | 0 |
| **D3** meta-hedge — loose | 4 (0.1) | 1 (0.2) | 0 | 0 | 2 (10.4) |
| **D3′** meta-hedge — author-framing, **strict** | **0** | 0 | 0 | **0** | **1 (5.2)** |
| **D4** navigation (`the next section`, `the rest of this paper`) | 50 (0.8) | 10 (1.5) | 4 (0.5) | 1 (0.4) | 1 (5.2) |
| **D5** `And`/`But` opening | 67 (1.0) | 9 (1.4) | 15 (1.8) | **26 (10.1)** | 0 |

Per-paper spread (strict forms): D1′ appears in 0/120 papers; D3′ in 0/120; D4 in 37/120;
D5 in 28/120.

Note on D1: the draft's LaTeX predates the sentence under discussion ("We measure both: accuracy
and pace."). The strict construction therefore scores 0 in all three corpora — that is the
finding: the construction is absent from 1.49M words of published prose, and the new sentence
would be the only instance in it.

---

## 3. Precision audit (the step that decides whether a detector is worth anything)

Each detector was run, its samples read, and the hits classified. This is where most of the
work was, and where two of the five hypotheses died.

| Detector | Sampled hits | True positives | Verdict |
|---|---|---|---|
| D1 loose | 10 | ~3 | **unusable**: matches `both humans and machines:` (pair named before the colon), math appendix junk (`Subtracting the two expressions:`), and definite references (`the two most recent eras:`) |
| D1 strict | 0 | — | construction does not occur; precision moot |
| D2 | 10 | ~1 | **not a defect detector**: it finds ordinary colon lists (`three challenges: A, B, C`), which published prose uses freely |
| D3 loose | 4 | 1 | **mixed**: three hits are `remains an open question whether X generalizes`, a statement about the world, not about the paper |
| D3′ strict | 0 in corpus, 1 in draft | 1 | **clean**: only author-framing forms |
| D4 | 10 | 10 | detector works, but the artifact is legitimate |
| D5 | 10 | 10 | detector works, but the artifact is register, not error |

---

## 4. Decisions

### 4.1 Rule confirmed — the quantifier colon (A18)

`both:`, `the two:`, `these two:` announce a pair that does not yet exist for the reader. Zero
occurrences in 120 papers and one magazine issue. Keep the rule, but state it narrowly: **do not
let a quantifier stand in front of a colon.** The loose variant (any quantifier within a few
words of a colon) is not a rule — it fires on correct prose.

### 4.2 Rule confirmed — the author-framing hedge (A19)

Sentences whose subject is the paper's own epistemic status:

- "That is an empirical question, not a premise."
- "We treat AI's role in that acceleration as an empirical question."

Zero hits in 64,889 published sentences; one in the draft. This survives the precision audit
because the strict form excludes the legitimate `X remains an open question`, which is about the
phenomenon and is common in limitations sections.

Fix: fold the caveat into the claim it qualifies ("… whatever role AI plays in that acceleration"),
or move it to the limitations section, where epistemic caveats belong.

### 4.3 Null result — label summaries (D2)

Colon lists whose tail is two abstract labels are **normal**: 2.8 per 1,000 sentences, in 89 of
120 papers, and 1.6 per 1,000 in the magazine. No rule. What is wrong in the draft is not the
colon list but that the labels were never defined as measurable quantities — a semantic problem,
caught by asking "what did the instrument produce?", not by a regex.

### 4.4 Null result — navigation (D4)

`The next section …`, `the rest of this paper …`: 0.8 per 1,000 sentences, in 37 of 120 papers.
No rule. Draft has one instance. Signposting is not a defect (this repeats the meta-discourse
null result in `ai-artifacts.md` §2, on a different construction).

### 4.5 Null result — `And` / `But` openers (D5)

Papers: 1.0 per 1,000 sentences. Magazine: **10.1 per 1,000** — ten times the conference rate.
No rule, and one explicit retraction: the earlier draft of this skill called sentence-initial
`And` a "paragraph-flattening" defect. The data say it is a register marker that magazines use
deliberately. Flag it only when a paragraph opens with `And` repeatedly.

---

## 5. What this round changed about the method

1. **Build the detector from the defect, not from the words.** The first two D1 regexes had about
   30% precision because they matched a surface token rather than the structural condition.
2. **A null result is a deliverable.** Three of five hypotheses died on the data. Keeping the
   nulls (here and in `ai-artifacts.md`) is what stops the skill from accumulating rules that
   fire on accepted papers.
3. **Stratify, then compare like with like.** Introduction and evaluation sections have different
   rates (D5: 1.4 vs 1.8 per 1,000); a whole-paper rate hides that.
4. **A rate is not the finding.** D3 had the same loose rate as D1 (0.1 per 1,000), but only D3
   survived manual classification. Rates locate; reading decides.

---

## 6. Reproduce

```bash
python build_corpus_v23.py 70        # fetch + segment (append-only JSONL)
python annotate_local.py --samples 12  # rates, per-paper spread, sample hits
```

Estimates from this run: 120 papers, 1.49M words, ~8 minutes of fetching. The corpus is a
convenience sample (arXiv HTML availability, venue from the comment field); it is stated as such
wherever the numbers are quoted.
