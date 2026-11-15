# skills

Some skills created by dr. Each folder is a self-contained skill: drop it into
`~/.claude/skills/` (global) or `<project>/.claude/skills/` (per project) and it is picked up
by the agent.

| Skill | What it does | Version |
|---|---|---|
| [`paper-survey`](paper-survey/) | 论文前期调研（方向调研与可行性论证）：九节阅读顺序，目的是让读者看懂调研了什么、为什么得出这个结论；不设字数、不强制表格，准确性约束（E1–E4、有界否定）保留 | 1.1 |
| [`paper-writing`](paper-writing/) | 论文从 RQ 长出来：故事五问 → 结构选型 → 结果清单 → 章节主张 → 术语与图表分配 → 先引言后摘要；附中英双语问卷 | 1.2.1 |
| [`paper-figures`](paper-figures/) | 论文图表设计、绘制与验收：图表选型 → 统一风格 → 导出 → 灰度/色盲/字体检查，附带示例图；可恢复自有 PDF 图的矢量版 | 1.1 |
| [`paper-prose-polish`](paper-prose-polish/) | 逐句润色英文安全/系统论文：测量 → 术语锁定 → 逐句改写 → 首读门槛 + 连贯性验收 | 2.6.1 |

四者覆盖一篇论文从 0 到投稿的流水线，都面向 **S&P / USENIX Security / CCS / NDSS** 以及 IEEE S&P Magazine：
**调研（paper-survey）→ 写作（paper-writing）→ 配图（paper-figures）→ 润色（paper-prose-polish）**。

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
- `scripts/figure_recovery.py` — 从 PDF 裁出自有图的矢量 SVG（PyMuPDF，无需 Chrome），带
  逐像素 QA 门禁；**只用于自己的图或有授权的图**，详见 `references/figure-recovery.md`
- `examples/` — 9 张参考图 + 一张「坏图 vs 好图」对照 + 灰度版；`examples/README.md` 说明
  每张图演示哪条规则

```bash
python scripts/make_examples.py
python scripts/check_figure.py "examples/*.png" --preview
python scripts/figure_recovery.py probe   --pdf paper.pdf --page 3      # 矢量还是位图
python scripts/figure_recovery.py extract --pdf paper.pdf --page 3 --out analysis/recovered
```

示例图全部由代码生成，数据是合成的：仓库保存的是**风格**，不包含任何已发表论文的图。

---

## paper-survey

润色解决"句子读不懂"，写作解决"文章从哪长出来"，这个 skill 解决更早的一层：
**这个方向值不值得做、到底缺什么、我们做不做得了**。

报告按九节组织（阅读顺序，不是填表）：

> 基本信息 → 目的与背景 → 范围与方法 → 相关工作 → 现状总结 → 空白与问题 →
> 可行性 → 初步思路 → 结论与建议

**验收标准只有一条：读者能一遍看懂调研了什么、为什么得出这个结论。** 因此：

- **不设字数限制**，每节写多少由它要回答的问题决定；
- **不强制表格/清单**，表格只是工具，三段散文能说清就不用表；
- **不为了填满某节而凑内容**，某节对这个方向没什么可说，就写少一点并说明为什么；
- 唯一的硬约束是**准确性**：每个事实有来源（链接 + venue + year）或标 `[unverified]`；
  E1 已确认 → E2 我们复现 → E3 候选 → E4 推断，候选不悄悄升级；"没找到"必须带检索窗口，
  "首次/填补空白"若无范围限定直接判 FAIL。

另外给了七条"可读"的具体含义（开头 100 字说清对象与结论、每节第一句就是判断、论证链可见、
术语一致、比较要带维度、预判读者疑问、不写口水话），以及一个读者测试：让没参与的人复述
"问题 / 最近的工作 / 缺口 / 建议"，四项有一项错就说明没写清。

`scripts/check_survey.py` 不再打分：它输出**结构地图**（每节多少字、有没有表），
并把**准确性**（未加范围的"首次/填补空白"）判 FAIL、把**可读性风险**（整节只有标题、
Gap 缺段、没有下一步）判 WARN。范例报告：**0 fail / 0 warn**；一篇纯散文、无表格的报告：
**0 fail / 3 warn**（只提示没表、没链接）；只有标题的薄报告：**1 fail / 多项 warn**。

```bash
python scripts/check_survey.py report.md           # 结构地图 + 准确性/可读性提示
python scripts/check_survey.py report.md --json    # 机器可读
```

模板：`templates/survey-plan.md`（可选的开工前提示单）、`templates/report-skeleton.md`
（可选的九节骨架，散文更清楚就删掉表格占位）。

---

## paper-writing

润色解决"句子读不懂"，这个 skill 解决更早的一层：**这篇文章要回答什么、凭什么值得回答**。
核心是一条五环故事线，任何一环缺失，对应章节就会写成流水账：

> 问题从哪来？→ 为什么值得回答？→ 怎么回答？→ 证据支持到哪一步？→ 最后多知道了什么？

写作顺序也固定：**引言与背景先写**（它们锁定用词与主张，后面变了也只影响这两节），
**中间章节按结果迭代**（缺实验就去跑，不要绕过去写），**摘要在最后写**（审稿人第一眼看到它，
而它只能等结论定稿）。

skill 里带一份 `templates/paper-plan.md` 问卷：RQ、五环、结构选型、每节主张、术语锁定、
图表正文/附录分配、缺口与风险。**填不出来的地方写 `?`**，那些 `?` 就是下一次讨论的议程——
比一个看似合理的猜测有用得多。

实测（120 篇顶会摘要）：中位 **212 词 / 9 句**，**99.2% 用 "we"**，70.8% 含数字，32.5% 含百分比。
所以中文期刊那套"第三人称、不用本文作主语"的摘要规范**在英文安全论文里正好是反的**——
`references/abstract.md` 里把可迁移的部分（自明、独立、不过度声称）和必须反转的部分分开写了。

---

## 版本

- `paper-survey` v1.1：九节阅读顺序、E1–E4 证据分级、相关工作三维距离、Gap 三段式、
  可行性/风险/路线、三组指标分离、Go/Narrow/Stop 判据；
  **v1.1 去掉字数限制与"必产出"清单**（表格改为可选工具），改为按可读性验收：
  开头说清对象与结论、每节第一句是判断、论证链可见、术语一致；
  `check_survey.py` 只报结构地图 + 准确性 FAIL + 可读性 WARN（范例 0/0，纯散文报告 0 fail/3 warn）。见
  [`CHANGELOG.md`](paper-survey/CHANGELOG.md)。
- `paper-prose-polish` v2.6.1：v2.0 首读门槛；v2.1 否定规范；v2.2 改写权限与 DELETE 判决；
  v2.3–v2.4 语料研究（局部缺陷、结构/位置）；v2.5 连贯性约束（接缝三测、MERGE、`--flow`）；
  v2.5.1 明确「原文已经写得好就不改」；v2.6 图表阅读顺序（先引用后出现）；
  **v2.6.1 把「不许为指标牺牲连贯」放到 gate、阈值表和模板上**（阈值一个没动）。
  每次改动的实测数字与 null result 见
  [`CHANGELOG.md`](paper-prose-polish/CHANGELOG.md)。
- `paper-writing` v1.2.1：初版（五环故事线、章节蓝图、摘要、正文/附录分配、作者问卷）；
  **v1.1 加实测解剖**（引言 10 段/1032 词、评估 24 段、附录 60.8%）、结果清单工作流、配色实测、中文问卷；
  **v1.2 完成四项补测**：99 篇引言人工标注（五环位置 0.00/0.12/0.38/0.62/0.78，出现率 100/76/100/58/90%）、
  评估子节（中位 4 个、62% 标题是主张专属）、图型（抽样全是示意图/截图）、分母修正（每篇 17 件、附录 10.9%）；
  **v1.2.1 补上两个研究脚本**（`build_intro_kit.py`、`aggregate_annotations.py`），使引言标注研究可复现。
  实测见 [`CHANGELOG.md`](paper-writing/CHANGELOG.md)。
- `paper-figures` v1.1：v1.0 初版（风格/编码/可访问性/生产）；
  **v1.1 新增"自有 PDF 图的矢量恢复 + 像素 QA"**（`figure_recovery.py`），
  并加了版权约束：不拿别人的图。上游灵感来自
  [`pdf-figure-vector`](https://github.com/tanzhouhu/pdf-figure-vector)，本仓库为独立实现。
