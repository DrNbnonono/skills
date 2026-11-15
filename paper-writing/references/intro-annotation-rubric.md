# Introduction annotation — instructions

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
