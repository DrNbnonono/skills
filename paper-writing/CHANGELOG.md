# Changelog

## v1.2.2 - the magazine abstract is 50 words, not 200

One line in `references/abstract.md` said "magazine: ≤200 words". The IEEE Security & Privacy
Magazine author page states "The abstract word limit is 50 words", and 200 published abstracts
(2022-2025) measure median **40 words**, **2 sentences**, 61% `we`/`our`, 15% any number. The 200
figure came from a secondary source describing IEEE journals. Corrected here to 50; the revision
layer in `paper-prose-polish` (`references/abstract.md` section 10, `--abstract --venue magazine`)
carries the measured magazine shape and the linter check.

---

## v1.2.1 - ship the two study scripts

Packaging only, no text change. `references/introduction-anatomy.md` and
`references/intro-annotation-rubric.md` cite two scripts that were not in the repository:
`scripts/build_intro_kit.py` (builds the annotation kit) and `scripts/aggregate_annotations.py`
(aggregates the five annotators' labels). Both are now shipped so the annotation study can be
repeated on another corpus. Version bumped here and in `SKILL.md` and the repository README so
the three stay in step.

---

## v1.2 - the four deferred measurements, finished

v1.1 left four things unmeasured and said so. This round measures them and fixes three denominators
that were inflating earlier numbers.

### Introductions, annotated (99 papers, five annotators)

| Move | Present | Median position in the intro |
|---|---|---|
| Where the problem comes from | **100%** | 0.00 |
| Why it is worth answering | 76% | 0.12 |
| How it is answered | **100%** | 0.38 |
| How far the evidence reaches | **58%** | 0.62 |
| What we now know | 90% | 0.78 |

The spine is real and monotone. 45% of introductions carry all five moves, 33% four, 20% three.
The two weak links are importance (76%, and only ~25% under a strict "named blocked decision"
reading) and boundary (58%). Openings: 63% a specific claim, 36% a general trend statement, and only
**1.7%** the stock "in recent years" phrase -- both numbers are reported, because they answer
different questions. Explicit RQ: 24% (annotated) vs 37% (regex), a definitional gap, reported as a
range.

New: `references/introduction-anatomy.md`, and `references/intro-annotation-rubric.md` so the
measurement can be repeated on another corpus. Scripts: `build_intro_kit.py`,
`aggregate_annotations.py`.

Annotator variance is reported rather than smoothed: the strict batch found importance in 25% of its
papers, the lenient ones in 95-100%. The disagreement is itself the finding -- authors state severity,
not the decision that is blocked.

### Evaluation subsections (60 papers)

Median **4** subsections (max 11); a setup subsection in 53% (first in 47%); a summary/discussion
subsection last in only **5%**; a named ablation in 13%; a named sensitivity subsection in 5%; and
**62% of subsection titles are claim-specific** rather than generic. The evaluation is organised
claim by claim, not by a fixed vocabulary.

### Figure types and palettes

A manual sample of six figures: **all six were diagrams or screenshots**, none a quantitative plot --
security figures carry the mechanism, tables carry the numbers. Colour, with top-level display items
and three share thresholds:

| Measure | Value |
|---|---|
| Display items per paper (top-level) | median **17** (was 36 with sub-figures) |
| In the appendix | **10.9%** |
| Hues at 3% / 5% / 10% threshold | median **3 / 2 / 2**; >=4 hues in 35% / 31% / 17% |
| Red+green pair | 18% |

### Denominator fixes

- Floats per paper: 36 -> **17** by counting only top-level figures/tables.
- Appendix share: 11.4% -> **10.9%** with the same correction.
- Hue breadth: a single number -> a **3/5/10% threshold range** (the median is stable, the ">=4
  hues" share is not).
- Appendix topics: noted that titles can match several topics, so the column does not sum.

### Still not measured

Inter-annotator kappa (no double coding); the figure-type distribution at n>6; the five-move
positions for the 21 papers whose extracts were truncated. All three are stated in the files rather
than implied away.

---

## v1.1 - anatomy, evidence first, and a Chinese questionnaire

v1.0 said what each section must do. v1.1 adds what 120 papers actually do, and a mechanism for
turning a pile of experiments into a draft.

### Added

- **`references/results-arrangement.md`**: the measured shape of evaluations (78.3% have one, median
  24 paragraphs, 2-3x the introduction), the claim-to-subsection mapping, the default order, the four
  sentences every results subsection needs, and six failure modes.
- **`references/appendix-catalog.md`**: appendices exist in 60.8% of papers, 3.4 sections each;
  topics ranked by frequency (parameters 16, additional results 11, proofs 11, protocol 10, ...);
  what belongs, what does not, and a decision checklist.
- **`references/figures-in-the-argument.md`**: one figure one claim, chart type by claim type, and
  the first measured palette data (50 figures, 20 papers): median 2 hues, 32% with >=4 hues, **18%
  using a red+green pair**, saturation 0.47, luminance std 55.
- **Step 3.5 results inventory** in `SKILL.md`, plus `templates/results-inventory.md`: every result
  mapped to the introduction claim it settles, then to a subsection and a display item. This is the
  "enough experiments produce a near-complete draft" path -- the draft is the mapping, and holes in
  the mapping are missing experiments, not missing paragraphs.
- **`templates/paper-plan.zh.md`**: the full questionnaire in Chinese, for authors who think in
  Chinese. Same sections, same `?` convention.

### Measured (120-paper corpus)

| Property | Value |
|---|---|
| Introduction: median paragraphs / words | 10 / 1,032 (p90 15 / 1,531) |
| Opens with boilerplate ("In recent years...") | **1.7%** |
| States a research question explicitly | 36.7% |
| Announces contributions in prose | 20.8% (bullet lists invisible to this count) |
| Ends with a roadmap | 17.5% |
| Evaluation section present | 78.3%; median 1 section, 24 paragraphs |
| Appendix present | 60.8%; 3.4 sections each |

The boilerplate figure is the strongest single number in this skill: accepted top-tier introductions
essentially never open with "in recent years" (1.7%), which is the opposite of what many drafts do.

### Not changed

The story spine, the skeleton choice, the drafting order (introduction and background first, abstract
last), and the non-negotiables.

---

## v1.0 - the story, before the sentences

A writing skill that starts at the research question and ends at the abstract, built from a
practice-tested account of how a paper tells a story (question -> why it matters -> how it is
answered -> how far the evidence reaches -> what we know now) and from measured conventions in 120
top-tier security papers.

### Contents

- **`SKILL.md`**: the one rule (nothing enters the paper that does not answer the RQ), the six
  steps (RQ gate -> venue and skeleton -> story spine -> section plan -> terminology and display
  items -> drafting order), drafting order (intro and background first, abstract last), compliance
  pass, seven non-negotiables.
- **`references/story-spine.md`**: the five links, the work-order/reading-order diagnosis, the
  failure and repair for each link, and the spine used as a research checklist.
- **`references/section-blueprints.md`**: per-section job, measured convention, common failure, for
  title through conclusion.
- **`references/abstract.md`**: four elements, three properties, four failure modes, a working
  8-move shape, and a field-difference table.
- **`references/appendix-and-display-items.md`**: the four-question body/appendix test, what
  typically goes where, measured appendix share, display-item rules.
- **`templates/paper-plan.md`**: the author questionnaire (RQ, spine, skeleton, section claims,
  terminology, display items, gaps, abstract), designed so that `?` marks become the agenda.
- **`scripts/story_study.py`**: reproduces the measurements below.

### Measured

On 120 top-tier security papers (arXiv abstracts):

| Property | Value |
|---|---|
| Abstracts using "we" | **99.2%** |
| Median length | 212 words (p10 146, p90 271) |
| Median sentences | 9 |
| Carries a number | 70.8% |
| Carries a percentage | 32.5% |

On 30 papers (appendix share of display items): **11.4%** of items in the appendix; 18/30 papers
have at least one. Counts include sub-figures, so the number is an order of magnitude, not a target.

### Deliberately not copied

The abstract guidance supplied by the author comes from the Chinese-journal tradition, where the
third person is required and "本文/作者" is discouraged as a subject. Measured on English security
papers, 99.2% of abstracts use "we". The transferable part (self-contained, independent, no
overclaiming) is kept; the person rule is inverted in `abstract.md`, with the evidence.

---
