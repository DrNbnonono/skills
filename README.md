# skills

Some skills created by dr. Each folder is a self-contained skill: drop it into
`~/.claude/skills/` (global) or `<project>/.claude/skills/` (per project) and it is picked up
by the agent.

| Skill | What it does | Version |
|---|---|---|
| [`paper-prose-polish`](paper-prose-polish/) | 逐句润色英文安全/系统论文：测量 → 术语锁定 → 逐句改写 → 首读门槛验收 | 2.0 |
| [`paper-figures`](paper-figures/) | 论文图表设计、绘制与验收：图表选型 → 统一风格 → 导出 → 灰度/色盲/字体检查，附带示例图 | 1.0 |

两者都面向 **S&P / USENIX Security / CCS / NDSS** 以及 IEEE S&P Magazine 的写作与配图。

---

## paper-prose-polish

动机很直接：**如果一个英语不是母语的读者不能一遍直接读懂，这句话就是有问题的**，不管它语法
多正确、听起来多地道。v2 把这句直觉变成了可执行的判定：首读测试（不回头、不停顿、不翻译）、
阴影测试、陌生人复述测试，以及四个 L2 阻塞指标（主动词前的词数、从句数、习语/短语动词、不透明
正式词）。

包含：

- `references/comprehension-gate.md` — 首读门槛：三个测试、S1–S8 卡顿分类、8 组改写示例
- `references/vocabulary.md` — 「透明优先」：对 L2 读者而言，`holds up` 比 `remains exploitable`
  更难；习语/短语动词替换表、歧义连接词表、什么**不要**简化
- `references/venue-prose-corpus.md` — 四大会议在散文层面奖励什么；可复现的语料测量协议
- `references/sentence-rules.md` — L1–L17 规则（v2 新增 L14–L17）
- `references/rubric.md` — 五问、缺陷码 A1–A16、五种判决、手术动作
- `references/diagnosis-playbook.md` — 测量与阈值（含 L2 阻塞指标）
- `references/magazine-mode.md` — 会议论文改杂志体
- `scripts/lint_prose.py` — 句长/被动/名词化/破折号 + 四个 L2 指标；`--gate` 通过/不通过，
  `--explain N` 列出卡顿最多的句子
- `templates/revision-table.md` — 每轮修订记录表

```bash
python scripts/lint_prose.py --path paper/ --glob "*.tex" --json baseline.json
python scripts/lint_prose.py --path paper/ --gate --venue magazine --explain 10
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

- `paper-prose-polish` v2.0：新增首读门槛、L2 词表、语料协议、A13–A16、L14–L17、linter v2。
  变更记录见 [`CHANGELOG.md`](paper-prose-polish/CHANGELOG.md)。
- `paper-figures` v1.0：初版。
