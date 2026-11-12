# Changelog

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
