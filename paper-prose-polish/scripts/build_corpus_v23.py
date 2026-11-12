#!/usr/bin/env python
"""Build a section-segmented corpus of top-tier security papers (v2.3).

Fetches arXiv full text (LaTeXML HTML), segments it into top-level sections, and labels
introduction / related work / results / conclusion. Output: JSONL, one paper per line.

Usage:  python build_corpus_v23.py [target_papers]
"""
from __future__ import annotations

import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request

from lxml import html as LH

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

QUERIES = [
    ('co:"USENIX Security"', "usenix"),
    ('co:"IEEE S&P"', "sp"),
    ('co:"IEEE Symposium on Security and Privacy"', "sp"),
    ('co:"ACM CCS"', "ccs"),
    ('co:"NDSS"', "ndss"),
    ('co:"Computer and Communications Security"', "ccs"),
    ('co:"Oakland"', "sp"),
]

SECTION_PATTERNS = {
    "intro": re.compile(r"\b(introduction|overview)\b", re.I),
    "related": re.compile(r"\brelated work\b|\bbackground\b", re.I),
    "results": re.compile(r"\b(result|evaluation|experiment|measurement|findings?)\b", re.I),
    "conclusion": re.compile(r"\b(conclusion|concluding|discussion and conclusion)\b", re.I),
}


def fetch(url: str, timeout: int = 35) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout, context=CTX).read()


def arxiv_ids(query: str, want: int) -> list[str]:
    # arXiv wants co:%22USENIX+Security%22: quotes percent-encoded, spaces as '+',
    # and the field prefix colon left literal.
    q = urllib.parse.quote_plus(query, safe=":")
    url = (
        "http://export.arxiv.org/api/query?search_query="
        + q
        + f"&start=0&max_results={want}&sortBy=relevance"
    )
    raw = fetch(url, 30).decode("utf-8", "ignore")
    return re.findall(r"<id>http://arxiv.org/abs/([^<]+)</id>", raw)[1:]


def clean(node) -> str:
    txt = " ".join(node.itertext())
    return re.sub(r"\s+", " ", txt).strip()


def segment(raw_html: str) -> dict:
    doc = LH.fromstring(raw_html)
    for bad in doc.xpath("//script|//style|//math|//nav|//footer"):
        bad.getparent().remove(bad)
    out = {"intro": [], "related": [], "results": [], "conclusion": [], "other": []}
    for sec in doc.xpath("//section[not(ancestor::section)]"):
        title = " ".join(sec.xpath("./h2//text()")).strip()
        body = clean(sec)
        if len(body.split()) < 200:
            continue
        label = "other"
        for name, pat in SECTION_PATTERNS.items():
            if pat.search(title):
                label = name
                break
        out[label].append(body)
    return {k: " ".join(v) for k, v in out.items()}


def main() -> None:
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 70
    dst = os.environ.get("PAPER_CORPUS", "corpus_v23.jsonl")
    seen, got = set(), 0
    with open(dst, "a", encoding="utf-8") as fh:
        for query, venue in QUERIES:
            if got >= target:
                break
            try:
                ids = arxiv_ids(query, 60)
            except Exception as e:
                print("query failed", query, repr(e)[:60])
                continue
            time.sleep(3)
            for vid in ids:
                if got >= target:
                    break
                base = vid.split("v")[0]
                if base in seen:
                    continue
                seen.add(base)
                for path in (f"https://arxiv.org/html/{vid}", f"https://arxiv.org/html/{base}v1"):
                    try:
                        raw = fetch(path).decode("utf-8", "ignore")
                        parts = segment(raw)
                        total = sum(len(v.split()) for v in parts.values())
                        if total < 3000:
                            raise ValueError("too short")
                        rec = {"id": vid, "venue": venue, "words": total,
                               "sections": {k: v for k, v in parts.items() if v}}
                        fh.write(json.dumps(rec) + "\n")
                        fh.flush()
                        got += 1
                        print(f"OK {got}/{target} {vid} {venue} {total}w")
                        break
                    except Exception as e:
                        print("  skip", vid, repr(e)[:50])
    print("done", got)


if __name__ == "__main__":
    main()

