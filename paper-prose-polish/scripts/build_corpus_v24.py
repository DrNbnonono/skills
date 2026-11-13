#!/usr/bin/env python
"""v2.4 corpus: section titles + paragraph boundaries.

The v2.3 corpus stored flat text per section bucket, which made two questions
unanswerable: where a section sits relative to the others, and where a paragraph ends.
This builder keeps the ordered section list, each section's title, and its paragraphs.

Record: {"id","venue","words","sections":[{"title":str,"paras":[str,...]},...]}

Usage: python build_corpus_v24.py <ids_file_or_jsonl> <out.jsonl>
"""
from __future__ import annotations

import json
import os
import re
import ssl
import sys
import time
import urllib.request

from lxml import html as LH

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch(url: str, timeout: int = 35) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout, context=CTX).read()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def parse(raw: str) -> list[dict]:
    doc = LH.fromstring(raw)
    for bad in doc.xpath("//script|//style|//math|//nav|//footer|//table"):
        bad.getparent().remove(bad)
    out = []
    for sec in doc.xpath("//section[not(ancestor::section)]"):
        title = norm(" ".join(sec.xpath("./h2//text()")))
        paras = []
        for p in sec.xpath(".//p"):
            txt = norm(" ".join(p.itertext()))
            if len(txt.split()) >= 25:
                paras.append(txt)
        if paras:
            out.append({"title": title, "paras": paras})
    return out


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    ids = []
    if src.endswith(".jsonl"):
        for line in open(src, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                ids.append((r["id"], r["venue"]))
    else:
        ids = [(l.strip(), "unknown") for l in open(src, encoding="utf-8") if l.strip()]

    done = set()
    if os.path.exists(dst):
        for line in open(dst, encoding="utf-8"):
            if line.strip():
                done.add(json.loads(line)["id"])
    ok = 0
    with open(dst, "a", encoding="utf-8") as fh:
        for vid, venue in ids:
            if vid in done:
                continue
            for path in (f"https://arxiv.org/html/{vid}", f"https://arxiv.org/html/{vid.split('v')[0]}v1"):
                try:
                    secs = parse(fetch(path).decode("utf-8", "ignore"))
                    words = sum(len(p.split()) for s in secs for p in s["paras"])
                    if words < 2500:
                        raise ValueError("short")
                    fh.write(json.dumps({"id": vid, "venue": venue, "words": words, "sections": secs}) + "\n")
                    fh.flush()
                    ok += 1
                    if ok % 10 == 0:
                        print(f"{ok} ok", flush=True)
                    break
                except Exception as e:
                    if path.endswith("v1"):
                        print("skip", vid, repr(e)[:40], flush=True)
                    time.sleep(0.3)
    print("done", ok)


if __name__ == "__main__":
    main()
