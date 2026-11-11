# The top-4 prose corpus: what the venues reward, and how to measure it

"Write like the top-4 venues" is advice that is easy to repeat and hard to verify. This file
separates the three things that are actually true:

1. **Official requirements** — what each venue's CFP and review criteria say (also in
   `venue-profiles.md`).
2. **Observed conventions** — how accepted papers in S&P, USENIX Security, CCS, and NDSS
   actually open, structure, and phrase their claims. Directional, not countable from memory.
3. **A measurement protocol** — how to re-derive the numbers on a fresh corpus instead of
   trusting remembered style advice.

Do not copy sentences, figures, or phrases from the corpus. The corpus is for measurement and
for calibrating structure, not for imitation; verbatim reuse is plagiarism, and the
similarity check of every venue will catch it.

---

## 1. Official requirements (verifiable)

| Venue | What the official text says | Consequence for prose |
|---|---|---|
| **IEEE S&P** | "novel research contributions"; `\documentclass[conference,compsoc]{IEEEtran}`; 13 pages body + 5 pages refs/appendices; anonymous; "Submitted papers should not include full CVE identifiers" | Prose is judged by novelty and clarity; the anonymity rules forbid identifying specifics. |
| **USENIX Security** | Submissions "judged on originality, relevance, correctness, and **clarity**"; desk-reject for "severe editorial problems … egregious spelling or grammar errors" | Clarity is a scored dimension; grammar can end the paper administratively. |
| **CCS** | Anonymous; enforced template; artifact description | Same class of hard gates as S&P. |
| **NDSS** | Double-blind; enforced template; ethics and responsible-disclosure discussion required | Ethics is a section, not a sentence. |

Sources are listed in `venue-profiles.md` §1. Check the current year's CFP before relying on
any of it; venue rules change.

## 2. Observed conventions (directional)

These hold across the four venues' accepted papers and explain why they read the way they
do. Treat them as structure, not statistics.

| Convention | What it looks like | Why reviewers reward it |
|---|---|---|
| **Result-first abstract** | The finding and its number appear in the first two or three sentences; the method comes after | A reviewer decides within one paragraph whether to keep reading |
| **Contributions visible by page 2** | A short list or one paragraph naming what is new, before the background | Conference reviewers need the claim to judge novelty |
| **Problem → gap → approach → result** in the opening | Each move is its own paragraph; the gap is stated as what prior work could not do | A missing gap is the most common rejection reason |
| **"We" for author actions** | "We collected", "we validated", "we measured" | Methods must be attributable and reproducible |
| **One claim per paragraph, claim in the topic sentence** | The first sentence names the claim; the rest supports it | Skimming works; reviewers skim |
| **Related work is comparative** | "X measured A; we measure B because A cannot see C" | A list of papers reads as uncited background, not positioning |
| **Tables and figures referenced with a claim** | "Table 2 shows the gap is concentrated in one claim", not "Table 2 shows the results" | The reader learns what to notice |
| **Limitations stated by the authors first** | A short section naming the boundary of the evidence | Reviewers look for over-claiming; naming it first disarms the objection |
| **Plain verbs** | "use", "show", "find", "test" | Fancy verbs read as non-native and add no precision |

The L2 overlay: top-4 papers are **not** written in difficult English. The memorable ones
are plain, short-sentenced, and terminologically stable. The readable ones are readable for
the same reasons this whole skill is about. When a paper is dense, it is usually dense for a
reason the author did not intend.

## 3. Measured baseline (fill this in from your own corpus)

Do not trust numbers quoted in a blog post, including numbers written here earlier. Measure.

```bash
# 1. Collect 20 accepted papers per venue from the current proceedings (LaTeX sources if
#    available; otherwise PDF text extracted to .txt, one file per paper).
# 2. Measure with the same linter used on drafts:
python scripts/lint_prose.py --path corpus/ --glob "*.tex,*.txt" --json corpus/<venue>.json
# 3. Record mean / median / p90 / >45-word share / passive / nominalisation / idioms.
```

| Venue | Year | n papers | Mean | Median | p90 | >45/100 sent | Passive % | Idioms/1k words |
|---|---|---|---|---|---|---|---|---|
| IEEE S&P | to measure | | | | | | | |
| USENIX Security | to measure | | | | | | | |
| CCS | to measure | | | | | | | |
| NDSS | to measure | | | | | | | |

**How to use the table.** Compare your draft's distribution to the corpus, not to its mean.
The useful question is not "is my mean 23.5?" but "does my paper have a tail the corpus does
not have?" A draft with a mean of 24 and twenty sentences over 50 words reads worse than a
draft with a mean of 27 and no tail.

Calibration anchor, for order of magnitude only: a full issue of IEEE S&P Magazine
(Vol. 15 No. 5, 2017; 419k characters, noise included) measures **mean 23.5, median 20.0**.
Magazine prose is the easier target; conference prose usually runs a few words longer.

## 4. What to imitate, and what not to

| Imitate | Do not imitate |
|---|---|
| The opening move (problem, gap, approach, result) | A specific author's rhetorical tics |
| The topic-sentence discipline | Sentences that happen to be famous |
| The use of "we" and active voice | Dense passive methods sections (they exist; they are not the model) |
| Terminology stability (one name per concept) | Clever titles that promise a mechanism the paper does not test |
| The way claims are tied to a table or a number | Idioms and flourishes that only a native reader enjoys |

## 5. The L2 question for any corpus

After measuring, read **the tail** of the corpus — the ten longest sentences in each venue.
You will usually find that even top-4 papers contain sentences that fail the first-read gate.
Those sentences survived on the strength of the result, not on the strength of the writing.

Do not reproduce them. The gate in `comprehension-gate.md` is stricter than the corpus
average, deliberately: it targets the reader who will judge your paper, not the distribution.
