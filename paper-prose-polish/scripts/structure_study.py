#!/usr/bin/env python
"""Structural / placement study over the v2.4 corpus (section titles + paragraphs).

Answers questions a reviewer asks about layout, not wording:
  - where does related work sit relative to the method and the evaluation?
  - how many papers carry a threat-model / assumptions / ethics / limitations section?
  - how long is a paragraph, and how do introductions differ from evaluations?
  - how often does an introduction end with a roadmap sentence?
  - how often does a paragraph close by announcing the next paragraph (redundant closure)?

Usage: python structure_study.py [corpus_v24.jsonl]
"""
from __future__ import annotations

import json
import os
import re
import statistics
import sys

ROLES = [
    ("threat", r"\b(threat model|threat models|adversar|security model|assumptions?)\b"),
    ("related", r"\brelated work\b|\bprior work\b|\bbackground\b"),
    ("design", r"\b(design|approach|method|system|architecture|construction|attack|protocol|technique|analysis|model)\b"),
    ("impl", r"\bimplementation\b"),
    ("eval", r"\b(evaluation|experiments?|results|measurements?|case study|findings)\b"),
    ("limitations", r"\blimitations?\b"),
    ("discussion", r"\bdiscussion\b"),
    ("ethics", r"\bethic"),
    ("conclusion", r"\bconclusion|concluding\b"),
    ("appendix", r"\bappendix\b"),
]
ROLE_RE = [(name, re.compile(pat, re.I)) for name, pat in ROLES]
ROADMAP_RE = re.compile(r"\b(rest of (this|the) (paper|article)|organized as follows|"
                        r"structured as follows|paper is organized|article is organized)\b", re.I)
CONTRIB_RE = re.compile(r"\bcontributions?\b", re.I)
FORWARD_RE = re.compile(r"\b(below|next section|following section|we (now )?(turn|describe|present)|"
                        r"section \d|§)\b", re.I)
STOP = set("""a an the of to in for on with and or but by as at from that this these those is are was
were be been being we our it its their they them not no can may which who whom whose what when where
how than then so such also more most less least all any each other into over under between among""".split())


def role_of(title: str) -> str:
    for name, pat in ROLE_RE:
        if pat.search(title):
            return name
    return "other"


def content_words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{4,}", s.lower()) if w not in STOP}


def sents(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", text) if len(x.split()) >= 5]


def analyse(paper: dict) -> dict:
    secs = paper["sections"]
    roles = [role_of(s["title"]) for s in secs]
    first = {}
    for i, r in enumerate(roles):
        first.setdefault(r, i)

    paras = [p for s in secs for p in s["paras"]]
    pw = [len(p.split()) for p in paras]
    ps = [len(sents(p)) for p in paras]

    intro = next((s for s, r in zip(secs, roles) if r == "other" and re.search(r"introduction", s["title"], re.I)), None)
    if intro is None:
        intro = secs[0] if secs else {"paras": []}
    intro_text = " ".join(intro["paras"])

    # closure redundancy: last sentence of paragraph i overlaps first sentence of i+1
    redund = 0
    for a, b in zip(paras, paras[1:]):
        la, fb = sents(a), sents(b)
        if not la or not fb:
            continue
        overlap = content_words(la[-1]) & content_words(fb[0])
        if len(overlap) >= 2 and FORWARD_RE.search(la[-1]):
            redund += 1

    return {
        "id": paper["id"],
        "venue": paper.get("venue", "?"),
        "n_sections": len(secs),
        "roles": roles,
        "first": first,
        "paras": len(paras),
        "para_words_median": statistics.median(pw) if pw else 0,
        "para_sents_median": statistics.median(ps) if ps else 0,
        "roadmap": bool(ROADMAP_RE.search(intro_text)),
        "contrib_word": bool(CONTRIB_RE.search(intro_text)),
        "redundant_closures": redund,
    }


def pct(n: int, d: int) -> str:
    return f"{100*n/d:5.1f}%" if d else "  n/a"


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else r"E:\php2shell\writing\corpus_v24.jsonl"
    rows = [analyse(json.loads(l)) for l in open(path, encoding="utf-8") if l.strip()]
    n = len(rows)
    print(f"papers {n}\n")

    print("== first-section position by role (index among top-level sections) ==")
    for role in ("threat", "related", "design", "eval", "limitations", "ethics", "conclusion"):
        have = [r["first"][role] for r in rows if role in r["first"]]
        print(f"  {role:12} present {len(have):3}/{n} ({pct(len(have), n)})", end="")
        if have:
            print(f"  median index {statistics.median(have):.0f}  range {min(have)}-{max(have)}")
        else:
            print()

    print("\n== related work placement ==")
    before_design = sum(1 for r in rows if "related" in r["first"] and
                        ("design" not in r["first"] or r["first"]["related"] < r["first"]["design"]))
    after_eval = sum(1 for r in rows if "related" in r["first"] and "eval" in r["first"] and
                     r["first"]["related"] > r["first"]["eval"])
    print(f"  before design: {before_design}/{n} ({pct(before_design,n)})")
    print(f"  after evaluation: {after_eval}/{n} ({pct(after_eval,n)})")

    print("\n== paragraphs ==")
    pw = [r["para_words_median"] for r in rows if r["para_words_median"]]
    ps = [r["para_sents_median"] for r in rows if r["para_sents_median"]]
    print(f"  median paragraph words:   mean {statistics.mean(pw):.0f}  median {statistics.median(pw):.0f}  p90 {sorted(pw)[int(len(pw)*0.9)-1]:.0f}")
    print(f"  median paragraph sentences: mean {statistics.mean(ps):.1f}  median {statistics.median(ps):.1f}  p90 {sorted(ps)[int(len(ps)*0.9)-1]:.1f}")

    print("\n== introduction conventions ==")
    print(f"  ends with a roadmap sentence: {sum(r['roadmap'] for r in rows)}/{n} ({pct(sum(r['roadmap'] for r in rows), n)})")
    print(f"  uses the word 'contribution': {sum(r['contrib_word'] for r in rows)}/{n} ({pct(sum(r['contrib_word'] for r in rows), n)})")

    print("\n== redundant closure (last sentence overlaps the next paragraph and points forward) ==")
    tot_paras = sum(r["paras"] for r in rows)
    tot_red = sum(r["redundant_closures"] for r in rows)
    aff = sum(1 for r in rows if r["redundant_closures"])
    print(f"  paragraphs {tot_paras}  flagged {tot_red} ({1000*tot_red/tot_paras:.1f} per 1,000)")
    print(f"  papers with >=1: {aff}/{n} ({pct(aff,n)})")


if __name__ == "__main__":
    main()
