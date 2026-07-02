#!/usr/bin/env python3
"""Deprecated: use 4-SYSTEM/Skills/translate-zero-shot/scripts/merge_chapters.py instead."""
import sys
from pathlib import Path

# Re-export for backward compatibility
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Skills" / "translate-zero-shot" / "scripts"))
from merge_chapters import merge_chapters  # noqa: E402

if __name__ == "__main__":
    track = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "3-TRANSFORMATIONS/Translations/en-beginner-audience"
    )
    result = merge_chapters(
        track.resolve(),
        track="en-beginner-audience",
        title="Entering the Bodhisattva's Way of Life — Full Text (Beginner English)",
        output_name="BCA-Full-Beginner-English.md",
    )
    print(f"Wrote {result} ({result.stat().st_size:,} bytes)")