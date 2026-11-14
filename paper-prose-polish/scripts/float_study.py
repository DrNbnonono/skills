#!/usr/bin/env python
"""Where floats sit relative to the paragraph that first cites them.

arXiv LaTeXML HTML keeps structured links: a body reference is <a href="#S3.F2">Figure 2</a>
and the float itself carries id="S3.F2". That lets us measure, per float:

  appear_gap   how many paragraphs separate the first in-text mention from the float element
               (>0: float after the mention, the usual reading order; <0: float first)
  uncited      the float is never referenced in body text
  caption      sentence caption (states the takeaway) vs title caption (a noun phrase)

Usage: python float_study.py [n_papers] [out.json]
"""
from __future__ import annotations

import json
import os
import random
import re
import ssl
import statistics
import sys
import time
import urllib.request

from lxml import html as LH

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch(url: str, timeout: int = 45) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout, context=CTX).read()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


FINITE = re.compile(r"\b(is|are|was|were|shows?|show|has|have|had|can|could|may|might|"
                    r"remains?|increases?|decreases?|drops?|rises?|reaches?|confirms?|"
                    r"indicates?|means?|gives?|takes?|occurs?|appears?|falls?|grows?)\b", re.I)


def caption_kind(cap: str) -> tuple[str, int]:
    words = cap.split()
    has_sentence = bool(FINITE.search(cap)) and len(words) >= 8 and cap.rstrip().endswith(".")
    return ("sentence" if has_sentence else "title"), len(words)


def analyse(raw: str) -> dict:
    doc = LH.fromstring(raw)
    for bad in doc.xpath("//script|//style|//nav|//footer"):
        bad.getparent().remove(bad)

    # document order: count paragraphs seen so far; record floats and their first mention
    floats: dict[str, dict] = {}
    mentions: dict[str, int] = {}
    para_no = 0
    for el in doc.iter():
        tag = el.tag if isinstance(el.tag, str) else ""
        if tag == "p":
            para_no += 1
            for a in el.xpath(".//a[starts-with(@href,'#')]"):
                tgt = a.get("href")[1:]
                if tgt and tgt not in mentions:
                    mentions[tgt] = para_no
        elif tag == "figure":
            cls = el.get("class") or ""
            # ar5iv wraps equations, algorithms and tables in <figure> too; keep only real ones
            if not ("ltx_figure" in cls or "ltx_table" in cls):
                continue
            fid = el.get("id") or ""
            if not fid:
                continue
            cap = norm(" ".join(el.xpath(".//figcaption//text()") or el.xpath(".//caption//text()")))
            kind, n = caption_kind(cap) if cap else ("none", 0)
            floats[fid] = {"id": fid, "at_para": para_no, "caption_kind": kind,
                           "caption_words": n, "is_table": "ltx_table" in (el.get("class") or "")}

    out = []
    for fid, f in floats.items():
        m = mentions.get(fid)
        out.append({**f, "mentioned": m is not None,
                    "gap": (f["at_para"] - m) if m is not None else None})
    return {"paragraphs": para_no, "floats": out}


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    dst = sys.argv[2] if len(sys.argv) > 2 else r"E:\php2shell\writing\float_corpus.json"
    rows = [json.loads(l) for l in open(r"E:\php2shell\writing\corpus_v23.jsonl", encoding="utf-8") if l.strip()]
    random.seed(11)
    sample = random.sample(rows, min(n * 2, len(rows)))
    ok, papers = 0, []
    for r in sample:
        if ok >= n:
            break
        vid = r["id"]
        for path in (f"https://ar5iv.labs.arxiv.org/html/{vid.split(chr(118))[0]}", f"https://arxiv.org/html/{vid}"):
            try:
                res = analyse(fetch(path).decode("utf-8", "ignore"))
                if not res["floats"] or res["paragraphs"] < 30:
                    raise ValueError("no floats / too short")
                res.update({"id": vid, "venue": r["venue"]})
                papers.append(res)
                ok += 1
                if ok % 10 == 0:
                    print(f"{ok} ok", flush=True)
                break
            except Exception as e:
                if path.startswith("https://arxiv"):
                    print("skip", vid, repr(e)[:40], flush=True)

    json.dump(papers, open(dst, "w", encoding="utf-8"), indent=1)

    allf = [f for p in papers for f in p["floats"]]
    cited = [f for f in allf if f["mentioned"]]
    gaps = [f["gap"] for f in cited]
    print(f"\npapers {len(papers)}  floats {len(allf)}  cited {len(cited)} "
          f"({100*len(cited)/max(len(allf),1):.1f}%)")
    print(f"floats per paper: median {statistics.median([len(p['floats']) for p in papers]):.0f}")
    print(f"gap (paragraphs): median {statistics.median(gaps):.0f}  mean {statistics.mean(gaps):.1f}")
    print(f"  float appears before its first mention: {sum(1 for g in gaps if g < 0)} "
          f"({100*sum(1 for g in gaps if g<0)/len(gaps):.1f}%)")
    print(f"  gap <= 1: {100*sum(1 for g in gaps if 0 <= g <= 1)/len(gaps):.1f}%   "
          f"gap >= 5: {100*sum(1 for g in gaps if g >= 5)/len(gaps):.1f}%")
    kinds = [f["caption_kind"] for f in allf]
    print(f"captions: sentence {100*kinds.count('sentence')/len(kinds):.1f}%  "
          f"title {100*kinds.count('title')/len(kinds):.1f}%  "
          f"median words {statistics.median([f['caption_words'] for f in allf]):.0f}")
    print(f"tables: {sum(1 for f in allf if f['is_table'])}  figures: {sum(1 for f in allf if not f['is_table'])}")


if __name__ == "__main__":
    main()



