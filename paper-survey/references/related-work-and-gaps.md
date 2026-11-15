# Related work and gaps

§4 is the evidence; §6 is the judgment. They are written together, because a gap that does not
trace to a row of §4 is unsupported.

---

## 1. Search protocol (reproducible or it is not a search)

Record, in the report (usually at the start of §3 or §4):

```
检索数据库：DBLP, ACM DL, USENIX, IEEE Xplore, arXiv, Semantic Scholar
会议/期刊：S&P, USENIX Security, CCS, NDSS, IMC, WWW, TDSC, Computers & Security
时间窗：2018-01 至 2025-12
查询式："email authentication" AND ("trust boundary" OR "authentication-results")
        ("email spoofing" OR "header injection") AND (measurement OR differential)
纳入标准：a. 提出/测量邮件身份认证相关机制；b. 有可评估的系统或测量
排除标准：a. 纯用户研究且无认证链路；b. 无全文；c. 与认证结果消费无关
滚雪球：对 3 篇最近邻工作做前向引用（被引）与后向引用（参考文献）扩展
停止条件：连续 10 篇新命中都已被覆盖
```

This block is what makes "在本次检索范围内" mean something. Keep it short but complete.

### Neck of the funnel

- **Venues**: top-4 for the research question; add measurement venues (IMC, WWW) and systems
  venues as needed; professional venues for practice.
- **Years**: at least 5; extend for foundational standards (RFCs are undated in practice).
- **Snowballing**: forward (who cites the closest work) and backward (its references); stop when
  ten consecutive hits are already covered.
- **Grey literature**: advisories, vendor audits, standards — labeled as such, not mixed into the
  peer-reviewed count.

---

## 2. The comparison table

```markdown
| 研究工作 | 主要研究内容 | 对本研究的启发及区别 |
|---|---|---|
| [End-to-End Measurements of Email Spoofing Attacks](url)（USENIX Security 2018） | 测量 35 个服务商对伪造邮件的检测、投递与用户警告 | 已测伪造与用户警告；本研究测认证结果消费 |
```

Rules that make the table persuasive (the table itself is optional — with only three close works,
three paragraphs may read better):

1. **Link + venue + year** in the first cell. No link, no row.
2. **Column 2 is what they did**, in their terms — not what they failed to do.
3. **Column 3 names one of three distances:**

| Distance | Question it answers | Example |
|---|---|---|
| **Object** | Different unit of study | "他们测服务商对伪造邮件的处理；我们测组件对认证声明的信任判定" |
| **Method** | Different technique | "他们用人工构造样本；我们把安全不变式转成属性引导生成" |
| **Evidence** | Different kind of proof | "他们止于输出差异；我们要求源码根因 + 端到端安全动作" |

4. **At least one row must be the closest work.** If no row is uncomfortable, the search was
   shallow.
5. **No row may be a strawman.** Before writing column 3, read the abstract, introduction, and
   evaluation of that paper; if you cannot state its claim to its author's satisfaction, you are
   not ready to state the distance.

### What §4 must establish

- The closest work and what it settled (so the report cannot claim it).
- The three-dimensional distance table.
- The residue: one paragraph ending with the entry-point question, explicitly marked as a
  hypothesis, not a novelty claim.

---

## 3. The three-part gap

Every gap, all three parts:

```markdown
### Gap 2：缺少面向认证结果消费逻辑的定向发现方法

**已有问题**
传统邮件 Fuzzing 关注语法异常、解析差异、崩溃；此类缺陷不导致解析失败，
组件可能正常运行却错误接受不可信声明（E1：[GHSA]，E3：[MSL-099]）。

**研究空白**
如何把已确认缺陷的根因转成可复用的测试约束，并定位错误消费路径，尚无系统研究。

**拟解决问题**
把根因抽象为可检查的安全不变式（来源可信、语义绑定、动作依赖），
以不变式引导结构化输入生成，并用跨组件对照判定违规；成功判据是
「相同测试预算下发现更多独立根因」。
```

Rules:

- **已有问题** carries grade labels and concrete mechanisms, not generalities.
- **研究空白** is one sentence that names the missing *kind of result* (model / method /
  measurement / bound), not "more research is needed".
- **拟解决** names an invariant, a metric, or an artifact. If it cannot be started next week, it
  is too vague.
- **Trace**: each gap cites at least one row of §4 by its short name.
- **How many:** as many as are real. Two strong gaps beat five padded ones; number them
  (`Gap 1…`) when there are more than two, so §8 can refer to them.

### Gap failure modes (the checker uses these)

| Failure | Example | Fix |
|---|---|---|
| Pseudo-gap | "No one has studied X" (no window) | add search window + venues; or drop |
| Already solved | Gap restates a paper's result | move to §4/§5, choose the residue |
| Untestable | "Secure email end to end" | narrow to one invariant + one measurement |
| Duplicate | Gap 2 and Gap 4 are the same at two scales | merge; keep the scale that can be tested |
| Disconnected | Gap has no corresponding module in §8 | add module, or cut gap |

---

## 4. Mapping: work → gap → module → metric (optional)

If the report has several gaps and several modules, this one table is the cheapest way to catch a
gap the plan does not address. If there are only two of each, a sentence is enough.

| §4 row | Distance | Gap | §8 module | Metric |
|---|---|---|---|---|
| Composition Kills | object | Gap 1 | A + C | independent root causes found |
| RFC 8601 | evidence | Gap 5 | F | blocked insecure statements / false positives |

A gap with no module is a gap the plan ignores. A module with no gap is scope creep.

---

## 5. Before you call it done

- Can the reader name the closest work and the distance without re-reading §5?
- Does every gap trace to something in §4?
- Would the authors of the closest work accept your description of it?
- Is there at least one sentence that says what would falsify the gap?
