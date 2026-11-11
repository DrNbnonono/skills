# Worked example

A full pass on one manuscript (PHP2Shell: advisories versus validated exploitability),
kept because the failure pattern is typical of non-native security writing: correct
content, missing agent.

---

## 1. Baseline

192 sentences, 6,474 words, mean **33.7** words/sentence, p90 58, max 94,
**47** sentences over 45 words, passive **26%**, nominalisations 2.08/sentence,
dashes 65.

| File | Sentences | Mean | Max | Passive % | Reading |
|---|---|---|---|---|---|
| abstract | 9 | 22.9 | 39 | 33 | short sentences, zero `We` |
| introduction | 42 | 26.1 | 85 | 17 | one 85-word contributions sentence |
| background | 27 | 28.7 | 65 | 37 | |
| RQ1 (measurement) | 30 | 33.2 | 65 | 23 | |
| RQ2 (dataset) | 22 | 32.8 | 70 | 23 | |
| discussion | 14 | 41.8 | 91 | 36 | worst ratio of claims to words |
| limitations | 13 | 36.6 | 68 | 46 | passive highest where agency matters |
| conclusion | 6 | 47.2 | 73 | 50 | |
| appendix | 29 | 46.1 | 94 | 14 | longest sentences in the paper |

Three headline findings:

1. **The abstract had 9 sentences and no sentence starting with `We`.** Its subjects were
   advisories, validation, chains, recall, completeness, ratio, findings — never the authors.
2. **The introduction had 1 `We`-initial sentence in 42.** Strong verbs replaced by
   "X was combined with Y".
3. **The two sections a reviewer uses to judge rigour (conclusion, appendix) were the two
   hardest to read** (mean 47.2 and 46.1).

---

## 2. Representative sentences

### A1/A3 — abstract, sentence 2 (RECAST)

Before: "To assess the accuracy and timeliness of disclosure information, dynamic validation
of the [family] in [subsystem] was combined with a cross-era analysis of public exploit
artifacts and advisories."

Reader stall: the subject spans 15 words, the passive verb arrives at word 21, and no agent
is named. In an abstract this costs the whole paper's first impression.

After: "We test the [family] end to end, and we pair those tests with a cross-era analysis
of public exploit artifacts and advisories."

### A4 + A8 — introduction, the "methodological ceiling" sentence (SPLIT)

Before (48 words): "Both lines of work share a methodological ceiling: they compare documents
and timestamps against each other---does this advisory agree with that commit log---rather
than independently verifying what either document claims against the vulnerability's actual,
dynamically confirmed exploitability."

Reader stall: the conclusion (only dynamic testing can settle it) is buried inside
`rather than`, and the sentence ends on a 12-word abstract noun string.

After: "Both lines of work run into the same limit: they compare one document with another.
Does this advisory agree with that commit log? Neither asks whether the claim is true,
because answering that takes dynamic testing — and neither study does any."

### A1 + A12 — the agreement statistic (needs a number first)

Before: "After independent coding and a subsequent adjudication pass, inter-rater agreement
(Cohen's κ) was [TODO] under the family lens and higher under the literal lens, where
disagreements were rarer simply because almost nothing qualified as literally covered."

Two problems: three passives with no agent, and a comparison ("higher") with no values.
The fix is not stylistic — the missing numbers must be supplied by the author.

After (values to be filled): "Two coders labeled each item independently and then resolved
disagreements in an adjudication pass. Agreement was κ = X under the family lens. Under the
literal lens it was higher (κ = Y), but only because so few items qualified that the coders
rarely had anything to disagree about."

### A2/A5/A6 — the "concentration" paragraph (SPLIT)

Before (40 words): "This concentration is itself informative: it is not that advisories are
diffusely incomplete everywhere, but that one specific claim---'version v is patched'---is
disproportionately where advisories overstate what has actually been fixed, which directly
motivates the patch-completeness analysis below."

Reader stall: bare `This` pointing at three percentages in the previous sentence; a
negative–affirmative double structure; `which` making the paper's structure the agent.

After: "The concentration matters. Advisories are not uniformly vague; they fail at one
claim. When an advisory says 'version v is patched', that is where it most often overstates
the fix. Section 3.3 therefore measures patch completeness directly."

---

## 3. Paragraph before/after

Before (4 sentences, 116 words, mean 29):

> **Why advisories matter.** When a software vendor publishes a security advisory, downstream
> users rely on it to decide whether their deployment is affected, which version to upgrade
> to, and whether a temporary mitigation is needed. For large, heterogeneous software
> ecosystems, the advisory---not the source diff, not the commit log---is the artifact that
> most defenders actually act on. This dependency carries an implicit assumption: the
> affected-version range, remediation status, and mitigation guidance that an advisory states
> are close enough to the vulnerability's true technical boundary that following the
> advisory's instructions removes the risk it names. When that assumption fails silently, a
> defender who does everything the advisory asks can still be exposed.

After (6 sentences, 139 words, mean 23.2):

> **Why advisories matter.** When a vendor publishes an advisory, defenders use it to decide
> three things: whether they are affected, which version to upgrade to, and whether they need
> a workaround in the meantime. In a large ecosystem, the advisory---not the source diff, not
> the commit log---is the document most defenders actually act on. Every advisory therefore
> rests on an unstated assumption. The versions it lists, the fix it names, and the
> mitigations it suggests are assumed to be close enough to the real vulnerability that
> following the advisory removes the risk. When that assumption fails silently, a defender can
> do everything the advisory asks and still be exploited. This article tests that assumption
> for one vulnerability family, and finds that it fails more often than the advisories suggest.

What changed, and why:

| Change | Code | Reason |
|---|---|---|
| `downstream users` → `defenders` | A9 | audience language; the reader is the defender |
| `a temporary mitigation is needed` → `a workaround in the meantime` | A9 | same meaning, ordinary words |
| three trailing parallels → `decide three things:` fronted | A11 | gives the reader a container before the items |
| `artifact` → `document` | A9 | "artifact" is opaque outside the field |
| 37-word colon sentence → two sentences | A3/A4 | subject and verb were 13 words apart |
| `be exposed` → `be exploited` | — | the study measures exploitation, so say so |
| added a signpost sentence | — | page one must state what the article does |

The paper's best sentence was left alone — it is the one with the dashes:

> the advisory---not the source diff, not the commit log---is the document most defenders
> actually act on.

Dashes are correct there because they hold a **contrast of examples**, not the argument
(L10). KEEP is a verdict.

---

## 4. Abstract rewrite

Before: 206 words, 0 `We` sentences, 33% passive.
After: 191 words, 3 `We` sentences, agent-named throughout, every number identical.

Structure of the rewrite: stakes → the single claim under test ("this version is patched")
→ object and scale (5 paths, 29 combinations, 149 tests) → data coded (12 advisories) →
result 1 (strict vs charitable reading) → result 2 (the one dominant gap shape) → patch
completeness (62% / 31%) → trend (40 events, ratio 0.63 → 1.83) → one actionable line.

The closing line is a claim, not a summary: **"'Patched' should be a claim we check, not a
fact we rely on."**

---

## 5. Order of work that avoided rework

1. Terminology table first (three spellings of the same lens would otherwise have survived
   every sentence pass).
2. Opening paragraph, because it fixes the voice for the rest.
3. Body sections next, abstract last — the abstract's numbers and terms come from the body.
4. Lint after each round, never rewriting an already-passing sentence.
