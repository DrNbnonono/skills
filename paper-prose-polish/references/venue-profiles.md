# Venue profiles

What each venue class actually rewards, with quotable evidence, and which writing rules
become **void** when the target changes. Apply the rules-void matrix before revising.

---

## 1. Top-4 security conferences

| Venue | Official standard | Consequence for prose |
|---|---|---|
| **USENIX Security** | Submissions "judged on originality, relevance, correctness, and **clarity**"; desk-reject for "severe editorial problems (broken references, **egregious spelling or grammar errors**, missing figures, etc.)" | Clarity is a scored dimension. Grammar errors can end the paper administratively. |
| **IEEE S&P** | Solicits "novel research contributions"; requires `\documentclass[conference,compsoc]{IEEEtran}` (1.8b); 13 pages body + 5 pages refs/appendices; anonymous; **"Submitted papers should not include full CVE identifiers"** | Template, page count, and anonymity are hard gates, not style preferences. |
| **NDSS** | Double-blind; enforced template; ethics and responsible-disclosure discussion required | Ethics is a section, not a sentence. |
| **CCS** | Anonymous; template; artifact description | Same class of hard gates. |

Sources:
<https://www.usenix.org/conference/usenixsecurity25/submission-policies-and-instructions> ·
<https://sp2025.ieee-security.org/cfpapers.html> ·
<https://www.ndss-symposium.org/ndss2026/call-for-papers/>

**Reader**: a PC member who works in security but not necessarily in this subfield, reading
three papers that day. By the end of page one they must know: the problem, why it matters
now, what was done, and why to believe it.

**Structural expectations**: contributions visible by page 2 (VUSEC: "Make sure to have them
on p2 at the latest"); an explicit threat model or assumptions paragraph for attack/defence
work; every claim traceable to a table or figure; limitations stated by the authors first.

---

## 2. Community style consensus

VUSEC, *Writing a System Security Paper: A Checklist*
(<https://download.vusec.net/resources/thesis/guidelines/PaperWritingChecklist.pdf>):

- "Omit needless words (you will find that most adjectives are superfluous)."
- "**Avoid the passive form!**" — *the house is cleaned by Tom* → *Tom cleans the house*.
- "Use topic sentences."
- Define a term at first use; write abbreviations out in full the first time.
- "Skim the paper to see if there is too much repetition. Readers find that very annoying."
- Pick American English and stay there.
- Avoid defensive writing ("we argue that…" in every section), boasting, preaching, colloquialism, humour.
- One idea per paper; lessons stated explicitly; know your audience (the PC, not the final reader).

Sentence-level foundations:

- Gopen & Swan, *The Science of Scientific Writing* — topic position / stress position.
- Williams, *Style: Lessons in Clarity and Grace* — characters as subjects, actions as verbs.
- Strunk & White, *The Elements of Style* — omit needless words.
- Peyton Jones, *How to Write a Great Research Paper* — the paper conveys one idea; structure serves the reader.

---

## 3. IEEE professional magazines (e.g. IEEE Security & Privacy)

| Item | Requirement | Confidence |
|---|---|---|
| Length | **6–10 double-column pages**, including figures and references | Secondary summary; verify on the official author page before submitting |
| Abstract | **≤200 words, no citations** | Same |
| Title | Short, attractive; avoid a subtitle full of jargon | Same |
| Review | **Single-blind**, at least two reviewers, ~6–8 weeks | Same |
| Audience | Security engineers, practitioners, adjacent researchers; "technical depth plus accessible expression" | Consistent with the magazine's stated scope |
| Proposal | Feature/special-issue articles may need a ~200-word proposal plus outline to the EIC first | Verify |
| Production | Two-column, 10 pt, figures inline; **publisher typesets the final version** | Verify |

Secondary source for the table: <https://www.aje.cn/arc/ieee-security--privacy>
Official author page (JavaScript-rendered, open manually):
<https://www.computer.org/csdl/magazine/sp/write-for-us/14680>

**Measured rhythm.** A full issue of IEEE S&P Magazine (Vol. 15, No. 5, Sep/Oct 2017,
100 pages, 419k characters) yields **2,658 sentences, mean 23.5 words, median 20.0**
(noise included: ads, bios, reference lists). Treat 23.5 as the order of magnitude, and
30 words as the point where a sentence already runs against the magazine's pace.

---

## 4. Rules-void matrix

Rules that are correct for one target and wrong for another. Check the row before applying.

| Rule | Top-4 conference | Professional magazine | Journal |
|---|---|---|---|
| Bold run-in headings as fragments (`**Why it matters.**`) | Discouraged (reads like slides) | **Standard furniture** — keep, but each head must be followed by a full sentence | Acceptable |
| Full CVE identifiers in the text | **Forbidden** (anonymity) | Required information | Allowed |
| `[conference,compsoc]` template | Mandatory at S&P | Irrelevant — publisher typesets | Journal template |
| Separate "Ethics considerations" section | USENIX: required, before references | Not required; disclose responsible handling in prose | Usually a subsection |
| Appendix | Allowed, reviewers may skip | **No appendices** — use a sidebar | Allowed |
| Explicit contribution list (C1/C2/C3) | Expected by page 2 | At most one paragraph, no numbering | Expected |
| Related work as its own section | Expected | Folded into the narrative | Expected |
| Second person ("you") | Avoid | Allowed in the takeaways | Avoid |
| Number of display items | More is fine | 4–6 total; one message per table | Moderate |
| Scene-setting opening | Optional | **Strongly preferred** | Optional |

---

## 5. Reader contract, side by side

| Dimension | Conference | Magazine |
|---|---|---|
| Page-one question | What is the contribution, and how does it differ from prior work? | Why should I care, now, concretely? |
| Method | Reproducible, complete | Believable and followable; details to a sidebar or tech report |
| Evidence | Tables and ablations | One number per claim, stated in words first |
| Tone | Restrained, defensive | Direct, opinionated, still accurate |
| Failure mode | Reviewer finds a hole | Reader stops reading on page 2 |

The most common magazine mistake is **shortening** a conference paper. The magazine needs a
**rewrite**: the same finding, opened with a specific person, machine, and failure.
