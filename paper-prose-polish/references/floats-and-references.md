# Floats and their references

A figure the reader meets before it has been introduced is worse than a figure on the next page:
the reader either skips it or reads it without knowing what to look for. This file is about the
**reading order of display items** — where a float sits relative to the sentence that first cites
it — and about the LaTeX mechanics that decide it.

Two layers are separated throughout:

- **Rules** that come from the venue's typography and LaTeX's float queue. These are mechanical,
  and breaking them is a defect.
- **Habits** measured on published papers. These are weaker evidence and are labelled as such.

---

## 1. What the venues require

IEEE's author material is explicit on two points, and both are production rules rather than style
preferences:

1. **A float appears near, but not before, its first mention in the text.** IEEE-derived style
   sheets repeat the phrase verbatim; the intent is reading order, not page geometry.
   ([IEEE-style tables/figures guidance](https://jecei.sru.ac.ir/jufile?issue_pdf=254))
2. **Introduce before, interpret after.** "Never drop a table or figure into your report without
   first introducing it and explaining why you are including it. Likewise, include some text after
   the illustration that summarizes or interprets the most important information in narrative
   form." ([IEEE tables and figures handout](https://my.eng.utah.edu/~ece3950/CLEAR_9_IEEE_TablesFigs.pdf))

And on captions: "It is good practice to explain the significance of the figure in the caption."
([IEEE Transmag author template](http://www.ieee.org/portal/cms_docs_iportals/iportals/publications/journmag/transactions/Transmag.pdf))

USENIX adds a constraint that interacts with placement: papers may not "squeeze space" by
manipulating layout, figures or tables; content alone must meet the page limit
([USENIX Security '25 policies](https://www.usenix.org/conference/usenixsecurity25/submission-policies-and-instructions)).
So shrinking floats or floating them into margins to fit pages is not an option.

---

## 2. The LaTeX mechanics that decide whether the rule holds

This is why "put it where it is discussed" is not simply a matter of typing `[h]`.

- **Floats are queued first-in, first-out.** `\begin{figure}` places the float into a queue at that
  point in the source. LaTeX then fills pages from the queue. The queue order is the source order,
  so **a float declared before its first mention can surface before the reader has been told about
  it** — no placement spec can undo that ordering.
- **In two-column IEEEtran, `[t]` is the reliable spec.** `[h]` is usually honoured as `[ht]` at
  best; `[b]` puts the float at the bottom of a column where discussion may already be over;
  `[p]` creates a float page and is a last resort.
- **`[!ht]` is a promise you cannot keep.** The `!` relaxes LaTeX's own restrictions, which can
  reorder floats relative to their neighbours and produce exactly the drift the reader notices.
- **`[H]` (float package) pins the float, but defeats column balancing.** In IEEEtran it commonly
  produces underfull columns and can push the bibliography. Use it only if the venue's template
  already allows the package.
- **`\FloatBarrier` (placeins) or a manual `\clearpage`** is the surgical tool when a float must not
  cross a section boundary — for example a table that belongs to the discussion and must not land
  in the conclusions.

Consequence: the author controls two things, **source order** and **the spec**; everything else is
LaTeX's judgement. The rules below are therefore written in terms of source order.

---

## 3. Rules

1. **Every float is cited in the body, at least once.** An unreferenced float is a defect: the
   reader has no instruction to look at it. Cite it, or delete it.
2. **The first citation precedes the float in the source.** Declare the float after the paragraph
   that first mentions it, so the queue order matches the reading order. This is the mechanical
   version of "near, but not before, its first mention".
3. **The citing sentence says what to look at**, not only that the float exists.
   - weak: "Table 2 reports the results."
   - strong: "Table 2, column *Lit.*, shows the four paths a reader would infer from the CVE text."
4. **A sentence after the float interprets it.** Repeat nothing from the caption; say what the
   reader should conclude.
5. **The caption stands alone.** One sentence with the takeaway, then the detail. A reader who
   jumps to the float and never reads the body must still get the claim.
6. **Default spec: `[t]`.** Use `[!ht]` only when the float is small and the section is short, and
   check the compiled PDF afterwards. Do not use `[H]` unless the template already loads `float`.
7. **Distance budget.** If the first citation and the float end up more than about one page apart
   in the compiled PDF, either move the float later in the source or add a pointer in the text
   ("Table 3, next page"). Authors cannot control the page, but they can control the queue.

### 3.1 The failure the reader actually sees

| Symptom | Cause | Fix |
|---|---|---|
| Float at the top of the page, first mention is halfway down the next column | float declared too early in the source | move the declaration below the first mention paragraph |
| Two floats swapped relative to their discussion | `[!ht]` on the first one | drop the `!`, keep `[t]` |
| A table lands in the conclusions | no barrier | `\FloatBarrier` before the conclusions, or move the table earlier |
| Reader cannot tell which panel is meant | reference names only the float number | name the panel, column, or axis |
| Caption duplicates the body sentence | caption and interpretation written together | caption states the takeaway; body states the consequence |

---

## 4. Pre-submission checklist

- [ ] Every float has at least one body reference.
- [ ] For every float, the first reference is above the float in the source.
- [ ] Each reference sentence names the panel/column/axis the reader should look at.
- [ ] Each float is followed by an interpreting sentence that does not restate the caption.
- [ ] Every caption is a sentence stating the takeaway.
- [ ] No orphan float files or unused labels in the repository.
- [ ] The compiled PDF has no float before its introduction, and no float separated from its
      discussion by more than one page.

---

## 5. What was measured, and why it is not a gate

`scripts/float_study.py` parses LaTeXML HTML (arXiv or the faster `ar5iv` mirror), reads the float
elements and the `Figure N` / `Table N` links, and computes the paragraph distance between a
float's element and its first body mention.

A 40-paper run produced numbers that **must not be used as thresholds**:

| Measure | Value | Why it is unreliable |
|---|---|---|
| Floats per paper, median | 23 | sub-figures are counted separately, so the true count is lower |
| Floats with at least one body reference | 69.7% | sub-figures are rarely cited individually, which depresses the figure |
| Float element before its first mention | 52.8% | this is **source order in the LaTeX**, not the printed page; authors often park floats near the top of the file |
| Captions classified as full sentences | 19.3% | the sentence detector needs a finite verb; many captions are noun phrases with a colon |

The honest conclusion: **HTML source order cannot tell you where a float lands on a page.** The
measurement measures the author's habit, not the reader's experience. Read the compiled PDF
instead — that is the only instrument that sees the page.

Keep the script for the narrower question it can answer (does this repository cite every float at
all?), and never turn its output into a gate.

---

## 6. This repository's paper (audited 2026-11-14)

| Check | Result |
|---|---|
| Tables | 5, all `[t]` except `04_rq2.tex:24` (`[!ht]`) |
| Figures | 4 `\input` (chain-tree, timeline, validated-cells, coverage-bar-new), all cited before the `\input` |
| **Unreferenced floats** | **`tab:typology` and `tab:rt-loo` are never cited in the body** |
| **Orphan figure files** | `fig3_heatmap.tex`, `fig4_coverage_bar.tex`, `fig5_artifact_growth.tex`, `fig6_advisory_cumulative.tex` are in `figures/` but not `\input` anywhere |
| Captions | mostly sentence-style with a claim (good); `tab:patch` is a bare title |

Actions, in order:

1. Cite the two appendix tables, or delete them. An appendix table that the text never mentions is
   dead weight and signals unfinished editing.
2. Delete or archive the four unused figure files; they will otherwise be re-included by mistake.
3. Change `[!ht]` to `[t]` in `04_rq2.tex`, then recompile and check that the table still lands on
   the page that discusses it.
4. For the two appendix tables, add "Table 4" / "Table 5" references at the paragraphs that
   interpret them (the typology paragraph and the LOO paragraph), with what to look at.

---

## 7. Magazine mode

A magazine feature inverts two of the rules and keeps the rest:

- **Placement is inline.** Practitioners expect the figure where it is discussed; a float that
  lands two pages later reads as a production error.
- **Fewer items, bigger.** Four to six display items, each carrying one message; the sidebar
  replaces the appendix table.
- **Captions carry the story.** A magazine reader may read only the figure and its caption, so the
  caption must state the claim, not the axes.
- Everything else holds: cite before it appears, say what to look at, interpret after.
