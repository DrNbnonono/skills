---
name: paper-prose-polish
description: Polish English academic prose for security/systems venues (S&P, USENIX Security, CCS, NDSS, journals, IEEE S&P Magazine), written for readers whose first language is not English. Use for 润色/改写/逐句修改论文表述, diagnosing why a paragraph is unreadable, converting a conference paper into a magazine feature, or a clarity review before submission. Core rule: if a competent non-native reader cannot follow a sentence on the first pass, the sentence is broken. Measures the draft first, then revises sentence by sentence with a defect code and a stated reader-stall reason for every change.
version: 2.6.1
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
10. **Do not manufacture edits.** If the original sentence or paragraph already does its job,
    it is KEEP, and KEEP means leave the words alone. The skill is a reader-stall detector,
    not a quota of changes: a round with three real fixes in ten pages is a successful round,
    and a paragraph that already reads well is evidence the draft is working — not a target.
    Rewriting a good sentence to look productive trades the author's voice for nothing and
    adds a chance to introduce meaning drift.

11. **Never win a metric by breaking the prose.** The metrics are targets; coherence between
    sentences is a constraint with veto power. If a change improves a number and breaks a
    referent, a causal link, or the topic chain, revert the change and record the missed metric
    with its reason (`references/coherence.md`). A gate that FAILS with a recorded reason is a
    decision; a gate that PASSES over a broken seam is a defect. This rule outranks every
    threshold in this file.

**A good draft is a valid finding.** State it and stop. Do not open a paragraph, find nothing
wrong, and invent a stylistic suggestion so the round looks thorough; "this section needs no
change" belongs in the report next to the changes. The green path is: measure, read, report
KEEP, done.

## Rewrite authority

Fidelity is owed to the **claim**, not to the sentence that currently carries it. Three tiers:

**Tier 1 - rebuild silently, then report.** Delete, merge, split, or reorder inside a paragraph
when the sentence is filler, a duplicate, a dangling quantifier, or a label summary. No
discussion needed; record the change and state what was removed and why nothing is lost.

**Tier 2 - replace the sentence.** Substitute a different sentence carrying the same claim. State
the old wording, the new wording, and confirm the claim is unchanged.

**Tier 3 - restructure, but discuss first.** Moving, merging, or reordering paragraphs; changing
what a section argues; deleting a claim. Ask, because this changes the shape of the argument and
the author may have a reason the text does not show.

Never silent, at any tier: numbers, the strength of a claim, a technical term's meaning, or the
removal of a citation or a fact. Those default to Tier 3.

## Coherence is a constraint; the metrics are an objective

The linter measures sentences one at a time. It cannot see whether the paragraph still reads as
one argument, so a revision can win every gate and produce prose that is shorter, flatter, and
harder to follow. Treat the two goals differently:

| Rank | Goal | Can it be traded? |
|---|---|---|
| 1 | **Claim fidelity** — numbers, strength, term meanings, citations | Never |
| 2 | **Coherence** — the reader can follow one sentence to the next | Only by the author |
| 3 | **Metrics** — length, passive, nominalisation, negation vs the venue corpus | Yes: they are targets, not rules |

So when hitting a threshold would cost cohesion, **miss the threshold and record why**:

```
Missed metric: p90 34 (target <=32)
Reason: the 46-word unit is a claim plus its scope ("... but only where opcache is enabled").
A split would detach the restriction and invite over-reading.
Alternative taken: trimmed 6 words elsewhere in the paragraph; seam preserved.
```

Three mechanisms, all testable at the seam between two sentences: **reference** (does every
pronoun still have one antecedent?), **logic** (did the `because / so / although` survive the
split?), **topic** (does sentence 2 start from where sentence 1 ended?). Read
`references/coherence.md` before your first SPLIT of the round; it also defines the legal and
illegal split points, and **MERGE**, the move that undoes an over-chopped paragraph.

---

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
sentences over 45 words, passive rate, nominalisation density, dash count, negation density
(negators per 1,000 words and the share of sentences with two or more), and the share of
sentences whose subject is an agent.

Since v2 the linter also measures the four **L2 blockers**: words before the main verb,
subordinate clauses per sentence, idioms/phrasal verbs, and non-transparent formal words.
Since v2.5 it also reports **flow** diagnostics — paragraph size, sentence-length variety, runs
of short sentences, repeated openers, connective density. Those are warnings, not a gate: they
describe the reading experience, which no per-sentence counter can.

```bash
python scripts/lint_prose.py --path <paper-dir> --glob "*.tex" --gate --venue magazine --flow
```

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
2. **Assign defect codes** A1–A21 (A13–A16 are the L2 codes; A20–A21 are the seam and rhythm
   codes added in v2.5).
3. **Assign a verdict**: KEEP / TRIM / SPLIT / MERGE / RECAST / REWRITE / DELETE.
4. **Before recording a SPLIT, name the seam and run the R/L/T tests** in
   `references/coherence.md` §3. If the split would detach a restriction from its claim, orphan
   a pronoun, or drop a connector, use TRIM or RECAST instead.
5. **Apply a surgery move**, not a paraphrase.
6. **Record** the change with the reason ("the reader stalls at X"), never "smoother".

Use `templates/revision-table.md`. A change without a stated reader-stall reason is
unjustified.

## Step 4 — Paragraph and structure pass

Only after sentences: check topic sentences, one claim per paragraph, duplicated content
between the introduction and related work, and whether the first page answers "what does
this paper do". Read `references/magazine-mode.md` when the target is a magazine — it
covers the restructure (display-item budget, sidebar instead of appendix, scene opening).

For each paragraph, also check the L2 reader's load: does the paragraph introduce one new
term, or three? Does the first sentence name the claim, or start with background?

## Step 4.5 — Placement review

After the sentences, read the paper for **where things sit**, not how they read. Use
`references/structure-and-placement.md`:

1. Compare the layout against measured conventions (120 papers): related work before design in
   75%, a dedicated limitations section in 13%, a roadmap sentence in 17.5%.
2. Flag paragraphs whose size is in the top decile (corpus p90: 97 words, 4 sentences).
3. Flag content that a reader needs earlier than it appears, and content that repeats a passage
   from another section.
4. **Raise every placement change as a question, never apply it silently.** State the convention,
   the cost, and two options; the author decides. Placement is Tier 3 in "Rewrite authority".

## Step 4.6 — Display-item order

Floats are read, not just counted. Before submission, check the reading order of every figure and
table against `references/floats-and-references.md`:

1. Every float is cited at least once in the body; an unreferenced float is a defect, not a
   stylistic choice.
2. The first citation precedes the float in the **source**, because LaTeX queues floats
   first-in, first-out; a float declared earlier can appear before the reader is introduced to it.
3. The citing sentence names what to look at (panel, column, axis), and a sentence after the float
   interprets it rather than restating the caption.
4. The caption stands alone: one sentence with the takeaway.
5. Default placement spec is `[t]`; `[!ht]` can reorder floats, `[H]` can break IEEEtran columns.
6. Check the **compiled PDF**, not the source: source order cannot tell you where a float landed.

## Step 5 — Verify

- **Coherence first.** Run the paragraph gate in `references/coherence.md` §6: seam tests
  (R/L/T) on every adjacent pair, short-run count, opening variety, glue density,
  topic sentence intact. If a metric was won by breaking a seam, revert the split.
- Re-run the linter with `--compare baseline.json --flow`; compare against the threshold table in
  `references/diagnosis-playbook.md`.
- Re-run the first-read gate; report stalls per 100 words before/after.
- Thresholds are directional, not targets to game: if a sentence loses information to hit
  a number, the edit is wrong. If coherence loses to a number, the same rule applies.
- Read the revised paragraph aloud once. A sentence the reviser cannot finish in one breath
  is still too long.
- Back-check: every number, `\cite`, `\ref`, and technical term unchanged.

## Deliverables per round

1. A revision table (position, original, code, verdict, rewrite, reader-stall reason,
   first-read status, seam check R/L/T).
2. The applied source change, with a backup of the previous file.
3. The before/after measurement table, including the L2 blockers.
4. The flow report (`--flow`) before and after, with any **missed metric and its reason**.
5. Two or three "so next time" rules tied to the author's recurring habits.

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
| **Negation-first framing** ("we do not assume ...", "that is not a premise") | Reads as defensive and costs the reader an extra inversion; top-tier papers spend far fewer sentences on what they do not claim (L18) |
| **"Simplifying" the domain vocabulary** | An expert reader does not need `vulnerability` renamed; they need the sentence's syntax fixed |
| **Hedging with unfamiliar forms** (`is liable to`, `stands to`) | An L2 reader may miss the hedge entirely and read a stronger claim than intended |
| **Using an idiom as compression** ("the fix fell through the cracks") | The idiom is opaque to most international readers, and the compression hides the agent |
| **Metric gaming by chopping** — splitting every long sentence until the mean passes | Wins the table, loses the paragraph: the ties between sentences are severed and the prose reads as bullet points (A20–A21, `coherence.md`) |
| **The orphan split** — a split that leaves `this` / `it` with no antecedent in its own sentence | The reader must reconstruct the referent across a sentence boundary, which is exactly the stall the skill exists to remove |
| **Splitting a claim from its restriction** ("…, but only for PHP 7.4") | Turns a bounded claim into an unbounded one; a reviewer reads over-claiming |
| **Sentence salad** — a paragraph of eight 12-word sentences | Each sentence is "clear"; together they read as a list. Merge back (MERGE verdict) |
| **Connective glue** — `However / Therefore / Thus` in more than ~18 % of sentences | The logic is asserted instead of carried by the order; readers skim scaffolding |
| **Nitpicking a good sentence** — rewriting prose that already passes the gates | Every unnecessary edit is a chance to introduce meaning drift; KEEP is ~40 % of a normal round by design, and three real fixes beat forty cosmetic ones |

## Resource map

| File | Use |
|---|---|
| `references/venue-profiles.md` | Official criteria per venue, magazine requirements, rules-void matrix |
| `references/venue-prose-corpus.md` | What the top-4 venues reward in prose; corpus protocol to re-measure |
| `references/comprehension-gate.md` | The first-read / shadow / stranger tests, stall taxonomy, worked pairs |
| `references/coherence.md` | Precedence (claim > coherence > metrics), the three seams, legal/illegal splits, MERGE, the paragraph gate |
| `references/vocabulary.md` | Transparent vocabulary, idiom and phrasal-verb avoidance, what not to simplify |
| `references/sentence-rules.md` | The 23 sentence rules (L1–L23) with mechanisms and before/after |
| `references/rubric.md` | Five questions, defect codes A1–A21, six verdicts, eight surgery moves |
| `references/diagnosis-playbook.md` | Measurement method, thresholds (incl. L2 blockers), how to report findings |
| `references/magazine-mode.md` | Converting a conference paper into a magazine feature |
| `references/local-artifacts.md` | Annotation study over 120 papers: five local artifacts, per-sentence rates, precision audit, and three null results |
| `references/floats-and-references.md` | Reading order of figures and tables: citation-before-appearance, LaTeX float mechanics, caption rules, and a submission checklist |
| `references/structure-and-placement.md` | Measured layout conventions, a placement checklist, and the protocol for raising a move as a question |
| `references/l2-grammar.md` | Article / agreement / tense detectors: what was measured, and the three that failed |
| `references/ai-artifacts.md` | What generated prose gets wrong, split into measured artifacts and local-only ones, with null results kept |
| `references/worked-example.md` | A full worked case: measured draft → revised paragraphs |
| `scripts/lint_prose.py` | Sentence-length / passive / nominalisation / dash / negation / L2-blocker counter, `--gate`, `--explain`, `--flow` (rhythm and seam warnings) |
| `templates/revision-table.md` | Per-round record format |
| `CHANGELOG.md` | What changed in v2 and why |
