# Section guide

For each section: the questions it must answer, what a convincing answer looks like, the failure
mode to avoid, and the questions to ask yourself before calling it done.

These are not completion forms. A section can answer its questions in three paragraphs of prose
with no table at all, or in one table plus two sentences. **Length is decided by the content, not
by this file.**

---

## §1 基本信息 / Basic Information

**Questions the reader needs answered**

- What direction is this, in words a search engine could use?
- What is the concrete subject — which components, data, or mechanisms, not which field?
- What are we trying to produce, and at what stage is this work?

**A convincing answer** reads like a scope statement: 3–5 keywords, one provisional topic
sentence, the subject, the goal in two layers (near-term from an existing result; longer-term
method), and the expected outputs as things a reader could receive. It ends by saying what the
final shape depends on.

**Failure mode:** it turns into a background essay; or the "expected outputs" are activities
("study X") rather than deliverables.

**Self-check**
- Could someone search for this with these words?
- Is the topic narrow enough to be wrong?
- Does the stage statement protect the report from being read as a fixed plan?

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
- How will evidence be gathered, and when does a finding count as a defect rather than an
  inconsistency?

**A convincing answer** states the layers being studied, names the adjacent topics left out (and
the condition under which they would be admitted), describes each method by what it produces,
and gives a clear rule for grading a finding — including the explicit note that inconsistency is
not automatically a vulnerability.

**Failure mode:** the scope only lists inclusions, so boundaries are invisible; methods are named
with no procedure.

**Self-check**
- Could a reader tell whether a given paper or component is in scope?
- Can the grading rule be applied to one concrete example?
- Are ethics and access boundaries operational, not decorative?

---

## §4 相关工作 / Related Work Survey

**Questions the reader needs answered**

- Who is closest, and what did they actually settle?
- Where is the distance — different object, different method, or different kind of evidence?

**A convincing answer** describes each close work in terms its authors would accept, then states
the distance as a sentence with a dimension. A comparison table is usually the clearest form
(work with link+venue+year / what it did / the distance), but a well-written paragraph per work
works too; the table is a tool, not a requirement. It concedes what prior work established before
explaining the residue, and ends with the entry point phrased as a question to be tested.

**Failure mode:** strawmen; "related but different" with no dimension; links without venue/year;
a survey paper used as a primary source without saying so.

**Self-check**
- Would the authors of the closest work accept your one-sentence description of it?
- Is the distance object, method, or evidence?
- Does §4 already contain the evidence that §6 will use?

---

## §5 现状总结 / State-of-the-Art Summary

**Questions the reader needs answered**

- What is settled, and what is not — as judgments, not as a second literature list?
- What is our own base, and what is its weakest point?

**A convincing answer** gives three to five judgments, each with its evidence and its boundary
("this holds within the search window; needs re-checking before submission"). It includes a short
honest account of the team's assets and the most obvious shortfall.

**Failure mode:** re-summarising §4; claims about the field as a whole without a window.

**Self-check**
- Could any judgment be overturned by one more search or one experiment?
- Is the shortfall specific enough to act on?

---

## §6 空白与问题 / Gaps & Open Problems

**Questions the reader needs answered**

- Which gap is real, and why is it not already solved?
- What would closing it look like, and how would we know it was closed?

**A convincing answer** takes each gap through three beats — the concrete problem with evidence,
the missing kind of result, and what we would build or measure — as prose. A table or numbered
list of gaps helps when there are many; with three gaps, three short subsections are enough.
Each gap should visibly trace to something in §4, and end at something checkable (an invariant, a
metric, an artifact).

**Failure mode:** "no one has studied X"; a gap that no experiment could close; a gap that does
not connect to any part of the plan.

**Self-check**
- Can each gap be turned into an experiment or a system requirement?
- Is there at least one result that would prove the gap closed?
- Are two of the gaps secretly the same problem at different scales?

---

## §7 可行性初步分析 / Feasibility Analysis

**Questions the reader needs answered**

- Can we do it with the assets and access we actually have?
- What could stop us, and how would we notice in time?

**A convincing answer** lists what already exists and therefore does not need building; states the
tasks with an honest feasibility level; and gives the major risks with a trigger, a response, and
a stop condition. A table makes this easier to compare but is not required; a short paragraph per
risk is equally readable.

**Failure mode:** optimism with no risk; risks without a response; assuming access that is not
secured.

**Self-check**
- Does every risk have something we could do next week?
- Is at least one stop condition written?
- Are dependencies named (who grants access, what must be built)?

---

## §8 初步思路 / Preliminary Ideas

**Questions the reader needs answered**

- How would this actually be done, end to end?
- How would we know whether it works, and whether it is better than what exists?

**A convincing answer** states the core idea in one or two sentences and what it changes compared
with the closest method; sketches the pieces and how they feed each other; gives a staged route
where the first stage is cheap and can kill the project; and reports success in separate groups —
can we find things, does it matter in deployment, does the defence work — each with its
denominator. Potential contributions are written as hypotheses, not achievements.

**Failure mode:** a wish list with no milestones; metrics that mix discovery, impact, and defence
into one number; contributions claimed as established.

**Self-check**
- Does each piece's output feed the next, and does the chain reach an evaluation?
- Is there a cheap first experiment that can change the decision?
- Are the three metric groups visibly separate?

---

## §9 结论与建议 / Conclusion & Recommendation

**Questions the reader needs answered**

- What is the decision, and what is the next step?
- What would change the decision?

**A convincing answer** states the decision (continue / narrow / stop), the short-horizon step
that comes first, what follows in the medium and long term, and which existing draft or project
is *not* treated as a fixed frame. It ends with the core question someone would remember.

**Failure mode:** ending on "very promising"; a recommendation with no stop condition; a core
question that restates the title.

**Self-check**
- Is the decision explicit?
- Can the short step start immediately?
- If it fails, does the report say what happens next?
