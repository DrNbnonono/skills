#!/usr/bin/env python
"""Venue checks for an IMC submission.

These are the checks that are specific to IMC and that a generic prose linter cannot make:
the abstract budget, the mandatory Ethics appendix, the artifact statement, and whether the
draft is actually written in the measurement register (numbers plus scope) rather than in
systems voice. Nothing here replaces `lint_prose.py`; run that first, then this.

Every threshold carries the measured base rate it came from (IMC 2022-2025, 75 full texts and
237 abstracts). A warning is a question, not a verdict: fix it or record why not.

Usage:
  python imc_check.py --path <paper-dir> --glob "*.tex"
  python imc_check.py --path sections/05_evaluation.tex
"""
from __future__ import annotations

import argparse
import glob as globlib
import os
import re
import sys

# Measured IMC medians (see references/venue-imc.md, section 2).
IMC = {
    "abstract_words": 200,          # stated limit; median accepted is 189
    "dash_per_1k": 5.5,             # 2x the measured 2.75
    "digit_sent_share": 25.0,       # measured 51.5%; below 25% is not a measurement paper
    "body_words": 11000,            # 13 pages of ACM two-column 10pt, median body is 9.4k
    "figures": 9,
    "tables": 5,
}
MEASURE_VERBS = re.compile(r"\bwe (measure|collect|crawl|observe|track|characteri[sz]e|"
                           r"quantify|instrument|scan|monitor|find|identify|analyz|analys)\w*", re.I)
EVAL_VERBS = re.compile(r"\bwe (evaluate|outperform|propose|design|implement|present)\w*", re.I)
TEST_WORDS = re.compile(r"\b(wilcoxon|mann[- ]whitney|kolmogorov|k[- ]s test|chi[- ]squared?|"
                        r"t[- ]test|bootstrap|confidence interval|p\s*[<=]|p-value)\b", re.I)
AVAIL = re.compile(r"(github\.com|gitlab|zenodo|dryad|figshare|available at|publicly available|"
                   r"we (will )?(release|publish|open[- ]source)|artifact)", re.I)
ETHICS_HEAD = re.compile(r"\\section\*?\{\s*(Ethics|Ethical[^}]*)\}", re.I)
FIRST_CLAIM = re.compile(r"\b(?:is|are|the|a|our) first (?:to|study|measurement|analysis|"
                         r"characteri|empirical|systematic|comprehensive|longitudinal|large|"
                         r"look|attempt|work)\b|\bto (?:the best of )?our knowledge,? (?:the )?first\b",
                         re.I)
HEDGE_FIRST = re.compile(r"to (the best of )?our knowledge|as far as we know", re.I)
UNBOUNDED = re.compile(r"\b(at scale|in the wild|large[- ]scale|widely deployed|web[- ]scale)\b", re.I)
SIGNIFICANT = re.compile(r"\bsignifican\w+", re.I)
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(\[\"“])")


def clean_tex(src: str) -> str:
    src = re.sub(r"(?<!\\)%.*", "", src)
    src = re.sub(r"\\(cite|ref|eqref|autoref|cref|Cref|label)\{[^}]*\}", " ", src)
    src = re.sub(r"\\begin\{(figure|table|equation|align|tabular)\*?\}.*?\\end\{\1\*?\}", " ", src,
                 flags=re.S)
    src = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", " ", src)
    src = re.sub(r"\\[a-zA-Z]+", " ", src)
    return re.sub(r"\s+", " ", src).strip()


def expand_inputs(src: str, root: str, depth: int = 0) -> str:
    """Inline \\input{sections/x.tex} so the abstract body is visible."""
    if depth > 6:
        return src

    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        for cand in (target, target + ".tex"):
            path = os.path.join(root, cand) if not os.path.isabs(cand) else cand
            if os.path.isfile(path):
                return expand_inputs(open(path, encoding="utf-8", errors="ignore").read(), root, depth + 1)
        return " "

    return re.sub(r"\\(?:input|include)\{([^}]*)\}", repl, src)


def collect(path: str, pattern: str) -> list[str]:
    if os.path.isfile(path):
        return [path]
    out: list[str] = []
    for p in [x.strip() for x in pattern.split(",") if x.strip()]:
        out += sorted(globlib.glob(os.path.join(path, "**", p), recursive=True))
    return out


def pct(n: float, d: float) -> float:
    return 100.0 * n / d if d else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    ap.add_argument("--glob", default="*.tex")
    args = ap.parse_args()

    files = collect(args.path, args.glob)
    if not files:
        print("no .tex files found", file=sys.stderr)
        return 2
    raw = {f: open(f, encoding="utf-8", errors="ignore").read() for f in files}
    root = args.path if os.path.isdir(args.path) else os.path.dirname(os.path.abspath(args.path))
    joined = expand_inputs("\n".join(raw.values()), root)
    body = clean_tex(joined)

    fails, warns, notes = [], [], []

    # ---- abstract
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", joined, re.S)
    abstract = clean_tex(m.group(1)) if m else ""
    if abstract:
        aw = len(abstract.split())
        if aw > IMC["abstract_words"]:
            fails.append(f"abstract is {aw} words; IMC states a 200-word limit "
                         f"(median accepted abstract: 189)")
        elif aw > 189:
            notes.append(f"abstract is {aw} words — inside the limit, above the 189-word median")
        if not re.search(r"\d", abstract):
            warns.append("abstract contains no number; 82% of accepted IMC abstracts carry one")
        if re.match(r"^(We|In this paper|This paper)\b", abstract):
            warns.append("abstract opens with 'We/In this paper'; only 8% of accepted IMC "
                         "abstracts do — open with the object of study and a fact about it")
        sents = [s for s in SENT.split(abstract) if len(s.split()) >= 4]
        if sents:
            mean = sum(len(s.split()) for s in sents) / len(sents)
            if mean > 28:
                warns.append(f"abstract sentences average {mean:.1f} words; IMC mean is 24.4")
    else:
        warns.append("no \\begin{abstract} found; abstract checks skipped")

    # ---- ethics appendix (mandatory at IMC)
    if not ETHICS_HEAD.search(joined) and not re.search(r"\\section\*?\{\s*Ethic", joined, re.I):
        fails.append("no section headed 'Ethics'; IMC requires one in the appendix "
                     "(a single sentence is enough, silence is not)")
    else:
        em = re.search(r"\\section\*?\{\s*Ethic[^}]*\}(.*?)(?=\\section|\Z)", joined, re.S | re.I)
        if em and len(clean_tex(em.group(1)).split()) < 12:
            warns.append("Ethics section is under 12 words; say what data, under what "
                         "agreement, with what aggregation")

    # ---- artifact availability (declaration + reason when absent)
    if not AVAIL.search(joined):
        warns.append("no artifact/data availability statement found; IMC asks for a "
                     "declaration (full/partial/none) and a reason when none")

    # ---- register: measurement verbs vs systems verbs
    nm, ne = len(MEASURE_VERBS.findall(body)), len(EVAL_VERBS.findall(body))
    if nm == 0:
        fails.append("no 'we measure/observe/find/...' in the body; this is not IMC voice")
    elif ne > nm:
        warns.append(f"systems verbs ({ne}) outnumber measurement verbs ({nm}); IMC's most "
                     f"frequent body verb is 'we find'")

    # ---- numbers per sentence
    sents = [s for s in SENT.split(body) if len(s.split()) >= 5]
    dshare = pct(sum(1 for s in sents if re.search(r"\d", s)), len(sents))
    if sents and dshare < IMC["digit_sent_share"]:
        warns.append(f"only {dshare:.0f}% of sentences carry a digit; IMC papers measure "
                     f"51.5% — the claims may be stated without their quantities")
    else:
        notes.append(f"digit-bearing sentences: {dshare:.0f}% (IMC 51.5%)")

    # ---- unbounded generality and first claims
    unb = UNBOUNDED.findall(body)
    if unb:
        warns.append(f"{len(unb)} unbounded generality phrase(s): "
                     f"{', '.join(sorted(set(x.lower() for x in unb)))} — replace with a count")
    for m in FIRST_CLAIM.finditer(body):
        window = body[max(0, m.start() - 120): m.end() + 120]
        if not HEDGE_FIRST.search(window):
            warns.append(f"unhedged 'first' claim ('{body[m.start():m.end() + 40].strip()[:70]}'): "
                         f"24% of IMC abstracts claim 'first'; bind it with "
                         f"'to our knowledge, ... across ...'")
            break

    # ---- statistics language
    if SIGNIFICANT.search(body) and not TEST_WORDS.search(body):
        warns.append("'significant' appears with no test or interval anywhere; either run "
                     "the test or say the difference is descriptive")

    # ---- dash density
    words = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", body)) or 1
    dash = 1000.0 * len(re.findall(r"[—–]", body)) / words
    if dash > IMC["dash_per_1k"]:
        warns.append(f"em-dash density {dash:.1f} per 1,000 words; IMC median is 2.75 "
                     f"(already 3x security) — keep one dash pair per paragraph")

    # ---- size, as a page-budget proxy (includes appendices and references)
    if words > IMC["body_words"]:
        notes.append(f"~{words} words including back matter; 13 IMC pages hold ~9-10k of body "
                     f"text (median 9.4k) — check the compiled page count, not this number")
    figs = len(set(re.findall(r"\\label\{(?:fig|figure)[^}]*\}", joined)))
    tabs = len(set(re.findall(r"\\label\{(?:tab|table)[^}]*\}", joined)))
    notes.append(f"figures {figs} (IMC median 9), tables {tabs} (median 5)")

    print(f"\n=== IMC checks ({len(files)} file(s), {words} body words) ===")
    for f in fails:
        print(f"  FAIL  {f}")
    for w in warns:
        print(f"  WARN  {w}")
    for n in notes:
        print(f"  note  {n}")
    if not fails and not warns:
        print("  PASS  no venue-specific issue found")
    print("\n  A FAIL or WARN may stand if the reason is recorded. Coherence outranks")
    print("  every threshold here (SKILL.md, non-negotiable 11).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
