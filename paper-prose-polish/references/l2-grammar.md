# L2 grammar patterns: what is measurable, and what is not

Patterns that appear often in English written by L1-Chinese authors: articles, tense, plural
agreement, `respectively`. This file records an attempt to measure them with POS tagging
(spaCy `en_core_web_sm`), including the three detectors that failed.

The result is deliberately negative: **mechanical grammar is not where this draft's problems
are, and POS heuristics are not a substitute for a grammar checker.** The point of writing it down
is to stop the skill from inventing article rules that fire on correct prose.

---

## 1. What was measured

Corpus: 25 papers sampled from the 120-paper set (211,802 words). Draft: 5,949 words.

| Pattern | Detector | Corpus | Draft | Verdict |
|---|---|---|---|---|
| `a`/`an` misuse | article + next word's initial sound, with acronym and `/j/`-word exemptions | 16 hits, **0.08/1k words** | 2 hits, both false positives (`a and`, `a of` from LaTeX cleanup) | **null**: the draft is clean |
| Bare singular count noun (missing article) | spaCy: `pos_=NOUN`, `tag_=NN`, no determiner/compound/possessor child, not a mass noun | **122.8 per 1,000 nouns** | — | **detector failed** |
| `this`/`these` agreement | `this` + plural noun, `these` + singular, `a` + plural | 0.30/1k | — | **unusable** |
| Tense mixing inside a paragraph | ≥2 past-tense and ≥2 present-tense finite verbs | **12.8% of paragraphs** | — | informative only, no baseline for "wrong" |
| `respectively` misuse | — | not measured | — | untested |

### 1.1 Why the bare-noun detector failed

122.8 hits per 1,000 nouns would mean one noun in eight lacks a determiner, which is not what
published prose looks like. The flagged words were `example`, `education`, `model`, `Problem`,
`Machine`, `cleaning` — mass nouns, title-case headings, and compound heads whose determiner sits
one level up ("the [model] comparison"). The exclusion rules needed to fix this (named entities,
compound heads, bare-plural generics, prepositional idioms) are exactly the cases a parser
resolves with a full dependency tree and a lexicon. Without them, the precision is too low to
report, let alone to write a rule from.

### 1.2 Why `this`/`these` failed the same way

The flagged examples were `these crash`, `these error`, `these output` — each is a **compound
modifier**, not the head noun (`these crash reports`, `these error messages`). The detector looked
at the token after `this`, not at the head of the noun phrase. Fixing it means walking to the head
noun, which is again work for a parser plus a lexicon.

### 1.3 What the tense result means

12.8% of published paragraphs mix past and present reporting ("we built X, the system uses Y").
That is normal in systems papers, which mix what was done (past) with what the system does
(present). The metric therefore cannot distinguish drift from convention, and no rule follows.

---

## 2. What this means for the skill

1. **Do not add mechanical-grammar rules.** The detectors that would carry them do not reach
   usable precision on this corpus.
2. **Use the right tool for the layer.** Mechanical grammar belongs to a real checker; the skill's
   value is the layers above it (see the table below).
3. **Record the null results** so a later round does not rediscover the same dead end.

| Layer | Tool | Catches | Misses |
|---|---|---|---|
| Articles, agreement, tense, prepositions | LanguageTool (needs Java) or a commercial checker | mechanical errors, with rule IDs | discourse, ambiguity, label nouns |
| Sentence shape | `lint_prose.py` | length, passive, nominalisation, dashes, negation, author-framing hedges | whether the sentence is true or well placed |
| Paragraph and section shape | `structure-and-placement.md` | misfiled content, oversized paragraphs, redundant closure | whether the paper's argument is right |

LanguageTool was not installed during this round: it needs a JVM, which this machine does not
have. If a JVM is available, the integration is one command:

```bash
pip install language-tool-python
python -c "import language_tool_python as lt; t=lt.LanguageTool('en-US'); print(len(t.check(open('draft.txt').read())))"
```

Run it on the final text, after the discourse pass: a sentence that is grammatical but malformed
at the level of information order should be fixed first, or the checker will report it as clean.

---

## 3. What the draft actually needs instead

The problems found in this draft were never article errors. They were:

- one claim per sentence violated (mean 33.6 words, 47 sentences over 45);
- agents deleted (26% passive, abstract subjects);
- negation stacked (9.7/1k vs 4.6 in published prose);
- an abstract whose subject is never the authors.

A grammar checker would have passed every one of those sentences. That is the argument for
keeping the discourse gates and treating mechanical grammar as a final, separate sweep.
