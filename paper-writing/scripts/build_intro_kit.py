#!/usr/bin/env python
"""Build the introduction annotation kit: 100 intros, 5 batches, instructions + schema.

Outputs under writing/intro_annot/:
  instructions.md      the annotation rubric
  schema.json          the required output shape
  batch_<n>/<id>.txt   one paper per file, paragraphs prefixed P1..Pn
  batch_<n>.index.csv  id, venue, paragraphs
"""
from __future__ import annotations

import csv
import json
import os
import re

CORPUS = r"E:\php2shell\writing\corpus_v24.jsonl"
OUT = r"E:\php2shell\writing\intro_annot"
INTRO = re.compile(r"\bintroduction\b", re.I)
N = 100
PER = 20

INSTRUCTIONS = """# Introduction annotation — instructions

You are annotating how the introduction of a top-tier security paper builds its argument.
For each paper you get a numbered list of paragraphs (`P1`, `P2`, ...). Do not rewrite anything;
record **where** each of five moves happens, or `null` when it is absent.

## The five moves

1. **problem_source** — the paragraph(s) that derive *this paper's* question: what the field needs
   to decide, what existing work established, where it falls short, then the narrowing to this
   object. A paragraph that only says a field is important is NOT this move.
2. **worth_answering** — the paragraph(s) that say which judgement or decision is blocked while the
   question is open (importance). "Few studies exist" is NOT this move.
3. **how_answered** — the paragraph(s) describing what the paper does: method, data, approach,
   named by what it establishes. Contribution lists belong here if they state what was done.
4. **evidence_boundary** — the paragraph(s) stating what the evidence covers and what it does not:
   scope, conditions, datasets, threat model, explicit non-claims.
5. **what_changed** — the paragraph(s) stating the change in knowledge: what is now known that was
   not, and under which conditions. Usually the last paragraph(s) before the contributions or the
   transition to the body.

Each move may span several paragraphs (`start_para`..`end_para`), may be absent (`null`), or may be
interleaved. Do not force all five to exist; the point of the annotation is to see which are missing.

## Extra fields

- `opening_type`: one of `boilerplate` ("in recent years", "with the rapid development"),
  `claim` (a specific assertion about the world), `question`, `anecdote` (a scenario or incident),
  `gap` (starts from what is missing), `other`.
- `explicit_rq`: true if a sentence states the research question explicitly ("we ask whether ...").

## Output

One JSON object per line, in `batch_<n>.jsonl`, exactly this shape:

{"id": "<arxiv id>", "n_paras": <int>, "opening_type": "<type>", "explicit_rq": <bool>,
 "links": {"problem_source": [start, end] or null,
           "worth_answering": [start, end] or null,
           "how_answered": [start, end] or null,
           "evidence_boundary": [start, end] or null,
           "what_changed": [start, end] or null},
 "notes": "<short, only if a judgement was hard>"}

Rules:
- Paragraph numbers are 1-based and refer to the `P` numbers in the file.
- If a move appears twice (e.g. boundary in the intro and again at the end), record the **main**
  occurrence and mention the second in `notes`.
- Never invent a move to make the paper look complete. `null` is a finding.
- Annotate every file in your batch; a batch with a missing line is not accepted.
"""

SCHEMA = {
    "id": "string",
    "n_paras": "int",
    "opening_type": "boilerplate|claim|question|anecdote|gap|other",
    "explicit_rq": "bool",
    "links": {
        "problem_source": "[start,end] | null",
        "worth_answering": "[start,end] | null",
        "how_answered": "[start,end] | null",
        "evidence_boundary": "[start,end] | null",
        "what_changed": "[start,end] | null",
    },
    "notes": "string",
}


def main() -> None:
    rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()][:N]
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "instructions.md"), "w", encoding="utf-8").write(INSTRUCTIONS)
    json.dump(SCHEMA, open(os.path.join(OUT, "schema.json"), "w", encoding="utf-8"), indent=1)

    per = (len(rows) + PER - 1) // PER
    for b in range(per):
        batch = rows[b * PER:(b + 1) * PER]
        d = os.path.join(OUT, f"batch_{b+1}")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(OUT, f"batch_{b+1}.index.csv"), "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh)
            w.writerow(["arxiv_id", "venue", "paragraphs", "file"])
            for r in batch:
                secs = r["sections"]
                intro = next((s for s in secs if INTRO.search(s["title"])), secs[0] if secs else None)
                if not intro:
                    continue
                paras = [p for p in intro["paras"] if len(p.split()) >= 12]
                if not paras:
                    continue
                lines = [f"# {r['id']}  (venue: {r.get('venue','?')})\n"]
                for i, p in enumerate(paras, 1):
                    lines.append(f"P{i}: {p}\n")
                fn = os.path.join(d, f"{r['id']}.txt")
                open(fn, "w", encoding="utf-8").write("\n".join(lines))
                w.writerow([r["id"], r.get("venue", "?"), len(paras), os.path.basename(fn)])
        print(f"batch {b+1}: {len(batch)} papers -> {d}")


if __name__ == "__main__":
    main()

