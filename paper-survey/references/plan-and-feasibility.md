# Plan and feasibility

§7 and §8 answer different questions: **can we** (capability, access, risk) versus **how would
it work** (method, route, metrics). Keep them separate; a plan that argues its own feasibility is
usually hiding a risk.

---

## 1. Feasibility: the four questions

| Question | What a good answer looks like | What fails |
|---|---|---|
| **Technical base** | "已有测试床 X（12 个组件），因此不需要从零搭建" | "我们有经验" |
| **Data and access** | "已获得 N 个授权部署；语料为公开邮件列表（GNU, lore），许可为…" | Assuming you can measure the internet |
| **Time and people** | Person-weeks per module; who owns which | "几个月应该够" |
| **Risk** | Trigger, response, stop condition | "难度较大" |

### Capability list

Three to five items, each: **asset → therefore not-from-scratch**.

```markdown
- **已有真实漏洞作为起点。** GHSA-xxxx 已获上游确认，可构建初始威胁模型与测试 oracle；
  因此不需要先证明缺陷存在。
- **已有跨组件环境。** 12 个组件、原始报文与日志采集能力；因此无需从零搭建实验基础设施。
```

### Feasibility/risk table

```markdown
| 研究任务 | 初步可行性 | 主要风险 |
|---|---|---|
| 已知漏洞复现与根因归纳 | 高 | 新版本可能已修复 |
| 消费者源码普查 | 高 | 可分析组件有限 |
| 定向发现系统 | 较高 | 静态分析误报与 oracle 错误 |
| 真实部署评估 | 中等 | 配置与版本信息不可见 |
```

Rules that make it useful (a table is easiest when there are many tasks; with three tasks, three
short paragraphs read just as well): every row's feasibility is one of 高 / 较高 / 中等 / 低, and
anything at 中等 or below reappears in the risk list below. A risk that is not on the list cannot
be monitored.

### Risk register

```markdown
**风险二：不同问题属于同一已知根因。**
触发条件：多个实现复现同样的行为，但都源于同一条标准警告被忽略。
应对：先建立根因去重流程，再统计"独立根因数"，不以"复现次数"计贡献。
停止条件：若 N 个候选中独立根因 < 2，则收窄为单一根因的深度研究，放弃"系统性发现"主张。
```

Every risk has **触发条件 / 应对 / 停止或转向条件**. A risk without a response is a worry; a
risk without a trigger cannot be monitored.

---

## 2. The plan: modules and route

### Module spec

Each module (A–F) answers four things, one sentence each:

| Field | Question |
|---|---|
| Input | what it consumes |
| What it does | the operation, in one verb phrase |
| Output | the artifact the next module consumes |
| Dependency | what must exist first (data, tool, access) |

A module that has no output consumed by another module is either a report or scope creep.

### Route table

```markdown
| 阶段 | 主要任务 | 预期输出 | 退出条件 |
|---|---|---|---|
| P0 漏洞复盘 | 复核公告与候选、版本回归、源码根因 | 已知漏洞模型、回归矩阵 | 至少 1 个可复现根因 |
| P1 系统挖掘 | 消费者审计、属性引导生成、异常确认 | 初版发现框架、独立候选 | 独立候选 ≥ 2 |
| P2 方法评估 | 与人工/通用变异对照 | 发现效率与覆盖率对比 | 显著优于基线 |
| P3 部署验证 | 受控与授权部署对照 | 成立条件、端到端影响 | 至少 1 条完整链路 |
| P4 防御消融 | 修复与合法流量回归 | 阻断率、误报、兼容性 | 兼容性可接受 |
```

Rules that make it credible — a table is optional, a numbered list works:

- **P0 must be cheap and fatal.** Its job is to kill the project early if the premise is false.
- **Every stage has an exit condition**, written as a number or a binary event.
- **No stage depends on a stage that has not been justified** (no "P3 requires internet-wide
  measurement" unless access is secured in §7).

---

## 3. Metrics: three groups, never mixed

The most common inflation is reporting one number for three claims. Keep them apart.

| Group | Answers | Example metrics (each with denominator) |
|---|---|---|
| **Discovery capability** | Can the method find things? | independent root causes found per test budget; precision of candidates (confirmed/total); coverage of consumer paths (paths hit/eligible) |
| **Real-world impact** | Does it matter in deployment? | vulnerable-in-deployment share (deployments vulnerable/tested); boundary-survival rate; positive-action rate |
| **Defence effectiveness** | Does the fix work and cost what? | block rate; false-positive rate on legitimate mail; loss of legitimate authentication results; compatibility on forwarding/lists |

Rules:

- Each metric: **numerator / denominator / window**.
- Report the three groups **separately**; never combine into "overall effectiveness".
- A metric that cannot move the §9 decision is decoration — cut it.
- Add one **cost** metric (person-weeks or test budget) per group, because efficiency claims need
  a denominator too.

The point is not the number of metrics. Two well-defined metrics with denominators are worth more
than six that measure the same thing.

---

## 4. Contributions are hypotheses

Write potential contributions as claims to be tested, not as achievements:

```markdown
本研究尝试形成以下潜在贡献，其成立取决于实验验证：
1. **信任边界模型** — 从真实漏洞抽象出可检查约束。
…
研究不预先假定以上各点都具有足够新颖性，而是通过与现有方法比较，决定最终保留哪些。
```

Never write "we propose a novel framework" in a survey report. The report's contribution is the
decision, not the system.

---

## 5. Stop / go criteria

Put the decision rule in §9, but derive it here:

- **Go** if: the P0 premise holds (≥1 reproducible root cause), ≥2 independent candidates
  appear in P1, and the deployment question is answerable with secured access.
- **Narrow** if: independent root causes < 2, or deployment access is unavailable — keep the
  single-root-cause depth study, drop the "systematic discovery" claim.
- **Stop** if: the premise fails (the known defect is not a class), or the closest work already
  covers the residue.

Writing this before the experiments is what separates a plan from a hope.

---

## 6. Before you call it done

- Can the reader tell which assets already exist and which must still be built?
- Does every risk have a response someone could execute next week?
- Is at least one stop condition written, and is it observable?
- Are the three metric groups visibly separate, each with a denominator?
- If P0 fails, does the report say what happens next?
