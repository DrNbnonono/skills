#!/usr/bin/env python
"""Anatomy of introductions, evaluations and appendices across the 120-paper corpus.

Questions:
  - how do top-tier introductions open, and how often do they state the RQ or list contributions?
  - how are evaluation sections organised, and how long are they?
  - what actually goes into appendices, ranked by frequency?

Usage: python anatomy_study.py
"""
from __future__ import annotations

import json
import os
import re
import statistics
from collections import Counter

CORPUS = os.environ.get("PAPER_CORPUS", "corpus_v24.jsonl")

BOILER = re.compile(
    r"^(in recent years|recently,?|with the (rapid )?(development|growth|advance|popularity)|"
    r"nowadays|over the past (few )?(years|decade)|in today'?s)", re.I)
RQ = re.compile(r"\b(we (ask|address|study|investigate|examine|measure|answer|pose|consider)|"
                r"this (paper|work|article) (asks|addresses|studies|investigates)|"
                r"our (research )?question|we seek to)\b", re.I)
CONTRIB = re.compile(r"\b(we (make|summari[sz]e|list|state)|our) (the )?(following )?contributions?\b|"
                     r"\bcontributions? (are|of this (paper|work))\b|\bwe contribute\b|"
                     r"\bin summary,? we\b|\bthis (paper|work) makes\b", re.I)
ROADMAP = re.compile(r"\b(rest of (this|the) (paper|article)|organized as follows|"
                     r"structured as follows|paper is organized)\b", re.I)
EVAL = re.compile(r"\b(evaluation|experiments?|results|measurements?|case study|findings)\b", re.I)
INTRO = re.compile(r"\bintroduction\b", re.I)

APPENDIX_TOPICS = [
    ("proofs", r"\bproof|theorem|lemma|derivation\b"),
    ("additional results", r"\badditional (results|experiments|evaluation)|extra (results|experiments)\b"),
    ("parameters / setup", r"\b(hyper)?parameters?|settings|configuration|implementation details\b"),
    ("datasets", r"\bdatasets?|corpus|data collection\b"),
    ("ablation", r"\bablations?\b"),
    ("robustness / sensitivity", r"\brobustness|sensitivity|stress test\b"),
    ("full protocol / instrument", r"\b(questionnaire|survey instrument|protocol|interview guide|prompts?)\b"),
    ("ethics / disclosure", r"\bethic|disclosure|responsible\b"),
    ("artifact / code", r"\bartifact|code|reproducib|availability\b"),
    ("extended background", r"\bbackground|preliminar|notation\b"),
    ("per-instance listings", r"\bper-(event|instance|case)|full list|complete list\b"),
]


def sents(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.split()) >= 4]


def main() -> None:
    rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()]
    n = len(rows)

    intro_paras, intro_words, boiler, rq, contrib, roadmap = [], [], 0, 0, 0, 0
    eval_paras, eval_sections = [], []
    app_titles: list[str] = []
    app_papers = 0

    for r in rows:
        secs = r["sections"]
        intro = next((s for s in secs if INTRO.search(s["title"])), secs[0] if secs else None)
        if intro:
            paras = intro["paras"]
            intro_paras.append(len(paras))
            intro_words.append(sum(len(p.split()) for p in paras))
            text = " ".join(paras)
            first = sents(text)[0] if sents(text) else ""
            if BOILER.search(first):
                boiler += 1
            if RQ.search(text):
                rq += 1
            if CONTRIB.search(text):
                contrib += 1
            if ROADMAP.search(text):
                roadmap += 1

        ev = [s for s in secs if EVAL.search(s["title"]) and not re.search(r"appendix", s["title"], re.I)]
        if ev:
            eval_sections.append(len(ev))
            eval_paras.append(sum(len(s["paras"]) for s in ev))

        app = [s for s in secs if re.search(r"\bappendix\b|^[A-Z]\s", s["title"])]
        app = [s for s in secs if re.search(r"\bappendix\b", s["title"], re.I)]
        if app:
            app_papers += 1
            app_titles += [s["title"] for s in app]

    def pct(x: int) -> str:
        return f"{x}/{n} ({100*x/n:.1f}%)"

    print(f"papers {n}")
    print("\n== introduction ==")
    print(f"  paragraphs: median {statistics.median(intro_paras):.0f}  p90 {sorted(intro_paras)[int(len(intro_paras)*0.9)-1]}")
    print(f"  words:      median {statistics.median(intro_words):.0f}  p90 {sorted(intro_words)[int(len(intro_words)*0.9)-1]}")
    print(f"  boilerplate opener ('in recent years'...): {pct(boiler)}")
    print(f"  states a research question explicitly:    {pct(rq)}")
    print(f"  announces contributions:                  {pct(contrib)}")
    print(f"  ends with a roadmap:                      {pct(roadmap)}")

    print("\n== evaluation ==")
    print(f"  papers with an evaluation section: {pct(len(eval_sections))}")
    if eval_sections:
        print(f"  evaluation sections per paper: median {statistics.median(eval_sections):.0f}  max {max(eval_sections)}")
    if eval_paras:
        print(f"  evaluation paragraphs per paper: median {statistics.median(eval_paras):.0f}  p90 {sorted(eval_paras)[int(len(eval_paras)*0.9)-1]}")

    print("\n== appendix ==")
    print(f"  papers with an appendix: {pct(app_papers)}")
    if app_titles:
        hit = Counter()
        for t in app_titles:
            for name, pat in APPENDIX_TOPICS:
                if re.search(pat, t, re.I):
                    hit[name] += 1
        print(f"  appendix sections: {len(app_titles)} across {app_papers} papers; topic hits:")
        for name, c in hit.most_common():
            print(f"    {name:28} {c}")
        print("  sample titles:")
        for t in app_titles[:12]:
            print("    -", t[:90])


if __name__ == "__main__":
    main()


