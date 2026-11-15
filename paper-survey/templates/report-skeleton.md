# Survey report skeleton (optional)

This is a prompt sheet, not a form. Use it when a blank page is the problem; ignore the table
placeholders when prose is clearer. Keep the nine `##` headings (the reader expects that order),
write each section as long as its question needs, and delete anything that does not help the
reader follow the argument.

Header block before §1:

```markdown
# <中文标题>

**<English title>**

研究阶段：方向调研与可行性论证
调研日期：YYYY 年 M 月 D 日
研究基础：<lab / repo>
目标：<one line>
```

---

## 一、基本信息 / 1. Basic Information

- 研究方向（3–5 个关键词）：
- 暂定研究主题（一句话）：
- 核心研究对象（具体组件/数据/机制）：
- 研究目标（近期 / 方法层）：
- 预期研究成果（编号 3–5 条，写可交付物）：
- 阶段声明（当前阶段 + 最终形态取决于什么）：

## 二、目的与背景 / 2. Purpose & Background

### 2.1 研究背景
（基础设施 → 现有机制 → 一句加粗转折 → 组件链路 → 问题发生在边界）

### 2.2 已有实验发现
（E1 锚点：公告/CVE 编号、日期、CWE、组件、一句话机制；E3 候选单独列出；
 结尾一句归纳："这些现象提示…不是偶发缺陷"）

### 2.3 调研目的
**RQ1：…** （问题句 + 2–3 句范围/意义/边界）

**RQ2：…**

**RQ3：…**

**RQ4：…**

（范围限定句：本研究不以证明…为目标）

## 三、范围与方法 / 3. Scope & Method

### 3.1 调研范围
| 层次 | 研究对象 | 重点问题 |
|---|---|---|

（纳入 / 排除清单：哪些相邻问题不纳入，什么条件下纳入）

### 3.2 方法与检索协议
（文献/标准/历史漏洞/源码/动态/真实部署；数据库、会议、时间窗、查询式、纳入排除、停止条件）

### 3.3 调研判断标准
（协议允许 / 潜在异常 / 可复现缺陷 / 上游确认；说明不一致≠漏洞）

（伦理与访问边界）

## 四、相关工作 / 4. Related Work Survey

| 研究工作 | 主要研究内容 | 对本研究的启发及区别 |
|---|---|---|

### 4.1 已有研究的主要贡献（4–6 条，先承认）

### 4.2 与本研究最接近的现有工作（2–3 个 + 切入点，标记为待验证）

## 五、现状总结 / 5. State-of-the-Art Summary

### 5.1 …（判断 + 证据）
### 5.2 …
### 5.3 …
### 5.4 我们当前的研究基础（资产 + 最明显不足）

## 六、存在的问题与空白 / 6. Gaps & Open Problems

### Gap 1：…
**已有问题：**
**研究空白：**
**拟解决问题：**

（Gap 2…n，≥3 个）

**预期研究重点：** 一句话收敛

## 七、可行性初步分析 / 7. Feasibility Analysis

### 7.1 已有技术基础（3–5 条：已有 X，因此不需要从零做 Y）
### 7.2 可行性与风险评估
| 研究任务 | 初步可行性 | 主要风险 |
|---|---|---|
### 7.3 当前主要风险（每条：风险 + 触发条件 + 应对 + 停止/转向条件）

## 八、初步思路 / 候选方案 / 8. Preliminary Ideas & Candidate Approaches

### 8.1 核心思路（一句加粗 + 与最近方法的一句区别）
### 8.2 候选系统设计（模块 A–F：输入 / 做什么 / 产出 / 依赖）
### 8.3 初步实验路线
| 阶段 | 主要任务 | 预期输出 | 退出条件 |
|---|---|---|---|
### 8.4 关键评估指标（三组分开：发现能力 / 实际影响 / 防御效果）
### 8.5 可能形成的方法创新（3–5 条 + "不预先假定新颖性"）

## 九、结论与建议 / 9. Conclusion & Recommendation

### 9.1 调研结论
### 9.2 下一步建议（短期 1–2 个前提验证 + "只有阳性才投入"；中期；长期）
### 9.3 最终定位（不把现有草稿当固定框架）+ 核心问题引用块

---

**主要研究基础：**（lab、公告、候选、标准、最近邻工作）

---

自查：`python <skill>/scripts/check_survey.py report.md`
