#!/usr/bin/env python
"""Local-artifact annotation (v2.3).

Five artifacts that a word-frequency counter cannot see, because each depends on the
sentence's position in its paragraph or on what the previous sentence established:

  D1 forward_quantifier   "both:" / "the two:" announced before the pair exists
  D2 label_summary        sentence-final colon + two bare noun labels ("...: accuracy and pace.")
  D3 meta_hedge           "we treat X as an empirical question" / "remains an open question"
  D4 navigation           "the rest of this paper" / "the next section" / "below"
  D5 and_opening          sentence begins with "And" / "But"

Rates are per 1,000 sentences (local artifacts are sentence-level, not word-level).
D1, D3, D5 are high-precision regexes. D2 and D4 are candidate extractors: their output
must be read by a human before any rule is written (see references/local-artifacts.md).

Usage:
    python annotate_local.py                 # table + samples
    python annotate_local.py --samples 15
"""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_prose import clean_md, clean_tex, split_sentences  # noqa: E402

CORPUS = os.environ.get("PAPER_CORPUS", "corpus_v23.jsonl")

PATTERNS = {
    # Precise: the quantifier is followed by a colon with no pair named before it.
    # "both humans and machines:" is excluded, because the pair precedes the colon.
    "D1_forward_quantifier": re.compile(
        r"\b(?:both|the two|these two|these three)\s*:"
        r"|\b(?:both|the two)\b(?:\s+(?!and\b|or\b|of\b)\w+){1,3}\s*:",
        re.I,
    ),
    "D2_label_summary": re.compile(
        r":\s*[a-z][a-z\-]*(?:\s+[a-z][a-z\-]*){0,2}\s+and\s+[a-z][a-z\-]*(?:\s+[a-z][a-z\-]*){0,2}\s*[.;]",
        re.I,
    ),
    "D3_meta_hedge": re.compile(
        r"\bwe (?:treat|consider|regard|view)\b[^.]{0,60}\bas (?:an? )?(?:empirical|open|separate|orthogonal)\b"
        r"|\b(?:is|remains|remained) an? (?:empirical|open) question\b"
        r"|\bopen question whether\b",
        re.I,
    ),
    "D4_navigation": re.compile(
        r"\b(?:rest of this (?:paper|article)|in the next section|the next section|"
        r"following section|as we show below|see below)\b",
        re.I,
    ),
    "D5_and_opening": re.compile(r"^(?:And|But)\b"),
}


def score(text: str) -> dict:
    sents = split_sentences(text)
    n = len(sents) or 1
    out = {"sentences": len(sents), "words": len(text.split())}
    for name, pat in PATTERNS.items():
        hits = [s for s in sents if pat.search(s)]
        out[name] = {"count": len(hits), "per_1k_sent": round(1000 * len(hits) / n, 1)}
    out["hits"] = {name: [s for s in sents if pat.search(s)][:50] for name, pat in PATTERNS.items()}
    return out


def load_corpus() -> list[dict]:
    if not os.path.exists(CORPUS):
        return []
    out = []
    for line in open(CORPUS, encoding="utf-8"):
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def draft_text() -> str:
    base = r"E:\php2shell\php2shell-paper\sections"
    return " ".join(
        clean_tex(open(os.path.join(base, f), encoding="utf-8").read())
        for f in sorted(os.listdir(base))
        if f.endswith(".tex")
    )


def merge(papers: list[dict], key: str | None = None) -> dict:
    text = " ".join(
        p["sections"].get(key, "") if key else " ".join(p["sections"].values()) for p in papers
    )
    return score(text)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=12)
    args = ap.parse_args()

    corpus = load_corpus()
    mag = open(r"E:\php2shell\writing\sources\spmag_sample.txt", encoding="utf-8", errors="ignore").read()
    draft = draft_text()

    results = {}
    if corpus:
        results["corpus_all"] = merge(corpus)
        for stratum in ("intro", "results"):
            subset = [p for p in corpus if p["sections"].get(stratum)]
            if subset:
                results[f"corpus_{stratum}"] = merge([{"sections": {stratum: p["sections"][stratum]}} for p in subset])
    results["magazine"] = score(mag)
    results["draft"] = score(draft)

    names = list(PATTERNS)
    hdr = f"{'corpus':18}{'sent':>7}" + "".join(f"{n[:14]:>16}" for n in names)
    print(hdr)
    print("-" * len(hdr))
    for label, r in results.items():
        row = f"{label:18}{r['sentences']:>7}"
        for n in names:
            row += f"{r[n]['count']:>5} ({r[n]['per_1k_sent']:>6.1f})"
        print(row)
    print("\n(cells: raw count (per 1,000 sentences))")

    if corpus:
        pw = [score(" ".join(p["sections"].values())) for p in corpus]
        print(f"\npapers: {len(corpus)}  words: {sum(p['words'] for p in corpus):,}")
        for n in names:
            vals = [p[n]["per_1k_sent"] for p in pw]
            nonzero = sum(1 for v in vals if v > 0)
            print(f"  {n:24} papers with >=1: {nonzero:2}/{len(pw)}   mean {statistics.mean(vals):5.2f}   max {max(vals):5.1f}")

    json.dump({k: {kk: vv for kk, vv in v.items() if kk != "hits"} for k, v in results.items()},
              open(r"E:\php2shell\writing\local_artifacts.json", "w", encoding="utf-8"), indent=1)

    print("\n=== samples ===")
    for n in names:
        print(f"\n--- {n} ---")
        for src in ("corpus_all", "magazine", "draft"):
            if src in results:
                for s in results[src]["hits"][n][: args.samples if src != "draft" else 50]:
                    print(f"  [{src}] {s[:220]}")


if __name__ == "__main__":
    main()

