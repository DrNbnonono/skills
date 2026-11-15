# Changelog

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
