# Changelog

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
