#!/usr/bin/env python
"""How evaluation sections are divided, from ar5iv HTML section hierarchy.

For each paper: find the evaluation section(s), count their immediate subsections, classify the
subsection titles, and record the order (does a setup come first? does a summary come last?).

Usage: python eval_subsection_study.py [n_papers]
"""
from __future__ import annotations

import json
import os
import random
import re
import ssl
import statistics
import sys
import urllib.request
from collections import Counter

from lxml import html as LH

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
CORPUS = os.environ.get("PAPER_CORPUS", "corpus_v23.jsonl")

EVAL = re.compile(r"\b(evaluation|experiments?|results|measurements?|case study)\b", re.I)
CLASSES = [
    ("setup", r"\b(setup|experimental|methodology|implementation|configuration|environment)\b"),
    ("overall", r"\b(overall|main result|end.to.end|summary of (the )?(result|evaluation))\b"),
    ("ablation", r"\bablations?\b"),
    ("sensitivity", r"\b(sensitiv|robust|parameter|vary|varies|impact of|effect of|stress)\b"),
    ("comparison", r"\b(compar\w*|baseline|against|versus|vs\.?)\b"),
    ("discussion", r"\b(discussion|summary|takeaway|threat|limitation|conclusion)\b"),
    ("rq", r"\b(rq\d|research question|claim \d)\b"),
]


def fetch(url: str, timeout: int = 45) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout, context=CTX).read()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def classify(title: str) -> str:
    for name, pat in CLASSES:
        if re.search(pat, title, re.I):
            return name
    return "other"


def analyse(raw: str) -> dict | None:
    doc = LH.fromstring(raw)
    evals = []
    for sec in doc.xpath("//section"):
        title = norm(" ".join(sec.xpath("./h2//text()")))
        if not title or not EVAL.search(title) or re.search(r"appendix", title, re.I):
            continue
        # immediate subsections
        subs = []
        for sub in sec.xpath("./section"):
            t = norm(" ".join(sub.xpath("./h3//text()") or sub.xpath("./h2//text()")))
            if t:
                subs.append(t)
        if subs:
            evals.append({"title": title, "subs": subs})
    if not evals:
        return None
    main = max(evals, key=lambda e: len(e["subs"]))
    subs = main["subs"]
    classes = [classify(s) for s in subs]
    return {
        "title": main["title"],
        "n_subs": len(subs),
        "classes": classes,
        "setup_first": bool(classes) and classes[0] == "setup",
        "summary_last": bool(classes) and classes[-1] == "discussion",
        "has_setup": "setup" in classes,
        "has_ablation": "ablation" in classes,
        "has_sensitivity": "sensitivity" in classes,
    }


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()]
    random.seed(9)
    sample = random.sample(rows, min(n * 2, len(rows)))
    out, got = [], 0
    for r in sample:
        if got >= n:
            break
        base = r["id"].split("v")[0]
        for url in (f"https://ar5iv.labs.arxiv.org/html/{base}", f"https://arxiv.org/html/{r['id']}"):
            try:
                a = analyse(fetch(url).decode("utf-8", "ignore"))
                if not a:
                    raise ValueError("no eval subsections")
                a["id"] = r["id"]
                out.append(a)
                got += 1
                if got % 10 == 0:
                    print(f"{got} ok", flush=True)
                break
            except Exception as e:
                if url.startswith("https://arxiv"):
                    print("skip", r["id"], repr(e)[:40])

    if not out:
        print("no data")
        return
    json.dump(out, open(r"E:\php2shell\writing\eval_subsections.json", "w", encoding="utf-8"), indent=1)
    ns = [x["n_subs"] for x in out]
    print(f"\npapers {len(out)}")
    print(f"subsections per evaluation: median {statistics.median(ns):.0f}  mean {statistics.mean(ns):.1f}  max {max(ns)}")
    print(f"setup subsection present: {100*sum(x['has_setup'] for x in out)/len(out):.1f}%   first: {100*sum(x['setup_first'] for x in out)/len(out):.1f}%")
    print(f"summary/discussion last:   {100*sum(x['summary_last'] for x in out)/len(out):.1f}%")
    print(f"ablation subsection:       {100*sum(x['has_ablation'] for x in out)/len(out):.1f}%")
    print(f"sensitivity subsection:    {100*sum(x['has_sensitivity'] for x in out)/len(out):.1f}%")
    c = Counter(k for x in out for k in x["classes"])
    tot = sum(c.values())
    print("\nsubsection classes:")
    for k, v in c.most_common():
        print(f"  {k:12} {v:4} ({100*v/tot:.0f}%)")


if __name__ == "__main__":
    main()

