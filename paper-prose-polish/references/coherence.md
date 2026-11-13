# Coherence: the constraint the metrics cannot see

The skill's sentence pass optimises length, passive rate, nominalisations, negation. Every one
of those is a *local* counter. None of them can see whether the paragraph still reads as one
argument. A revision can win every gate and leave prose that is shorter, flatter, and harder
to follow — the "sentence salad" failure.

This file is the missing constraint: **a change that breaks a cohesive tie is wrong, even if
it improves a metric.** The linter's output is a target; cohesion is a constraint with veto
power.

---

## 1. Precedence

When the three goals conflict, they resolve in this order:

| Rank | Goal | What it protects | Can it be traded? |
|---|---|---|---|
| 1 | **Claim fidelity** | Numbers, strength, technical meaning, citations | Never |
| 2 | **Coherence** | The reader's ability to follow one sentence to the next | Only by the author |
| 3 | **Metrics** | Length, passive, nominalisation, negation vs the venue corpus | Yes — they are targets, not rules |

So: if the only way to reach p90 ≤ 32 is a split that severs a claim from its scope
("…but only for PHP 7.4"), **miss the metric and record why**. The reading experience outranks
the distribution.

**Recording a missed metric** (add to the revision table):

```
Missed metric: p90 34 (target <=32)
Reason: the 46-word unit is a claim + its scope ("... but only where opcache is enabled").
Splitting would detach the restriction from the claim and invite the reader to over-read it.
Alternative taken: trimmed 6 words elsewhere in the paragraph; seam preserved.
```

---

## 2. What coherence is, mechanically

Three well-established mechanisms, all testable at the seam between sentences:

**Cohesive ties** (Halliday & Hasan, *Cohesion in English*, 1976). Five ties carry meaning
across a sentence boundary:

| Tie | Example | Breaks when |
|---|---|---|
| Reference | "the advisory … **it** lists" | the antecedent is in a sentence that was moved or split away |
| Substitution / ellipsis | "three paths … **the other two** fail" | the count is split so "the other two" loses its base |
| Conjunction | "**because** the patch is narrow" | the split drops the connector and leaves a bare assertion |
| Lexical cohesion | "recall … **coverage**" | the rewrite swaps one term for a near-synonym mid-chain |
| Collocation | "coordinated release … **embargo**" | the rewrite deletes the word the next sentence leans on |

**Given–new** (Gopen & Swan, "The Science of Scientific Writing", 1990). The topic position
(sentence start) should carry *given* information; the stress position (sentence end) carries
the *new* claim. A good seam repeats the previous sentence's stress as the next sentence's
topic. A split can invert this: the new sentence opens with information the reader has not
been given yet.

**Parallelism** (Williams, *Style*). Coordinate structures are read as a set. Splitting a
"both X and Y" or "not only X but also Y" construction destroys the set and leaves one member
looking like an afterthought.

---

## 3. The three seam tests (run on every SPLIT and MERGE)

A **seam** is the joint between two information units. Before splitting, name the seam. After
splitting, test it.

### 3.1 Reference seam — does every pronoun still have one antecedent?

- Read sentence 2 alone. Does `this`, `it`, `they`, `that` have a noun in its own sentence?
- If not, either name the noun (L16) or merge back.

> **Broken:** "We coded 123 gaps. This is where advisories overstate the fix."
> `This` now has no noun in its sentence; the reader must reconstruct from the previous one.
> **Repaired:** "We coded 123 gaps. The largest share of them is one claim: a version called
> patched that still exploits."

### 3.2 Logical seam — did the connector survive?

- If the original sentence carried `because / so / although / unless / while`, that relation was
  inside the sentence. After the split, it must be visible at the start of the new sentence or
  in the order of the two.
- A bare assertion after a cause is read as a second, independent claim.

> **Broken:** "The patch is scoped against the advisory text. Four paths remain exploitable."
> (reads as two unrelated facts)
> **Repaired:** "The patch is scoped against the advisory text. As a result, four paths remain
> exploitable."

### 3.3 Topic seam — does sentence 2 start from what sentence 1 ended with?

- Underline the last three words of sentence 1 and the first three of sentence 2.
- If sentence 2 starts with brand-new information, insert a bridge or merge.

> **Broken:** "Advisories under-describe the surface. The patch is under-scoped too."
> (the second topic "the patch" is new)
> **Repaired:** "Advisories under-describe the surface. Scoped against those descriptions, the
> patch is under-scoped too."

Three tests, ~10 seconds per seam. A split that passes all three is a good split.

---

## 4. Where you may split, and where you may not

| Legal seam | Example | Why it is safe |
|---|---|---|
| After the main clause, before a trailing example | "We coded 123 gaps. For example, 84 are patched-exclusion." | The example is an addition, not a restriction |
| Between two independent claims of the same agent | "We collected twelve advisories. We then coded each one twice." | Same subject; the order carries the logic |
| Before evidence that supports the previous claim | "Recall is near zero. No advisory names the SAPI." | The second sentence is the evidence for the first |
| After a definition, before its application | "A unit is one chain on one version. We scored 29 such units." | Definition and use are separate units |

| Illegal seam (do not split here) | Why | Do instead |
|---|---|---|
| Between a claim and its scope restriction | "…, but only for PHP 7.4" | keep together; trim elsewhere |
| Inside a paired construction | "both X and Y", "not only X but also Y", "from X to Y" | keep the pair in one sentence |
| Between a subject and its verb | the verb arrives too late | move the insertion to the end |
| Inside a definition (term : meaning) | the reader loses the term | split before the term |
| Between a cause and its effect that share one agent | the causal link disappears | keep, or start sentence 2 with "As a result" |
| In a list whose items share one verb | the list fragments into stubs | keep as a list (L1 exemption) |

---

## 5. MERGE is a legal move

The obsessive splitter's failure mode is a paragraph of eight 12-word sentences. The repair is
not "trim more"; it is **merge**. Merge when:

- two adjacent sentences share the same subject and the second only adds a qualifier;
- a sentence ends with a noun phrase that the next sentence repeats as its subject
  ("The patch is narrow. The narrow patch leaves four paths." → "Because the patch is narrow,
  it leaves four paths.");
- a one-line sentence carries a claim that belongs to the previous sentence's evidence.

MERGE is a verdict in `rubric.md` since v2.5 for this reason.

---

## 6. The coherence gate (per paragraph, ~60 seconds)

Do this **after** the sentence pass and **before** the metric re-check.

1. **Read the paragraph aloud.** Every place you take a breath that the punctuation does not
   predict is a rhythm problem.
2. **Run the three seam tests** on every adjacent sentence pair. Mark R / L / T failures.
3. **Count short runs.** Three or more consecutive sentences under 12 words: merge one back or
   lengthen one. The linter reports this (`--flow`, `chop`).
4. **Check the openings.** If more than ~12 % of adjacent pairs start with the same word, the
   paragraph is mechanical (`--flow`, `rep%`). Vary the subject or merge.
5. **Check the glue.** If more than ~18 % of sentences open with *However / Therefore / Thus*,
   the text is over-glued: let order carry the logic instead.
6. **Check the topic sentence.** The paragraph's first sentence must name its claim; the last
   must answer "so what". If the split moved either, fix it.

Warnings, not gates: a 2,000-word appendix may legitimately run 20 % connectives. The numbers
locate the paragraph; you decide.

---

## 7. Worked pairs

### 7.1 The split that wins the metric and breaks the claim

**Before (38 words):** "The official patch seals four of the nine known paths, but only where
the deployment disables `session.upload_progress`, which most shared hosts do not do."

- Split A: "The official patch seals four of the nine known paths." + "Most shared hosts do not
  disable `session.upload_progress`."
- Metrics: better. Coherence: **broken** — the restriction ("only where…") has become a
  separate fact, and the reader now over-reads the first sentence.
- **Verdict: reject Split A. TRIM instead:**
  "The official patch seals four of the nine known paths, and only where the deployment
  disables `session.upload_progress` — which most shared hosts do not do." (34 words; seam intact)

### 7.2 The split that orphans a pronoun

**Before:** "Twelve advisories describe the family, and none of them names all five chains."

- Split A: "Twelve advisories describe the family. None of them names all five chains."
- "them" is fine (twelve advisories is given). Split B would break it:
  "Twelve advisories exist. None of them names…" — the antecedent moved into the kind of
  sentence that does not license "them" as given.
- **Rule:** if sentence 2 starts with a pronoun, the noun must be in sentence 2 or be the
  subject of sentence 1.

### 7.3 The merge that restores the given–new chain

**Before (choppy):** "The patch is narrow. It covers four paths. Four of nine is 44 %."

**After:** "The patch is narrow: it covers four of the nine known paths, or 44 %."

One sentence, one claim, the number lands at the end (stress position).

### 7.4 The choppy run (the metric gate cannot see it)

**Before (after a metric pass):** "We coded the advisories. We found 123 gaps. Most are
patched-exclusion. Two other modes exist."

Four sentences, mean 9 words, all under the length target — and it reads like a list of
bullets with full stops. **Merge two and vary one:**
"We coded every advisory and found 123 gaps. Most are patched-exclusion; the other two modes
account for the rest."

### 7.5 The over-glued paragraph

**Before:** "However, the ratio rises. Therefore, artifacts outpace advisories. Thus, defenders
have less time."

Three connectives in three sentences. The relation is real, but the glue hides it.
**After:** "The ratio rises: artifacts outpace advisories, so defenders have less time." One
sentence, same claim, no scaffolding.

---

## 8. What this rule looks like on a real draft

Measured with `--flow` on the draft that motivated this file (9 sections, 316 sentences):

| Symptom | Where | Count |
|---|---|---|
| Choppy run (consecutive ≤12-word sentences) | three sections | 3 sentences |
| Repeated adjacent openers | rq1, limitations, appendix | 12–14 % of pairs |
| Over-glue (sentence-initial connective) | appendix | 8.9 % of sentences (below the 18 % warning, but rising) |

The same counters on the pre-revision text showed a **5-sentence** run in the introduction: the
metric pass did not create the problem, but it can preserve and spread it. That is why the flow
report is a deliverable of every round, next to the length table.

---

## 9. Rules to carry forward

1. Name the seam before you split; run R/L/T after.
2. If a split would detach a restriction from its claim, do not split.
3. If the paragraph becomes eight short sentences, merge — do not trim.
4. Record a missed metric with the reason; a gate miss with a reason is a decision, a gate miss
   without one is an accident.
5. Cohesion repairs are edits too: record them (connective added, pronoun named, sentences merged).
