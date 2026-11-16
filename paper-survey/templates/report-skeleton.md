# Survey report skeleton (optional)

This is a prompt sheet, not a form. Use it when a blank page is the problem; ignore the table
placeholders when prose is clearer. Keep the ten `##` headings (the reader expects that order),
write each section as long as its question needs, and delete anything that does not help the
reader follow the argument. Tables are tools, not quotas.

Header block before §1:

```markdown
# <中文标题>

**<English title>**

调研主题/方向 Topic/Direction：…
调研人 Researcher：…            起止时间 Duration：YYYY.MM – YYYY.MM
项目内容文档 Project Doc：<link>
```

---

## 一、基本信息 / 1. Basic Information

- 调研主题/方向（可与项目题目一致或更宽泛）：
- 调研人 / 起止时间 / 项目内容文档链接：
- 暂定研究主题（一句话）：
- 核心研究对象（具体组件/数据/机制）：
- 研究目标（近期 / 方法层）：
- 预期研究成果（可交付物）：
- 阶段声明（当前阶段 + 最终形态取决于什么）：

## 二、目的与背景 / 2. Purpose & Background

（基础设施 → 现有机制 → 一句转折：保护在哪里失效 → 组件链路 → 已确认的锚点（编号/日期）→
 RQ1…；结尾写清本研究不试图证明什么）

## 三、范围与方法 / 3. Scope & Method

检索关键词：
检索范围（会议/期刊/数据库、时间跨度）：
纳入 / 排除标准：
四条方法（按需写）：顺藤摸瓜（引用追溯）/ 找综述（Survey、SoK）/ 横向对比 / 多渠道
（新闻、博客、论坛、厂商公告、公众号）
判断标准（协议允许 / 潜在异常 / 可复现缺陷 / 上游确认）：

## 四、相关工作 / 4. Related Work Survey

（表格是推荐形式，不是必须；每行至少说清「它做了什么、局限、能借鉴什么」）

| 论文/工具 | 来源（venue/年份） | 核心思路 | 局限性/差距 | 可借鉴点 |
|---|---|---|---|---|
|  |  |  |  |  |

（结尾：已有工作确立了什么 → 与本研究的三维距离：对象 / 方法 / 证据）

## 五、现状总结 / 5. State-of-the-Art Summary

（3–5 个判断，每个判断带证据与边界；加上"我们的基础"与"最明显的不足"）

## 六、存在的问题与空白 / 6. Gaps & Open Problems

（先横向对比：已解决 / 不够好 / 尚未研究；再逐个 Gap 写清"问题—缺什么—怎么补"）

## 七、可行性初步分析 / 7. Feasibility Analysis

| 评估维度 | 情况 | 风险/应对 |
|---|---|---|
| 数据可得性 |  |  |
| 技术难度 |  |  |
| 所需资源/工具 |  |  |
| 时间成本 |  |  |
| 潜在风险 |  |  |

（每个维度要具体；每个风险给出触发条件、应对、停止/转向条件）

## 八、初步思路 / 候选方案 / 8. Preliminary Ideas / Candidate Approaches

方案 1：…（假设 / 做法 / 产出 / 风险）
方案 2：…（同上，供比较）
（核心思路一句；P0–Pn 路线，每步有退出条件；指标分三组分别报告：发现能力 / 实际影响 / 防御效果）

## 九、结论与建议 / 9. Conclusion & Recommendation

（明确一个结论：立项 / 放弃 / 继续调研 / 与导师讨论；短期先验证什么；中期、长期；
 最终定位与核心问题）

## 十、参考文献与资料 / 10. References & Links

不只是论文：新闻、博客、论坛、厂商公告、公众号都可以，但每条都要能看出类型。

| 类型 | 标题/来源 | 链接 | 备注 |
|---|---|---|---|
| 论文 / Paper |  |  |  |
| 综述 / Survey |  |  |  |
| 新闻 / News |  |  |  |
| 博客 / Blog |  |  |  |
| 论坛 / Forum |  |  |  |
| 厂商公告 / Advisory |  |  |  |
| 公众号 / WeChat |  |  |  |

---

自查：`python <skill>/scripts/check_survey.py report.md`（结构地图 + 准确性/可读性提示，不判字数）
