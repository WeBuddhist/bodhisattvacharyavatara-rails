#!/usr/bin/env python3
"""
keywords_by_reference.py
-------------------------
Reads the two existing keyword outputs:
    output/bca-en-general-readers_keyword.json   (TF-IDF single-word terms, with ids)
    output/bca-en-general-readers-keywords.md    (YAKE bi/trigram phrases, with ids)

and inverts them: instead of "keyword -> reference IDs", produces
"reference ID -> every keyword that has it". Keywords with no reference ID
(empty or "-") are ignored entirely — they never appear in the output.

Usage
-----
    python keywords_by_reference.py

Output
------
    output/keywords-by-reference.md

Format (one line per reference ID, sorted in document order):
    [1-1] keyword1, keyword2, keyword3
    [1-2] keywordA, keywordB
    ...
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "output"

JSON_PATH = OUTPUT_DIR / "bca-en-general-readers_keyword.json"
MD_PATH   = OUTPUT_DIR / "bca-en-general-readers-keywords.md"
DEST_PATH = OUTPUT_DIR / "keywords-by-reference.md"


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def load_json_keywords(path: Path) -> list[tuple[str, list[str]]]:
    """
    Reads {"word": [{"word": ..., "ids": [...]}, ...]} and returns
    [(word, ids), ...], skipping any entry with no ids.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for entry in data.get("word", []):
        ids = entry.get("ids", [])
        if ids:
            out.append((entry["word"], ids))
    return out


_MD_ROW_RE = re.compile(
    r"^\|\s*[\d.]+\s*\|\s*(?P<phrase>.+?)\s*\|\s*(?P<ids>.+?)\s*\|\s*$"
)


def load_md_keywords(path: Path) -> list[tuple[str, list[str]]]:
    """
    Reads the "| Score | Phrase | Reference IDs |" table and returns
    [(phrase, ids), ...], skipping rows whose Reference IDs cell is "-"
    (i.e. no reference ID) or otherwise empty.
    """
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        if line.startswith("|---") or line.startswith("| ---"):
            continue
        if line.startswith("| Score "):  # header row
            continue
        m = _MD_ROW_RE.match(line)
        if not m:
            continue
        phrase   = m.group("phrase").strip()
        ids_cell = m.group("ids").strip()
        if ids_cell == "-" or not ids_cell:
            continue
        ids = [tok.strip().lstrip("^") for tok in ids_cell.split(",")]
        ids = [i for i in ids if i]
        if ids:
            out.append((phrase, ids))
    return out


# ---------------------------------------------------------------------------
# Natural sort for block IDs like "1-1", "9-31-0", "10-a", "b-2"
# ---------------------------------------------------------------------------

def _id_sort_key(block_id: str):
    parts = block_id.split("-")
    key = []
    for part in parts:
        if part.isdigit():
            key.append((0, int(part), ""))
        else:
            key.append((1, 0, part))
    return key


# ---------------------------------------------------------------------------
# Build the inverted index
# ---------------------------------------------------------------------------

def build_index(*sources: list[tuple[str, list[str]]]) -> dict[str, list[str]]:
    """
    Merges any number of (keyword, ids) lists into {id: [keywords...]},
    deduped and sorted alphabetically (case-insensitive) within each id.
    """
    index: dict[str, set[str]] = {}
    for source in sources:
        for keyword, ids in source:
            for block_id in ids:
                index.setdefault(block_id, set()).add(keyword)

    return {
        block_id: sorted(keywords, key=str.lower)
        for block_id, keywords in index.items()
    }


def render(index: dict[str, list[str]]) -> str:
    lines = []
    for block_id in sorted(index.keys(), key=_id_sort_key):
        keywords = ", ".join(index[block_id])
        lines.append(f"[{block_id}] {keywords}")
    return "\n".join(lines) + "\n"


def main() -> None:
    if not JSON_PATH.exists():
        raise FileNotFoundError(f"Not found:\n  {JSON_PATH}")
    if not MD_PATH.exists():
        raise FileNotFoundError(f"Not found:\n  {MD_PATH}")

    json_keywords = load_json_keywords(JSON_PATH)
    md_keywords   = load_md_keywords(MD_PATH)

    print(f"Loaded {len(json_keywords)} JSON terms with reference IDs.")
    print(f"Loaded {len(md_keywords)} Markdown phrases with reference IDs.")

    index = build_index(json_keywords, md_keywords)
    print(f"Built index covering {len(index)} distinct reference IDs.")

    DEST_PATH.write_text(render(index), encoding="utf-8")
    print(f"Written → {DEST_PATH}")


if __name__ == "__main__":
    main()
