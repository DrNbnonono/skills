# Sentence rules L1–L17

Each rule: **rule → mechanism (why the reader stalls) → before → after**.
Examples are drawn from security manuscripts; the defect is what generalises, not the topic.

---

## L1 One action per sentence

One agent–action–result per full stop. A second action gets its own sentence, unless it is
the same agent's next step with no interruption.

**Mechanism.** English readers "settle the account" at the period. Every extra coordinated
verb is an unsettled semantic slot; past two, they re-read.

**Before**
> Starting from the five chains in Fig. 1, we enumerate every version and interface
> combination whose preconditions are satisfiable (e.g., chain D requires a cache and so is
> undefined for versions predating it; chain E requires a multi-worker server), yielding 29
> valid configurations.

**After**
> We start from the five chains in Fig. 1 and ask which (version, interface) pairs satisfy
> each chain's preconditions. Chain D needs a cache, so it does not apply to versions that
> predate it. Chain E needs a multi-worker server. This enumeration yields 29 valid
> configurations.

---

## L2 Let the subject be able to act

Subjects should be people, teams, systems, or concrete objects — not abstractions.

**Mechanism.** When the subject is `the comparison`, `this concentration`, or `recall`, the
verb collapses to `shows / suggests / reflects`, which carries no information.

**Before**
> The family-level coding lens requires a judgment call about what a "reasonably careful
> reader" would infer from an advisory's text.

**After**
> When we apply the family-level lens, we have to decide what a "reasonably careful reader"
> would infer from an advisory's text.

---

## L3 Do not let nouns steal the verb

`the validation of X` → `we validate X`; `the comparison of A and B` → `we compare A with B`;
`the concentration of gaps in one claim` → `gaps concentrate in one claim`.

**Mechanism.** Nominalisation freezes the action into a noun, leaving only "a relation
exists". Writers whose first language nominalises heavily (Chinese among them) over-produce it.

**Before**
> The defect is not specific to one advisory; it is a pattern that reproduces itself whenever
> a vulnerability's boundary is multi-dimensional.

**After**
> The defect is not specific to one advisory. It recurs whenever a vulnerability's boundary is
> multi-dimensional.

---

## L4 Known information first, new information last

Put what the reader already knows at the start; put the sentence's new claim at the end
(Gopen & Swan).

**Mechanism.** English stress falls on the final position. A conclusion buried in a
`rather than` clause, with an abstract noun string at the end, is read as an aside.

**Before** (48 words; the conclusion sits inside `rather than …`)
> Both lines of work share a methodological ceiling: they compare documents against each
> other---…---rather than independently verifying what either document claims against the
> vulnerability's actual, dynamically confirmed exploitability.

**After**
> Both lines of work run into the same limit: they compare one document with another. Does
> this advisory agree with that commit log? Neither asks whether the claim is true, because
> answering that takes dynamic testing — and neither study does any.

---

## L5 Keep subject and verb close

No more than ~5 words between subject and verb. Move longer material to the end or split.

**Before** (subject spans 15 words; the verb `was combined` arrives at word 21, passive)
> To assess the accuracy of disclosure information, dynamic validation of the vulnerability
> family in PHP's subsystem was combined with a cross-era analysis.

**After**
> We test the family end to end, and we pair those tests with a cross-era analysis.

---

## L6 Twenty-five words is the line; thirty-five must be split

Average 20–25 words per sentence. A sentence over 35 words needs a reason (a three-item
list); over 45, split it.

**Why**: a two-column 10 pt line holds 12–14 words. Three lines without a full stop
forces the eye to jump back.

---

## L7 Passive voice: three legitimate uses

Keep the passive only when (a) the agent is unknown or irrelevant, (b) the patient must be
emphasised, (c) naming an agent would be an accusation. Otherwise make it active. VUSEC's
formulation: "Avoid the passive form!"

**Mechanism.** The passive moves the agent out of the stress position and often deletes it.
In method sections a deleted agent means the work cannot be reproduced.

**Before**
> After independent coding and an adjudication pass, inter-rater agreement was X under one
> lens and higher under the other, where disagreements were rarer simply because almost
> nothing qualified.

**After**
> Two coders labeled every item independently, then resolved disagreements in an adjudication
> pass. Agreement was κ = X under the family lens. Under the literal lens it was higher
> (κ = Y), but only because so few items qualified that the coders rarely disagreed.

---

## L8 One `which` clause, adjacent to its antecedent

`, which` is a gloss; the reader attaches it to the nearest noun. For cause and effect use
`because / so / therefore / this is why`.

**Before**
> … one specific claim---"version v is patched"---is disproportionately where advisories
> overstate what is fixed, which directly motivates the patch analysis below.

**After**
> … one claim does most of the damage: "version v is patched". That is where advisories most
> often overstate the fix, so §3.3 measures patch completeness directly.

---

## L9 `This` needs a noun

Bare `This` forces the reader to look back. Write `This gap / This pattern / This result`.

**Before**: `This concentration is itself informative …`
**After**: `The concentration matters. Advisories are not uniformly vague; they fail at one claim.`

---

## L10 Dashes and parentheses hold examples, not arguments

Keep examples, data, and glosses inside dashes. Cause, contrast, and qualification belong in
the main clause. One dash per paragraph at most.

**Mechanism.** A dash signals "lower priority": native readers skim it.

**Before**
> Advisories under-describe the surface the patch was scoped against---and that is why the
> patch is under-scoped---so defenders stay exposed.

**After**
> Advisories under-describe the attack surface. The patch was scoped against those
> descriptions, so it is under-scoped too, and defenders stay exposed.

---

## L11 Numbers need an actor, a denominator, and a comparison

**Before**
> Of 123 coded gaps, 68% involved versions declared patched despite remaining exploitable.

**After**
> We coded 123 gaps between what an advisory claims and what our tests show. In 68% of them,
> the advisory calls a version patched while our tests still exploit that version.

---

## L12 One definition per term, one spelling per term

Define at first use; use the same word forever; expand every abbreviation at first use.

**Why it matters**: term drift (`family lens` / `family-level lens` / `family-level criterion`)
is read as carelessness and cannot be fixed at the sentence level later.

---

## L13 (Magazine and practitioner venues) One concrete thing every 800–1,000 words

A version number, a server, a repository name, a failed run. Purely abstract argument loses
a practitioner audience.

---

## L14 The first-read gate: if it needs a second read, it failed

**Rule.** Read the sentence once at normal speed as the reader model in `SKILL.md`. Any stall
(backtracking, decoding a phrase, translating a clause to get the meaning) is a defect, even
if the grammar is perfect. Fix the sentence; do not blame the reader.

**Mechanism.** A native reader silently repairs dense prose; an L2 reader does not repair it,
they stop. The stall is the measurement.

**Before**
> The extent to which advisories capture the family-level attack surface is, notwithstanding
> recent improvements in downstream aggregation, still limited.

**After**
> Advisories still miss much of the family-level attack surface, even after recent
> improvements in downstream aggregation.

**Gate numbers** (see `comprehension-gate.md`): ≤10 words before the main verb, ≤2 subordinate
clauses, ≤1 parenthesis, 0 idioms in a claim-bearing sentence.

---

## L15 No idioms or phrasal verbs where the claim lives

**Rule.** In the abstract, the contribution list, any finding, and any limitation, use words
that are transparent from the word itself. Replace idioms and phrasal verbs with a plain verb
or a direct statement. One idiom in incidental prose is tolerable; none in a claim.

**Mechanism.** For an L2 reader, "simple Anglo-Saxon" and "transparent" are not the same:
`hold up` is short and opaque; `remains exploitable` is longer and transparent.

**Before**
> The patch holds up for two chains, but the rest fall through the cracks.

**After**
> The patch works for two chains. The other three remain exploitable, and no advisory says so.

---

## L16 A pronoun must have one obvious antecedent

**Rule.** `this`, `it`, `they`, `the former`, `the latter` may only refer to the nearest
noun — and only when that noun is the one you mean. When the referent is a whole clause or a
list, name it: `this gap`, `the under-description`, `the ratio`.

**Mechanism.** The reader resolves pronouns from the last noun phrase. If the sentence's real
referent is an earlier sentence, the reader attaches the pronoun to the wrong noun and
misreads the claim.

**Before**
> Aggregators re-publish the advisory and keep its version range. This is why defenders stay
> exposed even after they follow it.

**After**
> Aggregators re-publish the advisory and keep its version range. That unchanged range is why
> a defender can follow the advisory and stay exposed.

---

## L17 One new concept per sentence

**Rule.** A sentence may introduce at most one new technical term. Two new terms in one
sentence is a rewrite: define the first in its own sentence, then use it.

**Mechanism.** An L2 reader's working memory is already taxed by reading in a second
language. Two new terms in one sentence forces a re-read even when each term is defined
somewhere else in the paper.

**Before**
> We model each exploit chain as a configuration unit over the SAPI and version axes, and
> score advisory recall against its closure.

**After**
> We model each exploit chain as a *configuration unit*: one PHP version on one SAPI. We then
> score an advisory's *recall* as the fraction of units it covers.

---

## L18 Affirm first; negate only against a named alternative

State the claim positively. Use a negation to contrast with **a specific, named alternative**
("unlike Project Zero's estimate, which ..."; "the patch does not cover chain E"), and keep at
most one negator per sentence.

**Mechanism.** A negated statement costs two steps: the reader builds the positive proposition,
then inverts it (the comprehension gate calls this stall S6). Two negators cost three. Worse,
negation about one's own framing ("we do not assume ...", "that is not a premise") reads as
*defensive*: the reviewer infers the author is pre-empting an objection instead of reporting a
result.

**Measured norm** (same counter, see `diagnosis-playbook.md` section 3.2):

| Metric | 16 top-tier papers | IEEE S&P Magazine issue | A non-native draft |
|---|---|---|---|
| Negators per 1,000 words | 4.6 (range 2.6-7.1) | 4.6 | **9.7** |
| Sentences with >=2 negators | 0.8% | 0.8% | **5.7%** |
| Contrast markers per 1,000 | 0.66 | 0.50 | **3.7** |
| "we do not / we cannot" per 1,000 | 0.14 | 0.00 | **0.90** |

Negation is not rare in top-tier prose: roughly one negator per 220 words is normal. What is
rare is **stacked** negation and **self-directed** negation. The fix is not to purge negation
but to stop paying for it when the positive form says the same thing.

**Before** (four sentences, two of them about what is *not* claimed):

> We deliberately do not assume that these trends make advisories less accurate or exploitation
> faster. That is an empirical question, not a premise. Our premise is narrower. If the pace of
> discovery and exploit-artifact dissemination changes, it is an open question whether vendor
> advisories, downstream advisories, and the remediation itself can keep pace.

**After** (one negator left, the positive claim promoted to the front):

> The premise is narrower: as discovery and exploit-artifact dissemination accelerate,
> advisories and remediation may fail to keep pace. Whether AI is what accelerates them is an
> empirical question, and RQ2 measures the trend descriptively.

**Three shapes to delete on sight**

1. **Meta-negation** - a sentence whose content is the status of the author's own claim:
   "that is an empirical question, not a premise", "we do not claim X", "this is not to say Y".
   Move the caveat into a subordinate clause, or delete it and let the limitations section carry it.
2. **Payload in the negative slot** - an "X, not Y" appositive where the reader needs X but is
   handed the contrast first ("a large attack surface, not an edge case"). Say X; drop Y.
3. **Double negation** - "not uncommon", "not unlikely", "not without risk", "cannot be ruled
   out". Replace with the positive adjective: "common", "likely", "risky", "possible".

**Where negation earns its place**: contrasting a named prior system; a genuine impossibility
that bounds a claim; a limitation the author is obliged to state. In those three cases keep it,
and make the alternative explicit.

---

## L19 Quantifiers point backwards; summaries name objects

`both`, `the two`, `the second`, `these three` presuppose that the reader has already stored the
set. Introduce the pair **before** the quantifier, never after it.

**Mechanism.** A forward-announcing quantifier makes the reader hold an empty slot while the
sentence fills it; if what arrives is two abstract labels rather than two objects, the slot never
resolves. The comprehension gate records this as a pause (S2) that no amount of re-reading fixes.

**Before**

> We measure both: accuracy and pace.

**After** (name the objects, drop the quantifier)

> We check the documents against dynamic exploitation, and we time the ecosystem's response
> against public artifacts.

**Or after** (keep the pair in front of the quantifier)

> Two measurements follow: how accurately the documents describe what is exploitable, and how
> fast the ecosystem responds. Both use the same disclosure timeline.

**Corpus note.** Published prose uses `both X and Y` at 0.45-0.56 per 1,000 words, and in a full
magazine issue every `both` points backwards to a pair the reader has already met; the
forward-announcing `both:` form appears zero times. Do **not** treat signposting itself as a
defect - meta-discourse runs at 0.77 per 1,000 words in top-tier papers, which is where the draft
sits. The defect is the unanchored quantifier and the label noun, not the act of signposting.
See `ai-artifacts.md` section 2 for the null result.

A closing sentence that restates the section's labels adds no information. Either replace the
labels with the objects the instrument produced, or delete the sentence and let the next
section's list carry the load.

---

## L20 The claim carries its own caveat

Do not spend a sentence on the paper's own epistemic status. Fold the caveat into the claim it
qualifies, or move it to the limitations section.

**Before** (two sentences, one claim, zero information about the world)

> We treat AI's role in that acceleration as an empirical question. That is an empirical question,
> not a premise.

**After** (the caveat rides inside the claim)

> The question is whether advisories and the fixes they describe can stay accurate and keep pace
> once discovery accelerates, whatever role AI plays in that acceleration.

**Measured.** Sentences whose subject is the paper's epistemic status ("That is an empirical
question, not a premise"; "we treat X as an empirical question") occur **0 times in 64,889
sentences** of 120 top-tier papers and **0 times** in a magazine issue; the draft had one. The
legitimate look-alike is `X remains an open question whether ...`, where the subject is the
phenomenon and the sentence belongs in limitations or future work - that form is common and
should be left alone.

See `local-artifacts.md` section 4.2 for the corpus and the precision audit.

---

## Paragraph-level companions

- First sentence = the paragraph's claim, not its background.
- One claim per paragraph; if you write `First … Second …`, you have two paragraphs.
- Final sentence answers "so what".
- The introduction must not duplicate the related-work section: numbers and case details
  belong in one of them, not both.
- Repeating the research question verbatim at the start of sections 3, 4, 5 reads as filler.
