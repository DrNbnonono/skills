#!/usr/bin/env python3
"""Collect and analyse top-4 security abstracts, to re-derive references/abstract.md.

Usage
-----
    python abstract_study.py --collect --out abstracts.jsonl
    python abstract_study.py --analyse abstracts.jsonl
    python abstract_study.py --analyse abstracts.jsonl --show 5

Collection
----------
* IEEE S&P, ACM CCS, NDSS: OpenAlex (`primary_location.source.id` for each conference),
  publication years 2022-2025, abstract reconstructed from `abstract_inverted_index`.
* USENIX Security: usenix.org technical-sessions pages (2024, 2025), abstract scraped from the
  paper-description field.

Only metadata and abstracts are fetched; nothing is redistributed. OpenAlex reconstruction
occasionally glues words and truncates a minority of abstracts, so the numbers are an order of
magnitude, not a pristine measurement. Re-measure before quoting them in a few years.

Analysis prints the tables used in references/abstract.md: length, person, move coverage, move
positions, number density, sentence-count distribution, openings and closings.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import statistics as st
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

OPENALEX_SOURCES = {
    "IEEE S&P": "S4210233669",
    "ACM CCS": "S4393917527",
    "NDSS": "S4306420590",
}
USENIX_YEARS = {2025: "usenixsecurity25", 2024: "usenixsecurity24"}
UA = {"User-Agent": "abstract-study/1.0 (paper-prose-polish skill)"}

ABBREV = re.compile(
    r"\b(e\.g|i\.e|et al|Fig|Figs|vs|approx|cf|resp|No|Sec|Tab|Eq|w\.r\.t|U\.S|U\.K)\."
)
WE_START = re.compile(r"^(we|our|here we|in this paper|this paper|this work)\b", re.I)
NUM = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?:%|x|k|M|B)?\b")
MOVES = {
    "problem": r"\b(attack|attackers?|adversar\w+|threat|vulnerab\w*|malicious|exploit\w*|"
               r"privacy|breach\w*|compromis\w+|security|defen[cs]e|protect\w*)\b",
    "gap": r"\b(however|yet|but|remains?|little is known|no (existing|prior|previous|systematic|"
           r"effective|practical)|unclear|has not been|have not been|lack(s|ing)?|under-?studied|"
           r"previous (work|studies|approaches)|prior (work|studies|approaches)|overlook\w*|"
           r"fail(s|ed)? to)\b",
    "approach": r"\b(we (present|propose|introduce|design|build|develop|implement|measure|conduct|"
                r"perform|collect|analy[sz]e|study|evaluate|examine|characteri[sz]e|test|apply|use|"
                r"run|report|discuss|show|demonstrate|find|provide|make|release|deploy|train|"
                r"formaliz|model|construct|create|devise|leverage|extend|combine|compare)|"
                r"in this (paper|work|article)|this paper (presents|proposes|describes|studies|"
                r"reports|introduces))\b",
    "results": r"\b(we (find|show|demonstrate|observe|discover|measure|report|reveal)|"
               r"our (results|findings?|analysis|evaluation|measurements?|study|experiments?)|"
               r"results (show|demonstrate|indicate|reveal))\b",
    "implication": r"\b(we (argue|conclude|recommend|call|suggest)|implications?|suggests?|"
                   r"these results|our findings|to (address|mitigate|fix|protect|defend)|"
                   r"would (help|allow|make|require)|can (help|enable)|points? to|underscores?|"
                   r"highlight\w*|motivat\w*)\b",
    "artifact": r"\b(available at|open[- ]sourc\w*|artifact|released at|github\.com|"
                r"publicly available|we release)\b",
}


# ---------------------------------------------------------------------------
# Collection
# ---------------------------------------------------------------------------
def fetch(url: str, timeout: int = 60) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def reconstruct(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def collect_openalex(venue: str, sid: str, per_venue: int) -> list[dict]:
    out: list[dict] = []
    cursor = "*"
    while len(out) < per_venue:
        url = (
            f"https://api.openalex.org/works?filter=primary_location.source.id:{sid},"
            f"publication_year:2022-2025,has_abstract:true&per-page=100"
            f"&cursor={urllib.parse.quote(cursor)}"
            f"&select=id,doi,title,publication_year,abstract_inverted_index"
        )
        data = json.loads(fetch(url))
        rows = data.get("results", [])
        if not rows:
            break
        for w in rows:
            abstract = reconstruct(w.get("abstract_inverted_index"))
            if len(abstract.split()) < 60:
                continue
            out.append({"venue": venue, "year": w.get("publication_year"),
                        "title": (w.get("title") or "").strip(), "doi": w.get("doi"),
                        "abstract": abstract})
            if len(out) >= per_venue:
                break
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor:
            break
        time.sleep(0.4)
    return out


def clean_fragment(fragment: str) -> str:
    fragment = re.sub(r"<script.*?</script>", " ", fragment, flags=re.S | re.I)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment)
    return re.sub(r"\s+", " ", fragment).strip()


def collect_usenix(per_year: int) -> list[dict]:
    out: list[dict] = []
    for year, slug in USENIX_YEARS.items():
        try:
            page = fetch(f"https://www.usenix.org/conference/{slug}/technical-sessions")
        except Exception as e:  # pragma: no cover - network
            print(f"  {year}: program page failed: {e}", file=sys.stderr)
            continue
        links: list[str] = []
        for m in re.finditer(r'href="(/conference/%s/presentation/[a-z0-9\-]+)"' % slug, page):
            if m.group(1) not in links:
                links.append(m.group(1))
        got = 0
        for link in links:
            if got >= per_year:
                break
            try:
                p = fetch("https://www.usenix.org" + link)
            except Exception:
                continue
            m = re.search(
                r'field-name-field-paper-description.*?<div class="field-item odd">(.*?)</div>',
                p, re.S)
            if not m:
                continue
            abstract = clean_fragment(m.group(1))
            if not 80 <= len(abstract.split()) <= 400:
                continue
            t = re.search(r"<title>(.*?)</title>", p, re.S)
            title = re.sub(r"\s*\|\s*USENIX$", "", clean_fragment(t.group(1))) if t else ""
            out.append({"venue": "USENIX Security", "year": year, "title": title,
                        "doi": None, "abstract": abstract})
            got += 1
            time.sleep(0.25)
        print(f"  USENIX {year}: {got} abstracts", file=sys.stderr)
    return out


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def normalise(text: str) -> str:
    t = text.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    t = re.sub(r"([.!?])([A-Z\"'(])", r"\1 \2", t)
    return re.sub(r"\s+", " ", t).strip()


def split_sentences(text: str) -> list[str]:
    t = ABBREV.sub(lambda m: m.group(0).replace(".", "<D>"), text)
    t = re.sub(r"(\d)\.(\d)", r"\1<D>\2", t)
    out = [p.replace("<D>", ".").strip() for p in re.split(r"(?<=[.!?])\s+", t)]
    return [p for p in out if len(p.split()) >= 3]


def analyse(rows: list[dict]) -> None:
    venues = sorted({r["venue"] for r in rows})
    per: dict[str, dict] = {}
    for r in rows:
        t = normalise(r["abstract"])
        ss = split_sentences(t)
        if len(ss) < 3:
            continue
        words = len(t.split())
        lens = [len(s.split()) for s in ss]
        v = per.setdefault(r["venue"], defaultdict(list))
        v["words"].append(words)
        v["sents"].append(len(ss))
        v["mean"].append(st.mean(lens))
        v["we"].append(bool(re.search(r"\b(we|our)\b", t, re.I)))
        v["we_start"].append(sum(1 for s in ss if WE_START.match(s)))
        v["first_we"].append(bool(WE_START.match(ss[0])))
        v["ip"].append(bool(re.search(
            r"\bin this (paper|work|article),? we\b", t, re.I)))
        v["nums"].append(len(NUM.findall(t)))
        v["dens"].append(100 * len(NUM.findall(t)) / words)
        for k, rx in MOVES.items():
            v["mv_" + k].append(bool(re.search(rx, t, re.I)))
        v["scount"].append(len(ss))
        v["last"].append(ss[-1])
        v["first"].append(ss[0])

    def pct(vals: list[bool]) -> str:
        return f"{100 * sum(vals) / len(vals):.0f}"

    print(f"\ncollected {len(rows)} abstracts, {len(venues)} venues\n")
    hdr = (f"{'venue':16}{'n':>4}{'words':>7}{'med':>6}{'sents':>6}{'mean':>6}"
           f"{'we%':>5}{'We-start%':>10}{'in-paper%':>10}{'>=1num%':>9}")
    print(hdr)
    print("-" * len(hdr))
    for venue in venues:
        v = per[venue]
        print(f"{venue:16}{len(v['words']):>4}{st.mean(v['words']):>7.0f}"
              f"{st.median(v['words']):>6.0f}{st.mean(v['sents']):>6.1f}"
              f"{st.mean(v['mean']):>6.1f}{pct(v['we']):>5}"
              f"{100 * st.mean(v['we_start']) / st.mean(v['sents']):>9.0f}"
              f"{pct(v['ip']):>10}{pct([n >= 1 for n in v['nums']]):>9}")

    print("\nmove coverage % (keyword heuristic)")
    print(f"{'venue':16}" + "".join(f"{k:>12}" for k in MOVES))
    for venue in venues:
        v = per[venue]
        print(f"{venue:16}" + "".join(f"{pct(v['mv_' + k]):>12}" for k in MOVES))

    allw = [w for v in per.values() for w in v["words"]]
    allm = [m for v in per.values() for m in v["mean"]]
    print(f"\nall: words p10/p50/p90 = "
          f"{[sorted(allw)[int(len(allw) * p)] for p in (0.1, 0.5, 0.9)]}; "
          f"mean sentence p10/p50/p90 = "
          f"{[round(sorted(allm)[int(len(allm) * p)], 1) for p in (0.1, 0.5, 0.9)]}")

    sc = Counter(s for v in per.values() for s in v["scount"])
    print("sentences per abstract:", dict(sorted(sc.items())))
    first_word = Counter(f.split()[0] for v in per.values() for f in v["first"])
    print("first word:", first_word.most_common(10))
    last_open = Counter(" ".join(l.split()[:3]) for v in per.values() for l in v["last"])
    print("last sentence opening:", last_open.most_common(8))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--collect", action="store_true", help="fetch the corpus into --out")
    ap.add_argument("--out", default="abstracts.jsonl")
    ap.add_argument("--per-venue", type=int, default=40)
    ap.add_argument("--analyse", default=None, metavar="JSONL")
    ap.add_argument("--show", type=int, default=0, help="print N sampled abstracts")
    args = ap.parse_args()

    if args.collect:
        rows: list[dict] = []
        for venue, sid in OPENALEX_SOURCES.items():
            got = collect_openalex(venue, sid, args.per_venue)
            print(f"  {venue}: {len(got)} abstracts", file=sys.stderr)
            rows += got
        rows += collect_usenix(args.per_venue // 2)
        with open(args.out, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"wrote {len(rows)} abstracts to {args.out}", file=sys.stderr)
        return

    if args.analyse:
        rows = [json.loads(l) for l in open(args.analyse, encoding="utf-8")]
        analyse(rows)
        if args.show:
            import random
            random.seed(7)
            for r in random.sample(rows, min(args.show, len(rows))):
                print(f"\n## {r['venue']} {r['year']} - {r['title']}\n\n"
                      f"{normalise(r['abstract'])}")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
