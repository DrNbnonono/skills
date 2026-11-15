#!/usr/bin/env python
"""Aggregate the introduction annotations.

Validates every batch, drops suspicious extracts (whole-paper dumps), then reports presence,
normalised start position, order, composition, and -- importantly -- per-batch variance, because
annotators applied the rubric with different strictness.

Usage: python aggregate_annotations.py
"""
from __future__ import annotations

import glob
import json
import os
import statistics
from collections import Counter

DIR = r"E:\php2shell\writing\intro_annot"
MOVES = ["problem_source", "worth_answering", "how_answered", "evidence_boundary", "what_changed"]


def load() -> list[dict]:
    rows = []
    for f in sorted(glob.glob(os.path.join(DIR, "batch_*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            n = r["n_paras"]
            for m in MOVES:
                v = r["links"].get(m)
                if v is not None:
                    assert isinstance(v, list) and len(v) == 2, (f, r["id"], m, v)
                    assert 1 <= v[0] <= v[1] <= n, (f, r["id"], m, v, n)
            r["src"] = os.path.basename(f)
            rows.append(r)
    return rows


def main() -> None:
    rows_all = load()
    suspicious = [r for r in rows_all if r["n_paras"] > 40]
    rows = [r for r in rows_all if r["n_paras"] <= 40]
    print(f"loaded {len(rows_all)} annotations; excluded {len(suspicious)} suspicious whole-paper extracts")
    for r in suspicious:
        print(f"  - {r['id']} ({r['n_paras']} paragraphs)")
    n = len(rows)
    ids = [r["id"] for r in rows]
    print(f"papers analysed {n}  unique ids {len(set(ids))}  batches {len(set(r['src'] for r in rows))}")
    if len(ids) != len(set(ids)):
        print("  WARNING: duplicate ids")

    print("\n== presence ==")
    for m in MOVES:
        c = sum(1 for r in rows if r["links"].get(m))
        print(f"  {m:18} {c:3}/{n}  ({100*c/n:.0f}%)")

    print("\n== where each move starts (normalised 0-1 within the intro) ==")
    for m in MOVES:
        rel = [(r["links"][m][0] - 1) / max(r["n_paras"] - 1, 1) for r in rows if r["links"].get(m)]
        if rel:
            print(f"  {m:18} median {statistics.median(rel):.2f}  "
                  f"p10 {sorted(rel)[int(len(rel)*0.1)]:.2f}  p90 {sorted(rel)[int(len(rel)*0.9)]:.2f}")

    print("\n== order ==")
    for a, b in [("problem_source", "worth_answering"), ("problem_source", "how_answered"),
                 ("how_answered", "evidence_boundary"), ("evidence_boundary", "what_changed")]:
        both = [r for r in rows if r["links"].get(a) and r["links"].get(b)]
        ok = sum(1 for r in both if r["links"][a][0] <= r["links"][b][0])
        if both:
            print(f"  {a} before {b}: {ok}/{len(both)} ({100*ok/len(both):.0f}%)")

    print("\n== composition ==")
    k = Counter(sum(1 for m in MOVES if r["links"].get(m)) for r in rows)
    for moves, c in sorted(k.items()):
        print(f"  moves present = {moves}: {c} papers ({100*c/n:.0f}%)")
    print("  mean moves per intro:", round(statistics.mean(sum(1 for m in MOVES if r["links"].get(m)) for r in rows), 2))

    print("\n== opening ==")
    for t, c in Counter(r.get("opening_type", "?") for r in rows).most_common():
        print(f"  {t:12} {c} ({100*c/n:.0f}%)")
    rq = sum(1 for r in rows if r.get("explicit_rq"))
    print(f"  explicit RQ: {rq}/{n} ({100*rq/n:.0f}%)")

    print("\n== per batch (annotator variance) ==")
    print(f"  {'batch':10}{'n':>3}" + "".join(f"{m[:6]:>9}" for m in MOVES))
    for b in sorted(set(r["src"] for r in rows)):
        sub = [r for r in rows if r["src"] == b]
        line = f"  {b:10}{len(sub):>3}"
        for m in MOVES:
            pct = 100 * sum(1 for r in sub if r["links"].get(m)) // len(sub)
            line += f"{pct:>8}%"
        print(line)

    json.dump({"rows": rows, "excluded": [r["id"] for r in suspicious]},
              open(os.path.join(DIR, "aggregate.json"), "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
