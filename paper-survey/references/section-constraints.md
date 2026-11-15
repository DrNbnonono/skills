# Section constraints

Each of the nine sections has a job, a required artifact, and things it must not contain. These
are constraints, not suggestions: a section that lacks its artifact is incomplete even if it reads
well.

Lengths are given in **units** = Chinese characters + Latin word tokens (the checker counts this
way). Baselines come from a 9,157-unit report that was judged good; the range is a guardrail, not
a target. Write what the section needs; if you fall outside the range, check whether you are doing
another section's job.

| § | Baseline units | Range |
|---|---|---|
| 1 基本信息 | 381 | 200–600 |
| 2 目的与背景 | 1,087 | 600–2,000 |
| 3 范围与方法 | 834 | 500–1,600 |
| 4 相关工作 | 1,153 | 800–3,000 |
| 5 现状总结 | 738 | 400–1,400 |
| 6 空白与问题 | 1,717 | 900–3,500 |
| 7 可行性 | 892 | 500–1,800 |
| 8 初步思路 | 1,491 | 800–3,000 |
| 9 结论与建议 | 774 | 400–1,200 |

---

## §1 基本信息 / Basic Information

**Job.** Fix what is being studied before anything is argued. This is a scope statement, not an
introduction.

**Must contain (five labeled fields + one statement):**

1. **研究方向** — 3–5 domain keywords that a search engine could use.
2. **暂定研究主题** — one sentence, explicitly "暂定" (provisional), narrow enough to be wrong.
3. **核心研究对象** — the concrete components/data/mechanisms, not the field.
4. **研究目标** — two layers: (a) what we do now, starting from an existing result; (b) what
   method/contribution we aim at. Each 2–4 sentences.
5. **预期研究成果** — a numbered list of 3–5 *deliverables* (artifact, model, dataset, measured
   result), not research activities.
6. **阶段声明** — one sentence: what stage this is, and what the final shape depends on
   ("处于研究设计阶段，最终贡献将根据实验结果确定").

**Must not contain:** literature review, background narrative, conclusions, promises of impact.

**Checklist**
- [ ] The subject could be searched for with these keywords.
- [ ] Each expected output is something a reader could receive.
- [ ] The stage statement prevents the report from being read as a fixed plan.

---

## §2 目的与背景 / Purpose & Background

**Job.** Make the question inevitable, then state the questions.

**Must contain:**

1. **Background ladder** (3–5 paragraphs): infrastructure → existing mechanisms (SPF/DKIM/DMARC
   style: name the real mechanisms) → **one bold turning sentence** stating the tension
   ("协议能产生正确结果，不代表系统会正确使用") → the component chain where the problem lives.
2. **Existing findings**: the concrete anchor (advisory/CVE/GHSA id, date, CWE, affected
   component, one-sentence mechanism), clearly separated from candidates (`MSL-xxx，待确认`).
   End with the induction sentence: "这些现象提示……不是偶发缺陷".
3. **Research questions**: RQ1–RQ4, each = one question sentence + 2–3 sentences of
   scope/why-it-matters/boundary. The four should cover: prevalence, method, real impact,
   defence. (Number may differ; ≥2 required, ≥3 recommended.)
4. **A delimiting sentence**: what this study does *not* aim to prove

**Must not contain:** a textbook history of the field; RQs that are topics ("we study email
security"); a background that does not end at the gap.

**Checklist**
- [ ] Exactly one bold turning sentence, and the gap starts there.
- [ ] Every RQ can be answered by an experiment or a measurement, not by opinion.
- [ ] The "we do not aim to prove" sentence is present and specific.

---

## §3 范围与方法 / Scope & Method

**Job.** Make the boundary and the evidence rules explicit, so §4–§6 have a denominator.

**Must contain:**

1. **Scope table** (≥3 rows): 层次 / 研究对象 / 重点问题.
2. **Explicit exclusions**: what adjacent topics are *not* in the main search space (SPF/DKIM
   bypass, SMTP smuggling, …), and under what condition an adjacent object is admitted.
3. **Method list**: each method (literature, standards, historical advisories, source audit,
   dynamic experiment, real-deployment validation) in one sentence that says how and what it
   produces.
4. **Claim-grading rule** — the four-level ladder: protocol-allowed / potential anomaly /
   reproducible defect / upstream-confirmed vulnerability. State that inconsistency is not
   automatically a vulnerability.
5. **Ethics and access boundary**: what you may test, on whose systems, and what you will not do.

**Must not contain:** method names with no procedure; a scope that only lists inclusions.

**Checklist**
- [ ] A reader can tell whether a given paper/component is in or out.
- [ ] The grading rule can be applied to one concrete finding.
- [ ] The ethics boundary is operational, not decorative.

---

## §4 相关工作 / Related Work Survey

**Job.** Place each close work precisely, with what it did and the distance to this study.

**Must contain:**

1. **Search protocol** (here or at the start of §3): databases, venues, years, query terms, and
   the inclusion decision. This is the denominator for every "we did not find" claim.
2. **Comparison table** with at least these columns:

   | 研究工作 (link + venue + year) | 主要研究内容 | 对本研究的启发及区别 |

   - Every row: link + venue + year. A link without venue/year is not a citation.
   - The third column answers one of three distance questions: **object** (different unit),
     **method** (different technique), or **evidence** (different kind of proof). "Similar but
     different" is not a distance.
3. **What prior work established** (4–6 items): concede it first. The report must read as
   "they did X, so we cannot claim X".
4. **The closest 2–3 works and the entry point**: what remains, phrased as a question to be
   tested, not as a confirmed novelty ("这是需要验证的切入点，不是已证实的创新").

**Must not contain:** strawmen; rows without a distance; "相关" as a substitute for "区别"; a
survey paper used as a primary source without saying so.

**Checklist**
- [ ] The closest work is described in terms its authors would accept.
- [ ] Each row's distance is object, method, or evidence.
- [ ] Every "we did not find" in this report can point at this protocol.

---

## §5 现状总结 / State-of-the-Art Summary

**Job.** Compress §4 + §6 into judgments a decision-maker can act on. This section is not a
second related-work section.

**Must contain:**

1. **3–5 judgments**, each as a subheading + evidence + boundary note. Typical set:
   - the sub-area is mature (so incremental variants add little);
   - the standard already names the risk, but implementations vary (so implementation security
     is worth studying);
   - the missing piece is an empirical closed loop (classification + discovery + impact +
     mitigation);
   - our own base: confirmed advisory, environment, corpora, candidates.
2. **"Our current base" subsection**: assets (confirmed findings, testbed, corpora, candidate
   issues) and one sentence on **the most obvious shortfall**.
3. **Boundary sentence** on each negative judgment: "此判断仅在本次检索范围内成立，投稿前需复核".

**Must not contain:** paper-by-paper summaries; claims about the field as a whole without a
window.

**Checklist**
- [ ] Each judgment is falsifiable by one more search or one experiment.
- [ ] The shortfall sentence is honest and specific.

---

## §6 空白与问题 / Gaps & Open Problems

**Job.** Turn each gap into a checkable research problem. This is the report's load-bearing
section.

**Must contain (per gap, three parts — all three, always):**

1. **已有问题** — concrete evidence: a named implementation, mechanism, or measurement.
2. **研究空白** — what is missing, stated so that a result could fill it (a model, a method, an
   evaluation, a bound).
3. **拟解决问题** — what we would build/measure, with the invariant or metric that makes success
   checkable.

Plus:

- **≥3 gaps**, each named (`Gap 1：…`) with a one-line title.
- **Each gap traces to at least one row of §4** ("行 3 说明他们只测了 X，所以 Y 没有覆盖").
- **A closing sentence** naming the overall research focus ("预期研究重点：从单点漏洞推广到…").

**Must not contain:** "no one has studied X"; gaps that no experiment could close; gaps that do
not connect to §8; gaps that restate a prior paper's future-work section as if it were absent.

**Checklist**
- [ ] Each 研究空白 can be turned into an experiment or a system requirement.
- [ ] Each 拟解决 names an invariant, metric, or artifact.
- [ ] The gap set is mutually distinct (no two gaps are the same problem at two scales).

---

## §7 可行性初步分析 / Feasibility Analysis

**Job.** Separate "we can" from "it is risky", in a form that supports the stop/go decision.

**Must contain:**

1. **Technical base** (3–5 items), each in the form "已有 X，因此不需要从零做 Y".
2. **Feasibility/risk table** (≥5 rows): 研究任务 / 初步可行性 (高/较高/中等/低) / 主要风险.
3. **Major risks** (3–5): each with **触发条件**, **应对**, and **停止/转向条件**. A risk without
   a response is just worry.
4. **Overall judgment**: engineering readiness vs academic novelty, stated separately.

**Must not contain:** optimism without risk; a risk table whose "risk" column is empty; claiming
access (deployments, data) that is not secured.

**Checklist**
- [ ] Every risk has a response someone could execute next week.
- [ ] At least one stop condition is written.
- [ ] Dependencies are named (who grants access, what must be built).

---

## §8 初步思路 / 候选方案 / Preliminary Ideas

**Job.** Say how it would be done, and how success would be measured — without pre-claiming it.

**Must contain:**

1. **Core idea** in one bold sentence, and **one sentence** on how it differs from the closest
   method.
2. **Modules** (A–F): each with input, what it does, output, dependency. Modules must map to the
   gaps of §6.
3. **Experiment route table**: 阶段 / 主要任务 / 预期输出 / **退出条件** (P0–Pn, 4–6 stages).
4. **Evaluation metrics in three separate groups**: discovery capability, real-world impact,
   defence effectiveness. Each group 3–5 metrics, each with its denominator. End with the rule:
   "上述指标分别报告，不把异常数、候选数、确认漏洞数混为一个指标".
5. **Potential contributions** (3–5), with the sentence: novelty is not assumed, it will be
   decided by comparison with prior work.

**Must not contain:** a wish list with no milestones; metrics without denominators; contributions
stated as established.

**Checklist**
- [ ] Each module's output feeds the next, and the chain reaches an evaluation.
- [ ] The route has a cheap P0 that can kill the project early.
- [ ] The three metric groups are visibly separate.

---

## §9 结论与建议 / Conclusion & Recommendation

**Job.** Give the decision, the next step, and the condition under which the decision changes.

**Must contain:**

1. **Conclusion**: (a) the area is mature; (b) but the anchor finding shows a residual gap;
   (c) therefore this direction is worth continuing, and (d) the value is *not* re-proving the
   known risk but the listed four contributions.
2. **Next steps** by horizon: short (1–2 prerequisite validations, with "only if positive, then
   invest"), mid (method contribution), long (closed loop: root cause → method → new findings →
   impact → defence).
3. **Final positioning**: the existing draft/project is not a fixed frame; scope follows results.
4. **The core question** in a quote block: 1–3 sentences a future reader will remember.
5. **Conditional close**: "如果这些问题能得到…证据支持，本研究有望…" — conditional, not a promise.

**Must not contain:** ending on "very promising"; a recommendation with no stop condition; a core
question that restates the title.

**Checklist**
- [ ] The decision is explicit (continue / narrow / stop).
- [ ] The short-horizon step can be started immediately.
- [ ] If the short step fails, the report says what happens next.
