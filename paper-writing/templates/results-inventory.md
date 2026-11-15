# Results inventory — from a pile of experiments to a section

Fill this **before** writing the evaluation. One row per result you actually have.

## 1. The inventory

| # | Result (what was run, on what) | What it shows (one sentence) | Intro claim it settles | Section | Display item | Body / Appendix |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

Rules for the columns:

- **Column 3 is a sentence, not a number.** "62% of paths sealed" is data; "the shipped patch leaves
  half of its own stated scope open" is what it shows.
- **Column 4 must point at a claim already written in the introduction.** If no claim fits, either
  the claim is missing from the introduction (add it) or the result is not needed (appendix or bin).
- **Column 6, one item per claim.** Two display items for one claim means the claim is two claims.

## 2. The reverse check

List the introduction's claims and point each at a row above:

| Intro claim | Row | Status (covered / missing / needs an experiment) |
|---|---|---|
| | | |

Any "missing" row is a research gap, not a writing gap. Do not write around it.

## 3. The order

After the mapping is complete, order the rows:

1. Setup (one short subsection).
2. Headline result — the claim the paper is named after.
3. Supporting claims, in the order the introduction promises.
4. Ablation — only with a stated hypothesis.
5. Sensitivity / robustness — where the boundary is established.
6. Failure cases / threats to validity.

## 4. Per-row draft

For each surviving row, write these four sentences before touching the prose:

```
Question:        <what this subsection decides, phrased so it could fail>
Design:          <what varied, what was fixed, why that isolates the effect>
Evidence:        <Table/Figure N, column/panel, the number>
Interpretation:  <what the number means for the claim>
```

Four sentences with no placeholders means the subsection is ready to write. Any blank means the
experiment or the claim is not ready.
