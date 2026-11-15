#!/usr/bin/env python3
"""Check a pre-paper survey report against the nine-section constraints.

What it checks (mechanical, fast):
  * the nine sections exist, exactly once, in order;
  * each section's length is near the calibrated range (warn, not fail);
  * the related-work table has >=5 rows, links, and a distance column;
  * gaps use the three-part form (already-problem / gap / plan) at least three times;
  * feasibility has a task/feasibility/risk table and a risk-response section;
  * a conclusion names next steps;
  * research questions, date, search protocol, and evidence grades are present;
  * overclaim wording ("first", "fills a gap", "no one has") appears only with a scope phrase.

What it cannot check: whether the search was good, whether the distance is honest, whether the
plan is feasible. Those are human judgments; see references/.

Usage
-----
    python check_survey.py report.md
    python check_survey.py report.md --json
    python check_survey.py report.md --strict     # treat warnings as failures

Exit code: 0 unless a FAIL (or a WARN under --strict).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:  # keep Chinese output readable in a cp936 console
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SECTIONS = [
    ("基本信息", ("基本信息", "basic information"), (200, 600)),
    ("目的与背景", ("目的", "purpose", "background"), (600, 2000)),
    ("范围与方法", ("范围", "scope", "method"), (500, 1600)),
    ("相关工作", ("相关工作", "related work"), (800, 3000)),
    ("现状总结", ("现状", "state-of-the-art", "state of the art"), (400, 1400)),
    ("空白与问题", ("空白", "gap", "open problem"), (900, 3500)),
    ("可行性", ("可行性", "feasibility"), (500, 1800)),
    ("思路", ("思路", "idea", "approach", "candidate"), (800, 3000)),
    ("结论与建议", ("结论", "conclusion", "recommendation"), (400, 1200)),
]

SCOPE_WORDS = ("检索", "范围内", "据我们所知", "截至", "本次调研", "本文调研", "window", "venues")
OVERCLAIM = re.compile(r"首次|填补空白|尚属首次|前所未有|从无到有|国内外尚无|尚无研究")
LINK = re.compile(r"https?://")
RISK_ITEM = re.compile(r"(?:\*\*)?风险[一二三四五六七八九十\d]+")
RESPONSE_WORDS = ("应对", "缓解", "处理", "停止条件", "转向", "兜底")


def units(s: str) -> int:
    """CJK characters + Latin word tokens."""
    cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
    latin = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))
    return cjk + latin


def split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    parts = re.split(r"(?m)^##\s+", text)
    preamble = parts[0]
    out = []
    for p in parts[1:]:
        lines = p.splitlines()
        out.append((lines[0].strip(), "\n".join(lines[1:])))
    return preamble, out


def match_section(heading: str) -> int:
    h = heading.lower()
    for i, (_, keys, _) in enumerate(SECTIONS):
        if any((k in h) if re.search(r"[\u4e00-\u9fff]", k) else (k in h) for k in keys):
            return i
    return -1


def table_rows(block: str) -> tuple[list[str], int]:
    """Return (header cells, data row count) for the first markdown table in a block."""
    lines = [ln.strip() for ln in block.splitlines()]
    for i, ln in enumerate(lines):
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1]):
            header = [c.strip() for c in ln.strip("|").split("|")]
            n = 0
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                n += 1
            return header, n
    return [], 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report")
    ap.add_argument("--json", action="store_true", help="print a JSON summary instead of the table")
    ap.add_argument("--strict", action="store_true", help="warnings count as failures")
    args = ap.parse_args()

    path = Path(args.report)
    text = path.read_text(encoding="utf-8", errors="replace")
    preamble, found = split_sections(text)

    checks: list[dict] = []

    def add(level: str, name: str, detail: str) -> None:
        checks.append({"level": level, "check": name, "detail": detail})

    # --- structure ---------------------------------------------------------
    matched = [(match_section(h), h, body) for h, body in found]
    positions = [i for i, _, _ in matched if i >= 0]
    missing = [SECTIONS[i][0] for i in range(len(SECTIONS)) if i not in positions]
    if missing:
        add("FAIL", "sections present", f"missing: {', '.join(missing)}")
    else:
        add("PASS", "sections present", f"{len(SECTIONS)}/9")
    dup = [SECTIONS[i][0] for i in positions if positions.count(i) > 1]
    if dup:
        add("WARN", "sections unique", f"duplicated: {', '.join(sorted(set(dup)))}")
    if positions != sorted(positions):
        add("FAIL", "section order", "headings out of order: " + " > ".join(str(p) for p in positions))
    else:
        add("PASS", "section order", "ok")

    bodies = {i: body for i, _, body in matched if i >= 0}

    # --- per-section length ------------------------------------------------
    for i, (name, _, (lo, hi)) in enumerate(SECTIONS):
        body = bodies.get(i)
        if body is None:
            continue
        n = units(body)
        if n < lo:
            add("WARN", f"§{i + 1} length", f"{n} units, below {lo} (section may be incomplete)")
        elif n > hi:
            add("WARN", f"§{i + 1} length", f"{n} units, above {hi} (may be doing another section's job)")
        else:
            add("PASS", f"§{i + 1} length", f"{n} units")

    # --- related work ------------------------------------------------------
    rw = bodies.get(3, "")
    header, rows = table_rows(rw)
    if not header:
        add("FAIL", "related-work table", "no markdown table in §4")
    else:
        add("PASS", "related-work table", f"{rows} data rows")
        if rows < 5:
            add("FAIL", "related-work rows", f"{rows} < 5")
        if len(LINK.findall(rw)) < max(3, rows // 2):
            add("WARN", "related-work links", f"{len(LINK.findall(rw))} links for {rows} rows")
        joined = " ".join(header).lower()
        if not any(k in joined for k in ("区别", "启发", "distance", "difference")):
            add("FAIL", "distance column", "table header has no 区别/启发/distance column")
        else:
            add("PASS", "distance column", "present")

    # --- gaps --------------------------------------------------------------
    gaps = bodies.get(5, "")
    counts = {k: len(re.findall(k, gaps)) for k in ("已有问题", "研究空白", "拟解决")}
    if min(counts.values()) >= 3:
        add("PASS", "gap three-part form", str(counts))
    else:
        add("FAIL", "gap three-part form", f"need >=3 of each, got {counts}")
    named = len(re.findall(r"Gap\s*\d+", gaps))
    if named < 3:
        add("WARN", "named gaps", f"{named} 'Gap N' headings (<3)")
    else:
        add("PASS", "named gaps", f"{named}")

    # --- feasibility -------------------------------------------------------
    feas = bodies.get(6, "")
    fheader, frows = table_rows(feas)
    joined = " ".join(fheader)
    if not fheader:
        add("FAIL", "feasibility table", "no table in §7")
    elif "可行性" not in joined or "风险" not in joined:
        add("FAIL", "feasibility table", f"header lacks 可行性/风险: {fheader}")
    else:
        add("PASS", "feasibility table", f"{frows} rows")
        if frows < 5:
            add("WARN", "feasibility rows", f"{frows} < 5")
    risks = RISK_ITEM.findall(feas)
    if len(risks) < 3:
        add("WARN", "risk register", f"{len(risks)} risk items (<3)")
    else:
        add("PASS", "risk register", f"{len(risks)} items")
    # each risk block should carry a response, not just a worry; accept imperatives too
    blocks = [b for b in re.split(r"(?m)^(?:\*\*)?风险[一二三四五六七八九十\d]+", feas)[1:] if b.strip()]
    markers = ("应对", "缓解", "处理", "停止条件", "转向", "兜底", "应优先", "需要通过", "可通过",
               "策略", "建议", "需", "须", "应")
    responded = sum(1 for b in blocks if any(w in b[:500] for w in markers))
    if blocks and responded == 0:
        add("FAIL", "risk responses", f"0/{len(blocks)} risk items carry a response")
    elif blocks and responded < len(blocks):
        add("WARN", "risk responses", f"{responded}/{len(blocks)} risk items carry a response")
    else:
        add("PASS", "risk responses", f"{responded}/{len(blocks) or 0}")

    # --- conclusion --------------------------------------------------------
    concl = bodies.get(8, "")
    if not any(w in concl for w in ("下一步", "短期", "中期", "长期", "建议")):
        add("FAIL", "next steps", "§9 has no 下一步/短期/中期/长期")
    else:
        add("PASS", "next steps", "present")
    if not any(w in concl for w in ("继续", "收窄", "放弃", "停止", "值得")):
        add("WARN", "decision", "§9 does not state continue/narrow/stop")
    else:
        add("PASS", "decision", "present")

    # --- purpose -----------------------------------------------------------
    purpose = bodies.get(1, "")
    rq = len(re.findall(r"RQ\s*\d", purpose))
    if rq < 2:
        add("WARN", "research questions", f"{rq} RQ (<2)")
    else:
        add("PASS", "research questions", f"{rq}")

    # --- metadata / protocol / grades -------------------------------------
    if re.search(r"调研日期|20\d{2}\s*年\s*\d{1,2}\s*月", text):
        add("PASS", "date", "present")
    else:
        add("WARN", "date", "no 调研日期 / date in the report")
    if re.search(r"检索|查询", text) and re.search(r"时间窗|年份|20\d{2}|停止条件", text):
        add("PASS", "search protocol", "present")
    else:
        add("WARN", "search protocol", "no search window / queries recorded")
    if re.search(r"\bE[1-4]\b|已确认|已验证|候选|待确认|推测|未确认", text):
        add("PASS", "evidence grades", "present")
    else:
        add("WARN", "evidence grades", "no E1–E4 / 已确认/候选 marks")

    # --- overclaims --------------------------------------------------------
    bad = []
    for m in OVERCLAIM.finditer(text):
        window = text[max(0, m.start() - 120):m.end() + 120]
        if not any(w in window for w in SCOPE_WORDS):
            bad.append(m.group(0))
    if bad:
        add("FAIL", "overclaim scope", f"unscoped: {', '.join(sorted(set(bad)))}")
    else:
        add("PASS", "overclaim scope", "ok")

    # --- totals ------------------------------------------------------------
    links = len(LINK.findall(text))
    add("PASS" if links >= 3 else "WARN", "links", str(links))
    tables = len(re.findall(r"(?m)^\|\s*---", text)) + len(re.findall(r"(?m)^\|[\s:|-]+\|?$", text))
    add("PASS" if tables >= 4 else "WARN", "tables", str(tables))

    fails = sum(1 for c in checks if c["level"] == "FAIL")
    warns = sum(1 for c in checks if c["level"] == "WARN")

    if args.json:
        print(json.dumps({"file": str(path), "fail": fails, "warn": warns, "checks": checks},
                         ensure_ascii=False, indent=2))
    else:
        width = max(len(c["check"]) for c in checks)
        print(f"{'LEVEL':6} {'CHECK':{width}}  DETAIL")
        print("-" * (6 + width + 40))
        for c in checks:
            print(f"{c['level']:6} {c['check']:{width}}  {c['detail']}")
        print()
        print(f"RESULT: {'PASS' if fails == 0 else 'FAIL'}  ({fails} fail, {warns} warn)")

    sys.exit(1 if fails or (args.strict and warns) else 0)


if __name__ == "__main__":
    main()
