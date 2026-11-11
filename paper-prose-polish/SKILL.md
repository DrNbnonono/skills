---
name: paper-prose-polish
description: Polish English academic prose for security/systems venues (S&P, USENIX Security, CCS, NDSS, journals, IEEE S&P Magazine), written for readers whose first language is not English. Use for 润色/改写/逐句修改论文表述, diagnosing why a paragraph is unreadable, converting a conference paper into a magazine feature, or a clarity review before submission. Core rule: if a competent non-native reader cannot follow a sentence on the first pass, the sentence is broken. Measures the draft first, then revises sentence by sentence with a defect code and a stated reader-stall reason for every change.
version: 2.0
---

# Paper prose polish

Revision of English academic writing for security and systems venues, aimed at authors
whose first language is not English — and at the much larger audience that includes every
reviewer reading six papers in one night.

The target is not "nicer prose". The target is: **a competent non-native reader gets the
claim on the first read**, without backtracking and without translating the sentence to
understand it.

## Core principle

If the author cannot state, after one read, **who did what**, the sentence is broken — not
the reader. And if a reader who is fluent but not native has to re-read a clause to decode
it, the sentence is broken even when it is grammatically perfect and sounds elegant to a
native ear. Native elegance is not the acceptance criterion. **First-read comprehension is.**

Nearly every unreadable sentence in non-native academic prose fails for one of four
mechanical reasons: the agent was deleted (passive), the verb was turned into a noun
(nominalisation), the new information sits in the wrong position, or the sentence is
decoded only by an idiom the reader does not share. All four are diagnosable and fixable
in bulk.

## The reader model (read this before editing a sentence)

Write for this person:

- reads English papers daily, has the technical background, knows the field's vocabulary;
- is **not** a native speaker: shares international/Latin technical vocabulary, does **not**
  share idioms, phrasal verbs, culture references, or native collocations;
- reads at speed, at 11 p.m., in a second language, possibly on a phone;
- will not re-read a sentence to rescue it. They will assume it was their fault, then
  assume the paper is unclear.

This reader is also the reviewer, the program-committee member skimming, and the
practitioner reading the magazine. Optimising for them does not hurt native readers; writing
only for native readers does hurt everyone else.

`references/comprehension-gate.md` turns this model into a repeatable test.

## When this applies

- A draft that must be readable to reviewers who do not work in the same subfield.
- A non-native author's manuscript that "reads strangely" without an obvious grammar error.
- A draft that passes grammar checkers but still needs re-reading.
- A conference paper being reshaped for a magazine, journal, or a broader audience.
- A pre-submission clarity pass, or a response to "the paper is hard to follow".

Not for: copy-editing that must preserve house style verbatim; proofreading-only requests
(use a grammar pass instead); writing the research itself.

## Non-negotiables

1. **Never change a number, a claim's strength, or a technical term's meaning.** If the
   strength of a claim must change, list it separately and ask the author.
2. **Never invent facts** — dates, team names, days elapsed, quotes. Insert `[placeholder]`
   and ask.
3. **Ask instead of guessing** when the sentence is ambiguous because the author may not
   have decided what it means. Code those `REWRITE` and batch the questions.
4. **Keep `\cite{}`, `\ref{}`, `\label{}`, math, and table data intact** in LaTeX sources.
5. **Back up before writing.** Copy `file.tex` to `file.tex.bak-YYYYMMDD` first.
6. **Do not improve KEEP sentences.** The goal is comprehension, not vocabulary display.
7. Do not swap common verbs for fancy ones (`use` → `utilize`, `show` → `demonstrate`).
   Native technical writing prefers the plain verb.
8. **Simplify syntax, never domain vocabulary.** `exploitability`, `deserialization`,
   `affected-version range` stay exactly as they are. The reader is an expert; the difficulty
   is the sentence, not the concept.
9. **Do not trade accuracy for readability.** If making a sentence easy requires dropping a
   qualifier, keep the qualifier and split the sentence instead.

## Step 0 — Venue gate (do this before touching a sentence)

Identify the target: top-4 security conference, systems conference, IEEE/ACM journal,
professional magazine, or arXiv preprint. Read `references/venue-profiles.md` and apply
its **rules-void matrix**: several rules that are mandatory for a conference paper
(anonymity, full CVE numbers, `compsoc` template, a separate ethics section) are wrong for
a magazine, which is single-blind, requires CVE numbers, and is typeset by the publisher.

Record the decision: venue class, page/word budget, abstract limit, audience
(researcher vs practitioner), review model.

`references/venue-prose-corpus.md` explains what the top-4 venues actually reward in prose,
and how to re-measure a fresh corpus instead of trusting remembered style advice.

## Step 1 — Measure before revising

Run the linter and record a baseline. Never start from impressions.

```bash
python scripts/lint_prose.py --path <paper-dir> --glob "*.tex" --out baseline.json
```

Read `references/diagnosis-playbook.md` for how to interpret the numbers and how to set
thresholds for the venue class. Report at minimum: mean/median/p90 sentence length,
sentences over 45 words, passive rate, nominalisation density, dash count, and the share of
sentences whose subject is an agent.

Since v2 the linter also measures the four **L2 blockers**: words before the main verb,
subordinate clauses per sentence, idioms/phrasal verbs, and non-transparent formal words.
Run it with `--gate --venue magazine|conference` for a pass/fail read.

## Step 1.5 — The first-read gate

Before the sentence pass, read the whole draft once at normal speed, as the reader model
above. Mark every sentence where you (a) backtracked, (b) paused to decode a phrase, or
(c) could not say in your own language what the clause asserted without looking at it again.

Three stalls in one paragraph means the paragraph is rewritten, not patched. One stall per
paragraph is normal in any draft; zero is the goal for a camera-ready.

`references/comprehension-gate.md` gives the three tests (first-read, shadow, stranger),
the stall taxonomy, and worked before/after pairs. Run it before and after the sentence
pass; the counts are your before/after metric for comprehension, not just style.

## Step 2 — Lock terminology

Build a glossary before sentence work: one canonical form per concept, its first-use
definition, and the banned variants. Then, if the audience is practitioners, add a
de-jargonisation mapping (replace invented abstractions with ordinary nouns). Inconsistent
terms read as carelessness and are a common reviewer complaint; they cannot be fixed
sentence by sentence later.

`references/vocabulary.md` covers the second half of this step: which words are transparent
to an L2 reader (international technical vocabulary) and which are not (idioms, phrasal
verbs, native flourish). The instinct "short Anglo-Saxon words are simpler" is wrong for
this audience; "internationally recognisable" is the criterion.

## Step 3 — Sentence pass

Work in batches of 20–30 sentences. For each sentence:

1. **Five questions** (see `references/rubric.md`): who does what; one breath; can it be
   restated in one sentence in the author's language; does the main clause survive deleting
   parentheticals; does it survive one first read without a stall.
2. **Assign defect codes** A1–A16 (A13–A16 are the L2 codes added in v2).
3. **Assign a verdict**: KEEP / TRIM / SPLIT / RECAST / REWRITE.
4. **Apply a surgery move**, not a paraphrase.
5. **Record** the change with the reason ("the reader stalls at X"), never "smoother".

Use `templates/revision-table.md`. A change without a stated reader-stall reason is
unjustified.

## Step 4 — Paragraph and structure pass

Only after sentences: check topic sentences, one claim per paragraph, duplicated content
between the introduction and related work, and whether the first page answers "what does
this paper do". Read `references/magazine-mode.md` when the target is a magazine — it
covers the restructure (display-item budget, sidebar instead of appendix, scene opening).

For each paragraph, also check the L2 reader's load: does the paragraph introduce one new
term, or three? Does the first sentence name the claim, or start with background?

## Step 5 — Verify

- Re-run the linter with `--compare baseline.json`; compare against the threshold table in
  `references/diagnosis-playbook.md`.
- Re-run the first-read gate; report stalls per 100 words before/after.
- Thresholds are directional, not targets to game: if a sentence loses information to hit
  a number, the edit is wrong.
- Read the revised paragraph aloud once. A sentence the reviser cannot finish in one breath
  is still too long.
- Back-check: every number, `\cite`, `\ref`, and technical term unchanged.

## Deliverables per round

1. A revision table (position, original, code, verdict, rewrite, reader-stall reason,
   first-read status).
2. The applied source change, with a backup of the previous file.
3. The before/after measurement table, including the L2 blockers.
4. Two or three "so next time" rules tied to the author's recurring habits.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Rewriting every sentence | Erodes the author's voice and technical precision; KEEP is a real verdict |
| Synonym inflation | Native technical prose is plain; "utilize" reads as non-native |
| Splitting a list sentence into three | Lists are legitimately long; only prose carried by one verb must be split |
| Deleting hedges wholesale | Hedges are epistemic claims; removing them changes what the paper asserts |
| Fixing sentences before locking terms | Produces consistent grammar over inconsistent vocabulary |
| Applying conference rules to a magazine | Wrong anonymity, template, CVE, and length decisions |
| **Trusting a grammar checker as the gate** | Grammatical sentences routinely fail first-read comprehension; the gate is the L2 reader, not the parser |
| **Native-style flourish** (rhetorical questions, fragments for drama, irony, metaphors that carry the claim) | Costs an L2 reader a re-read every time; the flourish is never worth it in a security paper |
| **"Simplifying" the domain vocabulary** | An expert reader does not need `vulnerability` renamed; they need the sentence's syntax fixed |
| **Hedging with unfamiliar forms** (`is liable to`, `stands to`) | An L2 reader may miss the hedge entirely and read a stronger claim than intended |
| **Using an idiom as compression** ("the fix fell through the cracks") | The idiom is opaque to most international readers, and the compression hides the agent |

## Resource map

| File | Use |
|---|---|
| `references/venue-profiles.md` | Official criteria per venue, magazine requirements, rules-void matrix |
| `references/venue-prose-corpus.md` | What the top-4 venues reward in prose; corpus protocol to re-measure |
| `references/comprehension-gate.md` | The first-read / shadow / stranger tests, stall taxonomy, worked pairs |
| `references/vocabulary.md` | Transparent vocabulary, idiom and phrasal-verb avoidance, what not to simplify |
| `references/sentence-rules.md` | The 17 sentence rules (L1–L17) with mechanisms and before/after |
| `references/rubric.md` | Five questions, defect codes A1–A16, verdicts, surgery moves |
| `references/diagnosis-playbook.md` | Measurement method, thresholds (incl. L2 blockers), how to report findings |
| `references/magazine-mode.md` | Converting a conference paper into a magazine feature |
| `references/worked-example.md` | A full worked case: measured draft → revised paragraphs |
| `scripts/lint_prose.py` | Sentence-length / passive / nominalisation / dash / L2-blocker counter, `--gate`, `--explain` |
| `templates/revision-table.md` | Per-round record format |
| `CHANGELOG.md` | What changed in v2 and why |
