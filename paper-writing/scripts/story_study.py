#!/usr/bin/env python
"""Story-level norms: abstracts, and how display items split between body and appendix.

Part A (fast, arXiv API): abstract length, sentence count, whether it carries a number,
whether it uses "we".
Part B (ar5iv mirror): display items per paper, and how many sit in the appendix.

Usage: python story_study.py [n_appendix_papers]
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
import urllib.parse
import urllib.request

from lxml import html as LH

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
CORPUS = r"E:\php2shell\writing\corpus_v23.jsonl"


def fetch(url: str, timeout: int = 40) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout, context=CTX).read()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- abstracts
def abstracts(ids: list[str]) -> list[dict]:
    out = []
    for i in range(0, len(ids), 40):
        batch = [x.split("v")[0] for x in ids[i:i + 40]]
        q = "http://export.arxiv.org/api/query?id_list=" + ",".join(batch) + "&max_results=40"
        try:
            raw = fetch(q, 40).decode("utf-8", "ignore")
        except Exception as e:
            print("abstract batch failed", repr(e)[:60])
            continue
        for m in re.finditer(r"<entry>.*?</entry>", raw, re.S):
            e = m.group(0)
            summ = re.search(r"<summary>(.*?)</summary>", e, re.S)
            aid = re.search(r"<id>http://arxiv.org/abs/([^<]+)</id>", e)
            if not (summ and aid):
                continue
            t = norm(summ.group(1)).replace("\n", " ")
            sents = [s for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]
            out.append({
                "id": aid.group(1),
                "words": len(t.split()),
                "sentences": len(sents),
                "has_number": bool(re.search(r"\d", t)),
                "has_percent": bool(re.search(r"\d\s*%|\d\s*percent|%", t)),
                "uses_we": bool(re.search(r"\bwe\b", t, re.I)),
                "opens_with_result": bool(re.search(r"\b(we (show|find|present|demonstrate|measure))\b", t[:200], re.I)),
            })
        time.sleep(3)
    return out


# ---------------------------------------------------------------- appendix
APPENDIX_RE = re.compile(r"\bappendix\b|\bappendix\b", re.I)


def float_split(raw: str) -> dict | None:
    doc = LH.fromstring(raw)
    for bad in doc.xpath("//script|//style|//nav|//footer"):
        bad.getparent().remove(bad)
    total = body = app = 0
    for sec in doc.xpath("//section"):
        title = norm(" ".join(sec.xpath("./h2//text()")))
        figs = [f for f in sec.xpath(".//figure") if "ltx_figure" in (f.get("class") or "") or "ltx_table" in (f.get("class") or "")]
        # count only direct-ish floats: skip figures nested in another counted figure
        own = []
        for f in figs:
            parent = f.getparent()
            nested = False
            while parent is not None:
                if isinstance(parent.tag, str) and parent.tag == "figure":
                    nested = True
                    break
                parent = parent.getparent()
            if not nested:
                own.append(f)
        if not own:
            continue
        total += len(own)
        if APPENDIX_RE.search(title):
            app += len(own)
        else:
            body += len(own)
    if total == 0:
        return None
    return {"total": total, "body": body, "appendix": app}


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()]
    ids = [r["id"] for r in rows]

    print("== abstracts ==")
    abs_ = abstracts(ids)
    if abs_:
        w = [a["words"] for a in abs_]
        s = [a["sentences"] for a in abs_]
        print(f"n {len(abs_)}  words: median {statistics.median(w):.0f}  mean {statistics.mean(w):.1f}  "
              f"p10 {sorted(w)[int(len(w)*0.1)]}  p90 {sorted(w)[int(len(w)*0.9)]}")
        print(f"sentences: median {statistics.median(s):.0f}  mean {statistics.mean(s):.1f}")
        print(f"has a number {100*sum(a['has_number'] for a in abs_)/len(abs_):.1f}%   "
              f"has a percent {100*sum(a['has_percent'] for a in abs_)/len(abs_):.1f}%   "
              f"uses 'we' {100*sum(a['uses_we'] for a in abs_)/len(abs_):.1f}%")
    json.dump(abs_, open(r"E:\php2shell\writing\abstract_stats.json", "w", encoding="utf-8"), indent=1)

    print("\n== display items: body vs appendix ==")
    random.seed(5)
    sample = random.sample(rows, min(n * 2, len(rows)))
    got, res = 0, []
    for r in sample:
        if got >= n:
            break
        base = r["id"].split("v")[0]
        for url in (f"https://ar5iv.labs.arxiv.org/html/{base}", f"https://arxiv.org/html/{r['id']}"):
            try:
                sp = float_split(fetch(url, 45).decode("utf-8", "ignore"))
                if not sp or sp["total"] < 3:
                    raise ValueError("few floats")
                sp["id"] = r["id"]
                res.append(sp)
                got += 1
                break
            except Exception as e:
                if url.startswith("https://arxiv"):
                    print("skip", r["id"], repr(e)[:40])
    if res:
        tot = sum(x["total"] for x in res)
        app = sum(x["appendix"] for x in res)
        print(f"papers {len(res)}  floats {tot}  in appendix {app} ({100*app/max(tot,1):.1f}%)")
        print(f"floats per paper: median {statistics.median([x['total'] for x in res]):.0f}")
        print(f"papers with any appendix float: {sum(1 for x in res if x['appendix'])}/{len(res)}")
        json.dump(res, open(r"E:\php2shell\writing\float_split.json", "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
