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
| Words | Peer-reviewed articles **4,900–7,200 words**, including abstract, keywords, bibliography, biography and table text (250 words per table/figure); **≤15 references** | Official author page |
| Abstract | **≤50 words, no citations** | Official: the author page says "The abstract word limit is 50 words" |
| Title | Short, attractive; avoid a subtitle full of jargon | Secondary summary |
| Review | **Single-blind**, at least two reviewers, ~6–8 weeks | Secondary summary |
| Audience | Security engineers, practitioners, adjacent researchers; "technical depth plus accessible expression" | Consistent with the magazine's stated scope |
| Proposal | Feature/special-issue articles may need a ~200-word proposal plus outline to the EIC first | Verify |
| Production | Two-column, 10 pt, figures inline; **publisher typesets the final version** | Verify |

Official author page (JavaScript shell; body read through the site's own content endpoint):
<https://www.computer.org/csdl/magazine/sp/write-for-us/14680>.

**Correction (v2.7.0).** Earlier versions of this skill said "≤200 words" for the magazine abstract.
That figure came from a secondary source and describes **journals**, not the magazine; the official
page states 50 words. Measured on 200 published magazine abstracts (2022–2025): median **40 words**,
median **2 sentences**, 92% have 1–3 sentences, 61% use `we`/`our`, only 15% contain a number.
A 200-word abstract is four times over the limit, not a style preference.

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

---

## 6. Measurement venues: ACM Internet Measurement Conference

IMC is not a security venue with a different name. The unit of contribution is a **finding
about an operational network**, and the reviewer's first question is not "is the attack
novel" but "over what population, in what period, from where". That question is answered in
the sentence that makes the claim, not in a threat model three sections away.

Full profile, with the measurements behind every number: `references/venue-imc.md`.
What belongs here is only how it changes the rules above.

| Dimension | Top-4 security | ACM IMC |
|---|---|---|
| First-page question | What is the contribution, and how does it differ? | What does the Internet do, and how do you know? |
| Claim's bound | Threat model, stated once | Population / place / period, in the same sentence |
| House verbs | design, implement, evaluate, outperform | measure, observe, find, identify, compare |
| Contribution list (C1/C2/C3) | Expected by page 2 | Used by only 25% of papers; not a defect either way |
| Related work | Often late (its own section near the end) | Early: second section in most papers |
| Ethics | USENIX: a section before references | **Mandatory appendix section headed "Ethics"**; the only appendix reviewers must read |
| Data / artifacts | Encouraged | **Declared** (full / partial / none); a "none" needs a reason and a cost |
| Appendix | Reviewers may skip | Cannot carry a contribution's primary evidence |
| Abstract | 200–250 words, claim-dense | **≤ 200 words**, median 189, 82% carry a number |
| Display items | Tables and ablations | Figures: median 9 figures + 5 tables |

**Rules that void at IMC** (relative to the top-4 rows in §4):

- Do **not** convert a measurement into a system contribution to look more novel; the
  venue reviews the finding.
- Do **not** delete the local scope clause to shorten a sentence — the scope is the claim.
- Do **not** import a threat-model section as the place where bounds live.
- Do **not** assume a bullet contribution list is required; it is the minority form.
- Do **not** treat "significantly" as free: only 16% of papers run a test, so a statistical
  word without one is conspicuous rather than conventional.

Measured fingerprint, 75 full texts and 237 abstracts (details in `venue-imc.md` §2):
mean sentence 23.7 words — **the same as top-4 security**; passive 19.0%; em dashes 2.75 per
1,000 words (3× security); and **51.5% of sentences contain a digit** (security: 39.7%).
The difference between the venues is not sentence length. It is how much a sentence must
carry.
