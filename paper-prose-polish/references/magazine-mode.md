# Magazine mode

Converting a conference paper into a professional-magazine feature (IEEE S&P Magazine,
IEEE Computer, ACM Queue, ;login:, CACM). The work is a rewrite, not a cut.

---

## 1. What actually changes

| | Conference paper | Magazine feature |
|---|---|---|
| Reader | PC member in the same field | Practitioner, adjacent researcher, manager |
| Page-one question | What is the contribution? | Why do I care, today, concretely? |
| Method | Complete and reproducible | Believable and followable; details to a sidebar |
| Contributions | Numbered list by page 2 | One paragraph, no numbering |
| Related work | Own section | Folded into the narrative |
| Appendices | Allowed | **None** — sidebars |
| Display items | As many as needed | 4–6; one message per item |
| Tone | Restrained | Direct; one opinion per section is allowed, over-claiming is not |

The usual mistake is deleting 40% of the text and shipping a thin paper. The magazine needs
the same evidence with a different spine.

---

## 2. Length economics

Budget 6–10 double-column pages including figures and references, roughly 700–1,000 words
per page once display items are counted. For a 6,500-word conference body this means:

- keep ~5,500 words of prose;
- delete the appendix entirely (~1,400 words) and recover 700–900 of it as **two sidebars**;
- cut display items from 11 to 6 (see §4), which frees half a page.

The word count is rarely the binding constraint. The binding constraint is that **every
paragraph must be readable by someone outside the subfield**.

---

## 3. Skeleton that works

```
Title + abstract (≤200 words, no citations) + keywords
1. Opening scene (150–250 words, no heading)
   A named person/machine/version fails after following the advisory.
   Last line states the thesis, not the method.
2. **Why this matters** (~500 words)
   The document in question is the one defenders actually act on; the implicit contract;
   what prior work checked (2–3 sentences with citations), and what it could not check.
3. **How we checked** (~600 words + one figure)
   Scope, units, counts, and the decision rule — no invented terminology.
4. **What we found** (~1,200 words + two tables)
   Three findings, each: claim in words → number → what it means for the reader.
5. **Is it getting better or worse?** (~700 words + one figure)
   The temporal trend, plus an explicit statement of what the data cannot establish.
6. **What this means** (~600 words)
   Separate short paragraphs for defenders / vendors / coordinators. Second person allowed here.
7. **What we do not know** (~250 words)
   Single case, observational trend, unfinished study.
8. Conclusion (~150 words, one paragraph, no new claims)
Sidebar A: how the work was done without releasing a weapon (ethics + reproducibility)
Sidebar B: the governance proposal (one idea, no statistics)
References (20–40) + author bios
```

---

## 4. Display-item budget

| Keep | Why |
|---|---|
| One conceptual figure | The mental model the reader retains |
| One timeline or scene figure | Carries the story |
| One trend figure | The temporal claim |
| One table per core result | At most two; one message each |

Everything else goes: per-category breakdowns, heatmaps that restate the bar chart,
design tables for a study that has not run. A reader who meets three tables on one spread
stops reading tables.

Caption rule: the caption states **what the reader should notice**, not what the axes are.

---

## 5. Voice

- Sentence mean 22–25 words; paragraphs of 3–5 sentences.
- Active voice; the agent is a person, a team, an organisation, or a system.
- One concrete object every 800–1,000 words: a version number, a server, a repository, a
  failed run.
- A short declarative sentence at the end of a section is the magazine's signature rhythm
  ("The contract does not hold.").
- Numbers first in words, then in digits: "public exploit code now appears faster than
  advisories: the 30-day ratio rose from 0.63 to 1.83".
- Keep the paper's own caution where it is load-bearing, but do not hedge every paragraph:
  a magazine reader reads hedging as the author not believing the result.

---

## 6. Opening scene

Do not fabricate. If the author has no documented incident, use their own test log.
Template:

```latex
\textbf{The <thing> that didn't <expected outcome>.}
On [date], [organisation] shipped a fix for <bug>, with an advisory that named the affected
versions, the fixed versions, and a workaround. A defender who read it would upgrade and move on.
[N] days later, the same exploit still worked on the version that advisory called fixed.
The advisory was not wrong about the bug it described. It described a smaller bug than the
one that existed.
```

The final two sentences are the thesis: not "the vendor lied" but "the document described a
smaller object than reality". That framing is defensible and survives fact-checking.

---

## 7. Title and abstract

**Title**: short, one hook, states the finding. Colon form works when the second half gives
the evidence scale. Reject titles that promise a mechanism the paper does not test
(e.g. "in the Era of AI-Assisted Discovery" when the data show only an era-level association).

**Abstract** (≤200 words, no citations), in this order:

1. Stakes in one sentence (who acts on this document, and why).
2. The single claim under test, quoted if possible ("this version is patched").
3. Object and scale: what was tested, how many units, how many runs.
4. Data: how many documents/events were coded, and by what reading.
5. Result 1 in words, then the number.
6. Result 2, the most surprising single point.
7. The temporal or secondary result.
8. One actionable sentence, short.

Then verify: does it contain at least two `We` sentences, zero passive agents, and no
terminology that a practitioner would have to look up?

---

## 8. Conversion checklist

- [ ] Appendix material re-homed into sidebars or dropped
- [ ] Display items ≤6; every caption states the takeaway
- [ ] Terminology de-jargonised (see the term-mapping method in `sentence-rules.md`, L12)
- [ ] Related work folded in; no standalone section
- [ ] Contribution list compressed to one paragraph or removed
- [ ] Opening scene present, with real facts only
- [ ] Abstract ≤200 words, no citations, ≥2 `We` sentences
- [ ] "What we do not know" present; claims match evidence strength
- [ ] Page count within 6–10 including figures and references
- [ ] If the venue requires a proposal: 200-word abstract + outline + audience statement drafted
