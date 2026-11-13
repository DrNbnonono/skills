# skills

Some skills created by dr. Each folder is a self-contained skill: drop it into
`~/.claude/skills/` (global) or `<project>/.claude/skills/` (per project) and it is picked up
by the agent.

| Skill | What it does | Version |
|---|---|---|
| [`paper-prose-polish`](paper-prose-polish/) | 逐句润色英文安全/系统论文：测量 → 术语锁定 → 逐句改写 → 首读门槛 + 连贯性验收 | 2.5.1 |
| [`paper-figures`](paper-figures/) | 论文图表设计、绘制与验收：图表选型 → 统一风格 → 导出 → 灰度/色盲/字体检查，附带示例图 | 1.0 |

两者都面向 **S&P / USENIX Security / CCS / NDSS** 以及 IEEE S&P Magazine 的写作与配图。

---

## paper-prose-polish

动机很直接：**如果一个英语不是母语的读者不能一遍直接读懂，这句话就是有问题的**，不管它语法
多正确、听起来多地道。v2 把这句直觉变成了可执行的判定：首读测试（不回头、不停顿、不翻译）、
阴影测试、陌生人复述测试，以及四个 L2 阻塞指标（主动词前的词数、从句数、习语/短语动词、不透明
正式词）。

v2.5 再加一条约束：**统计指标是目标，句子与句子之间的连贯性是底线**。拆分是为读者服务的，
不是为了把 p90 压到阈值以下；如果满足指标必须切断指代、因果或"主张—限定"关系，就**放弃这个
指标并记录原因**（claim fidelity > coherence > metrics）。

v2.5.1 补一句同样重要的：**原文已经写得好的句子和段落，就保持 KEEP，不要改**。这个 skill 是
"读者卡点检测器"，不是"必须改出点什么"的任务清单；一轮里只有三处真问题，就是一轮好活。

包含：

- `references/comprehension-gate.md` — 首读门槛：三个测试、S1–S8 卡顿分类、8 组改写示例
- `references/coherence.md` — 连贯性约束：三级优先序、三处接缝（指代/逻辑/话题）、可拆与
  不可拆的位置、MERGE 回并、段落级连贯性检查、指标未达标时的记录模板
- `references/vocabulary.md` — 「透明优先」：对 L2 读者而言，`holds up` 比 `remains exploitable`
  更难；习语/短语动词替换表、歧义连接词表、什么**不要**简化
- `references/venue-prose-corpus.md` — 四大会议在散文层面奖励什么；可复现的语料测量协议
- `references/sentence-rules.md` — L1–L23 规则（v2.5 新增 L21–L23：拆在接缝、拆后补缝、必要时回并）
- `references/rubric.md` — 五问、缺陷码 A1–A21、六种判决（新增 MERGE）、八种手术动作
- `references/diagnosis-playbook.md` — 测量与阈值（含 L2 阻塞指标与 flow 诊断）
- `references/magazine-mode.md` — 会议论文改杂志体
- `scripts/lint_prose.py` — 句长/被动/名词化/破折号 + L2 指标 + 否定指标；`--gate` 通过/不通过，
  `--explain N` 列出卡顿最多的句子，`--flow` 报告节奏与接缝问题（短句连排、重复开头、连接词过密）
- `templates/revision-table.md` — 每轮修订记录表（含接缝判定与"未达标指标"栏）

```bash
python scripts/lint_prose.py --path paper/ --glob "*.tex" --json baseline.json
python scripts/lint_prose.py --path paper/ --gate --venue magazine --explain 10 --flow
```

---

## paper-figures

一张图 = 一个主张。这个 skill 把四大会议强图共有的部分固定下来：单栏 3.5 in、8 pt 字、
Okabe–Ito 配色、矢量导出、灰度可读、caption 第一句就给结论。

包含：

- `SKILL.md` — 七步流程：先写主张 → 选编码 → 统一风格 → 直接标注 → 打印安全 → 导出 → 验收
- `references/encoding-guide.md` — 主张到图表的映射（CDF、dumbbell、swimlane、heatmap、
  small multiples、Pareto）、不确定性、何时表格更好、坐标轴完整性
- `references/venue-figure-profiles.md` — 各 venue 的栏宽、caption 规则、显示项预算，以及
  会议/杂志/期刊之间会变的规则
- `references/style-spec.md` — 每个 matplotlib 设置及其理由、配色 hex、LaTeX 引用方式
- `references/captions.md` — caption 公式与好坏对照
- `references/accessibility.md` — 色盲、灰度、对比度、alt text
- `references/production.md` — 矢量导出、字体嵌入、camera-ready 清单、常见编译问题
- `references/anti-patterns.md` — 15 种坏图与修法
- `scripts/figure_style.py` — rcParams、调色板、`new_fig/save/panel_label`
- `scripts/make_examples.py` — 生成 `examples/` 下全部示例（合成数据，固定种子）
- `scripts/check_figure.py` — 尺寸/dpi 检查、灰度与色盲预览、配色塌缩告警
- `examples/` — 9 张参考图 + 一张「坏图 vs 好图」对照 + 灰度版；`examples/README.md` 说明
  每张图演示哪条规则

```bash
python scripts/make_examples.py
python scripts/check_figure.py "examples/*.png" --preview
```

示例图全部由代码生成，数据是合成的：仓库保存的是**风格**，不包含任何已发表论文的图。

---

## 版本

- `paper-prose-polish` v2.5.1：v2.0 首读门槛；v2.1 否定规范；v2.2 改写权限与 DELETE 判决；
  v2.3–v2.4 语料研究（局部缺陷、结构/位置）；v2.5 连贯性约束（接缝三测、MERGE、`--flow`）；
  **v2.5.1 明确「原文已经写得好就不改」**（KEEP 是正常结果，不是失败）。
  每次改动的实测数字与 null result 见
  [`CHANGELOG.md`](paper-prose-polish/CHANGELOG.md)。
- `paper-figures` v1.0：初版。
