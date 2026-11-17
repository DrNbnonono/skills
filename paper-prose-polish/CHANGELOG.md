# Changelog

## v2.8.0 - IMC specialisation (additive; no existing rule moved)

The skill could polish a security paper, reshape one for a magazine, and repair an English
abstract. It had nothing to say about a **measurement** venue, where the reviewer's first
question is not "is the attack novel" but "over what population, in what period, from
where". This release adds ACM IMC as a venue profile, measured rather than remembered.

### Added

- **`references/venue-imc.md`**: official IMC 2026 gates (13/6 pages, abstract ≤200 words,
  double-blind with the unique-capability exception, **mandatory "Ethics" appendix**,
  artifact declaration, appendices may not carry a contribution's evidence, grayscale-safe
  figures, AI disclosure), the measured prose fingerprint, the abstract recipe with its
  base rates, the number-and-scope rule, the measurement-verb register, validity language
  for the four questions an IMC reviewer asks, ethics and artifact paragraphs, twelve
  IMC-specific anti-patterns, and a worked before/after in IMC voice.
- **`scripts/imc_check.py`**: the venue checks a prose linter cannot make — abstract budget
  and opening frame, presence of the Ethics section, artifact statement, measurement vs
  systems verb counts, digit-bearing sentence share, unbounded generality, unhedged "first"
  claims, "significant" with no test, em-dash budget. Every threshold prints the base rate
  it came from.
- **`venue-profiles.md` §6**, three anti-pattern rows, and a **Step 0 / Step 5 hook** in
  `SKILL.md`: the profile is entered from the existing venue gate, not from a parallel
  workflow.

### Measured

Two samples, both DOI-anchored to the ACM proceedings (2022-2025), never to an arXiv
comment field: **75 full texts** (32% of the 237-paper programme; the ACM DL answers 403,
so this is what arXiv and repositories could supply) and **all 237 camera-ready titles and
abstracts** from the programme pages.

- Prose: mean sentence **23.7** words, median 21, p90 38, passive 19.0%, negation 5.7 per
  1,000, hedges 3.8 per 1,000, em dashes **2.75** per 1,000, and **51.5% of sentences carry
  a digit**.
- Against the 120-paper top-4 corpus: sentence length is **identical** (23.7 vs 23.1),
  negation identical, passive slightly lower — the IMC difference is not at the sentence
  level. It is the digit-bearing share (51.5% vs 39.7%), the em-dash density (3x), and the
  verb register (`we find` is IMC's most frequent body verb; `we use / evaluate / propose`
  lead in security).
- Sections: introduction 98.7%, background/related 81.3%, method 64.0%, results-or-
  evaluation 40.0%, discussion 46.7%, limitations 26.7%, conclusion 78.7%, Ethics anywhere
  92.0%, appendices 21.3%. Only 40% name a section "Evaluation"; the middle of an IMC paper
  is usually named after the object measured.
- Abstracts: median **189** words (29.5% exceed the 200-word limit anyway — recorded, not
  imitated), 82.3% carry a number, 95.8% use "we", only **8.0%** open with
  "We / In this paper" (first sentence, as defined in `imc_abstracts.py`), 52% open with a
  property of the object, 24.1% claim "first".
- Titles: median 10 words, 55.3% with a colon, 24.5% naming measurement work.

### Explicitly not done

No threshold in `lint_prose.py` was touched, and `--venue imc` was not added: the measured
IMC numbers sit inside the existing conference limits, and the venue-specific checks live in
their own script. No existing reference file was rewritten, no rule was renumbered, and the
precedence rule (claim fidelity > coherence > metrics) is unchanged: a `WARN` from
`imc_check.py` may stand with a recorded reason, exactly like a gate miss.

### Recorded as not measured

Inter-rater agreement on the section roles (single layout detector, no double annotation);
prose from 2021 and earlier (different template, different ethics rule); whether an IMC
paper's arXiv preprint is the camera-ready text (76% of the sample carries camera-ready
furniture; the Ethics figures are also reported on that subset). The caveats are printed in
`venue-imc.md` §11 rather than hidden.

---

## v2.7.0 - the abstract is an English genre, not a translated one

The previous abstract guidance was inherited from Chinese-journal conventions (目的 / 方法 / 结果 /
结论): front the finding, delete the actor, close with a sentence about significance. Measured on
accepted papers, the four venues do the opposite. This release replaces the advice with the
measurement.

### Measured (164 abstracts: S&P 40, USENIX Security 44, CCS 40, NDSS 40; 2022-2025)

- median **207 words**, **9 sentences**, mean sentence **22.5** (p10 18.7, p90 28.9);
- **92%** contain `we`/`our`; 28% of sentences start with `We`; only 9% of first sentences do;
- **54%** use `In this paper, we`; passive markers in 12% of sentences;
- the approach sentence arrives by sentence 4 in **54%**; a result before the approach in **1%**;
- **70%** carry at least one number, **48%** at least three.

### Added

- **`references/abstract.md`**: the five moves measured in the corpus, person/order/rhythm rules,
  a symptom-to-repair table for translated Chinese-template abstracts, a synthetic before/after,
  a checklist, and the collection method with its caveats.
- **`lint_prose.py --abstract`** (and `--limit`): words against the venue limit, sentences, mean,
  person, gap marker, number density, opening and closing class, with WARN/NOTE mapped to A22-A25.
  Calibrated so only 8-10% of accepted abstracts trip a warning; never fails the build.
- **`scripts/abstract_study.py`**: re-collects and re-analyses the abstract corpus (OpenAlex for
  S&P/CCS/NDSS, usenix.org for USENIX Security) and prints the tables used in `abstract.md`.
- **Rubric A22-A25** (abstract without an actor, result before the question, ceremonial closing,
  fact-sheet abstract) and **surgery move 9** (restore the abstract's agent).
- **`diagnosis-playbook.md` section 3.4**: measured abstract targets, separate from the generic
  sentence thresholds.
- **`SKILL.md` Step 4.7**: the abstract is revised last, then linted with `--abstract`.
- **`magazine-mode.md` section 7**: rewritten to the five moves plus the linter check.

### Corrected

- `venue-prose-corpus.md` claimed a **result-first abstract** (finding and number in the first two
  or three sentences). Measured: the approach arrives before the result, and result-first is 1%.
  The row is replaced, not reworded.
- `diagnosis-playbook.md` treated "0 `We` sentences in the abstract" both as a red flag and as
  something the rewrite removed. The rewrite now restores the agent (A22), and the target is
  stated as 2-4 `We`-starting sentences in 9.
- `worked-example.md` section 4 described the old result-first structure as the target; it now
  diagnoses the translated-template defect and records the repair.
- **Magazine abstract: 50 words, not 200.** The official author page states "The abstract word
  limit is 50 words"; the earlier "≤200" came from a secondary source that described IEEE
  *journals*. Measured on 200 published magazine abstracts (2022-2025): median **40 words**, **2
  sentences**, 61% use `we`/`our`, 15% contain a number. Fixed in `venue-profiles.md`,
  `magazine-mode.md` §7, `diagnosis-playbook.md` §3.4, `abstract.md` §10, and the linter's
  magazine default (`--venue magazine` now implies `--limit 50` and a magazine-specific shape).
  A 200-word magazine abstract is four times over the limit.

### Not changed

No gate threshold moved. The abstract warnings are advisory: 8-10% of accepted abstracts trip one,
which is why `--abstract` always exits 0.

---

## v2.6.1 - put the precedence rule where the temptation is

The rule already existed (v2.5): claim fidelity > coherence > metrics, and a gate miss with a
recorded reason is a decision. What was missing is that nothing enforced it **at the gate**, which
is exactly where a reviser is tempted to buy a PASS.

### Added

- **Non-negotiable 11**: never win a metric by breaking the prose. Explicitly outranks every
  threshold in the file.
- **`lint_prose.py --gate`** now prints, on FAIL: a gate miss is acceptable when recorded with its
  reason, and a PASS bought by breaking a seam is a defect.
- **`diagnosis-playbook.md` section 3** opens with the same statement, above the threshold table.
- **Revision template**: verification item "no metric was improved by breaking a seam".

### Not changed

No threshold moved. This release only makes the existing precedence visible where numbers are
consumed.

---

## v2.6 - display items have a reading order

A figure the reader meets before it is introduced is worse than a delayed one: the reader either
skips it or reads it without knowing what to look for. This round adds the reading-order layer for
figures and tables.

### Added

- **`references/floats-and-references.md`**: venue requirements (IEEE: near, but not before, the
  first mention; introduce before, interpret after; explain significance in the caption), the
  LaTeX mechanics that decide whether those hold (FIFO float queue, `[t]` vs `[!ht]` vs `[H]`,
  `\FloatBarrier`), seven rules, a symptom-to-cause table, and a submission checklist.
- **Step 4.6 display-item order** in `SKILL.md`, including the instruction to check the compiled
  PDF rather than the source.
- **`scripts/float_study.py`**: parses LaTeXML HTML (arXiv or the faster `ar5iv` mirror), maps
  `Figure N` / `Table N` links to float elements, and reports citation coverage and source-order
  distance.

### Measured, and deliberately not turned into thresholds

A 40-paper run: 23 floats per paper (median), 69.7% with at least one body reference, 52.8% of
float elements appearing before their first mention **in the source**. The last figure is a
statement about authors' LaTeX habits, not about printed pages, because arXiv HTML preserves
source order. The caption classifier (19.3% full sentences) also proved too brittle. The numbers
are recorded in the reference with their failure modes, and the file says explicitly: read the
compiled PDF, never gate on these.

### Audited in the paper under revision

Two appendix tables (`tab:typology`, `tab:rt-loo`) are never cited in the body; four figure files
exist without being `\input` anywhere; one table uses `[!ht]` while every other float uses `[t]`.
All four input figures are cited before their `\input`, which is correct.

---

## v2.5.1 - do not manufacture edits

A small correction to the skill's own incentives. After v2.5, the risk is a reviser who finds
nothing wrong and invents a change so the round looks thorough. The skill's verdict distribution
already expects KEEP to be the majority (~40 %); this release makes the rule explicit.

### Added

- **SKILL.md non-negotiable 10**: if the original sentence or paragraph already does its job, it
  is KEEP and the words stay. The skill is a reader-stall detector, not a quota of changes.
- **"A good draft is a valid finding"** paragraph: measure, read, report KEEP, done.
- **Rubric**: KEEP is the expected majority and a round may be almost all KEEP; forcing a
  SPLIT to look productive is a defect.
- **Diagnosis playbook**: "if the draft is already good, say so and stop" in Reporting, and the
  "polishing past the gate" pitfall.
- **Template**: `Changes this round: __ (zero is a valid answer)`.
- **Anti-pattern row**: nitpicking a good sentence.

### Not changed

Nothing else. v2.5's coherence constraint and all prior corpus findings stand.

---

## v2.5 - coherence is a constraint, not a metric

Two rounds of corpus work taught the skill to split sentences until the numbers pass. This
round adds the counterweight: **the metrics are targets; the reader's ability to follow one
sentence to the next is a constraint with veto power.** Motivated by a reader's report that a
draft revised to the targets read worse: correct length, broken seams.

### Added

- **`references/coherence.md`** - the precedence ladder (claim fidelity > coherence > metrics),
  the three seam tests (reference / logic / topic), the legal and illegal split points, MERGE
  as a legal move, the paragraph-level coherence gate, and the format for recording a missed
  metric with its reason.
- **MERGE verdict** in `rubric.md` (six verdicts; SPLIT now requires a named legal seam) and an
  eighth surgery move ("merge two stubs").
- **`references/sentence-rules.md` L21-L23**: split at a seam, never through a joint; every split
  needs an R/L/T seam repair; merge when the bond is stronger than the boundary.
- **`references/rubric.md` A20-A21**: orphan split / seam break, and choppy run / sentence salad.
- **`scripts/lint_prose.py --flow`**: paragraph size, sentence-length CV, longest run of
  sentences <=12 words, repeated-adjacent-opener share, sentence-initial connective share.
  Warnings only, never a gate - they describe the reading experience, which no per-sentence
  counter can see.
- **`references/diagnosis-playbook.md` §3.3** flow thresholds and the warning rule, plus a new
  reporting item ("the flow report, with every missed metric and its reason").
- **Template**: seam column, flow baseline, missed-metric table, and a verification item that
  every SPLIT has an R/L/T result.

### Measured (on the draft that motivated this round, 9 sections, 316 sentences)

| | Pre-revision text | Post-revision text |
|---|---|---|
| Longest choppy run (consecutive <=12-word sentences) | 5 (introduction) | 3 (three sections) |
| Adjacent pairs sharing a first word | up to 14.5% | up to 14.3% |

The metric pass did not create the problem from nothing, but it can preserve and spread it.
Neither number is visible in the length table.

### Not changed

Every threshold and corpus finding from v2.1-v2.4. This round changes what a gate *miss* means
(recorded, not failed) and adds a constraint the gates cannot enforce.

---

## v2.4 - placement, paragraphs, and an honest grammar dead end

Three things a sentence counter cannot see: where a paragraph sits, where a paragraph ends, and
whether the grammar is broken at all. One of the three produced a usable method.

### Structure and placement (new reference)

120 papers, 12,146 paragraphs, section roles detected from headings:

| Convention | Share |
|---|---|
| Related work before design | 75.0% (after evaluation: 15.0%) |
| Dedicated limitations section | 13.3% |
| Threat model / assumptions section | 17.5% |
| Ethics section | 29.2% |
| Conclusion section | 90.8% |
| Introduction ends with a roadmap sentence | **17.5%** |
| Paragraph median / p90 | 75 / 97 words; 3 / 4 sentences |

`references/structure-and-placement.md` adds a placement checklist and a **protocol**: a
placement problem is raised with the convention, the cost, and two options, and the author
decides. Placement is Tier 3 in the rewrite authority - never moved silently.

### Paragraph boundaries

The v2.3 corpus kept flat section text, so paragraph ends were approximated. v2.4 re-parsed all
120 papers with `<p>` boundaries: 12,146 paragraphs, redundant closure at **10.6 per 1,000
paragraphs** (55.8% of papers have at least one). Definition and draft comparison in
`local-artifacts.md` section 7. The draft's paragraphs are 112 words at the median against 75;
its sentence count per paragraph is normal, so the excess is sentence length again.

### L2 grammar (mostly a null result)

Four detectors on spaCy POS tags: `a`/`an`, bare singular nouns, `this`/`these` agreement, tense
mixing. Results:

- `a`/`an`: corpus 0.08 per 1,000 words; the draft is clean (its two hits are LaTeX artifacts).
- Bare singular nouns: **122.8 per 1,000 nouns**, which is impossible; false positives from mass
  nouns, headings, and compound heads. Detector discarded.
- `this`/`these`: false positives from compound modifiers (`these crash [reports]`). Detector
  discarded.
- Tense mixing: 12.8% of published paragraphs mix past and present; convention, not error.

`references/l2-grammar.md` records the dead ends and routes mechanical grammar to LanguageTool
(needs a JVM, not installed here), keeping the skill's gates for discourse.

### Added

- `references/structure-and-placement.md`, `references/l2-grammar.md`
- `scripts/build_corpus_v24.py`, `scripts/structure_study.py`, `scripts/l2_grammar.py`
- **Step 4.5 placement review** in `SKILL.md`

---

## v2.3 - local artifacts, measured by annotation

v2.2 measured what a word counter can see. This round measures what it cannot: defects that
depend on where a sentence sits and what the previous sentence established. Five hypotheses, a
precision audit, and **three null results**.

### Corpus

120 top-tier security papers (USENIX 58, CCS 30, NDSS 20, S&P 12), 1,489,207 words, 64,889
sentences, segmented into introduction (165,399 words) and evaluation (204,398 words) strata;
plus one magazine issue and the draft. Unit: per 1,000 sentences.

### Confirmed

- **A18 quantifier colon** (narrowed). Strict form - a quantifier standing directly before a
  colon - occurs **0 times** in 120 papers and 0 times in the magazine. The loose form (any
  quantifier near a colon) had ~30% precision: it fires on `both humans and machines:` and on
  math appendix lines. Rule rewritten to the strict form; the loose form is explicitly not a rule.
- **A19 author-framing hedge** (new). `That is an empirical question, not a premise`, `we treat X
  as an empirical question`: **0 hits in 64,889 published sentences**, 1 in the draft. Excludes
  `X remains an open question whether ...`, whose subject is the phenomenon and which is common
  in limitations sections.

### Null results (no rule written)

| Artifact | Corpus | Magazine | Draft | Why no rule |
|---|---|---|---|---|
| Label summaries (colon + `X and Y`) | 2.8/1k, 89/120 papers | 1.6/1k | 0 | ordinary colon lists; published prose uses them freely |
| Navigation (`the next section`) | 0.8/1k, 37/120 papers | 0.4/1k | 1 hit | signposting is not a defect |
| `And` / `But` openers | 1.0/1k, 28/120 papers | **10.1/1k** | 0 | a register marker; **retracted** the v2.2 "paragraph-flattening" claim |

### Added

- **`references/local-artifacts.md`** - corpora, stratified rates, the per-detector precision
  audit, the three nulls, and the four method lessons (including "build the detector from the
  defect, not from the words").
- **L20** the claim carries its own caveat; **A19** author-framing hedge.
- **Linter**: `ah` / `ah_per_1k`; gate checks `fq_per_1k <= 0.2` and `ah_per_1k <= 0.2`. The
  `fq` regex was tightened to the strict form.
- **`ai-artifacts.md`**: section 3.4 upgraded from "local only" to measured; section 3.5
  retracted with the magazine counter-evidence.

### Not changed

Everything v2.2 established: rewrite authority tiers, the DELETE verdict, negation norms,
reader model.

---

## v2.2 - what generated prose gets wrong, and one null result

### Measured, and rejected

The hypothesis: generated prose over-narrates itself, so signposting should be rare in published
papers and the draft should exceed the norm. Measured on the same three corpora:

| Metric | 16 papers | Magazine | Draft |
|---|---|---|---|
| Meta-discourse per 1,000 words | 0.77 (0.13-1.18) | 0.48 | 0.91 |
| Share of sentences with meta-discourse | 1.65% | 1.2% | 2.6% |
| "both X and Y" per 1,000 | 0.45 | 0.56 | 0.15 |

The draft sits inside the published range. **No rule was added.** The null result is recorded in
`references/ai-artifacts.md` section 2, so the skill does not later acquire a rule that would
flag accepted papers.

### Added

- **`references/ai-artifacts.md`** - generated-prose artifacts split into (a) measured, (b)
  measured-and-rejected, (c) local-only, with the extension procedure that keeps null results.
- **L19 quantifiers point backwards; summaries name objects**. The surviving defect is local: a
  quantifier announcing a pair it has not introduced ("We measure both: accuracy and pace"), and
  a closing sentence that restates the section's labels instead of the measured objects. Corpus
  check: in one magazine issue every `both` points backwards; the forward-announcing `both:`
  form appears zero times.
- **A18 unanchored quantifier / label summary**.
- **DELETE verdict** in `rubric.md` and in Step 3: nothing to preserve is a legitimate outcome.
- **Rewrite authority** section in `SKILL.md`: three tiers (rebuild silently and report;
  replace the sentence; restructure across paragraphs only after discussion), with the invariant
  that numbers, claim strength, term meanings, and citations are never changed silently.
- **Linter**: `fq` / `fq_per_1k` (forward-announcing quantifiers) and a gate check at <= 0.2 per
  1,000.

### Why the policy change matters

The old instruction "do not improve KEEP sentences" was read as "keep the author's wording
whenever the claim is intact". That produces polite rewrites of sentences that should not exist.
Fidelity is owed to the claim, not to the sentence.

---

## v2.1 - the negation norm

A reader's hypothesis, tested rather than accepted: top-tier papers state claims positively and
rarely negate. Half right, and the half that is wrong matters.

### Measured

Same counter on three corpora:

| Corpus | Words | Negators /1k | >=2-negator sentences | Contrast /1k | "we do not" /1k |
|---|---|---|---|---|---|
| 16 top-tier security papers | 250,316 | 4.6 (2.6-7.1) | 0.8% (0.1-1.7) | 0.66 | 0.14 |
| IEEE S&P Magazine, one issue | 64,197 | 4.6 | 0.8% | 0.50 | 0.00 |
| The non-native draft in the worked example | 6,480 | 9.7 | 5.7% | 3.70 | 0.90 |

Negation is **not** rare: one negator per 220 words is normal, and two independent corpora land
on the same figure. What is rare is stacked negation and self-directed negation. The draft sits
beyond the maximum of every sampled paper on every metric - the signature of defensive framing.

### Added

- **L18 affirm first; negate only against a named alternative** in `sentence-rules.md`, with the
  corpus table, the three shapes to delete (meta-negation, payload in the negative slot, double
  negation), and a before/after taken from the draft.
- **A17 negation stack** in `rubric.md`, plus the fixed-direction recast table.
- **Section 3.2 negation calibration** in `diagnosis-playbook.md`, including the method note
  (arXiv HTML whose comment field names the venue; convenience sample, stated as such).
- **Linter**: `neg/1k`, `dbl%` columns; `neg_per_1k`, `double_neg_pct`, `contrast_per_1k` in the
  JSON; three new gate checks (`neg_per_1k <= 6`, `double_neg_pct <= 1.5`, `contrast_per_1k <= 1.5`).

### Not changed

Everything else. L18 does not contradict L2/L7 (agent as subject) - it is the same principle
applied to polarity: say what is, then contrast it with something specific.

---

## v2.0 — the first-read gate (L2 reader model)

The v1 skill measured sentences for a native reader: length, passive, nominalisation,
dashes. It could still pass a draft that a fluent non-native reader has to re-read. v2 makes
**first-read comprehension** the acceptance criterion and instruments it.

### Added

- **`references/comprehension-gate.md`** — the user's rule, operationalised:
  *if a competent non-native reader cannot get the gist on the first direct read, the
  sentence is broken.* Contains the three tests (first-read, shadow, stranger), the stall
  taxonomy S1–S8, operating thresholds, and eight worked pairs.
- **`references/vocabulary.md`** — transparency over simplicity. The key correction to
  native-style advice: for an L2 reader, short Anglo-Saxon phrasal verbs (`hold up`) are
  *less* transparent than longer international words (`remains exploitable`). Includes
  idiom/phrasal-verb replacement table, formal-word table, ambiguous function words
  (`while`, `since`, `as`, `significant`), and what **not** to simplify.
- **`references/venue-prose-corpus.md`** — what the top-4 venues (S&P, USENIX Security,
  CCS, NDSS) actually reward in prose, separated into official requirements, observed
  conventions, and a reproducible measurement protocol (no invented corpus statistics).
- **Four L2 defect codes** A13 (opaque to L2 reader), A14 (referent lost), A15 (clause
  stack), A16 (misordered information) in `references/rubric.md`, plus Q0 (first-read) as
  the leading question.
- **Four sentence rules** L14–L17: first-read gate, no idioms where the claim lives, one
  obvious antecedent per pronoun, one new concept per sentence.
- **Five-question rubric** — Q0 runs before Q1–Q4 and overrides a grammar-level pass.
- **Linter v2** (`scripts/lint_prose.py`): words before the main verb, subordinate clauses,
  parentheses, idiom count, non-transparent formal words, Flesch estimate; `--gate
  --venue conference|magazine` for pass/fail; `--explain N` to list the sentences with the
  most blockers. Now also accepts `.txt` corpora.
- **L2 thresholds** in `references/diagnosis-playbook.md` §3.1.
- **Revision-table columns** for "first read" and stall counts.

### Changed

- `SKILL.md`: new reader model, non-negotiable #8 (simplify syntax, never domain
  vocabulary) and #9 (never trade accuracy for readability), Step 1.5 first-read gate,
  anti-patterns for native flourish, idiom-as-compression, and grammar-checker trust.
- `>45 words` is now a **rate per 100 sentences** rather than an absolute count, so the
  gate means the same thing for a 6-page paper and a 14-page one.
- The linter exits `1` in `--gate` mode when a check fails (CI-friendly); normal mode still
  exits 0.

### Not changed

Terminology lock, the five verdicts, the surgery moves, `magazine-mode.md`,
`venue-profiles.md`, `worked-example.md`, and the backup-first rule. v1 was right about
*what* to fix; v2 changes *what counts as fixed*.

---

## v1.0 — initial release

Venue gate, measurement, terminology lock, sentence pass (A1–A12), paragraph pass,
verification; magazine conversion mode; worked example.
