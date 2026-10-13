#!/usr/bin/env python3
"""
generate_idf_corpus.py
======================
Builds a general-English IDF reference corpus from the NLTK Reuters-21578
newswire corpus using scikit-learn's TfidfVectorizer.

Outputs
-------
  idf_corpus.pkl   — pickled dict[str, float]  (fast load at runtime)
  idf_corpus.py    — Python module exporting IDF_CORPUS: dict[str, float]
                     (human-readable, importable without extra dependencies)

The IDF formula used by scikit-learn (smooth=True, default):
  idf(t) = log((1 + N) / (1 + df(t))) + 1
where N = number of documents, df(t) = documents containing term t.

Usage
-----
    python3 generate_idf_corpus.py          # from repo root or this directory
    python3 generate_idf_corpus.py --top 50000   # keep only top-N terms by IDF

Dependencies
------------
    pip install scikit-learn nltk
    python -c "import nltk; nltk.download('reuters')"
"""

import argparse
import pathlib
import pickle
import sys
from datetime import date

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = pathlib.Path(__file__).parent
OUT_PKL = HERE / "idf_corpus.pkl"
OUT_PY  = HERE / "idf_corpus.py"


# ---------------------------------------------------------------------------
# Corpus builder
# ---------------------------------------------------------------------------

def build_idf(top_n: int | None = None) -> dict[str, float]:
    """Return a mapping of token → IDF value from the Reuters corpus."""
    try:
        import nltk
        from nltk.corpus import reuters
    except ImportError:
        sys.exit("nltk is not installed.  Run:  pip install nltk")

    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
    except ImportError:
        sys.exit("scikit-learn is not installed.  Run:  pip install scikit-learn")

    # Ensure the corpus data is present
    try:
        reuters.fileids()
    except LookupError:
        print("Downloading Reuters corpus …")
        nltk.download("reuters", quiet=True)

    fileids = reuters.fileids()
    print(f"Reuters corpus: {len(fileids):,} documents")

    print("Loading document texts …")
    documents = [reuters.raw(fid) for fid in fileids]

    print("Fitting TF-IDF vectorizer …")
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words=None,       # keep everything — caller can filter later
        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z\-']+[a-zA-Z]\b",  # 3+ char alphabetic
        smooth_idf=True,       # log((1+N)/(1+df)) + 1  — avoids division by zero
        sublinear_tf=False,
    )
    vectorizer.fit(documents)

    feature_names = vectorizer.get_feature_names_out()
    idfs = vectorizer.idf_

    corpus: dict[str, float] = {
        word: round(float(idf), 6)
        for word, idf in zip(feature_names, idfs)
    }

    if top_n is not None:
        # Keep the top_n terms sorted by ascending IDF (most common first)
        sorted_items = sorted(corpus.items(), key=lambda kv: kv[1])
        corpus = dict(sorted_items[:top_n])

    print(f"Vocabulary size: {len(corpus):,}")
    return corpus


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_pickle(corpus: dict[str, float], path: pathlib.Path) -> None:
    path.write_bytes(pickle.dumps(corpus, protocol=pickle.HIGHEST_PROTOCOL))
    print(f"Written pickle → {path}  ({path.stat().st_size / 1024:.1f} KB)")


def write_python_module(corpus: dict[str, float], path: pathlib.Path) -> None:
    """Write a self-contained Python module with the IDF dict as a literal."""
    today = date.today().isoformat()
    n_docs = 10_788   # Reuters-21578 document count (fixed, for the docstring)

    lines: list[str] = [
        '"""',
        "idf_corpus.py — General-English IDF reference built from Reuters-21578.",
        "",
        f"Generated : {today}",
        f"Corpus    : NLTK Reuters-21578  ({n_docs:,} newswire documents)",
        "Vectorizer: sklearn TfidfVectorizer(smooth_idf=True, lowercase=True)",
        "Formula   : idf(t) = log((1 + N) / (1 + df(t))) + 1",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        f"IDF_CORPUS: dict[str, float] = {{",
    ]

    for word, idf in sorted(corpus.items(), key=lambda kv: kv[1]):
        escaped = word.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'    "{escaped}": {idf},')

    lines += ["}", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    size_kb = path.stat().st_size / 1024
    print(f"Written module → {path}  ({size_kb:.0f} KB)")


# ---------------------------------------------------------------------------
# Quick sanity check
# ---------------------------------------------------------------------------

def print_samples(corpus: dict[str, float]) -> None:
    samples = ["the", "system", "bank", "government", "profit", "quantum",
               "arbitrage", "jhana", "consciousness", "zest"]
    print("\nSample IDF values:")
    for w in samples:
        v = corpus.get(w)
        tag = f"{v:.4f}" if v is not None else "— not in corpus"
        print(f"  {w:20s} {tag}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--top", type=int, default=None, metavar="N",
        help="Keep only the top N terms by ascending IDF (most common first). "
             "Default: keep all (~45 000 terms)."
    )
    parser.add_argument(
        "--no-pickle", action="store_true",
        help="Skip writing the .pkl file (write only the .py module)."
    )
    parser.add_argument(
        "--no-module", action="store_true",
        help="Skip writing the .py module (write only the .pkl file)."
    )
    args = parser.parse_args()

    corpus = build_idf(top_n=args.top)
    print_samples(corpus)

    if not args.no_pickle:
        write_pickle(corpus, OUT_PKL)
    if not args.no_module:
        write_python_module(corpus, OUT_PY)

    print("\nDone.")


if __name__ == "__main__":
    main()