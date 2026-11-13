# Revision record — <round> — <file / section>

Baseline (before this round): mean __ / p90 __ / >45 __ / passive __% / idioms __ / stalls/100w __ / flow: chop __ rep% __ / `\todo` __
Target (after this round): mean ≤ __ / p90 ≤ __ / >45 ≤ __ / passive ≤ __% / idioms ≤ __ / stalls ≤ __ / flow: chop ≤2

Changes this round: __ sentences (zero is a valid answer; record the KEEP share instead)

## Sentences

| # | Location | Original (truncated) | Code | Verdict | Rewrite | Where the reader stalls | First read | Seam R/L/T |
|---|----------|----------------------|------|---------|---------|-------------------------|------------|------------|
| 1 |  |  |  |  |  |  | pass / stall S__ | n/a |
| 2 |  |  |  |  |  |  |  |  |

Verdicts: KEEP / TRIM / SPLIT / MERGE / RECAST / REWRITE / DELETE. A SPLIT requires a named
legal seam; record `R/L/T` and any repair (e.g. `R: pronoun named`, `T: bridge added`). A MERGE
records which two sentences were joined and the tie it restored.

## Missed metrics (with reason)

| Metric | Target | Achieved | Why the target was not worth the cost | Alternative taken |
|---|---|---|---|---|
|  |  |  |  |  |

## Flow report (`--flow`)

| File | Chop (max run) | Rep% | Conn% | CV | Note |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Questions for the author (REWRITE batch)

| # | Location | The sentence | What I cannot decide | Why it matters |
|---|----------|--------------|----------------------|----------------|
| 1 |  |  |  |  |

## Structural findings (not fixed in this round)

- Duplication between §X and §Y:
- Claim exceeds evidence:
- Missing definition / abbreviation:

## Rules to carry into the next round

1.
2.

## Verification

- [ ] Numbers and claim strength unchanged
- [ ] `\cite` / `\ref` / math / table data untouched
- [ ] Previous file backed up as `.bak-YYYYMMDD`
- [ ] Linter re-run and compared against baseline (`--compare`), including L2 blockers
- [ ] `--flow` re-run; no new choppy run or repeated-opener warning
- [ ] Every SPLIT has a named seam and an R/L/T result; every orphan pronoun repaired
- [ ] Any missed metric recorded with its reason
- [ ] First-read gate re-run; stalls per 100 words recorded before/after
- [ ] Revised paragraph read aloud once without losing the subject
- [ ] Read once as the reader model (non-native expert): no sentence needed a second read
