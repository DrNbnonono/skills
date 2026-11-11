# Vocabulary: transparency, not simplicity

The instinct "use short, simple, Anglo-Saxon words" is a native writer's rule. It is **wrong**
for this audience in one important way.

An L2 reader shares *international* vocabulary. `vulnerability`, `mitigation`, `coordinate`,
`serialize`, `exploitation` are learned from the field itself and are transparent to a
Chinese, German, or Brazilian researcher alike. What they do **not** share is idioms,
phrasal verbs, native collocations, and culture references — which are often made of the
shortest, most "simple" words in English (`hold up`, `a host of`, `fall short`).

So the criterion is not *simple*. It is **transparent**: the reader can assign a meaning on
first sight, from the word itself or from the technical context.

---

## 1. The three vocabularies

| Vocabulary | Example | Rule |
|---|---|---|
| **Technical terms of the field** | `exploitability`, `affected-version range`, `SAPI`, `deserialization`, `advisory` | **Keep.** Define once at first use, then never vary. |
| **International academic vocabulary** | `mitigation`, `prevalence`, `coordinate`, `validate`, `systematic` | **Keep.** Understood across languages from academic reading. |
| **Opaque ordinary language** | `hold up`, `a host of`, `notwithstanding`, `whilst`, `shed light on`, `at odds with` | **Replace** with a transparent equivalent. |

The rule of thumb: **if a competent researcher whose L1 is not English could meet the word
for the first time in this paper and still assign a meaning, it is transparent.** If they
would need a dictionary or a native friend, it is opaque — even if it is only three words
long.

---

## 2. Idioms and phrasal verbs (the main trap)

Phrasal verbs are the single most common source of L2 stalls in otherwise strong papers,
because they look easy and are almost never transparent.

| Opaque | Transparent replacement |
|---|---|
| carry out (an experiment) | run, perform |
| come up with | propose, design |
| fall short of | is less than, does not reach |
| fall through the cracks | is not checked, is missed |
| hold up (under testing) | still works, still holds |
| look into | investigate, check |
| figure out | determine |
| get around (a limit) | avoid |
| end up | result in, become |
| set up | configure, create |
| rule out | exclude |
| single out | isolate, distinguish |
| take into account | consider |
| play a role in | contributes to, affects |
| shed light on | explain |
| a host of | many |
| at odds with | conflicts with, contradicts |
| in the face of | despite |
| on the fly | at runtime |
| in turn | in response, then |
| as a result of | because of |
| due to the fact that | because |
| it is worth noting that | (delete; state the fact) |
| it should be noted that | (delete; state the fact) |
| a number of | several, many |
| the vast majority of | most |
| prior to | before |
| subsequent to | after |
| in order to | to |
| with respect to | for, about |

Allow one idiom in incidental prose (an aside, a caption) at most. **Zero** in the
abstract, the contribution list, any sentence that states a finding, and any sentence that
states a limitation.

---

## 3. Formal words with a transparent alternative

These are not wrong, but they add decoding cost with no precision gain:

| Replace | With |
|---|---|
| utilize | use |
| demonstrate | show |
| facilitate | help, enable |
| leverage (verb) | use |
| commence / terminate | start / end |
| endeavor | try |
| ascertain | find, determine |
| elucidate | explain |
| constitute | is, makes up |
| comprise | consist of, include |
| render | make |
| aforementioned | this, the, the earlier |
| henceforth | from now on |
| notwithstanding | even so, despite |
| whilst / amongst | while / among |
| thereby | so, this way |
| herein / thereof | (delete) |
| plethora | many |

Keep words that are precise, even if long: `deterministic`, `idempotent`, `concurrent`,
`observational`, `confounded`, `longitudinal`. Precision is not the problem.

---

## 4. Ambiguous function words (silent meaning errors)

These words have two readings, and an L2 reader may take the wrong one. Prefer the
unambiguous form whenever the sentence carries a claim.

| Ambiguous | Two readings | Prefer |
|---|---|---|
| `while` | at the same time / although | `although` for contrast; `at the same time` for time |
| `since` | from that time / because | `because` for cause; `since 2014` only for time |
| `as` | because / when / in the role of | name the relation: `because`, `when`, `as a` |
| `significant` | statistically significant / important | `statistically significant (p < ...)` or `large`, `substantial` |
| `respectively` | (requires the reader to re-map two lists) | rewrite as two sentences, or pair items directly |
| `may` + `not` scope | `may not` = not permitted / possibly not | `might not` for possibility; `is not allowed to` for permission |
| `only` | placement changes scope | put `only` immediately before the word it limits |
| `most` | majority / superlative | `most of` (majority) vs `the most` (superlative) |

The linter counts `while`/`since`/`as`/`significant` but cannot disambiguate them; judge each
in context.

---

## 5. Native flourish: never in a security paper

These are the constructions a native-writing coach would praise and an L2 reviewer will
stall on. They add no information:

- rhetorical questions ("So why does this matter?");
- one-word or fragment sentences for drama ("Every time.");
- metaphors and similes that carry the claim ("a hall of mirrors");
- irony, sarcasm, understatement;
- repeated antithesis ("It is not X. It is not Y. It is Z.");
- em-dashes used for stylistic suspense.

Keep the paper's own memorable short claim at the end of a section (magazine rhythm), but
make it literal: *"The contract does not hold."* is memorable and transparent;
*"Advisories are a hall of mirrors."* is memorable and opaque.

---

## 6. Hedges: use the common forms

An L2 reader can miss a hedge and read a stronger claim than the author intends. Use the
forms every researcher has seen a thousand times.

| Unfamiliar hedge | Common hedge |
|---|---|
| stands to reflect | may reflect |
| is liable to overstate | may overstate |
| is apt to | tends to |
| bids fair to | is likely to |
| in all likelihood | likely |
| arguably | (fine, common) |

Keep the strength identical when you swap. `may` → `may`; never turn `may` into `suggests`.

---

## 7. What not to touch

- Domain terms with an established meaning: `CVE`, `SAPI`, `PoC`, `FPM`, `opcache`.
- Numbers, units, ratios, CI notation.
- Names of methods, datasets, systems.
- Words whose precision matters: `association` vs `effect`, `observational` vs
  `experimental`, `correlation` vs `causation`. Do not "simplify" an epistemic distinction.

---

## 8. Quick self-check per sentence

1. Is there an idiom or phrasal verb? → replace it.
2. Is there a non-technical word I would not expect a B2 reader to know? → replace it.
3. Does a function word (`while`, `since`, `as`, `only`, `significant`) have two readings? →
   make it explicit.
4. Did I use a fancy verb where a plain one exists? → use the plain one.
5. Did I simplify a technical term by accident? → restore it.
