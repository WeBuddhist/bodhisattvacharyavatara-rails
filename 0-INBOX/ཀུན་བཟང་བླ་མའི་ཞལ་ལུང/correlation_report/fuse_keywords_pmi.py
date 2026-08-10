#!/usr/bin/env python3
"""Fuse TF-IDF and YAKE into one ranking, with a PMI gate on multi-word phrases.

Two independent problems:

1. Scale mismatch. TF-IDF is higher=better, YAKE lower=better, and neither
   scale is comparable to the other -> fuse on rank position (RRF).
2. Phrase quality. YAKE happily emits "great teacher" or "people die" —
   phrases that are frequent only because their parts are frequent. PMI asks
   whether the words co-occur more than chance predicts, so compositional
   filler drops out while genuine collocations ("bodh gaya", "trisong detsen",
   "guru yoga") survive.

PMI needs the raw phrase count, which no input file carries — the normalized
rows give count(word), not count(phrase) — so the source text is re-tokenized
here. Those rows are still used for two things the raw text can't supply: the
variant->lemma map (so "buddhas" counts as "buddha", matching how the terms
were lemmatized) and the authoritative content-token total.

    python fuse_keywords_pmi.py path/to/en.md
"""
import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
TFIDF_MD = HERE / "en-tfidf.md"
YAKE_JSON = HERE / "en-n-gram-keyword.json"
ROWS_JSON = HERE / "en-tfidf-normalized-rows.json"
OUT_MD = HERE / "en-keywords-fused-pmi.md"

K = 60           # RRF damping constant
W_TFIDF = 1.0
W_YAKE = 1.0

NPMI_MIN = 0.30  # phrases below this are compositional, not collocations
MIN_COUNT = 3    # PMI is unstable on hapax phrases; require a few sightings

ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*"
    r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$"
)
WORD = re.compile(r"[a-z]+(?:[-'][a-z]+)*")


# ---------------------------------------------------------------- inputs

def num(cell):
    cell = cell.strip().replace(",", "")
    if not cell or cell == "-":
        return None
    try:
        return float(cell)
    except ValueError:
        return None


def load_terms():
    terms = {}
    for line in TFIDF_MD.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        _, term, count, tfidf, idf, band, yake, variants, glossary = m.groups()
        terms[term] = {
            "term": term, "count": num(count), "tfidf": num(tfidf),
            "idf": num(idf), "band": band.strip(), "yake": num(yake),
            "variants": variants.strip(), "glossary": glossary.strip(),
            "words": term.count(" ") + 1,
        }
    return terms


def merge_yake(terms):
    for term, score in json.loads(YAKE_JSON.read_text(encoding="utf-8")).items():
        rec = terms.get(term)
        if rec is None:
            terms[term] = {
                "term": term, "count": None, "tfidf": None, "idf": None,
                "band": "-", "yake": score, "variants": "-", "glossary": "—",
                "words": term.count(" ") + 1,
            }
        elif rec["yake"] is None:
            rec["yake"] = score
    return terms


# ---------------------------------------------------------------- PMI

def load_lemmas():
    """surface form -> lemma, from the normalized rows' `variants` lists.

    The terms are lemmatized but the source text isn't, so a literal match
    would count "buddha" and miss "buddhas". The rows already record exactly
    which surface forms were folded into each lemma; reuse that mapping rather
    than re-guessing the lemmatizer's decisions.
    """
    if not ROWS_JSON.exists():
        return {}, {}
    rows = json.loads(ROWS_JSON.read_text(encoding="utf-8"))
    lemma = {v: r["word"] for r in rows for v in r["variants"]}
    return lemma, {r["word"]: r["count"] for r in rows}


def tokenize(path, lemma):
    """Lemmatized token stream, minus frontmatter and verse markers."""
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)   # YAML frontmatter
    text = re.sub(r"\^\d+(?:-\d+)?", " ", text)                 # ^1-2 verse markers
    return [lemma.get(w, w) for w in WORD.findall(text.lower())]


def check_counts(counts, expected):
    """How well our tokenization reproduces the recorded unigram counts.

    A low match rate means the tokenizer disagrees with the one that produced
    the rows, and every phrase count below it is suspect — so surface it rather
    than silently gating on bad numbers.
    """
    if not expected:
        return None
    hits = sum(1 for w, c in expected.items() if counts[1].get(w, 0) == c)
    return hits / len(expected)


def ngram_counts(tokens, max_n):
    """Counts for every n-gram length we need, in one pass per length."""
    counts = {1: Counter(tokens)}
    for n in range(2, max_n + 1):
        counts[n] = Counter(
            " ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)
        )
    return counts


def npmi(phrase, counts, total):
    """Normalized PMI over a phrase's words. None if the phrase never occurs.

    NPMI = PMI / -((n-1) * log2 p(phrase)), which pins the range to [-1, 1]:
      1  -> the words only ever appear together
      0  -> exactly what independence predicts
     <0  -> they avoid each other

    The (n-1) matters: an n-gram's maximum PMI is (n-1) * -log2 p(phrase),
    so normalizing by -log2 p alone would score trigrams on a scale twice as
    generous as bigrams, and the gate would filter by length, not collocation.
    """
    words = phrase.split()
    n = len(words)
    joint = counts[n].get(phrase, 0)
    if joint == 0:
        return None
    p_joint = joint / total   # same N as the unigrams, so NPMI stays <= 1
    p_indep = 1.0
    for w in words:
        c = counts[1].get(w, 0)
        if c == 0:
            return None
        p_indep *= c / total
    pmi = math.log2(p_joint / p_indep)
    return pmi / (-(n - 1) * math.log2(p_joint))


def apply_gate(terms, counts, total, npmi_min, min_count):
    """Score every phrase; mark the ones that fail as gated."""
    for rec in terms.values():
        if rec["words"] == 1:
            rec["npmi"] = None
            rec["phrase_count"] = rec["count"]
            rec["gated"] = False
            continue
        rec["phrase_count"] = counts[rec["words"]].get(rec["term"], 0)
        rec["npmi"] = npmi(rec["term"], counts, total)
        rec["gated"] = (
            rec["npmi"] is None
            or rec["npmi"] < npmi_min
            or rec["phrase_count"] < min_count
        )
    return terms


# ---------------------------------------------------------------- fusion

def rank_map(terms, key, reverse):
    scored = [t for t in terms if t[key] is not None]
    scored.sort(key=lambda t: t[key], reverse=reverse)
    return {t["term"]: i for i, t in enumerate(scored, 1)}


def fuse(kept):
    r_tfidf = rank_map(kept, "tfidf", reverse=True)
    r_yake = rank_map(kept, "yake", reverse=False)
    penalty = len(kept) + 1
    for rec in kept:
        rt = r_tfidf.get(rec["term"], penalty)
        ry = r_yake.get(rec["term"], penalty)
        rec["rank_tfidf"] = r_tfidf.get(rec["term"])
        rec["rank_yake"] = r_yake.get(rec["term"])
        rec["fused"] = W_TFIDF / (K + rt) + W_YAKE / (K + ry)
    return sorted(kept, key=lambda r: -r["fused"])


# ---------------------------------------------------------------- output

def fmt(v, spec=""):
    return "-" if v is None else format(v, spec)


def write(ranked, dropped, total, args):
    both = sum(1 for r in ranked if r["rank_tfidf"] and r["rank_yake"])
    multi = sum(1 for r in ranked if r["words"] > 1)
    out = [
        "---",
        "title: Fused Keyword Ranking (PMI-gated) — en",
        "method: NPMI gate on multi-word phrases, then Reciprocal Rank Fusion",
        f"npmi_min: {args.npmi_min}",
        f"min_count: {args.min_count}",
        f"rrf_k: {K}",
        f"corpus_tokens: {total}",
        f"terms: {len(ranked)}",
        "status: draft",
        "---",
        "",
        "# Fused Keyword Ranking (PMI-gated) — en",
        "",
        "Every multi-word candidate is first asked whether it is a real collocation:",
        "",
        "```",
        "NPMI(t) = log2( p(phrase) / prod p(word) ) / -((n-1) * log2 p(phrase))",
        f"keep if NPMI >= {args.npmi_min} and count >= {args.min_count}",
        "```",
        "",
        "Phrases that are only frequent because their parts are frequent score near 0",
        "and drop out. Survivors are then fused with the single words on rank position,",
        "since TF-IDF (higher=better) and YAKE (lower=better) are not comparable scales:",
        "",
        "```",
        f"fused(t) = {W_TFIDF} / ({K} + rank_tfidf(t)) + {W_YAKE} / ({K} + rank_yake(t))",
        "```",
        "",
        "| Coverage | Terms |",
        "|----------|-------|",
        f"| Kept | {len(ranked):,} |",
        f"| Gated out (phrases) | {len(dropped):,} |",
        f"| In both lists | {both:,} |",
        f"| Multi-word phrases kept | {multi:,} |",
        "",
        "---",
        "",
        "| Rank | Term | W | Count | NPMI | TF-IDF | YAKE | R(tfidf) | R(yake) | Fused | Band | Glossary |",
        "|------|------|---|-------|------|--------|------|----------|---------|-------|------|----------|",
    ]
    for i, r in enumerate(ranked, 1):
        out.append(
            f"| {i} | **{r['term']}** | {r['words']} | {fmt(r['phrase_count'], '.0f')} | "
            f"{fmt(r['npmi'], '.3f')} | {fmt(r['tfidf'], ',.2f')} | {fmt(r['yake'], '.6f')} | "
            f"{fmt(r['rank_tfidf'], ',')} | {fmt(r['rank_yake'], ',')} | "
            f"{r['fused']:.6f} | {r['band']} | {r['glossary']} |"
        )

    out += ["", "---", "", "## Gated out",
            "", "Phrases whose words co-occur no more than chance predicts.", "",
            "| Term | Count | NPMI | YAKE |", "|------|-------|------|------|"]
    for r in sorted(dropped, key=lambda r: (r["npmi"] is None, -(r["npmi"] or 0))):
        out.append(
            f"| {r['term']} | {fmt(r['phrase_count'], '.0f')} | "
            f"{fmt(r['npmi'], '.3f')} | {fmt(r['yake'], '.6f')} |"
        )
    OUT_MD.write_text("\n".join(out) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path, help="the en.md the counts came from")
    ap.add_argument("--npmi-min", type=float, default=NPMI_MIN)
    ap.add_argument("--min-count", type=int, default=MIN_COUNT)
    args = ap.parse_args()

    terms = merge_yake(load_terms())
    max_n = max(r["words"] for r in terms.values())
    lemma, expected = load_lemmas()
    tokens = tokenize(args.source, lemma)
    counts = ngram_counts(tokens, max_n)
    total = len(tokens)

    agree = check_counts(counts, expected)
    if agree is not None:
        print(f"unigram counts reproduced: {agree:.1%} of {len(expected):,} words")
        if agree < 0.9:
            print("  WARNING: tokenization disagrees with the recorded counts;")
            print("  phrase counts (and so every NPMI below) are unreliable.")

    apply_gate(terms, counts, total, args.npmi_min, args.min_count)
    kept = [r for r in terms.values() if not r["gated"]]
    dropped = [r for r in terms.values() if r["gated"]]
    ranked = fuse(kept)
    write(ranked, dropped, total, args)

    print(f"{total:,} tokens; {len(terms):,} candidates")
    print(f"  kept {len(ranked):,}  gated {len(dropped):,} -> {OUT_MD.name}")
    print("\nTop 25 fused:")
    for i, r in enumerate(ranked[:25], 1):
        print(f"  {i:>3}. {r['term']:<32} npmi={fmt(r['npmi'], '.2f'):>6}")
    print("\nHighest-NPMI phrases:")
    top = sorted((r for r in ranked if r["npmi"] is not None),
                 key=lambda r: -r["npmi"])[:15]
    for r in top:
        print(f"       {r['term']:<32} npmi={r['npmi']:.2f}  n={r['phrase_count']}")


if __name__ == "__main__":
    main()
