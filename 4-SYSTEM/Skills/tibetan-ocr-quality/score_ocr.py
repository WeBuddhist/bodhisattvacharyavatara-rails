#!/usr/bin/env python3
"""Score Tibetan OCR output quality using KenLM perplexity.

Usage:
    python score_ocr.py <input_file> [--model <arpa_path>]

Requires:
    pip install kenlm botok
"""

import argparse
import math
import sys
from pathlib import Path


def ensure_dependencies():
    """Check that kenlm and botok are importable."""
    missing = []
    try:
        import kenlm  # noqa: F401
    except ImportError:
        missing.append("kenlm")
    try:
        from botok.utils.corpus_normalization import normalize_for_perplexity  # noqa: F401
    except ImportError:
        missing.append("botok")
    if missing:
        print(
            f"ERROR: Missing packages: {', '.join(missing)}\n"
            f"Install with: pip install {' '.join(missing)} --break-system-packages",
            file=sys.stderr,
        )
        sys.exit(1)


def score_file(input_path: str, model_path: str) -> None:
    """Normalize the input text and compute perplexity with KenLM."""
    import kenlm
    from botok.utils.corpus_normalization import normalize_for_perplexity

    # --- load model ---
    model_p = Path(model_path)
    if not model_p.exists():
        print(
            f"ERROR: Model file not found: {model_path}\n"
            "Download from https://huggingface.co/openpecha/BoKenlm-syl-v0.4\n"
            "and place the .arpa file at the expected path.",
            file=sys.stderr,
        )
        sys.exit(1)

    model = kenlm.Model(model_path)

    # --- read and normalize ---
    input_p = Path(input_path)
    if not input_p.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    raw_text = input_p.read_text(encoding="utf-8")
    if not raw_text.strip():
        print("ERROR: Input file is empty.", file=sys.stderr)
        sys.exit(1)

    normalized = normalize_for_perplexity(raw_text)
    if not normalized.strip():
        print(
            "ERROR: Normalization produced no tokens. "
            "The file may not contain Tibetan text.",
            file=sys.stderr,
        )
        sys.exit(1)

    # --- split into sentences on shad (།) ---
    sentences = [s.strip() for s in normalized.split("།") if s.strip()]
    if not sentences:
        print("ERROR: No sentences found after normalization.", file=sys.stderr)
        sys.exit(1)

    # --- score ---
    total_log_prob = 0.0
    total_tokens = 0

    for sentence in sentences:
        log_prob = model.score(sentence)
        token_count = len(sentence.split())
        total_log_prob += log_prob
        total_tokens += token_count

    if total_tokens == 0:
        print("ERROR: Zero tokens after scoring.", file=sys.stderr)
        sys.exit(1)

    # Perplexity = 10^(-log_prob / token_count)
    # KenLM returns log10 scores
    avg_log_prob = total_log_prob / total_tokens
    perplexity = math.pow(10, -avg_log_prob)

    # --- report ---
    print("=== Tibetan OCR Quality Report ===")
    print(f"File:       {input_path}")
    print(f"Model:      {model_path}")
    print(f"Sentences:  {len(sentences)}")
    print(f"Tokens:     {total_tokens}")
    print(f"Log-prob:   {total_log_prob:.4f}")
    print(f"Perplexity: {perplexity:.4f}")
    print("================================")


def main():
    parser = argparse.ArgumentParser(
        description="Score Tibetan OCR quality via KenLM perplexity"
    )
    parser.add_argument("input_file", help="Path to the Tibetan .txt file")
    parser.add_argument(
        "--model",
        default="4-SYSTEM/models/BoKenlm-syl-v0.4.arpa",
        help="Path to the KenLM ARPA model (default: 4-SYSTEM/models/BoKenlm-syl-v0.4.arpa)",
    )
    args = parser.parse_args()

    ensure_dependencies()
    score_file(args.input_file, args.model)


if __name__ == "__main__":
    main()
