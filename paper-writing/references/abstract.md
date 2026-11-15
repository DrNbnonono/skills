# The abstract

Four elements, three properties, four failure modes — and one field difference that trips up
authors trained in the Chinese-journal tradition.

Write it **last**. It is the only part every reviewer reads, and it can only be written once the
claims and numbers are final.

---

## 1. Four elements

| Element | Question it answers | Length |
|---|---|---|
| **Purpose** | Why study this, and within what scope? | 1–2 sentences |
| **Method** | What was studied, and how? | 1–2 sentences |
| **Result** | What was found, with what evidence? | 2–3 sentences, with numbers |
| **Conclusion** | What does it change, and where does it hold? | 1–2 sentences |

The purpose must not repeat the title. The conclusion must not repeat the result.

---

## 2. Three properties

- **Self-contained.** A reader who sees only the abstract knows the question, the method, the
  answer, and the boundary.
- **Independent.** It is not a shortened introduction. The introduction argues why the question
  matters; the abstract reports what was found. An abstract whose second half is background is an
  introduction wearing a summary's clothes.
- **Objective.** In English security papers this means *no unverifiable adjectives*
  ("significant", "novel", "powerful") and *no claims beyond the measurements* — **not**
  impersonal grammar. See the field table below.

---

## 3. A field difference that must be stated

Chinese-journal style guides (and the GB abstract standard) require the third person and advise
against "本文/作者" as the subject. English security papers do the opposite: the authors are the
agents.

Measured on **120 top-tier security papers** (arXiv abstracts, see `scripts/story_study.py`):

| Property | Measured |
|---|---|
| Abstracts using **"we"** | **99.2%** |
| Median length | **212 words** (p10 146, p90 271) |
| Median sentences | **9** |
| Contains a number | 70.8% |
| Contains a percentage | 32.5% |

So:

| Chinese-journal convention | English security convention |
|---|---|
| Third person, avoid "本文/作者" | **First person plural "we"** is standard |
| No citations in the abstract | also no citations here |
| Emphasis on background and method | emphasis on **result and boundary** |
| Numbers optional | numbers expected: 71% carry at least one |
| Length often 200–300 characters | 150–270 words |

Keep the transferable part (self-contained, independent, objective in the sense of *no
overclaiming*), drop the part that belongs to another publication culture. If the target is a
Chinese journal, the third-person rule applies again — check the venue, not the habit.

---

## 4. Four failure modes

**A. The table of contents.**
> "This paper studies the judicial review of connected administrative acts. It is organised as
> follows: the introduction reviews…, chapter 1 defines…, chapter 2 analyses…"

The reader learns the structure and nothing else. An abstract reports findings.

**B. The mini-introduction.**
> "With the rapid development of X, problems have emerged. However, existing regulations lack clear
> provisions, causing… This phenomenon has attracted wide attention."

Background without method and result. This is the introduction's job.

**C. The collapsed structure.**
> "The system has multiple stages. Review should enter litigation. Agencies should be prudent.
> Courts should adjust their standards."

Five assertions in a row with no logical connective. An abstract is a chain: each sentence earns the
next.

**D. The empty result.**
> "Our approach is effective and efficient."

Not checkable. Replace with the measurement: "seals 2.5 of 4 in-scope paths (62%)".

---

## 5. A working shape (security measurement paper)

```
1  Stakes            who acts on what, and why the gap costs them
2  The claim tested   the single sentence under test, quoted if possible
3  Object and scale   what was tested, how many units, how many runs
4  Data coded         how many documents/events, under which reading
5  Result 1           in words, then the number
6  Result 2           the most surprising single point
7  Secondary result   the trend or the second RQ
8  Boundary + action  where it holds, and what the reader should do
```

Each move is one sentence at most; the whole lands at 180–230 words, inside the measured range.

---

## 6. Checklist

- [ ] Purpose, method, result, conclusion all present.
- [ ] At least one number; the headline number appears in words, not only in a table.
- [ ] No sentence whose content is "this paper is organised as follows".
- [ ] No background paragraph that belongs to the introduction.
- [ ] Boundary stated where the claim is strongest (one clause is enough).
- [ ] Uses "we" (English security venue) or the impersonal form the venue requires (Chinese journal).
- [ ] Length within the venue's limit (magazine: ≤200 words, no citations).
- [ ] Every number identical to the one in the body.
