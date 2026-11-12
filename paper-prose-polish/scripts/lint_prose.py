#!/usr/bin/env python3
"""Sentence-level prose linter for academic manuscripts (v2).

Measures the surface features that make reviewers stall: sentence length, dropped agents
(passive), nominalisation stacks, loose `which` clauses, bare `This`, dash density.

v2 adds the four **L2 blockers** — the measures that predict whether a competent
non-native reader gets the sentence on the first pass:
  * words before the main verb,
  * subordinate clauses per sentence,
  * idioms / phrasal verbs,
  * non-transparent formal words,
plus a Flesch reading-ease estimate and a `--gate` pass/fail mode.

Usage
-----
    python lint_prose.py                          # current directory, *.tex
    python lint_prose.py --path paper/ --glob "*.tex"
    python lint_prose.py --path draft.md          # a single file
    python lint_prose.py --json baseline.json --worst 15
    python lint_prose.py --compare baseline.json  # per-file deltas after a revision round
    python lint_prose.py --gate --venue magazine  # pass/fail against magazine thresholds
    python lint_prose.py --explain 10             # the 10 sentences with the most stalls

Exit code: 0 normally; with --gate, 1 when a gate check fails (so it can be used in CI).
"""
from __future__ import annotations

import argparse
import glob as globlib
import json
import os
import re
import statistics
import sys

FLOAT_RE = re.compile(r"\\begin\{(table|figure|algorithm)\}.*?\\end\{\1\}", re.S)
INPUT_RE = re.compile(r"\\input\{[^}]*\}")
MATH_RE = re.compile(r"\$[^$]*\$|\$\$.*?\$\$", re.S)
TEXCMD_RE = re.compile(r"\\[a-zA-Z]+\*?")

CMD_WITH_ARG_RE = re.compile(
    r"\\(?:cite|citep|citet|ref|eqref|autoref|cref|emph|textbf|textit|textsc|texttt|textsf|"
    r"url|href|footnote|todo|mbox|mathrm|text)\*?(?:\[[^\]]*\])?\{([^{}]*)\}"
)

# Names that must expand to a capitalised token; otherwise the splitter sees a lowercase
# word after a full stop and fuses two sentences.
NAMED = {r"\sysname": "System", r"\S": "Section", r"\ieeeparstart": ""}

PASSIVE_RE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
    r"(?:\w+ed|\w+en|built|made|shown|given|taken|found|held|kept|left|written|drawn|set|"
    r"split|run|done|known|seen|chosen|driven|put|read)\b",
    re.I,
)
NOM_RE = re.compile(
    r"\b\w{4,}(?:tion|tions|ment|ments|ance|ences?|ization|isation|ity|ities|ness)\b", re.I
)
BARE_THIS_RE = re.compile(
    r"(?:^|[.;:]\s)(?:This|These)\s+(?:is|are|was|were|has|have|means|makes|shows|suggests|"
    r"implies|leaves|requires)\b"
)
WE_START_RE = re.compile(r"(?:^|[.!?]\s+)(?:We|Our)\b")

# Negation metrics (L18 / A17). Reference norm measured with this counter: 16 top-tier
# security papers average 4.6 negators per 1,000 words (range 2.6-7.1), 0.8% of sentences
# carry two or more, and author-negation ("we do not claim/assume") is near zero. A full
# issue of IEEE S&P Magazine measures the same 4.6 / 0.8%.
CORE_NEG_RE = re.compile(
    r"\b(?:not|no|never|none|nobody|nothing|neither|nor|cannot|without)\b|n't\b", re.I
)
CONTRAST_RE = re.compile(
    r"\b(?:rather than|instead of|as opposed to|unlike|in contrast|by contrast|"
    r"on the contrary|contrary to)\b",
    re.I,
)
AUTHOR_NEG_RE = re.compile(
    r"\bwe\s+(?:do not|don't|did not|didn't|cannot|can't|never|are not)\b", re.I
)

# L19: a quantifier that announces a pair it has not introduced ("We measure both: X and Y").
FORWARD_QUANT_RE = re.compile(
    r"\bboth\s*:|\btwo (?:things|parts|measurements|questions)\s*:|"
    r"\bthe (?:two|three)\s+(?:things|parts|measurements)\s*:",
    re.I,
)

# ---------------------------------------------------------------------------
# L2 blocker lexicons
# ---------------------------------------------------------------------------

AUX = {
    "is", "are", "was", "were", "be", "been", "being", "am", "do", "does", "did", "has",
    "have", "had", "can", "could", "may", "might", "must", "shall", "should", "will",
    "would", "ought",
}

COMMON_VERBS = {
    "ask", "argue", "assemble", "attempt", "become", "begin", "build", "call", "carry",
    "change", "claim", "code", "collect", "compare", "connect", "consider", "continue",
    "count", "cover", "decide", "decrease", "define", "depend", "describe", "design",
    "differ", "divide", "do", "double", "draw", "drop", "end", "expect", "explain",
    "fail", "fall", "find", "follow", "gather", "generalise", "generalize", "give", "grow",
    "guide", "hold", "identify", "imply", "improve", "increase", "indicate", "keep",
    "leave", "let", "limit", "look", "make", "mean", "measure", "meet", "motivate",
    "move", "name", "need", "note", "pair", "pick", "present", "propose", "provide",
    "put", "reach", "reason", "recall", "record", "reduce", "reflect", "remain", "report",
    "require", "rise", "run", "see", "separate", "show", "split", "start", "stop",
    "succeed", "suggest", "support", "surface", "take", "tend", "test", "trace", "treat",
    "triple", "turn", "use", "validate", "vary", "verify", "want", "work",
}

SUBORDINATORS = {
    "because", "although", "though", "while", "whereas", "which", "who", "whom", "whose",
    "if", "unless", "since", "until", "when", "where", "after", "before", "that",
}

# Idioms and phrasal verbs: short, native, opaque to a reader who does not share them.
IDIOMS = [
    r"carry(?:ing|ied|ies)? out",
    r"come up with", r"came up with", r"coming up with",
    r"fall(?:s|ing)? short", r"fell short",
    r"fall(?:s|ing)? through the cracks", r"fell through the cracks",
    r"hold(?:s|ing)? up", r"held up",
    r"look(?:s|ing|ed)? into",
    r"figure(?:s|d)? out", r"figuring out",
    r"get(?:s|ting)? around",
    r"end(?:s|ed|ing)? up",
    r"set(?:s|ting)? up",
    r"rule(?:s|d)? out",
    r"single(?:s|d)? out",
    r"take(?:s|n|ing)? into account",
    r"play(?:s|ed|ing)? a role",
    r"shed(?:s|ding)? light",
    r"a host of", r"at odds with", r"in the face of", r"on the fly",
    r"in turn", r"the vast majority", r"a number of",
    r"leave(?:s|ing)? room", r"make(?:s|ing)? sense",
    r"go(?:es|ing)? without saying", r"rule of thumb",
]

# Non-transparent formal words: each has a plain replacement in references/vocabulary.md.
FORMAL_WORDS = [
    r"utiliz(?:e|es|ed|ing)", r"demonstrat(?:e|es|ed|ing)", r"facilitat(?:e|es|ed|ing)",
    r"leverag(?:e|es|ed|ing)", r"commenc(?:e|es|ed|ing)", r"terminat(?:e|es|ed|ing)",
    r"endeavor(?:s|ed|ing)?", r"endeavour(?:s|ed|ing)?", r"ascertain(?:s|ed|ing)?",
    r"elucidat(?:e|es|ed|ing)", r"constitut(?:e|es|ed|ing)", r"compris(?:e|es|ed|ing)",
    r"aforementioned", r"henceforth", r"notwithstanding", r"whilst", r"amongst",
    r"thereby", r"herein", r"thereof",
    r"prior to", r"subsequent to", r"in order to", r"with respect to",
    r"due to the fact that", r"it is worth noting that", r"it should be noted that",
]

IDIOM_RE = [re.compile(r"\b" + p + r"\b", re.I) for p in IDIOMS]
FORMAL_RE = [re.compile(r"\b" + p + r"\b", re.I) for p in FORMAL_WORDS]

VOWEL_GROUP = re.compile(r"[aeiouy]+", re.I)


def syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    n = len(VOWEL_GROUP.findall(w))
    if w.endswith("e") and n > 1 and not w.endswith(("le", "ee", "ye")):
        n -= 1
    return max(1, n)


def words_before_verb(words: list[str]) -> int | None:
    """Heuristic distance from sentence start to the first finite verb."""
    for i, raw in enumerate(words):
        w = re.sub(r"[^a-z]", "", raw.lower())
        if not w:
            continue
        if w in AUX or w in COMMON_VERBS:
            return i
        if len(w) > 3 and w.endswith("ed"):
            return i
        if len(w) > 3 and w.endswith("s") and w[:-1] in COMMON_VERBS:
            return i
    return None


def count_clauses(words: list[str]) -> int:
    return sum(1 for w in words if re.sub(r"[^a-z]", "", w.lower()) in SUBORDINATORS)


# ---------------------------------------------------------------------------
# Cleaning and splitting (unchanged from v1, plus .txt support)
# ---------------------------------------------------------------------------
def clean_tex(tex: str) -> str:
    tex = re.sub(r"(?<!\\)%.*", "", tex)
    tex = FLOAT_RE.sub(" ", tex)
    tex = INPUT_RE.sub(" ", tex)
    tex = re.sub(r"\\label\{[^{}]*\}", " ", tex)
    tex = re.sub(r"\\S\s*\\c?ref\{[^{}]*\}", " Section ", tex)
    tex = re.sub(r"\\c?ref\{[^{}]*\}", " Section ", tex)
    tex = re.sub(r"\\eqref\{[^{}]*\}", " MATH ", tex)
    tex = re.sub(r"\\cite[a-z]*\{[^{}]*\}", " ", tex)
    tex = re.sub(r"\\(?:sub)*section\*?\{[^{}]*\}", " . ", tex)
    tex = re.sub(r"\\paragraph\*?\{[^{}]*\}", " . ", tex)
    tex = re.sub(r"\\item\b", " . ", tex)
    tex = re.sub(r"\\begin\{itemize\}(\[[^\]]*\])?", " . ", tex)
    tex = re.sub(r"\\end\{itemize\}", " . ", tex)
    for k, v in NAMED.items():
        tex = re.sub(re.escape(k) + r"\b", v, tex)
    tex = MATH_RE.sub(" MATH ", tex)
    prev = None
    while prev != tex:
        prev = tex
        tex = CMD_WITH_ARG_RE.sub(r" \1 ", tex)
    tex = TEXCMD_RE.sub(" ", tex)
    tex = re.sub(r"[{}~]", " ", tex)
    return re.sub(r"\s+", " ", tex).strip()


def clean_text(txt: str) -> str:
    """LaTeX-free text (.txt, .md): strip references and tables, keep the prose."""
    lines = []
    for line in txt.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith(("REFERENCES", "References", "Bibliography")):
            break
        if s.startswith("|") or re.match(r"^\[?\d+\]?\s", s):
            continue
        lines.append(s)
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def clean_md(md: str) -> str:
    out, fenced = [], False
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("```"):
            fenced = not fenced
            out.append(" . ")
            continue
        if fenced:
            continue
        if s in {"---", "***", "___"} or set(s) <= {"-", "*", "_", " "} and len(s) >= 3:
            out.append(" . ")
            continue
        if s.startswith("|") or s.startswith("    ") or s.startswith("\t"):
            continue
        if s.startswith("#"):
            out.append(" . ")
            continue
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"[*_`>]", "", s)
        s = re.sub(r"^\s*[-*+]\s+(\[[ xX]\]\s*)?", "", s)
        s = re.sub(r"^\s*\d+[.)]\s+", "", s)
        out.append(s + " . ")
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def split_sentences(text: str, min_words: int = 6) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[\"'`$0-9])", text)
    return [p.strip() for p in parts if len(p.strip().split()) >= min_words]


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def analyse_file(path: str) -> tuple[list[dict], dict]:
    raw = open(path, encoding="utf-8", errors="replace").read()
    low = path.lower()
    if low.endswith(".tex"):
        text = clean_tex(raw)
    elif low.endswith(".md"):
        text = clean_md(raw)
    else:
        text = clean_text(raw)
    rows = []
    for s in split_sentences(text):
        words = s.split()
        w2v = words_before_verb(words)
        clauses = count_clauses(words)
        idioms = sum(len(r.findall(s)) for r in IDIOM_RE)
        formal = sum(len(r.findall(s)) for r in FORMAL_RE)
        syl = sum(syllables(w) for w in words)
        neg = len(CORE_NEG_RE.findall(s))
        contrast = len(CONTRAST_RE.findall(s))
        author_neg = len(AUTHOR_NEG_RE.findall(s))
        fq = len(FORWARD_QUANT_RE.findall(s))
        rows.append(
            {
                "file": os.path.basename(path),
                "words": len(words),
                "sent": s,
                "passive": bool(PASSIVE_RE.search(s)),
                "nom": len(NOM_RE.findall(s)),
                "which": len(re.findall(r",?\s+which\b", s)),
                "bare_this": bool(BARE_THIS_RE.search(s)),
                "we_start": bool(WE_START_RE.search(s)),
                "dash": s.count("---"),
                "w2v": w2v,
                "clauses": clauses,
                "parens": s.count("("),
                "idioms": idioms,
                "formal": formal,
                "syll": syl,
                "neg": neg,
                "contrast": contrast,
                "author_neg": author_neg,
                "fq": fq,
            }
        )
    n = len(rows)
    words = [r["words"] for r in rows]
    w2v_valid = [r["w2v"] for r in rows if r["w2v"] is not None]
    total_words = sum(words) or 1
    total_sent = n or 1
    total_syl = sum(r["syll"] for r in rows) or 1
    agg = {
        "file": os.path.basename(path),
        "sentences": n,
        "words": sum(words),
        "mean": round(statistics.mean(words), 1) if words else 0.0,
        "median": statistics.median(words) if words else 0,
        "p90": sorted(words)[max(0, int(n * 0.9) - 1)] if words else 0,
        "max": max(words) if words else 0,
        "over35": sum(1 for w in words if w > 35),
        "over45": sum(1 for w in words if w > 45),
        "over45_per100": round(100 * sum(1 for w in words if w > 45) / total_sent, 1),
        "passive_pct": round(100 * sum(r["passive"] for r in rows) / total_sent),
        "nom_per_sent": round(sum(r["nom"] for r in rows) / total_sent, 2),
        "which_per_sent": round(sum(r["which"] for r in rows) / total_sent, 2),
        "bare_this": sum(r["bare_this"] for r in rows),
        "we_start": sum(r["we_start"] for r in rows),
        "dashes": sum(r["dash"] for r in rows),
        # negation (L18)
        "neg_per_1k": round(1000 * sum(r["neg"] for r in rows) / total_words, 1),
        "double_neg_pct": round(
            100 * sum(1 for r in rows if r["neg"] >= 2) / total_sent, 1
        ),
        "contrast_per_1k": round(1000 * sum(r["contrast"] for r in rows) / total_words, 2),
        "author_neg_per_1k": round(
            1000 * sum(r["author_neg"] for r in rows) / total_words, 2
        ),
        "fq": sum(r["fq"] for r in rows),
        "fq_per_1k": round(1000 * sum(r["fq"] for r in rows) / total_words, 2),
        # L2 blockers
        "w2v_mean": round(statistics.mean(w2v_valid), 1) if w2v_valid else 0.0,
        "w2v_over10": sum(1 for v in w2v_valid if v > 10),
        "clauses_mean": round(sum(r["clauses"] for r in rows) / total_sent, 2),
        "clauses_over2": sum(1 for r in rows if r["clauses"] > 2),
        "parens_mean": round(sum(r["parens"] for r in rows) / total_sent, 2),
        "idioms": sum(r["idioms"] for r in rows),
        "idioms_per_1k": round(1000 * sum(r["idioms"] for r in rows) / total_words, 2),
        "formal": sum(r["formal"] for r in rows),
        "formal_per_1k": round(1000 * sum(r["formal"] for r in rows) / total_words, 2),
        "flesch": round(
            206.835 - 1.015 * (total_words / total_sent) - 84.6 * (total_syl / total_words), 1
        ),
    }
    return rows, agg


def collect(path: str, pattern: str) -> list[str]:
    if os.path.isfile(path):
        return [path]
    patterns = [p.strip() for p in pattern.split(",") if p.strip()]
    files: list[str] = []
    for p in patterns:
        files += sorted(globlib.glob(os.path.join(path, "**", p), recursive=True))
    seen, out = set(), []
    for f in files:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
GATE_TABLE = {
    "conference": [
        ("mean", "<=", 25, "mean sentence length"),
        ("p90", "<=", 38, "p90 sentence length"),
        ("over45_per100", "<=", 2.5, "sentences over 45 words, per 100"),
        ("passive_pct", "<=", 18, "passive rate %"),
        ("nom_per_sent", "<=", 1.6, "nominalisations per sentence"),
        ("w2v_mean", "<=", 10, "mean words before the main verb"),
        ("clauses_over2", "<=", 0.15, "share of sentences with >2 clauses"),
        ("idioms_per_1k", "<=", 2, "idioms per 1,000 words"),
        ("formal_per_1k", "<=", 5, "non-transparent formal words per 1,000"),
        ("neg_per_1k", "<=", 6, "negators per 1,000 words"),
        ("double_neg_pct", "<=", 1.5, "sentences with >=2 negators %"),
        ("contrast_per_1k", "<=", 1.5, "contrast markers per 1,000 words"),
        ("fq_per_1k", "<=", 0.2, "forward-announcing quantifiers per 1,000"),
    ],
    "magazine": [
        ("mean", "<=", 25, "mean sentence length"),
        ("p90", "<=", 32, "p90 sentence length"),
        ("over45_per100", "<=", 1.5, "sentences over 45 words, per 100"),
        ("passive_pct", "<=", 12, "passive rate %"),
        ("nom_per_sent", "<=", 1.4, "nominalisations per sentence"),
        ("w2v_mean", "<=", 10, "mean words before the main verb"),
        ("clauses_over2", "<=", 0.10, "share of sentences with >2 clauses"),
        ("idioms_per_1k", "<=", 2, "idioms per 1,000 words"),
        ("formal_per_1k", "<=", 3, "non-transparent formal words per 1,000"),
        ("neg_per_1k", "<=", 6, "negators per 1,000 words"),
        ("double_neg_pct", "<=", 1.5, "sentences with >=2 negators %"),
        ("contrast_per_1k", "<=", 1.5, "contrast markers per 1,000 words"),
        ("fq_per_1k", "<=", 0.2, "forward-announcing quantifiers per 1,000"),
    ],
}


def run_gate(agg: dict, venue: str) -> bool:
    print(f"\n=== GATE ({venue}) ===")
    ok = True
    total_sent = agg["sentences"] or 1
    for key, op, limit, label in GATE_TABLE[venue]:
        val = agg[key]
        if key == "clauses_over2":
            val = round(val / total_sent, 3)
        passed = val <= limit
        ok = ok and passed
        print(f"  {'PASS' if passed else 'FAIL'}  {label:45s} {val:>8} (limit {op} {limit})")
    print("  RESULT:", "PASS" if ok else "FAIL")
    return ok


def explain(rows: list[dict], n: int) -> None:
    print(f"\n=== {n} sentences with the most L2 blockers ===")
    scored = []
    for r in rows:
        score = 0
        reasons = []
        if r["passive"]:
            score += 2
            reasons.append("passive (S1)")
        if r["w2v"] is not None and r["w2v"] > 10:
            score += 2
            reasons.append(f"verb at word {r['w2v']} (S2)")
        if r["clauses"] > 2:
            score += 2
            reasons.append(f"{r['clauses']} clauses (S3)")
        if r["parens"] > 1:
            score += 1
            reasons.append(f"{r['parens']} parentheses")
        if r["idioms"]:
            score += 2
            reasons.append(f"{r['idioms']} idiom(s) (S4)")
        if r["formal"]:
            score += 1
            reasons.append(f"{r['formal']} formal word(s) (S4)")
        if r["nom"] >= 3:
            score += 1
            reasons.append(f"{r['nom']} nominalisations (S7)")
        if r["bare_this"]:
            score += 1
            reasons.append("bare This (S5)")
        if r["words"] > 45:
            score += 1
            reasons.append(f"{r['words']} words")
        if score:
            scored.append((score, r, reasons))
    for score, r, reasons in sorted(scored, key=lambda x: -x[0])[:n]:
        print(f"\n[{r['file']}] score {score} :: {r['sent'][:300]}")
        print(f"    blockers: {', '.join(reasons)}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=".", help="file or directory")
    ap.add_argument("--glob", default="*.tex", help="comma-separated globs, e.g. '*.tex,*.md,*.txt'")
    ap.add_argument("--json", default=None, help="write metrics to this JSON file")
    ap.add_argument("--compare", default=None, help="baseline JSON to diff against")
    ap.add_argument("--worst", type=int, default=12, help="how many longest sentences to print")
    ap.add_argument("--gate", action="store_true", help="print pass/fail against venue thresholds")
    ap.add_argument("--venue", default="conference", choices=["conference", "magazine"])
    ap.add_argument("--explain", type=int, default=0, help="print N sentences with the most L2 blockers")
    args = ap.parse_args()

    files = collect(args.path, args.glob)
    if not files:
        print(f"no files matched {args.glob} under {args.path}")
        sys.exit(0)

    all_rows, aggs = [], []
    for f in files:
        rows, agg = analyse_file(f)
        all_rows += rows
        aggs.append(agg)

    hdr = (
        f"{'file':24}{'sent':>6}{'words':>6}{'mean':>6}{'med':>6}{'p90':>5}{'max':>5}"
        f"{'>35':>5}{'>45':>5}{'pass%':>6}{'nom/s':>6}{'This':>5}{'We':>4}{'---':>4}"
        f"{'w2v':>5}{'cl/s':>5}{'idiom':>6}{'formal':>7}{'FRES':>6}{'neg/1k':>7}{'dbl%':>6}"
    )
    print(hdr)
    print("-" * len(hdr))
    for a in aggs:
        print(
            f"{a['file'][:23]:24}{a['sentences']:>6}{a['words']:>6}{a['mean']:>6}"
            f"{a['median']:>6}{a['p90']:>5}{a['max']:>5}{a['over35']:>5}{a['over45']:>5}"
            f"{a['passive_pct']:>6}{a['nom_per_sent']:>6}{a['bare_this']:>5}{a['we_start']:>4}"
            f"{a['dashes']:>4}{a['w2v_mean']:>5}{a['clauses_mean']:>5}{a['idioms']:>6}"
            f"{a['formal']:>7}{a['flesch']:>6}{a['neg_per_1k']:>7}{a['double_neg_pct']:>6}"
        )

    n = len(all_rows) or 1
    w = [r["words"] for r in all_rows]
    total = {
        "sentences": n,
        "words": sum(w),
        "mean": round(statistics.mean(w), 1) if w else 0,
        "p90": sorted(w)[max(0, int(n * 0.9) - 1)] if w else 0,
        "over45": sum(1 for x in w if x > 45),
        "over45_per100": round(100 * sum(1 for x in w if x > 45) / n, 1),
        "passive_pct": round(100 * sum(r["passive"] for r in all_rows) / n),
        "nom_per_sent": round(sum(r["nom"] for r in all_rows) / n, 2),
        "bare_this": sum(r["bare_this"] for r in all_rows),
        "we_start": sum(r["we_start"] for r in all_rows),
        "dashes": sum(r["dash"] for r in all_rows),
        "w2v_mean": round(statistics.mean([r["w2v"] for r in all_rows if r["w2v"] is not None]), 1)
        if any(r["w2v"] is not None for r in all_rows)
        else 0,
        "clauses_over2": sum(1 for r in all_rows if r["clauses"] > 2),
        "idioms": sum(r["idioms"] for r in all_rows),
        "idioms_per_1k": round(1000 * sum(r["idioms"] for r in all_rows) / (sum(w) or 1), 2),
        "formal": sum(r["formal"] for r in all_rows),
        "formal_per_1k": round(1000 * sum(r["formal"] for r in all_rows) / (sum(w) or 1), 2),
        "flesch": round(statistics.mean([a["flesch"] for a in aggs]), 1) if aggs else 0,
        "neg_per_1k": round(1000 * sum(r["neg"] for r in all_rows) / (sum(w) or 1), 1),
        "double_neg_pct": round(100 * sum(1 for r in all_rows if r["neg"] >= 2) / n, 1),
        "contrast_per_1k": round(1000 * sum(r["contrast"] for r in all_rows) / (sum(w) or 1), 2),
        "author_neg_per_1k": round(
            1000 * sum(r["author_neg"] for r in all_rows) / (sum(w) or 1), 2
        ),
        "fq": sum(r["fq"] for r in all_rows),
        "fq_per_1k": round(1000 * sum(r["fq"] for r in all_rows) / (sum(w) or 1), 2),
    }
    print("-" * len(hdr))
    print(
        f"{'TOTAL':24}{n:>6}{total['words']:>6}{total['mean']:>6}"
        f"{statistics.median(w):>6}{total['p90']:>5}{max(w):>5}"
        f"{sum(1 for x in w if x > 35):>5}{total['over45']:>5}{total['passive_pct']:>6}"
        f"{total['nom_per_sent']:>6}{total['bare_this']:>5}{total['we_start']:>4}{total['dashes']:>4}"
        f"{total['w2v_mean']:>5}{round(sum(r['clauses'] for r in all_rows) / n, 2):>5}"
        f"{total['idioms']:>6}{total['formal']:>7}{total['flesch']:>6}"
        f"{total['neg_per_1k']:>7}{total['double_neg_pct']:>6}"
    )

    if args.compare and os.path.exists(args.compare):
        base = json.load(open(args.compare, encoding="utf-8")).get("aggregate", [])
        bmap = {b["file"]: b for b in base}
        print(f"\n=== deltas vs {os.path.basename(args.compare)} ===")
        print(f"{'file':24}{'mean':>12}{'p90':>10}{'>45':>10}{'pass%':>10}{'w2v':>10}{'idiom':>10}")
        for a in aggs:
            b = bmap.get(a["file"])
            if not b:
                continue
            print(
                f"{a['file'][:23]:24}"
                f"{b['mean']:>6.1f}->{a['mean']:<5.1f}"
                f"{b['p90']:>4}->{a['p90']:<4}"
                f"{b['over45']:>4}->{a['over45']:<4}"
                f"{b['passive_pct']:>4}->{a['passive_pct']:<4}"
                f"{b.get('w2v_mean', 0):>5.1f}->{a['w2v_mean']:<4.1f}"
                f"{b.get('idioms', 0):>4}->{a['idioms']:<4}"
            )

    print(f"\n=== {args.worst} longest sentences ===")
    for r in sorted(all_rows, key=lambda r: -r["words"])[: args.worst]:
        print(f"[{r['file']}] {r['words']}w :: {r['sent'][:240]}")

    gate_ok = True
    if args.gate:
        gate_ok = run_gate(total, args.venue)

    if args.explain:
        explain(all_rows, args.explain)

    if args.json:
        json.dump(
            {"aggregate": aggs, "sentences": all_rows},
            open(args.json, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=1,
        )
        print(f"\nwrote {args.json}")

    if args.gate and not gate_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
