#!/usr/bin/env python3
"""Second pair of eyes for a pre-paper survey report.

This is not a compliance gate. The report's real test is whether a reader can follow what was
investigated and why the conclusion follows; no script can check that. The script does two
smaller things:

  * maps the report's structure (sections, size in units, tables, links) so you can see the shape;
  * flags accuracy problems (unscoped "first / fills a gap / no one has") and a few clarity
    risks (a section that is only a heading, gaps without their three beats, a recommendation
    with no next step).

There are no length limits and no mandatory artifacts. Missing a table is a warning, not a
failure; a short section can be a complete one.

Usage
-----
    python check_survey.py report.md
    python check_survey.py report.md --json
    python check_survey.py report.md --strict     # warnings count as failures

Exit code: 0 unless a FAIL (accuracy or structure), or a WARN under --strict.
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
    ("基本信息", ("基本信息", "basic information")),
    ("目的与背景", ("目的", "purpose", "background")),
    ("范围与方法", ("范围", "scope", "method")),
    ("相关工作", ("相关工作", "related work")),
    ("现状总结", ("现状", "state-of-the-art", "state of the art")),
    ("空白与问题", ("空白", "gap", "open problem")),
    ("可行性", ("可行性", "feasibility")),
    ("思路", ("思路", "idea", "approach", "candidate")),
    ("结论与建议", ("结论", "conclusion", "recommendation")),
    ("参考文献与资料", ("参考文献", "references", "资料链接", "references & links")),
]
REQUIRED = len(SECTIONS) - 1  # §10 is recommended, not required

SCOPE_WORDS = ("检索", "范围内", "据我们所知", "截至", "本次调研", "本文调研", "window", "venues")
OVERCLAIM = re.compile(r"首次|填补空白|尚属首次|前所未有|从无到有|国内外尚无|尚无研究")
LINK = re.compile(r"https?://")
RISK_ITEM = re.compile(r"(?:\*\*)?风险[一二三四五六七八九十\d]+")
RESPONSE_MARKERS = ("应对", "缓解", "处理", "停止条件", "转向", "兜底", "应优先",
                    "需要通过", "可通过", "策略", "建议", "需", "须", "应")


def units(s: str) -> int:
    """CJK characters + Latin word tokens. Reported for orientation only; no limits apply."""
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
    for i, (_, keys) in enumerate(SECTIONS):
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
    missing = [SECTIONS[i][0] for i in range(REQUIRED) if i not in positions]
    if missing:
        add("FAIL", "sections present", f"missing: {', '.join(missing)}")
    else:
        add("PASS", "sections present", f"{REQUIRED}/{REQUIRED} core sections")
    if len(SECTIONS) - 1 not in positions:
        add("WARN", "references section", "no §10 — put every source (incl. news/blogs) in one place")
    dup = [SECTIONS[i][0] for i in positions if positions.count(i) > 1]
    if dup:
        add("WARN", "sections unique", f"duplicated: {', '.join(sorted(set(dup)))}")
    if positions and positions != sorted(positions):
        add("FAIL", "section order", "headings out of order: " + " > ".join(str(p) for p in positions))
    elif positions:
        add("PASS", "section order", "ok")

    bodies = {i: body for i, _, body in matched if i >= 0}

    # --- structure map (orientation, not a gate) ---------------------------
    for i, (name, _) in enumerate(SECTIONS):
        body = bodies.get(i)
        if body is None:
            continue
        n = units(body)
        hdr, rows = table_rows(body)
        extra = f", {rows} table rows" if hdr else ""
        add("INFO", f"§{i + 1} {name}", f"{n} units{extra}")
        if n < 30:
            add("WARN", f"§{i + 1} near-empty", f"{n} units — a reader cannot tell what you concluded")

    # --- clarity risks (warnings) -----------------------------------------
    rw = bodies.get(3, "")
    header, rows = table_rows(rw)
    if header:
        add("INFO", "related-work table", f"{rows} rows")
        if rows < 3:
            add("WARN", "related-work table thin", f"only {rows} rows — is the closest work missing?")
    else:
        add("WARN", "related-work table", "no table (fine if prose names closest work and distance)")
    if len(LINK.findall(rw)) < 3:
        add("WARN", "related-work links", f"{len(LINK.findall(rw))} links")

    gaps = bodies.get(5, "")
    counts = {k: len(re.findall(k, gaps)) for k in ("已有问题", "研究空白", "拟解决")}
    if min(counts.values()) == 0:
        add("WARN", "gap beats", f"some gaps miss a beat: {counts} (已有问题/研究空白/拟解决)")
    else:
        add("INFO", "gap beats", str(counts))
    named = len(re.findall(r"Gap\s*\d+", gaps))
    if named:
        add("INFO", "named gaps", str(named))

    feas = bodies.get(6, "")
    fheader, frows = table_rows(feas)
    if not fheader:
        add("WARN", "feasibility table", "no table (prose per risk is fine)")
    else:
        add("INFO", "feasibility table", f"{frows} rows, header: {' / '.join(fheader)}")
    blocks = [b for b in re.split(r"(?m)^(?:\*\*)?风险[一二三四五六七八九十\d]+", feas)[1:] if b.strip()]
    if blocks:
        responded = sum(1 for b in blocks if any(w in b[:500] for w in RESPONSE_MARKERS))
        add("INFO", "risk register", f"{len(blocks)} risks, {responded} with a response")
        if responded == 0:
            add("WARN", "risk responses", "risks without any 应对/停止条件 — they are worries, not risks")
        elif responded < len(blocks):
            add("WARN", "risk responses", f"{responded}/{len(blocks)} carry a response")

    # --- metadata (research's who/when) -----------------------------------
    first = bodies.get(0, "")
    has_who = re.search(r"调研人|Researcher|姓名|Name", first)
    has_when = re.search(r"起止时间|Duration|20\d{2}\.\d{2}", first)
    if has_who and has_when:
        add("INFO", "§1 metadata", "researcher and duration present")
    else:
        add("WARN", "§1 metadata", "missing 调研人/起止时间 — the reader cannot tell who asked, over what window")

    concl = bodies.get(8, "")
    if not any(w in concl for w in ("下一步", "短期", "中期", "长期", "建议")):
        add("WARN", "next steps", "§9 has no next step")
    if not any(w in concl for w in ("立项", "放弃", "继续调研", "导师", "继续", "收窄", "停止", "值得")):
        add("WARN", "decision", "§9 does not state continue/narrow/stop/kick-off")

    # --- references section ------------------------------------------------
    refs = bodies.get(len(SECTIONS) - 1, "")
    if refs:
        links = len(LINK.findall(refs))
        kinds = re.findall(r"论文|综述|新闻|博客|论坛|厂商|微信|paper|survey|news|blog|forum|advisory", refs, re.I)
        add("INFO", "§10 references", f"{links} links, {len(kinds)} typed entries")
        if links < 3:
            add("WARN", "§10 links", f"{links} links — is every in-text source listed?")

    purpose = bodies.get(1, "")
    rq = len(re.findall(r"RQ\s*\d", purpose))
    if rq < 1:
        add("WARN", "research questions", "no RQ found")
    else:
        add("INFO", "research questions", str(rq))

    # --- accuracy (the only hard failures besides structure) --------------
    if re.search(r"调研日期|20\d{2}\s*年\s*\d{1,2}\s*月", text):
        add("INFO", "date", "present")
    else:
        add("WARN", "date", "no date — the report ages without one")
    if re.search(r"检索|查询", text) and re.search(r"时间窗|年份|20\d{2}|停止条件", text):
        add("INFO", "search protocol", "present")
    else:
        add("WARN", "search protocol", "no search window / queries recorded")
    if re.search(r"\bE[1-4]\b|已确认|已验证|候选|待确认|推测|未确认", text):
        add("INFO", "evidence grades", "present")
    else:
        add("WARN", "evidence grades", "no E1–E4 / 已确认/候选 marks")

    bad = []
    for m in OVERCLAIM.finditer(text):
        window = text[max(0, m.start() - 120):m.end() + 120]
        if not any(w in window for w in SCOPE_WORDS):
            bad.append(m.group(0))
    if bad:
        add("FAIL", "overclaim scope", f"unscoped: {', '.join(sorted(set(bad)))}")
    else:
        add("PASS", "overclaim scope", "ok")

    links = len(LINK.findall(text))
    add("INFO", "links", str(links))

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
        if warns:
            print("note: warnings are about readability, not compliance; fix them when a reader would stumble.")

    sys.exit(1 if fails or (args.strict and warns) else 0)


if __name__ == "__main__":
    main()
