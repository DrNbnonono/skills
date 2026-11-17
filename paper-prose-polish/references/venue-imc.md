# IMC mode — polishing for the ACM Internet Measurement Conference

A specialisation of this skill, not a replacement. Everything in `SKILL.md` still holds:
the core gate is still first-read comprehension, the precedence rule still is
claim fidelity > coherence > metrics, and the rewrite-authority tiers are unchanged.
What changes is **what a sentence has to carry** and **what an IMC reviewer will refuse**.

Read this file after `venue-profiles.md` and before the sentence pass, when the target is
IMC (or a measurement venue with the same review culture: IMC, SIGCOMM IMC workshops,
TMA, PAM; use it with care for SIGCOMM itself, which is not covered by these measurements).

---

## 0. What the venue rewards, in the venue's own words

> "The Internet Measurement Conference (IMC) is a highly selective venue for the
> presentation of measurement-based research in data communications."
> — IMC 2026 Call for Papers

> "The focus of IMC 2026 will be on research that improves the practice of network
> measurement, illuminates some facet of an operational network, or both."
> — IMC 2026 Submission Guidelines

Two consequences for prose, both of which a security draft gets wrong by default:

1. **The object of study is the Internet, not your system.** A security paper says what
   the attacker or the defence does. An IMC paper says what the Internet does, and your
   instrument is how you found out. When the sentence makes the tool the subject, the
   reviewer reads a systems paper in the wrong venue.
2. **A finding must be about an operational network, not about a dataset.** "We observe
   1.2M certificates" is an inventory. "1.2M certificates, 4.1% of which are misissued
   for a domain the issuer does not control" is a finding.

The in-scope list in the CFP is worth reading once, because it names the kinds of
contribution the prose must make legible: new insight about network structure or
performance; insight about application and end-user behaviour; measurement-based
modelling; monitoring methods; systems built on measurement findings; **reappraisal of
previous measurements**; and **descriptions of challenges and future directions**.
That last item is the one non-native authors under-use: IMC accepts a paper whose
contribution is a well-argued statement of what the community cannot currently measure.

---

## 1. Hard gates, and the sentence-level obligation each one creates

Source: IMC 2026 Call for Papers and Submission Guidelines
(<https://conferences.sigcomm.org/imc/2026/cfp/>,
<https://conferences.sigcomm.org/imc/2026/submission-instructions/>). Verify the numbers
on the current-year page before submitting; they have changed year to year.

| Gate | Requirement | Obligation in the prose |
|---|---|---|
| Length | Full paper: **13 pages** of technical content + unlimited references and appendices. Short: **6 pages**. A paper with more than 6 pages of technical content is reviewed as a full paper. | The body must be self-contained. Anything a reviewer needs in order to believe the claim belongs in the 13 pages, not the appendix. |
| Abstract | **≤ 200 words** | Measured: the median IMC abstract is 189 words. Twenty-nine percent of accepted abstracts exceed 200 — do not copy that; the limit is a stated rule and a desk-check item. |
| Template | `\documentclass[10pt,sigconf,letterpaper,anonymous,nonacm]{acmart}`; Letter paper; 10 pt; ≤ 55 lines per column | Two-column ACM layout means a figure costs half a page. Budget display items against the page limit, not against a word count. |
| Anonymity | Double-blind; own prior work in the **third person**; grant numbers removed. Exception: unique capabilities (a telescope, a private vantage point) may be named when blinding them would gut the paper. Public datasets and public platforms **should** be named. | "as we showed in [12]" is a violation. "Prior work showed [12]" is not. Naming RouteViews, RIPE Atlas, or a public dataset is allowed and useful. |
| Ethics | A **mandatory appendix section headed "Ethics"**; may be one sentence ("This work does not raise any ethical issues") but may not be missing. Human-subjects work needs IRB status. Discovered vulnerabilities need a disclosure discussion. | This is the **only appendix reviewers are required to read** (see the appendix rule below). Write it as prose, not as a checkbox. |
| Artifacts | A declaration of full / partial / no availability. With none, **explain why in a specific section**. Accepted papers are shepherded until the promised artifacts exist. | A refusal needs a reason and a cost statement, not a shrug. |
| Appendices | "may not be used to abuse page limits"; "apart from the Ethics section, reviewers are not required to read any of the appendices — and in fact will be discouraged from reading them"; appendices **cannot count towards the main contributions** | Any plot that is the primary evidence for a contribution must be in the body. An appendix is for the question a reviewer might ask next, not for the answer they must accept. |
| Figures | Must be legible in grayscale and to colour-blind readers; fonts ≥ 9 pt in figures | Say the takeaway in the caption; a caption that says "Figure 4: Results." is a wasted caption. |
| Language | Avoid charged terminology (ACM *Words Matter*) | "blacklist/whitelist" → "blocklist/allowlist"; "master/slave" → "primary/replica". |
| Generative AI | Acknowledgement required; footnote for phrases, appendix disclosure for larger passages | A footnote saying "generated by an LLM" is more damaging than the sentence it excuses. Rewrite instead. |
| Season | Two deadlines per year, with **one-shot revision** (accept / one-shot-revision / reject) | A revision is judged by whether the named action points were met. Prose that hides what changed makes the revision look evasive. |

---

## 2. The measured fingerprint

Sample A: **75 full texts** of IMC 2022–2025 papers (32% of the 237-paper programme;
reachable copies only — arXiv preprints and institutional repositories, since the ACM DL
refuses automated clients). Sample B: **all 237 camera-ready titles and abstracts** from
the programme pages. Compared against the 120-paper top-4 security corpus already used by
this skill, measured with the same splitter and the same regular expressions.

### 2.1 Prose, IMC vs top-4 security

| Metric | IMC (75) | top-4 security (120) | Reading |
|---|---|---|---|
| Mean sentence | 23.7 words | 23.1 | **No difference.** |
| Median / p90 sentence | 21 / 38 | 21 / 37 | **No difference.** |
| Sentences > 45 words | 5.5% | 4.1% | Marginally more long sentences. |
| Passive sentences | 19.0% | 21.6% | Slightly lower; both are far above the 12% magazine target. |
| Negation / 1,000 words | 5.7 | 5.5 | **No difference.** |
| Hedges / 1,000 words | 3.8 | 3.3 | IMC hedges a little more, because scope limits are part of the claim. |
| First person (we/our/us) / 1,000 | 22.1 | 20.4 | Slightly higher. |
| Em dashes / 1,000 words | **2.75** | **0.97** | IMC uses roughly **three times** the em-dash density. |
| **Sentences containing a digit** | **51.5%** | **39.7%** | The real difference: **every second sentence carries a number.** |

The headline: **IMC prose is not longer or more complex than security prose; it is more
numerical.** A revision that only shortens sentences has not moved the draft toward IMC.

### 2.2 The verb register

Most frequent `we <verb>` in the body text:

| IMC | count | top-4 security | count |
|---|---|---|---|
| we **find** | 457 | we use | 653 |
| we use | 384 | we also | 543 |
| we also | 344 | we can | 380 |
| we **observe** | 272 | we **evaluate** | 306 |
| we can | 180 | we consider | 269 |
| we have | 163 | we find | 256 |
| we do | 153 | we have | 237 |
| we **analyze** | 150 | we first | 229 |
| we **identify** | 134 | we **present** | 228 |
| we **see** | 133 | we **propose** | 225 |

`find` is IMC's most frequent verb; `evaluate` and `propose` are security's. This is the
register the venue expects: **observe, quantify, identify, compare — then interpret.**
A draft whose verbs are `design / implement / evaluate / outperform` reads as a systems
paper that happens to contain numbers.

### 2.3 What sections an IMC paper actually has

Share of the 75 papers with a heading of that role (layout-based detection, see §11):

| Section role | Present | Median position among named sections |
|---|---|---|
| Introduction | 98.7% | 0 |
| Background / Related work | 81.3% | 1 |
| Method / data collection / setup | 64.0% | 2 |
| Results or evaluation (generic name) | 40.0% | 3 |
| Discussion | 46.7% | 3 |
| Limitations (own section) | 26.7% | 3.5 |
| Conclusion | 78.7% | 4 |
| Acknowledgements | 78.7% | — |
| Appendix | 21.3% | — |
| Ethics (anywhere, usually appendix) | 92.0% | — |

Three readings:

- **Related work sits early** (median position 1): the second section in most papers. This
  differs from the security habit of pushing related work to §8.
- **Only 40% name a section "Evaluation" or "Results".** IMC papers name the middle
  sections after the thing measured ("The GFW", "Impact on the DNS ecosystem",
  "Nameserver inconsistency"), not after the activity. A section titled "Evaluation" is
  not wrong, but it is the minority choice.
- **Limitations is usually not a section** (26.7%). The limit is stated where the claim is
  made, in the same paragraph, and then discussed in the Discussion. A standalone
  "Limitations" section is acceptable but does not discharge the obligation to bound each
  claim locally (§7).

### 2.4 The abstract, at population scale (n = 237)

| Property | Value |
|---|---|
| Words | median **189**, mean 184, p90 231, max 303 |
| Over the 200-word limit | 29.5% (do not imitate) |
| Sentences | median 8; mean sentence 24.4 words |
| Contains a number | **82.3%** |
| Contains a percentage | 34.6% |
| Uses "we" | 95.8% |
| Opens with "We …" / "In this paper …" | **8.0%** |
| Opens with a property of the object ("X is …") | **52%** |
| Names a dataset | 15.6% |
| Claims "first" | 24.1% |
| Title length | median 10 words; 55.3% contain a colon; 24.5% contain measure/characterize/empirical; 1.7% are questions |

The opening frame distribution over all 237 first sentences:

| Frame | Share | Example shape |
|---|---|---|
| A property of the object | 52% | "Active DNS measurement is fundamental to understanding and improving the DNS ecosystem." |
| Other (usually a scene with a concrete actor) | 26% | "People can extract various kinds of information about the Internet from BGP routes tagged with BGP community values." |
| "We …" / "In this paper …" | 8% | — |
| A trend | 6% | "Over the last decade, Web traffic has significantly shifted towards HTTPS …" |
| A concession | 5% | "Given the importance of privacy, many Internet protocols are designed with privacy in mind …" |
| A dated event | 3% | "In 2019, the US Department of Homeland Security issued an emergency warning about DNS infrastructure tampering." |

### 2.5 Statistics vocabulary (share of the 75 papers using it at least once)

| Term | Papers |
|---|---|
| median | 57.3% |
| correlation | 58.7% |
| CDF / ECDF | 49.3% |
| percentile / p95 | 22.7% |
| a significance test (Wilcoxon, Mann-Whitney, KS, χ²) | 16.0% |
| bootstrap | 10.7% |
| regression | 9.3% |
| confidence interval | 6.7% |

Read this as a **license, not an obligation**: the median, the CDF, and the correlation are
house vocabulary; a confidence interval is a minority choice. If you report a difference
between two populations and claim it is real, a test or a CI is still the honest move even
though most papers skip it — that is a content decision, and this skill does not trade
correctness for house style.

### 2.6 Other measured habits

| Pattern | Share of 75 papers |
|---|---|
| Explicit contribution list ("we make the following contributions") | 25.3% |
| Explicit research question | 8.0% |
| Data / artifact availability statement | 69.3% |
| "to the best of our knowledge" | 32.0% |
| "in the wild" | 29.3% |
| "at scale" | 14.7% |
| An "Implications" or "Lessons" heading | 5.3% |
| Measurement vocabulary, per 1,000 words: measure\* | 3.0 (present in 100%) |
| dataset | 1.7 (89.3%) |
| sampling | 0.5 (72.0%) |
| coverage | 0.2 (48.0%) |
| vantage point | 0.3 (38.7%) |
| bias\* | 0.1 (36.0%) |
| ground truth | 0.1 (30.7%) |
| longitudinal | 0.1 (25.3%) |
| Figures per paper | median 9 (mean 9.9, max 36) |
| Tables per paper | median 5 (mean 4.8) |
| Digits per 100 body words | median 17.5 |

### 2.7 What does **not** differ (recorded so nobody "fixes" it)

- Sentence length, median, p90, and the share over 45 words are **the same** as top-4
  security. Do not shorten sentences in the name of IMC style.
- Negation density is the same. The existing L18 rule (negation-first framing costs the
  reader) still applies unchanged.
- Passive rate is *lower* in IMC than in security, but 19% is still high; the existing
  18% conference target stays.
- Only 25% of papers use an explicit contribution list, so **the absence of C1/C2/C3 is
  not a defect at IMC**, and the presence of one is not a virtue either. What the intro
  must do is still the five-link job from `paper-writing/references/introduction-anatomy.md`.

---

## 3. The IMC abstract: five moves, with the measured base rate

Write it last (see `references/abstract.md`, which measures the English abstract on 164 top-4
papers; that file's rule — the abstract narrates who did what — applies here unchanged). For
IMC, the shape that 82% of
accepted abstracts follow:

1. **The object and its stake**, one or two sentences, naming the protocol, system, or
   population — 52% open exactly like this. Not "In this paper".
2. **What is not known, or what is assumed and wrong.** The gap is about the Internet, not
   about your tool.
3. **What you did, at what scale, with what instrument.** Put the scale in the sentence:
   "we measure X across N vantage points over M months". This is where the number enters
   (82% of abstracts carry at least one).
4. **The finding, with its bound.** One sentence per finding, each with a number and a
   scope. Two findings beat five.
5. **What changes for the community** — what an operator, a protocol designer, or the next
   measurement should do differently. Half a sentence is enough.

**The opening is where IMC and the top-4 differ most.** `abstract.md` measures 54% of top-4
abstracts using `In this paper, we`; at IMC **8.0%** of first sentences open with
"We / This paper / In this paper" (definition: the first sentence of the abstract begins with
one of those three strings — `imc_abstracts.py`). The two measurements use different windows,
so read the direction rather than the gap: at IMC the first sentence is about the object, not
about the authors. The "who did what" rule from `abstract.md` is not repealed — a paper whose
abstract never says who measured anything still fails this skill's agent test.

Anti-patterns measured in the same sample, and what to do instead:

| Anti-pattern | Why it fails at IMC | Fix |
|---|---|---|
| Opening "In this paper, we …" (8% do) | Spends the most valuable sentence on the paper instead of on the Internet | Open with the object and a fact about it |
| No number anywhere | 82% of accepted abstracts have one; a measurement abstract without a quantity reads as a proposal | Add the scale you measured, even if the finding is qualitative |
| Five findings in eight sentences | Each gets half a sentence and no bound | Keep two, bound them |
| "First" with no bound (24% claim it) | Reviewers discount it; a bare "first" invites a counter-example | "to our knowledge, the first measurement of X across Y" |
| Tool-first framing ("We present a tool that …") | Reads as a systems contribution, which is a different (and harder) review | Lead with the finding; the tool is the method |

---

## 4. The IMC sentence: number **and** scope, in the same sentence

This is the single highest-yield revision for a draft written in security voice. A security
claim is bounded by a threat model stated elsewhere. An IMC claim is bounded **in the
sentence that makes it**, because the reviewer's first question is "over what population,
in what period, from where?".

Three moves, in order of preference:

**A. Put the scope in a second clause of the same sentence.**

> Before: We find that 12% of domains fail validation.
> After: We find that 12% of the 1.4M domains in our crawl fail validation, and that the
> failure rate is 3.1× higher for domains hosted on shared infrastructure.

The scope (`of the 1.4M domains in our crawl`) and the comparison ride in the same
sentence as the number. Nothing is weakened; the claim becomes checkable.

**B. Put the scope in a front adjunct when the reader needs it first.**

> Before: Measurements in 2023 show a shift toward encrypted DNS.
> After: Between January and December 2023, the share of queries we observe using
> encrypted DNS rises from 8% to 31% across our 14 resolvers.

**C. When the scope cannot fit, split and make the second sentence the bound — never
leave the number unbounded.**

> We measure 2.3M certificates. All of them come from certificate transparency logs, so
> the count excludes private CAs and anything not logged.

Test: cover the rest of the paragraph and read the sentence alone. If the number has no
population, no place, or no period attached, the sentence is not an IMC sentence yet.

**Numbers discipline that does not change:** never invent, never round silently, never
change a digit during polishing; every number keeps its unit and its denominator. If the
draft says "12%", the rewrite says "12%", and if the denominator is missing, that is a
question for the author (`[denominator?]`), not a guess.

---

## 5. Measurement verbs, and the register they create

| Use | Not this | Why |
|---|---|---|
| we measure, we collect, we crawl, we observe, we track | we evaluate | "Evaluate" implies a system you built and a metric you optimised |
| we find, we identify, we see | we demonstrate | "Demonstrate" promises a proof or a decisive experiment |
| we characterize, we quantify | we analyze deeply | Vague intensifier; the reader cannot check it |
| 12% of domains, up from 8% | performance improved | Prevalence is not performance |
| the failure rate is 3× higher | significantly worse | Unless a test was run, "significantly" is a statistical claim |
| we compare A and B | A outperforms B | Outperform needs a metric and a direction |

Two register rules:

1. **Do not promote a measurement to a system contribution.** If the artefact is a means,
   say so: "To answer this, we built X" — not "We present X, a system that …".
2. **Do not demote a measurement to an anecdote.** "Interestingly, we noticed …" turns a
   finding into a curiosity. State the rate and the population.

---

## 6. Section skeleton, and where the limits go

Measured order (§2.3): Introduction → Background/Related work → Data and method →
two to four content-named sections → Discussion → Conclusion. Ethics in the appendix.

**Naming.** Name the middle sections after the question they answer
("Where do these certificates come from?", "How stable is the answer over time?"), not
after the activity ("Analysis", "Experiments"). Only 40% of papers use a generic
"Evaluation"; the rest name the object. Both are acceptable; the content-named version is
the majority and it makes the contribution legible on the table of contents.

**Where limits go.** Three placements, all attested:

| Placement | Share | When it works |
|---|---|---|
| Inside the claim's paragraph, one sentence | most papers | Always. This is the default and it is not optional. |
| A Discussion section | 46.7% | When the limits interact (coverage bias feeds the temporal claim) |
| A standalone Limitations section | 26.7% | When a reviewer would otherwise hunt for it, or when the venue's shepherd asked |

A standalone section **never replaces** the local bound: a reviewer who reads only §4 must
still see what §4's number does not cover.

**Do not** put the primary evidence for a contribution in an appendix. The IMC
instructions say appendices "cannot count towards the paper's main contributions", and
reviewers are told they need not read them.

---

## 7. Validity language: the four questions an IMC reviewer asks

Every empirical claim in an IMC paper is read against these four. Write the answer into the
text before the reviewer writes it into the review.

### 7.1 Coverage — "who is missing from your data?"

> Template: "Our vantage points are 14 recursive resolvers in 6 countries, all operated by
> the same ISP; residential clients of other ISPs and all mobile networks are absent, so
> the rates we report are lower bounds for the population we care about."

Note the move: state the gap, then state the **direction** of the resulting bias. A limit
with a direction is a contribution; a limit without one is an apology.

### 7.2 Ground truth — "how do you know the label is right?"

> Template: "We validate the classifier against 500 hand-labelled domains (κ = 0.81). The
> residual error is concentrated in shared-hosting domains, where 6 of the 19 false
> positives occur."

### 7.3 Temporal validity — "measurements age"

> Template: "These measurements cover March–May 2024. Because the deployment we track
> changed twice during that window, the monthly series should not be read as a trend."

### 7.4 Ethics and disclosure — "would a reader object to how you got this?"

See §8. The Ethics appendix is the one appendix reviewers read.

**Wording that keeps the claim intact.** Weakening is not the same as bounding:

| Weak (loses the claim) | Bounded (keeps it) |
|---|---|
| "Our results may not generalize." | "Our results come from one eyeball ISP, so they generalize to that ISP's residential customers and to no other." |
| "There are some limitations to our approach." | "The crawl cannot see certificates issued by private CAs, which excludes enterprise deployments." |
| "We believe the trend is real." | "The trend holds in all six months of data and in both vantage points; we cannot test it before 2023, when the log format changed." |

---

## 8. Ethics, artifacts, and the one appendix that is read

Official text, worth quoting to a co-author who wants to skip it:

> "All papers must include, in a clearly marked appendix section with the heading 'Ethics',
> a statement about ethical issues; papers that do not include such a statement may be
> rejected."
> "Apart from the Ethics section, reviewers are not required to read any of the appendices."

So: the Ethics section is **inside the reading path**. Measured: 92% of the 75 papers carry
an Ethics heading, and among the 57 PDFs with camera-ready furniture it is 91%.

**Minimum viable Ethics section** (three sentences, in this order):

1. What the work touches: "This work analyses passive DNS traces from one ISP."
2. What was done about it: "Traces were collected under the ISP's standard data-processing
   agreement, pseudonymised at collection, and analysed only in aggregate."
3. What the reader should know: "No human subjects were involved; the study used
   operational data already collected for network management."

If the paper finds vulnerabilities, add a fourth sentence naming the disclosure: who was
contacted, when, and what the response was. IMC states that failing to disclose before
submission, without a convincing argument, "may be rejected".

**Artifact paragraph** (body or the artifact section, not a footnote):

> "Datasets and code are available at `[URL]`. The raw traces cannot be released because
> the ISP's agreement forbids redistribution; we release the per-domain aggregates and the
> analysis scripts, which reproduce every figure in this paper."

A "no" without a reason and a substitute reads as a refusal to be checked.

---

## 9. Anti-patterns specific to IMC

| Anti-pattern | Why it fails here | Fix |
|---|---|---|
| **Security framing**: "we propose a novel attack/defence" | IMC reviews the measurement, not the novelty of the mechanism | Lead with what the measurement reveals; the mechanism is the method |
| **Tool-first introduction** | Turns a measurement paper into a systems paper with a weaker evaluation | Object → gap → measurement → finding → implication |
| **Unbounded number** | The first reviewer question is "over what population?" | §4: number and scope in one sentence |
| **Generality by adjective** ("at scale", "in the wild", "large-scale") with no quantity | 29% of papers use "in the wild"; the phrase means nothing without a number | Replace with the count, or delete |
| **A "first" claim with no bound** | 24% of abstracts claim it; reviewers test it | "to our knowledge, the first … across …" |
| **A generic "Evaluation" section that evaluates the tool** | The venue wants findings about the Internet | Rename to the question; report what was learned, not how fast the crawler ran |
| **Statistics as decoration** ("significant" with no test) | A statistical word without a test is a claim about method | Either run the test or write "we do not test this; the difference is descriptive" |
| **Limits gathered at the end only** | Reviewers read sections, not the whole paper | Bound each claim where it is made |
| **Appendix as evidence** | Instructions: appendices cannot count toward contributions | Move the load-bearing plot into the body |
| **Empty Ethics section** ("This work does not raise any ethical issues.") when the work used user data | Reads as not having thought about it; the PC may ask | Say what data, under what agreement, with what aggregation |
| **Em-dash asides carrying the claim** | IMC tolerates 3× the dash density of security, but an L2 reader still pays for each one | One dash pair per paragraph; never put the number or the bound inside it |
| **Contribution list as the whole introduction** | Only 25% of IMC intros do this, and it flattens the argument | Keep the narrative; a short list may follow it |

---

## 10. Worked example

A measurement paragraph written in security voice, then in IMC voice. Claims, numbers, and
scope are preserved exactly; nothing is added that the data does not support.

**Before**

> We propose PHP2Shell, a novel approach to detecting malicious PHP web shells. Our system
> achieves high accuracy on a large-scale dataset. We evaluate PHP2Shell against several
> baselines and it outperforms them significantly. Moreover, we find that web shells are
> widely deployed in the wild, which is a serious threat to website security. Finally, we
> discuss the limitations of our approach.

**After**

> To measure how many PHP web shells are reachable on the public web, we scan 1.4M hosts
> drawn from the Tranco top-1M list plus 400k hosts discovered by following outbound links,
> once per week for 12 weeks (March–May 2024). We identify a web shell by requesting a
> small set of PHP files that a shell exposes and checking whether the response matches the
> shell's expected banner; the classifier is validated on 500 manually labelled hosts
> (κ = 0.81). Across the 12 weeks we find 6,214 reachable shells on 4,908 hosts — 0.35% of
> the hosts we could resolve — and the count is stable within ±6% week to week. The shells
> cluster on shared-hosting ASes: 71% of them sit in 12 ASes, which is 3.4× the
> concentration we would expect if they were spread in proportion to host count. Two
> limits bound these numbers. Our host list is a convenience sample of popular and
> link-reachable sites, so the rate is not a population estimate for the web; and our
> banner check misses shells that rename their entry points, which biases the count down
> and biases the AS concentration up, because renamed shells survive longer on cheap
> hosting.

What changed, and why each change is the IMC move:

1. The subject of the first sentence is now the thing measured ("how many PHP web shells are
   reachable"), not the tool.
2. Every number carries population, place, and period in the same sentence (§4).
3. `outperforms them significantly` became a rate with a comparison and no statistical
   claim the data cannot support (§5).
4. `widely deployed in the wild` became `0.35% of the hosts we could resolve` plus a
   concentration finding — an unbounded adjective became a bounded fact.
5. The limits moved from a closing gesture into the paragraph that makes the claims, and
   each limit carries its **direction** (§7.1).
6. The paragraph got longer. That is expected: at IMC, the same claim costs more words
   because it must carry its own bound. Do not measure this revision by word count.

---

## 11. How this was measured, and how to re-measure

Files live in the research workspace, not in this skill: `writing/imc/`. Scripts are
shipped here so the numbers can be reproduced against a fresh year.

| File / script | What it does |
|---|---|
| `harvest_imc.py` | Parses the IMC programme pages (2022–2025) into a DOI-anchored index: title, authors, session, length label, camera-ready abstract |
| `resolve_arxiv.py` | Maps each DOI to an arXiv id and any open mirror via OpenAlex |
| `unpaywall_pass.py` | Collects non-ACM repository copies (HAL, university repositories, arXiv) |
| `match_arxiv_by_title.py` | Second chance at full text: arXiv title search with a 0.90 similarity gate (returned nothing — see the caveats below) |
| `fetch_fulltext.py` | Downloads and text-extracts what is reachable; records provenance per paper |
| `imc_headings_pdf.py` | Recovers the section tree from PDF layout (bold / size / preceding number), not from line patterns |
| `imc_study.py` | Prose, sections, lexicon, statistics vocabulary, display items, per-paper record |
| `imc_abstracts.py` | Abstract and title study over the whole programme (population, not sample) |

**Sample caveats, to be repeated whenever these numbers are quoted.**

- Full text was reachable for **75 of 237** papers (32%). The gap is not random: papers
  with an arXiv or repository copy are over-represented, which likely over-represents
  authors who preprint and under-represents industry measurement papers.
- A second attempt was made to close that gap: an arXiv title search over 162 papers
  without full text (`match_arxiv_by_title.py`, accepting only near-exact titles at
  similarity ≥ 0.90, so that no wrong paper enters the corpus). **It returned no match on
  143 of them** (best similarity 0.73). The missing 68% are therefore not merely unlinked
  arXiv copies — they were not on arXiv under a searchable title, and no public mirror was
  recorded. That is a null result, and it is the honest limit of this sample.
- 76% of the 75 PDFs (57) carry camera-ready furniture (CCS Concepts, ACM ISBN); the rest
  are preprints. Statements about mandatory sections were therefore also checked on that
  camera-ready subset (Ethics: 52/57).
- Section roles come from a layout heuristic; the "40% name an Evaluation section" figure
  is a lower bound, because a content-named section doing evaluation work is invisible to
  the detector.
- Abstracts are the accepted-paper abstracts published on the programme site. They are the
  final text a reviewer saw, but not necessarily the copy-edited proceedings version.
- Four consecutive years (2022–2025) only. IMC before 2022 had a different template and a
  different ethics requirement; do not extrapolate backwards.
- A null result is recorded, not hidden: §2.7 lists the four prose metrics where IMC and
  top-4 security do not differ. If a future measurement contradicts these numbers, replace
  them — the thresholds in §2.1 are consequence-free, and this file should not outlive its
  evidence.
