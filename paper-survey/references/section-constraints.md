# Section guide

For each section: the questions it must answer, what a convincing answer looks like, the failure
mode to avoid, and the questions to ask yourself before calling it done.

These are not completion forms. A section can answer its questions in three paragraphs of prose
with no table at all, or in one table plus two sentences. **Length is decided by the content, not
by this file.** Where a table is suggested, its columns are a recommendation for making the
comparison visible, not a requirement.

---

## §1 基本信息 / Basic Information

**Questions the reader needs answered**

- What direction is this, in words a search engine could use?
- Who is doing it, over what period, on top of which project document?
- What is the concrete subject — which components, data, or mechanisms, not which field?
- What are we trying to produce, and at what stage?

**A convincing answer** is a scope statement with metadata: topic/direction, researcher, duration,
link to the project document; a provisional topic sentence; the concrete subject; the goal in two
layers; expected outputs as things a reader could receive; and a sentence on what the final shape
depends on.

A four-cell header table is the easiest form (topic / researcher / duration / project doc), and
matches the template this skill was built from. Prose is fine if it carries the same four facts.

**Failure mode:** it turns into a background essay; the "expected outputs" are activities, not
deliverables.

**Self-check**
- Could someone search for this with these words?
- Is the topic narrow enough to be wrong?
- Does the reader know who asked and when the survey was done?

---

## §2 目的与背景 / Purpose & Background

**Questions the reader needs answered**

- Why does this question exist now, and what in the current state makes it live?
- What exactly must the study answer?

**A convincing answer** builds a short ladder: infrastructure → existing mechanisms (name the
real ones) → **one place where the expected protection stops holding** → the components where that
gap lives → what has already been observed (with a concrete anchor: advisory id, date, component)
→ the questions (RQ1…), each a question with a sentence of scope.

**Failure mode:** a field history that never turns toward the gap; RQs phrased as topics.

**Self-check**
- Can the reader point at the sentence where the problem becomes live?
- Can each RQ be answered by an experiment or a measurement, not by opinion?
- Is it clear what this study does *not* try to prove?

---

## §3 范围与方法 / Scope & Method

**Questions the reader needs answered**

- What is inside the scope, what is deliberately outside, and why?
- **How was the search done — keywords, venues/databases, time span** — so a later reader can
  check for omissions?
- When does a finding count as a defect rather than an inconsistency?

**A convincing answer** lists keywords, venues/databases, and the time span; names the adjacent
topics left out and the condition under which they would be admitted; and gives a rule for grading
a finding (protocol-allowed / potential anomaly / reproducible defect / upstream-confirmed).

**Four search methods worth naming** (they explain *how* coverage was achieved, and they are the
practical advice a new researcher needs):

1. **顺藤摸瓜 (citation chasing).** Start from the most recent 1–2 years of top-venue papers;
   their references already cover most prior work — trace backward from there.
2. **找综述 (Survey / SoK).** Use a survey or systematization for the taxonomy and the development
   line; faster than scattered reading, then verify primary sources.
3. **横向对比 (side-by-side comparison).** Line up method, assumptions, data, and metrics; what
   remains unsolved becomes §6.
4. **多渠道 (multi-channel).** News, technical blogs, HN/Reddit/Zhihu, vendor advisories, WeChat
   posts — for recency, real-world impact, and industry reaction that papers do not carry.

**Failure mode:** the scope only lists inclusions, so boundaries are invisible; methods are named
with no procedure; no time span, so "we did not find" cannot be checked.

**Self-check**
- Could a reader tell whether a given paper or component is in scope?
- Could a reader re-run the search from this description?
- Can the grading rule be applied to one concrete example?

---

## §4 相关工作 / Related Work Survey

**Questions the reader needs answered**

- Who is closest, and what did they actually settle?
- For each work: what is its **limitation**, and what can we **borrow** from it?

**A convincing answer** records each relevant paper/tool/project with five things: name, source
(venue/journal + year), core idea in one line, limitation or gap, and takeaway (what to borrow).
A table is the natural form when there are many:

| 论文/工具 Paper/Tool | 来源 Venue/Year | 核心思路 Core Idea | 局限性/差距 Limitation/Gap | 可借鉴点 Takeaway |
|---|---|---|---|---|

The table is a tool, not a quota: with three close works, a paragraph each carrying the same five
facts reads better. The point is that **limitation and takeaway are the load-bearing columns** —
a row without them is a citation, not a survey.

It ends by conceding what prior work established and stating the distance to this study in one
dimension (object / method / evidence).

**Failure mode:** strawmen; rows with no limitation; "related but different" with no dimension;
links without venue/year.

**Self-check**
- Would the authors of the closest work accept your one-line description of it?
- Does every row say what it cannot do, and what can be learned from it?
- Does §4 already contain the evidence that §6 will use?

---

## §5 现状总结 / State-of-the-Art Summary

**Questions the reader needs answered**

- What is settled, and what is not — as judgments, not as a second literature list?
- What is our own base, and what is its weakest point?

**A convincing answer** gives a few judgments (three to five usually), each with its evidence and
its boundary ("holds within the search window; needs re-checking before submission"). It includes
a short honest account of the team's assets and the most obvious shortfall.

**Failure mode:** re-summarising §4; claims about the field as a whole without a window.

**Self-check**
- Could any judgment be overturned by one more search or one experiment?
- Is the shortfall specific enough to act on?

---

## §6 空白与问题 / Gaps & Open Problems

**Questions the reader needs answered**

- What has existing work solved, where does it fall short, and what has nobody studied?
- Which of those gaps is real, i.e. not already solved and small enough to attack?

**A convincing answer** builds on the §4 comparison, not on impressions. The clearest structure
for each gap is three beats — what the problem is (with evidence), what kind of result is missing,
and what we would build or measure. A sentence that frames the three as "解决了什么 / 不够好在哪里
/ 尚未研究什么" is often enough before the numbered gaps.

**Failure mode:** "no one has studied X"; a gap that no experiment could close; a gap that does
not connect to any part of the plan; a gap that is really a prior paper's future-work section.

**Self-check**
- Can each gap be turned into an experiment or a system requirement?
- Is there at least one result that would prove the gap closed?
- Are two of the gaps secretly the same problem at different scales?

---

## §7 可行性初步分析 / Feasibility Analysis

**Questions the reader needs answered**

- Is the data obtainable? Is the technique within reach? What resources/tools are needed, and what
  will it cost in time?
- What are the risks, and what is the mitigation?

**A convincing answer** covers the five standard dimensions — data availability, technical
difficulty, required resources/tools, time cost, and risk — and gives each a concrete assessment
plus a risk/mitigation. A small table is the easiest form:

| 评估维度 Dimension | 情况 Assessment | 风险/应对 Risk/Mitigation |
|---|---|---|
| 数据可得性 Data availability | … | … |

The same content as three short paragraphs also works. What fails is a list of "we are
experienced" claims with no assessment of data or time.

**Failure mode:** optimism with no risk; risks without a mitigation; assuming access that is not
secured.

**Self-check**
- Does each dimension have a concrete answer, not an adjective?
- Does every risk have something we could do next week?
- Is at least one stop condition written?

---

## §8 初步思路 / 候选方案 / Preliminary Ideas

**Questions the reader needs answered**

- How could this be done — and is there more than one plausible route worth comparing?
- How would we know whether it works?

**A convincing answer** offers **candidate approaches**, not a single inevitable plan: two or
three routes with the trade-off between them, each described enough to discuss (what it assumes,
what it produces, what could go wrong). It states the core idea in one or two sentences, sketches
the pieces and how they feed each other, gives a staged route whose first stage is cheap and can
kill the project, and reports success in separate groups — can we find things, does it matter in
deployment, does the defence work — each with its denominator.

**Failure mode:** one approach presented as the only option; a wish list with no milestones;
metrics that mix three claims into one number.

**Self-check**
- Could a reader compare the candidates and say why one is preferred?
- Does each piece's output feed the next, and does the chain reach an evaluation?
- Is there a cheap first experiment that can change the decision?
- Are the three metric groups visibly separate?

---

## §9 结论与建议 / Conclusion & Recommendation

**Questions the reader needs answered**

- Is this direction worth pursuing as a formal project?
- What exactly is the next step — kick off / drop / keep surveying / discuss with advisor?

**A convincing answer** states the recommendation using one of those four outcomes (or a close
equivalent), the short-horizon step that comes first, what follows in the medium and long term,
and which existing draft or project is *not* treated as a fixed frame. It ends with the core
question someone would remember.

**Failure mode:** ending on "very promising"; a recommendation with no stop condition; a core
question that restates the title.

**Self-check**
- Is the recommendation one of the four outcomes, stated plainly?
- Can the short step start immediately?
- If it fails, does the report say what happens next?

---

## §10 参考文献与资料 / References & Links

**Questions the reader needs answered**

- Can every source named in the report be found, and can the reader tell what kind of source it
  is?
- Are the non-paper channels (news, blogs, forums, vendor advisories, WeChat) included where they
  carried the evidence?

**A convincing answer** lists sources with four things: type, title or outlet, link, and a note on
what it supports. A table is the easiest form:

| 类型 Type | 标题/来源 Title/Source | 链接 Link | 备注 Notes |
|---|---|---|---|

Prose or a plain list is acceptable if each entry still carries the type and the link; what fails
is a bare list of URLs, or a bibliography that silently drops the non-paper evidence the report
actually relied on.

**Failure mode:** links without type or venue/year; sources cited in the body but missing here;
grey literature mixed in without being labelled.

**Self-check**
- Is every in-text source present here?
- Can a reader tell a peer-reviewed paper from a blog post?
- Do the non-paper sources say what they contributed?
