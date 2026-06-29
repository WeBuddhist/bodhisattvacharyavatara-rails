"""
keywords.py
-----------
Extracts English keywords from a rough translation using YAKE.

Install dependencies:
    pip install yake spacy
    python -m spacy download en_core_web_sm
"""

import json
import spacy
import yake
from dataclasses import dataclass
from pathlib import Path


# Custom stop words specific to Pali translation style
PALI_TRANSLATION_STOPWORDS = {
    "thus", "said", "therefore", "herein", "monks", "monk",
    "bhikkhu", "bhikkhus", "verily", "indeed", "hereby", "wherefore",
    "thereof", "therein", "hath", "thou", "thee", "shall", "unto",
    "saying", "spoke", "replied", "asked", "come", "went", "go",
}


@dataclass
class Keyword:
    """A single extracted keyword with both raw and normalized forms."""
    raw:        str     # as YAKE extracted it,   e.g. "mental states"
    normalized: str     # lemmatized + filtered,   e.g. "mental state"
    score:      float   # YAKE score — lower = more important


class KeywordExtractor:
    """
    Extracts and normalizes English keywords from a rough Pali translation.

    Pipeline:
        1. YAKE  — scores and extracts keywords (unigrams + bigrams + trigrams)
        2. spaCy — lemmatizes keywords ("teachings" -> "teaching")
        3. Stop word filtering — removes noise words

    Usage:
        extractor = KeywordExtractor(score_threshold=0.3)
        keywords = extractor.extract(text)
        extractor.save_json(keywords, "yake_raw.json", "yake_normalized.json")
        extractor.save_md(keywords, "keywords.md")
        extractor.preview_scores(text, "preview.md")
    """

    def __init__(self, score_threshold: float = 0.3, ngram_size: int = 3):
        """
        Args:
            score_threshold: YAKE score cutoff — keep only keywords BELOW this value.
                             Lower score = more important in YAKE.
                             0.1 = very strict (only highly important keywords)
                             0.3 = balanced (default)
                             0.5 = lenient (keeps more keywords)
            ngram_size:      max phrase length (3 = up to trigrams)
        """
        self.score_threshold = score_threshold

        print("Loading spaCy model...")
        self.nlp = spacy.load("en_core_web_sm")

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
        Extract keywords from English text.

        Keeps only keywords whose YAKE score is below score_threshold.
        Lower score = more important. Anything above threshold is excluded.

        Returns a list of Keyword objects (raw + normalized + score)
        sorted by YAKE importance (lowest score = most important).
        """
        raw_keywords = self.yake_extractor.extract_keywords(text)

        seen = set()
        keywords = []

        for phrase, score in raw_keywords:
            # Exclude keywords above threshold (less important)
            if score > self.score_threshold:
                continue
            normalized = self._normalize(phrase)
            if not normalized:
                continue
            if normalized in seen:
                continue
            seen.add(normalized)
            keywords.append(Keyword(
                raw=phrase,
                normalized=normalized,
                score=score,
            ))

        print(f"Kept {len(keywords)} keywords with score <= {self.score_threshold}.")
        return keywords

    # -----------------------------------------------------------------------
    # Save outputs
    # -----------------------------------------------------------------------

    def _write_score_json(self, data: dict[str, float], path: str) -> None:
        items = list(data.items())
        lines = ["{"]
        for i, (key, score) in enumerate(items):
            suffix = "," if i < len(items) - 1 else ""
            lines.append(
                f'  {json.dumps(key, ensure_ascii=False)}: {round(score, 6):.6f}{suffix}'
            )
        lines.append("}")
        Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")

    def save_json(self, keywords: list[Keyword], raw_path: str, normalized_path: str) -> None:
        """
        Save keywords to two JSON files — one raw, one normalized.
        Format: { "keyword": score, ... } sorted by score (most important first).
        Args:
            raw_path:        path for raw YAKE keywords        e.g. "yake_raw.json"
            normalized_path: path for normalized keywords      e.g. "yake_normalized.json"
        """
        sorted_keywords = sorted(keywords, key=lambda k: k.score)

        raw_data = {
            kw.raw: round(kw.score, 6)
            for kw in sorted_keywords
        }
        normalized_data = {
            kw.normalized: round(kw.score, 6)
            for kw in sorted_keywords
        }

        self._write_score_json(raw_data, raw_path)
        print(f"Saved {len(raw_data)} raw keywords to {raw_path}")

        self._write_score_json(normalized_data, normalized_path)
        print(f"Saved {len(normalized_data)} normalized keywords to {normalized_path}")


    def save_md(self, keywords: list[Keyword], path: str) -> None:
        """
        Save keywords to a Markdown file.
        Format: score | normalized keyword
        Sorted by score (most important first).
        """
        lines = ["# Keywords\n", "| Score | Keyword |", "|-------|---------|"]
        for kw in sorted(keywords, key=lambda k: k.score):
            lines.append(f"| {round(kw.score, 6):.6f} | {kw.normalized} |")
        Path(path).write_text("\n".join(lines), encoding="utf-8")
        print(f"Saved {len(keywords)} keywords to {path}")

    def preview_scores(self, text: str, path: str) -> None:
        """
        Saves ALL YAKE keywords and their scores to a Markdown file,
        along with the lemmatized form.
        Use this to decide what score_threshold to set.

        Format: lemmatized | raw word
        Sorted by score (most important first).
        """
        raw_keywords = self.yake_extractor.extract_keywords(text)
        sorted_keywords = sorted(raw_keywords, key=lambda x: x[1])

        lines = ["# Score Preview\n", "| Score | Lemmatized | Raw |", "|-------|-----------|-----|"]
        for phrase, score in sorted_keywords:
            lemmatized = self._normalize(phrase) or "-"
            lines.append(f"| {round(score, 6):.6f} | {lemmatized} | {phrase} |")

        Path(path).write_text("\n".join(lines), encoding="utf-8")
        print(f"Saved score preview ({len(sorted_keywords)} entries) to {path}")

    # -----------------------------------------------------------------------
    # Internal
    # -----------------------------------------------------------------------

    def _normalize(self, phrase: str) -> str | None:
        """
        Lemmatize a phrase using spaCy and filter out stop words.

        e.g. "mental states" -> "mental state"
             "teachings"     -> "teaching"
             "this"          -> None  (stop word, filtered)
             "monks"         -> None  (custom stop word, filtered)
        """
        doc = self.nlp(phrase.lower())

        tokens = []
        for token in doc:
            if token.is_stop:
                continue
            if token.lemma_ in PALI_TRANSLATION_STOPWORDS:
                continue
            if token.is_punct or len(token.lemma_) < 3:
                continue
            tokens.append(token.lemma_)

        if not tokens:
            return None

        return " ".join(tokens)


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    OUTPUT_DIR = Path(__file__).resolve().parent

    #SOURCE_PATH = Path(r"C:\Users\geshe lobzang tseten\repos\abhidhamma-rails\1-SOURCES\Translations\en-1-rhys_davids.md")  # <-- change this to your .md file path
    SOURCE_PATH = Path(r"C:\Users\geshe lobzang tseten\repos\abhidhamma-rails\1-SOURCES\Translations\en-1-ukyaw_khine.md")
    source_stem = SOURCE_PATH.stem

    with open(SOURCE_PATH, "r", encoding="utf-8") as f:
        SOURCE = f.read()

    extractor = KeywordExtractor(score_threshold=0.3)

    # Preview all scores first to tune threshold
    extractor.preview_scores(SOURCE, OUTPUT_DIR / "output" / f"{source_stem}-preview.md")

    # Extract keywords
    keywords = extractor.extract(SOURCE)

    # Save outputs
    extractor.save_json(keywords, OUTPUT_DIR /"output"/ f"{source_stem}-raw.json", OUTPUT_DIR / "output" / f"{source_stem}-normalized.json")
    extractor.save_md(keywords, OUTPUT_DIR/ "output" / f"{source_stem}-keywords.md")