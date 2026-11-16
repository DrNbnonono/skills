# The abstract: English conventions from the top four

The abstract is the only paragraph every reviewer reads, and the one most often written in a
different tradition from the paper that follows it. This file replaces an earlier version of the
skill whose abstract advice was inherited from Chinese-journal conventions (目的 / 方法 / 结果 /
结论), where the finding is fronted, the author disappears, and a closing sentence asserts
significance. The four venues do something else, and the difference is measurable.

**Writing vs revising.** The companion file `paper-writing/references/abstract.md` covers the
writing side (four elements, failure modes, the working shape). This file is the revision layer:
person, order, rhythm, the defect codes, and the measurement. Read that one first if the abstract
does not yet exist; read this one to fix an abstract that exists.

Everything below is measured: **164 accepted abstracts** from IEEE S&P (40), USENIX Security
(44), ACM CCS (40), and NDSS (40), published 2022–2025. Method and caveats in §8. The numbers
are an order of magnitude and a shape, not a target to hit exactly; the shape is the point.

---

## 1. Length and rhythm

| Measure | Median | p10 | p90 |
|---|---|---|---|
| Words | **207** | 122 | 279 |
| Sentences | **9** | — | — |
| Mean sentence length | **22.5** | 18.7 | 28.9 |

52% of abstracts have 8–11 sentences; 80% have 6–12. Only **5%** have a mean sentence under 18
words. An abstract is a compressed paper, not a fact sheet: it keeps the paper's sentence rhythm
(~23 words), and it gets its compactness from selection, not from chopping.

USENIX and CCS run shorter (median 196 and 176 words); S&P and NDSS longer (224 and 236). An
abstract outside 150–280 words is unusual at these venues. **None of the four conferences states a
word limit** in its current CFP (2026 editions checked); they require a complete abstract at
registration and freeze it, so write the real one early. The magazine is a different genre and a
hard limit: see §10.

## 2. Person: the author appears

| Measure | Share |
|---|---|
| Abstracts containing `we` or `our` | **92%** |
| Sentences starting with `We` / `Our` (mean) | **28%** |
| Abstracts with ≥3 `We`-starting sentences | 46% |
| Abstracts with zero `We`-starting sentences | 15% |
| Abstracts with **no first person at all** | **8%** |
| Abstracts containing `In this paper, we` | **54%** |
| First sentence starting with `We` | **9%** |
| Sentences with a passive marker | 12% |

Two facts matter for a non-native author:

1. **First person is the norm, not a modesty problem.** `In this paper, we present / measure /
   validate / design` is a standard English formula at all four venues (54%), not a cliché to
   avoid. Deleting the agent does not make the abstract more objective; it makes it read as a
   results dump (A22).
2. **The agent arrives late on purpose.** 91% of first sentences do *not* start with `We`; they
   set up the problem. The `we` sentence lands at sentence 2–4, after the reader knows what is
   at stake. Starting with `We present X` is legal but a minority style.

## 3. The five moves, in the order the corpus uses them

| # | Move | Typical sentences | Share of abstracts |
|---|---|---|---|
| M1 | **Stakes / problem** — a fact about the world the reader accepts | 1–2 | 87% mention the problem |
| M2 | **Gap** — `However / Yet / Existing / little is known / we lack` | 0–2 | 66% state a gap explicitly |
| M3 | **What we did** — named object, scale, method | 1–2 | 90% have an agentive approach sentence |
| M4 | **What we found** — the result, usually with a number | 2–4 | 70% carry ≥1 number; 48% carry ≥3 |
| M5 | **What it means, or availability** — one sentence | 0–1 | 11% end on a takeaway; 4% on availability |

**Where M3 lands:** by sentence 3 in 32% of abstracts, by sentence 4 in 54%. **Only 1% put the
headline result before the question it answers.** Result-first abstracts are press-release style,
not top-4 style: the reviewer needs to know what question is being answered before the number is
meaningful.

Sentence frames that recur (write your own content into them, never copy the corpus):
`X is ..., yet ...` · `Existing approaches ..., but ...` · `We present X, a ... that ...` ·
`We evaluate X on N ...` · `We find that ...` · `Our results show ...` · `X is available at ...`.

## 4. Sentence-level rules

1. **Name the agent for actions, the system for behaviour, the world for stakes.** `We validate
   X`; `X detects Y`; `Defenders rely on Z`. A sentence may be subjectless when the subject is
   obvious ("The comparison is observational."), but not four in a row.
2. **Name the system and keep the name.** 32% of abstracts reuse the system name introduced in
   the title, and once named it becomes a subject (`X provides ...`, `X mitigates ...`). "Our
   system" repeated is weaker than a name.
3. **Put the question before the answer.** M1–M3 before M4.
4. **Every number needs an object and a denominator.** `68% of the 123 gaps` beats `68% of
   gaps`; a bare percentage in an abstract is A12.
5. **Tense.** Present for what the paper establishes (`we show that X is exploitable`); past for
   the specific run (`we logged 149 runs`); present perfect for the field's state.
6. **Rhythm.** 8–11 sentences, mean 22–25 words. If your abstract has 13 sentences and a mean of
   15, it is a table of contents, not an abstract (A25).
7. **No citations.** All four venues discourage them; the magazine forbids them. `\cite` in an
   abstract is a defect.
8. **Do not restate the contribution in the last sentence.** The corpus's last sentence is
   normally still a result, or a one-line availability statement. A closing "this paper has
   important implications" is absent (A24).
9. **Skip the translationese opener.** `Nowadays`, `With the development of`, `plays an important
   role`, `in order to` appear in about 5% of accepted abstracts — tolerated, not rewarded, and
   they carry no claim. Start with the problem itself instead. `of great significance` and
   `lays the foundation` do not appear at all.

## 5. What a Chinese-template abstract looks like when translated

If the abstract was drafted in Chinese and translated, or written to a Chinese-journal template
(研究目的 → 研究方法 → 研究结果 → 研究结论/意义), these are the symptoms. They are the same
defects the rest of the skill repairs, concentrated in one paragraph.

| Symptom in the English text | Mechanism | Repair |
|---|---|---|
| `End-to-end validation of X covers 27 units and 130 runs.` | 名词化主语; the study acts by itself | `We validate X end to end, covering 27 units and 130 logged runs.` |
| `Nine advisories are mapped onto that space, and the patch is audited path by path.` | 被删除的主语 (A1) | `We map nine advisories onto that space and audit the patch path by path.` |
| `Advisory recall is 1–4%.` repeated as the abstract's spine | 结果前置, no question | `We find that advisories recall 1–4% of what is exploitable.` |
| `This paper proposes ...` then four subjectless findings | 本文 as the only agent | Keep one `we` sentence, then carry `we` through the findings |
| `... which is of great significance for defenders.` | 意义句 (A24) | Say what changes: `so a defender who follows the advisory can still be exploited` |
| `The ratio ... rises from 0.5 to 1.7` with no actor | 数据罗列 | `We measure the ratio ...; it rises from 0.5 to 1.7` |
| 12–14 short sentences, each one number | 一条结果一句 | Merge into result sentences with a verb and an object (A25) |

The rule behind all of them: **English abstracts narrate who did what and what happened.**
Chinese-journal abstracts often report what was found and leave the actor implicit. A translation
inherits the omission, and the reviewer reads a laboratory log instead of a paper.

## 6. Worked repair (synthetic)

Before — fact-sheet abstract, 11 sentences, mean 15.5, zero first person (the signature of A22 +
A25):

> Advisories and patches guide remediation, yet their stated scope may not match what is
> exploitable. End-to-end validation of the family covers 27 units and 130 logged runs. Nine
> advisories are mapped onto that space, and the official patch is audited path by path. Advisory
> recall is 1–4% under a literal lens and 58–73% under a family lens; 64% of 118 gaps call a
> version patched while it still works. Patch completeness is 55% within the literal scope and
> 28% across the family, leaving four of nine paths unsealed. A separate 36-event, 540-record
> study across four disclosure eras finds public exploit artifacts outpacing advisories. The
> ratio rises from 0.5 to 1.7, and the latest era has no first-PoC delay above 2.1 days. That
> comparison is observational. A 300-respondent vignette adds exploratory evidence on remediation
> intent. The gap is structural, not one vendor's defect: advisories describe the CVE's literal
> scope, while defenders face a multi-dimensional boundary.

After — same claims and numbers, five moves, agent restored (9 sentences, mean 21, three `We`):

> Advisories and patches are the documents defenders act on, yet the scope they state may not
> match what is exploitable. We validate the family end to end: 27 chain–version–SAPI units and
> 130 logged runs. We map nine advisories onto that space and audit the official patch path by
> path. We find that advisories recall 1–4% of what is exploitable under a literal reading of
> their wording, and 58–73% at family level. In 64% of the 118 gaps we coded, the advisory calls
> a version patched while it still works, and the patch covers 55% of the literal scope but 28%
> of the family, leaving four of nine paths unsealed. In a separate study of 36 disclosure events
> and 540 records across four eras, we measure public exploit artifacts outpacing advisories: the
> ratio rises from 0.5 to 1.7, and the latest era has no first-PoC delay above 2.1 days. That
> comparison is observational; a 300-respondent vignette adds exploratory evidence on remediation
> intent. The gap is structural, not one vendor's defect: advisories and patches describe the
> CVE's literal scope, while defenders face a multi-dimensional boundary.

What changed: two nominalised methods became `We validate` / `We map ... and audit`; the
subjectless recall figure became `We find that ...`; the semicolon chain was split at a seam and
the second half kept its subject; the closing sentence states the paper's claim instead of a
significance judgement. No number, hedge, or scope condition changed.

## 7. Checklist (run it in this order)

**Conference abstract:**

- [ ] Word count within the venue's stated limit (none of the four states one; typical 150–280).
- [ ] 8–11 sentences; mean sentence 20–26 words.
- [ ] `we` / `our` present; at least one `We`-starting sentence; no four-sentence subjectless run.
- [ ] The question (M1–M2) comes before the headline number.
- [ ] An explicit gap sentence, or a stated limitation of prior work.
- [ ] 2–4 sentences carry numbers; every number has an object and a denominator.
- [ ] The system is named and reused, if the paper has one.
- [ ] No `\cite`, no "Nowadays", no "important significance / plays an important role".
- [ ] The last sentence is a result, an implication the paper actually supports, or availability
      — not a summary of the paper.
- [ ] Terminology matches the body; no term is introduced here that the body does not define.

**Magazine abstract (IEEE S&P Magazine):**

- [ ] **≤50 words** (hard limit; published median 40).
- [ ] 2–3 sentences; mean 18–22 words.
- [ ] `we` or `this article` as the actor; object named.
- [ ] No citation, no contribution list, no background paragraph, no significance sentence.
- [ ] At most one number; none is fine.

## 8. Method, and how to re-measure

Corpus: 164 abstracts. S&P, CCS, NDSS metadata and abstracts via OpenAlex
(`primary_location.source.id` for each conference, `publication_year:2022-2025`,
`abstract_inverted_index` reconstructed); USENIX Security via usenix.org program pages (2024 and
2025 editions). Kept only abstracts of ≥3 sentences. Manual read of 16 sampled abstracts to
validate the keyword heuristics.

Caveats: OpenAlex reconstruction occasionally glues two words together and truncates a minority
of abstracts (about 10% are under 120 words); the move coverage uses keyword heuristics, so treat
"66% state a gap" as an order of magnitude; venue granularity is by source, so a few workshop or
journal-adjacent items may slip in. The sentence/person/length statistics are stable across the
four venues; the move percentages are directional.

Re-measure with `scripts/abstract_study.py` (same collection and analysis code) rather than
trusting these numbers after a few years. The venue changes; the shape has not.

**Cross-check.** `paper-writing/references/abstract.md` reports an independent sample of 120
top-tier abstracts (arXiv): median **212 words**, **9 sentences**, **99.2%** use `we`. This corpus
gives 207 / 9 / 92%. Two independent samples, the same shape; the gap in the person figure is the
corpus (venue proceedings vs arXiv) and the counter (`we`/`our` tokens vs any `we`), and both are
far from the 8% tail.

## 9. Linting an abstract

```bash
python scripts/lint_prose.py --abstract sections/00_abstract.tex                 # conference shape
python scripts/lint_prose.py --abstract sections/00_abstract.tex --venue magazine # 50-word genre
```

Reports words vs limit, sentences, mean, first person, gap marker, number count, opening and
closing class, and a WARN list mapped to A22–A25. A normal top-4 abstract shows 0–1 warnings; the
fact-sheet example in §6 shows two (`no first person`, `fact-sheet rhythm`). Warnings are
advisory: 8–10% of accepted abstracts trip one, which is why the linter never fails the build
over them.

## 10. Magazine abstracts: 50 words, not 200

IEEE Security & Privacy Magazine's author page states: **"The abstract word limit is 50 words."**
The same page caps peer-reviewed articles at 4,900–7,200 words (including the abstract) and 15
references. This is a hard submission rule, and it overturns the earlier versions of this skill,
which carried "≤200 words" from a secondary source whose 100–200-word figure applied to IEEE
*journals*, not the magazine.

Measured on **200 published magazine abstracts** (IEEE S&P Magazine, 2022–2025, OpenAlex):

| Measure | Value |
|---|---|
| Words | median **40** (mean 47, p90 78) |
| Sentences | median **2** (92% have 1–3) |
| Mean sentence length | 20–21 words |
| Uses `we`/`our` | 61% |
| Names `we` or `this article` | 71% |
| Contains a number | 15% |

The conference skeleton in §3 does not fit: 40 words cannot carry five moves and four numbers.
The magazine shape is two, at most three, sentences:

1. **Stakes**: the practice, document, or failure the reader already meets — one sentence.
2. **What the article does**: `We validate ...`, `We measure ...`, or `This article describes ...`
   — one sentence, with the object named.
3. *(Optional)* **One number, or one action** the reader can take.

Example shape (synthetic, 43 words): "Advisories are what defenders act on, yet their stated
scope may not match what is exploitable. We validate a five-chain PHP family end to end and audit
the official patch path by path. Disabling the vulnerable module is the only broad mitigation."

What is banned: citations, a contribution list, a background paragraph, a second result, a
significance sentence. What is allowed: no number at all — only 15% of published abstracts carry
one.

A 200-word abstract on a magazine desk is not a style problem; it is over the limit by 4×.
