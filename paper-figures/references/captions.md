# Captions

The caption is read **before** the figure. It is the figure's abstract: one claim, then the
evidence needed to trust it.

---

## 1. Formula

```
Sentence 1  — the claim, in words, with the number if there is one.
Sentence 2  — what the axes/rows encode, including units and scale (log).
Sentence 3  — n, uncertainty, and the one caveat a reader must not miss.
```

Two to four sentences. The first sentence must be understandable with the figure hidden.

## 2. Before / after

**Bad (describes the axes):**
> Figure 4: The X axis shows days since disclosure and the Y axis shows the fraction of
> events with a public PoC. Four eras are shown in different colours.

**Good (states the claim, then the evidence):**
> Public exploit code now appears within days rather than weeks. The curves show the fraction
> of events with at least one public PoC as a function of days since disclosure, by era
> (log-scaled x-axis); the median falls from 19 days in the Pre-AI era to 3 days in the AI era.
> Each curve covers 40 events.

**Bad (no number, no n):**
> Figure 5: Recall is higher under the family lens.

**Good:**
> Every advisory under-reports the vulnerable surface under a literal reading. Dots mark
> recall under the literal lens (left) and the family lens (right) for five source types;
> the gap is the coverage the literal text hides. Recall is the mean share of the 29 validated
> configuration units covered.

**Bad (a legend in words):**
> Figure 6: The blue line is the artifact count and the orange line is the advisory count.

**Good:**
> Exploit artifacts overtake advisories in the most recent era only. Median 30-day counts per
> event are shown; the two series cross between the Pre-LLM and AI eras, at an
> artifact-to-advisory ratio of 1.18 → 1.83.

## 3. Rules

1. **Claim first.** If the caption starts with "Figure N shows…", rewrite it.
2. **No unexplained abbreviations.** Expand at first use in the caption, even if the text
   already did; captions are read independently.
3. **n and uncertainty.** "median over 40 events"; "95 % CI from 1,000 bootstrap resamples";
   "error bars are ±1 s.d. over 5 runs".
4. **State the scale.** "(log scale)", "(normalised to the Pre-AI era)".
5. **One caveat, only if load-bearing.** "The comparison is observational; the eras differ in
   more than AI tooling." Do not re-argue the paper in the caption.
6. **Do not repeat the text.** The text should say what the figure *means*; the caption says
   what it *shows*. If they are identical, delete one.
7. **Numbering**: use `\label`/`\ref` in LaTeX; never type "Figure 4" by hand.
8. **Consistent terms.** If the text says "artifact-to-advisory ratio", the caption does not
   say "counts ratio".

## 4. Panel captions

When a figure has panels A–D, the caption addresses them in order, one clause each:

> (A) Coverage by chain. (B) Coverage by version. (C) Coverage by SAPI. (D) The union of the
> three. Bars show the share of validated units covered under the family lens (n = 29).

Or, if the panels share one message:

> Panels A–D repeat the measurement for each era; the same ordering holds in all four, which
> is why the era effect is not an artefact of one subsample.

## 5. Length by venue

| Venue | Caption length | Note |
|---|---|---|
| Top-4 conference | 2–4 sentences | Self-contained; reviewers read captions first |
| Magazine | 2–3 sentences | Takeaway first, minimal jargon |
| Journal | 3–5 sentences | Can carry more methodological detail |

## 6. Check before submitting

- [ ] First sentence states the claim and survives without the figure
- [ ] Units and scale on every axis mentioned
- [ ] n and uncertainty stated
- [ ] Abbreviations expanded
- [ ] No "Figure N shows"
- [ ] Numbers match the table, the text, and the abstract
- [ ] Caption ends at the takeaway, not at a list of colours
