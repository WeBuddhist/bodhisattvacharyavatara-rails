#!/usr/bin/env python3
"""Statistical safety net: flag high-scoring English keywords that no extracted term covers.

  ../../.venv-python recall_check.py <run-dir> [--top-tfidf 200] [--top-yake 200]

For each baseline translation (dm, gm) it ranks words with the vault's TF-IDF
(keyword-extract/scripts/generate_en_translation_idf.py) and phrases with YAKE
(keyword-extract/scripts/keywords.py), then, per segment, lists the top-ranked
ones that occur in the segment but are not part of any extracted term's
rendering in that translation. Writes <run-dir>/recall-flags.json; the Gemini
review uses the flags as hints for missed terms. Costs no model tokens.
"""
import argparse
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "4-SYSTEM/Skills/keyword-extract/scripts"))
import generate_en_translation_idf as g  # noqa: E402
from keywords import KeywordExtractor  # noqa: E402


def ranked_words(texts, top):
    counts = {}
    for t in texts:
        for w in g.tokenize(t):
            if w not in g.STOPWORDS and len(w) > 2:
                counts[w] = counts.get(w, 0) + 1
    return [r["word"] for r in g.build_rows(counts)[:top]]


def ranked_phrases(texts, top):
    ex = KeywordExtractor(score_threshold=0.3)
    kws = ex.extract("\n".join(texts))
    out = []
    for k in kws:
        p = k.raw.lower().strip()
        if p and p not in out:
            out.append(p)
    return out[:top]


def present(cand, text):
    return re.search(r"(?<![\w-])" + re.escape(cand) + r"(?![\w-])", text, re.I) is not None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("run_dir")
    p.add_argument("--top-tfidf", type=int, default=200)
    p.add_argument("--top-yake", type=int, default=200)
    a = p.parse_args()
    run = pathlib.Path(a.run_dir)
    segs = json.loads((run / "segments.json").read_text(encoding="utf-8"))
    occ = json.loads((run / "occurrences.json").read_text(encoding="utf-8"))
    flags, n = {}, {"dm": 0, "gm": 0}
    for eng in ("dm", "gm"):
        texts = [s[eng] for s in segs]
        cands = ranked_words(texts, a.top_tfidf) + ranked_phrases(texts, a.top_yake)
        for s in segs:
            rend = [o[eng].lower() for o in occ if o["id"] == s["id"] and o.get(eng)]
            miss = []
            for c in cands:
                if c in miss or not present(c, s[eng]):
                    continue
                if any(c in r or r in c for r in rend):
                    continue
                miss.append(c)
            if miss:
                flags.setdefault(s["id"], {})[eng] = miss
                n[eng] += len(miss)
    (run / "recall-flags.json").write_text(json.dumps(flags, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"segments flagged={len(flags)} flags dm={n['dm']} gm={n['gm']}")


if __name__ == "__main__":
    main()
