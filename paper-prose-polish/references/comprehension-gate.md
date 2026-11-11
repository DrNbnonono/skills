# The comprehension gate

The revision rule this file implements:

> **If a reader whose first language is not English cannot get the gist of a sentence on the
> first direct read, the sentence is broken — regardless of whether it is grammatically
> correct, and regardless of how good it sounds to a native ear.**

This is stricter than grammar and different from style. It is the acceptance criterion for
every sentence in the paper.

---

## 1. Why this is the right gate

A native reader can often repair a dense sentence without noticing they did it. They decode
an idiom, infer the missing agent, and move on. A non-native reader who is otherwise a
strong researcher does the same work **once**: if the first pass does not yield the meaning,
they assume the paper is unclear, and trust drops.

The gate therefore optimises for the worst realistic reader in the audience:

- an expert who knows the vocabulary but not the idioms;
- reading fast, in a second language;
- with no patience for a re-read.

This reader is also the senior reviewer at 11 p.m., the PC member on their sixth paper, and
the practitioner the magazine is written for. Passing this gate is not "writing down" to a
weaker audience; it is removing the work that native fluency normally does for free.

Different venue, same gate. The magazine version is simply strict about it.

---

## 2. Three tests

Run all three on the paragraphs that carry the argument (abstract, introduction, results,
discussion). Spot-check the rest.

### 2.1 First-read test (the operational one)

Read the draft once, at normal speed, with no pencil and no going back. Mark a sentence every
time you:

1. **backtrack** — you reach the period and realise you lost the subject;
2. **pause** — you stop on a phrase to decode it (an idiom, a double negative, a noun stack);
3. **paraphrase** — you can only say what it meant after rephrasing it in your head.

Each mark is a **stall**. Stalls are objective: you can count them, and so can a colleague.
Record `stalls / 100 words`. Before/after that number is the comprehension metric.

**Decision rule**

| Stalls per 100 words | Reading |
|---|---|
| 0–1 | camera-ready |
| 2–3 | acceptable only in dense method text; fix the rest |
| ≥4 | the section is not readable; fix before any style pass |

Three stalls in one paragraph → rewrite the paragraph, not the sentences. The problem is
usually ordering, not vocabulary.

### 2.2 Shadow test (density test)

While reading a sentence in English, try to *shadow* it — silently render it into your first
language as you go. This is how you simulate your reader's load.

- Shadowing flows → read it, understood.
- You must stop shadowing to finish the English clause, then go back → the clause is too
  dense. Split it, or move the insertion out.
- You can only shadow a paraphrase, not the sentence → the sentence is carrying two ideas.

The shadow test is a diagnostic. Do **not** use translation as a crutch or write
translated-from-Chinese English; use it to find the clause where the load breaks.

### 2.3 Stranger test (calibration test)

Give one paragraph to someone who knows security but not this subfield — a labmate, a
colleague, or a model prompted to "read as a CEFR B2 reader and restate each claim in one
sentence". If their restatement is wrong, the sentence did not carry its meaning.

Do this on the abstract and the first page only. It catches the errors you can no longer see
because you know what you meant.

---

## 3. Stall taxonomy: what "I can't understand it" actually is

Every stall has a mechanical cause. Diagnose before editing.

| # | Stall | What the reader experiences | Cause | Fix |
|---|---|---|---|---|
| S1 | Subject lost | "What is doing this?" | passive with no agent; subject is a 15-word noun phrase | add `we` or make the actor the subject |
| S2 | Verb late | "Where is the main verb?" | long pre-modifiers or parenthetical before the verb | move insertion to the end; split |
| S3 | Clause stack | "Which clause attaches to which?" | ≥3 subordinate clauses in one sentence | split at the second subordinator |
| S4 | Unknown word | "Is this a technical term or an ordinary word I should know?" | non-transparent word, idiom, phrasal verb, culture reference | replace with a transparent word or delete |
| S5 | Referent unknown | "What does 'this' / 'it' / 'the former' point to?" | bare demonstrative or pronoun with a distant antecedent | name the noun |
| S6 | Double negation | "So … does it or doesn't it?" | `not … unless`, `never … without`, `fail to` + negative | rewrite affirmatively, or split |
| S7 | Nominal stack | "This sentence contains no action." | verb buried in a noun (`the validation of`) | turn the noun back into a verb |
| S8 | Wrong order | "The conclusion arrived before I knew what it was about." | new information in topic position, old information at the end | old → new; claim first, then the evidence |

The linter detects S1–S4 and S7 mechanically (passive, words before verb, subordinators,
idiom list, formal-word list, nominalisation). S5, S6, S8 need a human read — which is what
the gate is for.

---

## 4. Operating thresholds

Use these as a gate for every paragraph that carries a claim. They are directional; see
`diagnosis-playbook.md` for how to report them.

| Measure | Threshold | Why |
|---|---|---|
| Words before the main verb | ≤ 10 | The reader cannot hold a subject longer than that without the verb |
| Subordinate clauses per sentence | ≤ 2 | Three clauses is where backtracking starts |
| Parenthetical insertions per sentence | ≤ 1 | Each one suspends the main clause |
| Non-technical unknown words per sentence | 0 | The reader should never meet an ordinary word that is not transparent |
| Idioms / phrasal verbs per *argument* sentence | 0 | Allowed in incidental prose at most |
| Stalls per 100 words | ≤ 1 (camera-ready), ≤ 3 (draft) | Aggregate first-read measure |
| Sentences needing a second read, per paragraph | ≤ 1 | Above that, rewrite the paragraph |

---

## 5. Worked pairs (L2 lens)

Read each "before" as the reader model would. The stall is stated, then the fix.

### 5.1 Idiom carrying the claim (S4)

> **Before:** "The advisory claims a fix, but the remaining paths fall through the cracks."
> *Stall: "fall through the cracks" is opaque; worse, it hides who failed to check.*

> **After:** "The advisory claims a fix, but four paths are still exploitable, and no advisory mentions them."

### 5.2 Phrasal verb where a transparent verb exists (S4)

> **Before:** "We looked into whether the patch holds up across versions and came up with a different picture."
> *Stall: two phrasal verbs in one sentence; "holds up" and "came up with" must be decoded.*

> **After:** "We tested the patch across versions. It holds for two chains but not for the other three."

("holds" is transparent; "holds up" is not.)

### 5.3 Nominal stack (S7)

> **Before:** "Implementation of the validation of the completeness of the advisory was performed."
> *Stall: four nouns, one empty verb; the reader cannot tell who did what.*

> **After:** "We validated how complete each advisory was."

### 5.4 Verb late / subject long (S2, S3)

> **Before:** "The fact that a given advisory, once re-published by downstream aggregators and distribution trackers, still names the same affected-version range, means that…"
> *Stall: the main verb is at word 30; the reader has lost the subject.*

> **After:** "Downstream aggregators re-publish the advisory and keep the same version range. So the range survives even when the advice behind it does not."

### 5.5 Referent unknown (S5)

> **Before:** "This is not a documentation defect; it reflects the format's assumption."
> *Stall: "this" could be the gap, the omission, or the previous claim.*

> **After:** "The under-description is not a documentation defect. It reflects an assumption built into the format."

### 5.6 Double negation (S6)

> **Before:** "None of the advisories that we coded fails to omit at least one path."
> *Stall: the reader must compute two negatives to get one positive fact.*

> **After:** "Every advisory we coded leaves out at least one path."

### 5.7 Native flourish (S4, S8)

> **Before:** "Advisories are a hall of mirrors: what you see is rarely the vulnerability that is there."
> *Stall: the metaphor carries the claim; the reader must first decode the image.*

> **After:** "Advisories describe a smaller vulnerability than the one that exists."

### 5.8 Hedge in an unfamiliar form (S4)

> **Before:** "The trend stands to reflect AI-assisted discovery."
> *Stall: an L2 reader may read "stands to reflect" as a firm claim, or not parse it at all.*

> **After:** "The trend may reflect AI-assisted discovery."

---

## 6. What the gate does **not** mean

- **Not "shorter is always better".** A 30-word sentence with one clause can pass; a 15-word
  sentence with three nominalisations can fail. Split or simplify; do not amputate.
- **Not "remove technical terms".** `deserialization` is transparent to the audience. The
  gate applies to syntax and to ordinary vocabulary.
- **Not "no advanced words".** `mitigation`, `prevalence`, `coordinate` are internationally
  transparent. `notwithstanding`, `aforementioned`, `whilst` are not.
- **Not "write like a textbook".** A precise, direct technical voice passes easily. Dumbing
  down is a different failure, and a worse one.

---

## 7. Recording the result

Add these two lines to every revision round:

```
First-read gate: <n> stalls / <m> words = <x> per 100 words   (before → after)
Sentences requiring a second read: <k> of <n>   (paragraph-level rewrites: <p>)
```

Keep the marked-up read in the round's folder (`stalls-<date>.md`, one line per stall with
sentence number and stall code). It is the evidence that the revision was a comprehension
fix, not a vocabulary preference.
