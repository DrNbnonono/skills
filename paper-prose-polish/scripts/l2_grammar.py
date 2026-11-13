#!/usr/bin/env python
"""L2 (Chinese-first-language) grammar patterns, measured with POS tagging.

Four patterns that are frequent in L2 academic English and that a regex alone cannot see:

  bare_singular   a singular count noun with no determiner  ("we test on version" )
  a_an            "a" before a vowel sound, "an" before a consonant sound
  this_these      "this" + plural noun, "these" + singular noun, "a" + plural noun
  tense_mix       a paragraph that switches between past and present reporting

Rates are per 1,000 nouns (bare_singular), per 1,000 words (a_an, this_these), and as a
share of paragraphs (tense_mix), so papers of different lengths compare.

Usage:
    python l2_grammar.py --corpus N   # N papers from corpus_v24.jsonl
    python l2_grammar.py --draft      # the paper under revision
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import statistics
import sys

import spacy

import re as _re

def clean_tex(tex: str) -> str:
    tex = _re.sub(r"(?<!\\)%.*", "", tex)
    tex = _re.sub(r"\\begin\{(table|figure)\}.*?\\end\{\1\}", " ", tex, flags=_re.S)
    tex = _re.sub(r"\\input\{[^}]*\}", " ", tex)
    tex = _re.sub(r"\\label\{[^{}]*\}", " ", tex)
    tex = _re.sub(r"\\c?ref\{[^{}]*\}", " Section ", tex)
    tex = _re.sub(r"\\cite[a-z]*\{[^{}]*\}", " ", tex)
    tex = _re.sub(r"\$[^$]*\$", " MATH ", tex)
    prev = None
    while prev != tex:
        prev = tex
        tex = _re.sub(r"\\(?:texttt|emph|textbf|textit|textsc|sysname|todo|text)\*?\{([^{}]*)\}", r"\1", tex)
    tex = _re.sub(r"\\[a-zA-Z]+\*?", " ", tex)
    tex = _re.sub(r"[{}~]", " ", tex)
    return _re.sub(r"\s+", " ", tex).strip()

MASS_NOUNS = set("""research work evidence data information software hardware malware code traffic
behavior behaviour access security privacy performance accuracy robustness efficiency scalability
functionality availability integrity confidentiality authentication authorization detection
prevention mitigation analysis evaluation validation verification measurement measurement
sensitivity latency throughput bandwidth memory storage computation communication interaction
training inference learning supervision annotation labeling labelling deployment maintenance
governance policy compliance regulation legislation enforcement disclosure coordination
time space energy cost value risk trust usability complexity uncertainty randomness progress
knowledge understanding awareness adoption usage utilization utilization practice experience
attention interest concern criticism debate discussion motivation context structure semantics
syntax grammar vocabulary terminology notation representation abstraction implementation""".split())

LABEL_NOUNS = set("""accuracy precision recall robustness efficiency scalability performance
security privacy usability correctness completeness generality reliability fairness transparency
interpretability explainability maintainability portability adaptability flexibility
effectiveness quality speed cost overhead coverage""".split())


def load_nlp():
    return spacy.load("en_core_web_sm", disable=["ner", "lemmatizer"])


def bare_singular(doc) -> list[str]:
    out = []
    for t in doc:
        if t.pos_ != "NOUN" or t.tag_ != "NN":
            continue
        low = t.text.lower()
        if low in MASS_NOUNS or low in LABEL_NOUNS:
            continue
        if t.ent_type_:
            continue
        # a determiner, possessive, numeral, or compound premodifier counts as licensed
        if any(c.dep_ in ("det", "poss", "nummod", "compound", "amod", "nmod:poss") for c in t.children):
            continue
        if t.i == 0:
            continue
        prev = doc[t.i - 1]
        if prev.pos_ in ("ADJ", "NUM", "DET", "PRON", "PROPN"):
            continue
        if prev.text.lower() in ("of", "the", "a", "an", "this", "these", "those", "its", "their", "our", "your"):
            continue
        out.append(str(t))
    return out


def a_an(doc) -> list[str]:
    out = []
    for i, t in enumerate(doc[:-1]):
        w = t.text.lower()
        nxt = doc[i + 1]
        if w == "a" and nxt.text[:1].lower() in "aeiou":
            if re.match(r"(one|once|uni|use|usu|uti|eu|ubiq)", nxt.text, re.I):
                continue
            out.append(f"a {nxt.text}")
        elif w == "an" and nxt.text[:1].lower() not in "aeiou" and nxt.text[:1].isalpha():
            if re.match(r"(hour|honest|honor|honour|heir|MRI|MBA|FBI|NSA|SVM|S&P|SMS|XSS|RFID|HTML|HTTP|API|RDF|XML|LSTM|GAN|NLP)", nxt.text, re.I):
                continue
            out.append(f"an {nxt.text}")
    return out


def this_these(doc) -> list[str]:
    out = []
    for i, t in enumerate(doc[:-1]):
        w = t.text.lower()
        nxt = doc[i + 1]
        if nxt.pos_ != "NOUN":
            continue
        plural = nxt.tag_ == "NNS" or nxt.tag_ == "NNS"
        if w == "this" and plural:
            out.append(f"this {nxt.text}")
        elif w == "these" and nxt.tag_ == "NN":
            out.append(f"these {nxt.text}")
        elif w == "a" and plural and nxt.tag_ == "NNS" and not nxt.text.lower().endswith("ics"):
            out.append(f"a {nxt.text}")
    return out


def tense_mix(paras: list[str], nlp) -> tuple[int, int]:
    mixed = 0
    for p in paras:
        doc = nlp(p)
        past = sum(1 for t in doc if t.tag_ == "VBD")
        pres = sum(1 for t in doc if t.tag_ in ("VBP", "VBZ"))
        if past >= 2 and pres >= 2:
            mixed += 1
    return mixed, len(paras)


def score(text: str, nlp) -> dict:
    doc = nlp(text)
    nouns = sum(1 for t in doc if t.pos_ == "NOUN")
    words = sum(1 for t in doc if t.is_alpha)
    bs = bare_singular(doc)
    aa = a_an(doc)
    tt = this_these(doc)
    return {
        "words": words,
        "nouns": nouns,
        "bare": len(bs),
        "bare_per_1k_nouns": round(1000 * len(bs) / max(nouns, 1), 1),
        "a_an": len(aa),
        "a_an_per_1k": round(1000 * len(aa) / max(words, 1), 1),
        "this_these": len(tt),
        "this_these_per_1k": round(1000 * len(tt) / max(words, 1), 1),
        "examples": {"bare": bs[:40], "a_an": aa[:40], "this_these": tt[:40]},
    }


def corpus_texts(n: int) -> list[str]:
    rows = [json.loads(l) for l in open(r"E:\php2shell\writing\corpus_v24.jsonl", encoding="utf-8") if l.strip()]
    random.seed(7)
    sample = random.sample(rows, min(n, len(rows)))
    return [" ".join(p for s in r["sections"] for p in s["paras"]) for r in sample]


def corpus_paras(n: int) -> list[str]:
    rows = [json.loads(l) for l in open(r"E:\php2shell\writing\corpus_v24.jsonl", encoding="utf-8") if l.strip()]
    random.seed(7)
    sample = random.sample(rows, min(n, len(rows)))
    return [p for r in sample for s in r["sections"] for p in s["paras"]]


def draft_text() -> str:
    base = r"E:\php2shell\php2shell-paper\sections"
    return " ".join(clean_tex(open(os.path.join(base, f), encoding="utf-8").read())
                    for f in sorted(os.listdir(base)) if f.endswith(".tex"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=int, default=25)
    ap.add_argument("--draft", action="store_true")
    args = ap.parse_args()
    nlp = load_nlp()

    if args.corpus:
        texts = corpus_texts(args.corpus)
        res = [score(t, nlp) for t in texts]
        for key in ("bare_per_1k_nouns", "a_an_per_1k", "this_these_per_1k"):
            vals = [r[key] for r in res]
            print(f"{key:22} mean {statistics.mean(vals):6.2f}  median {statistics.median(vals):6.2f}  "
                  f"p90 {sorted(vals)[int(len(vals)*0.9)-1]:6.2f}  max {max(vals):6.2f}")
        paras = corpus_paras(args.corpus)
        m, n = tense_mix(paras, nlp)
        print(f"{'tense_mix_paragraphs':22} {m}/{n} = {100*m/max(n,1):.1f}%")
        allx = {"bare": [], "a_an": [], "this_these": []}
        for r in res:
            for k in allx:
                allx[k] += r["examples"][k]
        for k, v in allx.items():
            print(f"\n--- corpus {k} examples ---")
            for e in v[:12]:
                print("   *", e)

    if args.draft:
        t = draft_text()
        r = score(t, nlp)
        print(f"\nDRAFT words {r['words']} nouns {r['nouns']}  bare/1kN {r['bare_per_1k_nouns']}  "
              f"a-an/1k {r['a_an_per_1k']}  this-these/1k {r['this_these_per_1k']}")
        for k in ("bare", "a_an", "this_these"):
            print(f"\n--- draft {k} ---")
            for e in r["examples"][k][:25]:
                print("   *", e)


if __name__ == "__main__":
    main()

