"""
keywords.py
-----------
Extracts raw bigram/trigram keywords from a single English text file using YAKE,
along with the Obsidian block ID(s) (e.g. "1-1", "9-31-0") of every verse/heading
block where each keyword phrase actually occurs.

No lemmatization, no normalization, no stop-word list — raw YAKE output only,
filtered to phrases of 2-3 words and a score cutoff.

Install dependencies:
    pip install yake
"""

import json
import re
import yake
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Block-ID mapping
# ---------------------------------------------------------------------------
# The vault marks every verse/heading/prose block with a trailing Obsidian
# block ID, e.g. "... ^1-1", "## Chapter 1 ^1-0", "... ^9-31-0", "... ^10-a".
_BLOCK_ID_RE = re.compile(r"\^([\w]+(?:-[\w]+)*)\s*$")


def extract_blocks(text: str) -> list[tuple[str | None, str]]:
    """
    Split a vault markdown file into (block_id, block_text) pairs.

    Splits on blank lines and attaches each run of paragraphs to the block ID
    it ends with, so a keyword found inside that text can be traced back to
    its source block. Paragraphs before the first block ID (e.g. frontmatter
    remnants) are attached to block_id=None and ignored for reference lookup.
    """
    paragraphs = re.split(r"\n\s*\n", text)
    blocks: list[tuple[str | None, str]] = []
    pending: list[str] = []

    for para in paragraphs:
        pending.append(para)
        m = _BLOCK_ID_RE.search(para.strip())
        if m:
            blocks.append((m.group(1), "\n\n".join(pending)))
            pending = []

    if pending:
        blocks.append((None, "\n\n".join(pending)))

    return blocks


def find_ids_for_phrase(phrase: str, blocks: list[tuple[str | None, str]]) -> list[str]:
    """
    Return every block ID whose text contains `phrase` (case-insensitive,
    whole-word match), in document order.
    """
    pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
    ids = []
    for block_id, block_text in blocks:
        if block_id is None:
            continue
        if pattern.search(block_text):
            ids.append(block_id)
    return ids


@dataclass
class Keyword:
    """A single raw keyword extracted by YAKE."""
    phrase: str                              # exactly as YAKE extracted it, e.g. "mental states"
    score:  float                            # YAKE score — lower = more important
    ids:    list[str] = field(default_factory=list)  # block IDs where the phrase occurs, e.g. ["1-1", "1-14"]


class KeywordExtractor:
    """
    Extracts raw bi/trigram keywords from English text, with reference block IDs.

    Usage:
        extractor = KeywordExtractor(score_threshold=0.2)
        keywords = extractor.extract(text)
        extractor.save_json(keywords, "keywords-raw.json")
        extractor.save_md(keywords, "keywords.md")
        extractor.preview_scores(text, "preview.md")
    """

    def __init__(self, score_threshold: float = 0.2, ngram_size: int = 3):
        """
        Args:
            score_threshold: YAKE score cutoff — keep only keywords BELOW this value.
                             Lower score = more important in YAKE.
            ngram_size:      max phrase length (3 = up to trigrams)
        """
        self.score_threshold = score_threshold

        print("Loading YAKE...")
        self.yake_extractor = yake.KeywordExtractor(
            lan="en",
            n=ngram_size,
            dedupLim=0.9,
            top=9999,       # extract everything, filter by threshold after
            features=None,
        )
        print("KeywordExtractor ready.\n")

    # -----------------------------------------------------------------------
    # Extract
    # -----------------------------------------------------------------------

    def extract(self, text: str) -> list[Keyword]:
        """
        Extract bigram/trigram keywords from English text.

        Keeps only phrases of 2-3 words whose YAKE score is below
        score_threshold (lower score = more important). Each keyword is
        tagged with the block ID(s) of every source block it appears in.

        Returns a list of Keyword objects (phrase + score + ids), sorted by
        YAKE importance (lowest score first).
        """
        raw_keywords = self.yake_extractor.extract_keywords(text)
        blocks = extract_blocks(text)

        seen = set()
        keywords = []

        for phrase, score in raw_keywords:
            if score > self.score_threshold:
                continue
            word_count = len(phrase.split())
            if word_count < 2 or word_count > 3:
                continue
            if phrase in seen:
                continue
            seen.add(phrase)
            keywords.append(Keyword(
                phrase=phrase,
                score=score,
                ids=find_ids_for_phrase(phrase, blocks),
            ))

        print(f"Kept {len(keywords)} bi/trigram keywords with score <= {self.score_threshold}.")
        return keywords

    # -----------------------------------------------------------------------
    # Save outputs
    # -----------------------------------------------------------------------

    def save_json(self, keywords: list[Keyword], path: str) -> None:
        """
        Save keywords to a JSON file.
        Format: { "phrase": {"score": ..., "ids": [...]}, ... }
        Sorted by score (most important first).
        """
        sorted_keywords = sorted(keywords, key=lambda k: k.score)

        lines = ["{"]
        for i, kw in enumerate(sorted_keywords):
            suffix = "," if i < len(sorted_keywords) - 1 else ""
            entry = {"score": round(kw.score, 6), "ids": kw.ids}
            lines.append(
                f'  {json.dumps(kw.phrase, ensure_ascii=False)}: '
                f'{json.dumps(entry, ensure_ascii=False)}{suffix}'
            )
        lines.append("}")
        Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")

        print(f"Saved {len(sorted_keywords)} raw keywords to {path}")

    def save_md(self, keywords: list[Keyword], path: str) -> None:
        """
        Save keywords to a Markdown file.
        Format: score | phrase | reference IDs
        Sorted by score (most important first).
        """
        lines = ["# Keywords\n", "| Score | Phrase | Reference IDs |", "|-------|--------|----------------|"]
        for kw in sorted(keywords, key=lambda k: k.score):
            ids_str = ", ".join(f"^{i}" for i in kw.ids) if kw.ids else "-"
            lines.append(f"| {round(kw.score, 6):.6f} | {kw.phrase} | {ids_str} |")
        Path(path).write_text("\n".join(lines), encoding="utf-8")
        print(f"Saved {len(keywords)} keywords to {path}")

    def preview_scores(self, text: str, path: str) -> None:
        """
        Saves ALL YAKE bi/trigram keywords and their scores to a Markdown file
        (no threshold applied), to help decide what score_threshold to set.
        Reference IDs are not looked up here (this is just for tuning the
        threshold, and skipping the lookup keeps it fast).

        Format: score | phrase
        Sorted by score (most important first).
        """
        raw_keywords = self.yake_extractor.extract_keywords(text)
        bigrams_trigrams = [
            (phrase, score) for phrase, score in raw_keywords
            if 2 <= len(phrase.split()) <= 3
        ]
        sorted_keywords = sorted(bigrams_trigrams, key=lambda x: x[1])

        lines = ["# Score Preview\n", "| Score | Phrase |", "|-------|--------|"]
        for phrase, score in sorted_keywords:
            lines.append(f"| {round(score, 6):.6f} | {phrase} |")

        Path(path).write_text("\n".join(lines), encoding="utf-8")
        print(f"Saved score preview ({len(sorted_keywords)} entries) to {path}")


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

def _chunk_text(text: str, marker: str = "\n## ", max_chars: int = 20000) -> list[str]:
    """
    Split a large document into chunks for YAKE (its extraction time grows
    faster than linearly with text length, so chunking a long file is much
    faster than running it as one block). Splits on top-level headings first;
    any chunk still longer than max_chars is further cut at the nearest
    paragraph break.
    """
    parts = text.split(marker)
    chunks = [parts[0]] + [marker.lstrip("\n") + p for p in parts[1:]]

    final_chunks = []
    for chunk in chunks:
        if len(chunk) <= max_chars:
            final_chunks.append(chunk)
            continue
        # further split an oversized chunk on blank lines
        paragraphs = chunk.split("\n\n")
        buf = ""
        for para in paragraphs:
            if len(buf) + len(para) + 2 > max_chars and buf:
                final_chunks.append(buf)
                buf = para
            else:
                buf = f"{buf}\n\n{para}" if buf else para
        if buf:
            final_chunks.append(buf)

    return [c for c in final_chunks if c.strip()]


if __name__ == "__main__":

    HERE = Path(__file__).resolve().parent
    REPO_ROOT = HERE.parent.parent
    OUTPUT_DIR = HERE / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    SOURCE_PATH = REPO_ROOT / "tibetan/bca-en-general-readers.md"

    extractor = KeywordExtractor(score_threshold=0.2)

    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Source file not found:\n  {SOURCE_PATH}")

    source_stem = SOURCE_PATH.stem
    source_text = SOURCE_PATH.read_text(encoding="utf-8")

    print(f"\nProcessing {SOURCE_PATH.name}...")

    # Process in chunks (by chapter) — much faster than one pass over the
    # whole file, and the results are merged/deduped (best score wins) below.
    chunks = _chunk_text(source_text)
    print(f"Split into {len(chunks)} chunks.")

    all_keywords: dict[str, float] = {}
    preview_rows: list[tuple[str, float]] = []

    for i, chunk in enumerate(chunks, 1):
        print(f"  chunk {i}/{len(chunks)} ({len(chunk)} chars)...")

        raw_keywords = extractor.yake_extractor.extract_keywords(chunk)
        for phrase, score in raw_keywords:
            word_count = len(phrase.split())
            if 2 <= word_count <= 3:
                preview_rows.append((phrase, score))
                if phrase not in all_keywords or score < all_keywords[phrase]:
                    all_keywords[phrase] = score

    # Preview: all bi/trigram scores across the whole document
    preview_rows.sort(key=lambda x: x[1])
    preview_lines = ["# Score Preview\n", "| Score | Phrase |", "|-------|--------|"]
    for phrase, score in preview_rows:
        preview_lines.append(f"| {round(score, 6):.6f} | {phrase} |")
    preview_path = OUTPUT_DIR / f"{source_stem}-preview.md"
    Path(preview_path).write_text("\n".join(preview_lines), encoding="utf-8")
    print(f"Saved score preview ({len(preview_rows)} entries) to {preview_path}")

    # Extract: keep only scores <= threshold
    kept_phrases = {
        phrase: score
        for phrase, score in all_keywords.items()
        if score <= extractor.score_threshold
    }
    print(f"Kept {len(kept_phrases)} bi/trigram keywords with score <= {extractor.score_threshold}.")

    # Map each kept phrase to the block ID(s) it appears in, using the whole
    # (unchunked) document so references aren't limited to one chapter.
    print("Mapping keywords to reference block IDs...")
    blocks = extract_blocks(source_text)
    keywords = [
        Keyword(phrase=phrase, score=score, ids=find_ids_for_phrase(phrase, blocks))
        for phrase, score in kept_phrases.items()
    ]

    # Save outputs
    extractor.save_json(keywords, OUTPUT_DIR / f"{source_stem}-raw.json")
    extractor.save_md(keywords, OUTPUT_DIR / f"{source_stem}-keywords.md")
