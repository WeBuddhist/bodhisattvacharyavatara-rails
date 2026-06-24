---
name: tibetan-segmenter
description: Segment a Tibetan text file into sentences. Use this skill whenever the user wants to segment, split, or break a Tibetan book or text into sentences or lines, normalize Tibetan spacing, or prepare a Tibetan corpus for further processing. Trigger when the user mentions "segment Tibetan", "Tibetan sentence segmentation", "split Tibetan text into sentences", "normalize Tibetan text", "prepare Tibetan corpus", "clean up Tibetan text", or any task involving breaking continuous Tibetan text into sentence-per-line format. Also trigger when the user uploads a .txt file containing Tibetan script and wants it cleaned or restructured.
---

# Tibetan Text Segmenter

Segments a Tibetan text file into one-sentence-per-line format. Zero third-party dependencies — Python stdlib only.

## What it does

1. **Remove all newlines** — merges the text into one continuous string, inserting a tsheg where a Tibetan letter would lose its syllable boundary at a line break.
2. **Normalize spaces** — Tibetan-specific space normalization (inlined from [Botok's normalize_spaces](https://github.com/OpenPecha/Botok/blob/master/botok/utils/corpus_normalization.py#L30)): collapses multiple spaces, removes spaces after tsheg before initial letters, removes spaces between final letters and tsheg.
3. **Sentence segmentation** — character-by-character scanner that splits at all shad types (། ༎ ༏ ༐ ༑ ༒ ༔) while skipping shad inside yig mgo sequences (༄༅། །, ༁-༊, ࿐-࿘). Each sentence is output on its own line with trailing punctuation preserved.

## Dependencies

Python 3.8+ (no third-party packages).

## Usage

```bash
python scripts/segment_tibetan.py <input_file> [-o output_file]
```

If `-o` is omitted, output is written to `<input_file_stem>_segmented.txt` in the same directory.
