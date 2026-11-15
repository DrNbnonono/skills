# Evidence and claims

The report is trusted because every claim carries its status. This file defines the statuses,
the wording, and the traps.

---

## 1. The four grades

| Grade | Name | What qualifies | How it is written |
|---|---|---|---|
| **E1** | Confirmed | Official advisory (CVE/GHSA), merged fix, vendor security bulletin, or a peer-reviewed result we reproduced | cite id + date + component |
| **E2** | Reproduced | We ran it in a recorded environment, with logs or artifacts | "our run, N/M configurations, `runs/…`" |
| **E3** | Candidate | Behavior consistent with a defect; no upstream confirmation yet | "候选 `MSL-xxx`，待维护者确认" |
| **E4** | Inferred | Analogy, source-code reasoning, or hypothesis | "如果实现遵循同样的模式，则可能…" |

### Promotion rules

- **E3 → E1** requires an external confirmation: advisory, merged fix commit, or maintainer reply.
  An independent reproduction moves E3 to E2, not to E1.
- **E4 → E3** requires at least a code-level mechanism or a reproducible behavior, not intuition.
- **E1 → E2** is possible when the original report cannot be reproduced; say so explicitly
  ("公告已确认，但我们在 N 个版本上未能复现").
- Never promote in the middle of a section without writing the new grade.

### Where each grade may appear

| Section | Allowed grades |
|---|---|
| §1 | none (scope only) |
| §2 | E1 + E3 (anchors and candidates), never E4 as fact |
| §3 | E1 (standards, protocol text) |
| §4 | E1 (published work); E3 only if labeled "preprint/unconfirmed" |
| §5 | E1/E2 for own base; boundary statements for everything negative |
| §6 | E1/E3 in 已有问题; E4 allowed only inside 拟解决 as a hypothesis |
| §7 | E2 for own assets; E4 for projections, marked |
| §8 | E4 by default (it is a plan) |
| §9 | inherits, no new facts |

---

## 2. Wording rules

### Scope a negative claim

| Don't write | Write |
|---|---|
| "X has never been studied." | "在本次检索范围内（S&P/USENIX/CCS/NDSS + IMC/WWW，2018–2025），未找到同时覆盖 A 与 B 的工作。" |
| "There is no method for X." | "我们未找到把 A 用于 B 的公开方法；最接近的是 [work]，它只做到 C。" |
| "No one has measured Y." | "Y 的测量仅见于 [work]（单一服务商）；跨组件测量未见报道。" |
| "The first systematic study of Z." | "据我们所知，首个把 Z 作为一类问题系统处理的工作；检索见附录。" |

The formula: **negative claim = object + window + venues + query + what would change our mind.**
The checker flags "首次/填补空白/尚无/前所未有" without a scope phrase nearby.

### Grade the claim, not the topic

- "该漏洞可导致认证绕过" — needs E1/E2.
- "该类缺陷可能普遍存在" — E4, must be written as a hypothesis.
- "已有 3 个独立实现出现同类问题" — E1 count, with links and dates.

### Numbers

Every number needs: **n** (denominator), **window** (when), **unit** (what is counted), and
**source**. Examples:

- "在 35 个邮件服务商中，X 的检出率为 4/35 (11%)，采集于 2018 年 [link]。"
- "中位数 6.9 年（样本：N 个漏洞，来源 [link]）。"

A percentage without n, a ratio without direction (which over which), or a count without a
window is not a measurement.

---

## 3. Source record format

Every row of evidence (including the appendix) carries:

```
[short id] Authors/Org, Title, Venue Year. URL.
What it establishes: one sentence.
What it does not establish: one sentence.
Grade: E1 (peer-reviewed) / E3 (preprint)
```

Rules:

- **Link + venue + year.** A bare URL is not a citation.
- **Secondary sources** ("转引") are labeled as such and, when the claim is load-bearing, traced
  to the primary source.
- **Vendor statements** are E1 for "the vendor says X", E3 for "X is true".
- **Blog posts and vendor audits** can be E2/E3 evidence when dated and specific; they are never
  E1 for a general claim.

---

## 4. Ten traps

1. **Single case → class.** One implementation's bug is one implementation's bug; the class claim
   needs N ≥ 2 independent implementations or a stated hypothesis.
2. **Candidate → confirmed.** A maintainer's silence is not a confirmation.
3. **Absence → nonexistence.** "Not found" is a search result, not a property of the field.
4. **Correlation → cause.** Two numbers moving together, in an observational window, is an
   association; say so.
5. **Vendor claim → fact.** "Fixed in version X" is E1 for the claim, E3 for the fix's
   completeness.
6. **Prototype → deployment.** Laboratory reachability does not imply internet exposure; separate
   "vulnerable component", "default-enabled", "reachable in deployment", "impactful".
7. **Anomaly → vulnerability.** Inconsistent outputs are E3 until a security consequence is shown.
8. **Known limitation → new gap.** If RFC/paper already states it, the gap is implementation or
   measurement, not knowledge.
9. **Different wording → different problem.** Two names for the same defect is one gap.
10. **Plan → result.** §8 is a hypothesis about a method; it is not evidence.

---

## 5. When you are not sure

Write the uncertainty instead of hiding it:

- "我们未能在当前版本复现（3 个版本，N 次运行），但公告与源码看起来一致；差异可能来自配置（E2/E1 冲突）。"
- "若把 X 视为可信来源，则结论成立；该前提在部署中是否常见尚不清楚（E4）。"

An explicit uncertainty is a finding. A silent hedge is a future retraction.

---

## 6. Self-check before submitting the report

- [ ] Every factual sentence has a source or `[unverified]`.
- [ ] Every negative/"first" claim names the window and venues.
- [ ] Every candidate is labeled E3 or lower.
- [ ] Every percentage has a denominator.
- [ ] No grade was promoted without writing it.
- [ ] The appendix lists queries and the evidence that did not fit.
