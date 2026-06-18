#!/usr/bin/env python3
"""
translate-plain-english.py
==========================
Extracts Sanskrit verses from sk-dev.md by chapter, reads each verse's
2-RAILS context package for commentary synthesis, then calls the Claude API
to produce a Grade 8 plain-English translation and writes it to the
workspace root.

Rail usage: for each verse, the script reads 2-RAILS/Verses/{ch}-{v}.md
and extracts the ## Synthesis section (actual Tibetan summary text, not
transclusion refs). This is passed to the model as "commentary context"
alongside the Sanskrit root. Falls back to Sanskrit-only if the rail is
absent or status != complete.

Usage:
    python translate-plain-english.py --chapter 1
    python translate-plain-english.py --chapter 2
    python translate-plain-english.py --chapter 1-3      # range
    python translate-plain-english.py --chapter all      # all 10 chapters

Requirements:
    pip install anthropic

Set your API key:
    export ANTHROPIC_API_KEY=sk-...
"""

import re
import sys
import argparse
import os

# ---------------------------------------------------------------------------
# Paths (relative to this script's location = 0-INBOX/)
# ---------------------------------------------------------------------------
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
ROOT         = os.path.dirname(SCRIPT_DIR)                          # project root
SOURCE_FILE  = os.path.join(ROOT, "1-SOURCES", "Text", "sk-dev.md")
RAILS_DIR    = os.path.join(ROOT, "2-RAILS", "Verses")
REQ_FILE     = os.path.join(ROOT, "3-TRANSFORMATIONS", "Translations", "en-plain-english", "requirements.md")
TERM_FILE    = os.path.join(ROOT, "3-TRANSFORMATIONS", "Translations", "en-plain-english", "termbase.md")
OUTPUT_DIR   = ROOT                                                  # save at workspace root


# ---------------------------------------------------------------------------
# Chapter metadata
# ---------------------------------------------------------------------------
CHAPTER_TITLES = {
    1:  "The Benefits of the Mind of Enlightenment",
    2:  "Confessing Wrongdoing",
    3:  "Taking Up the Mind of Enlightenment",
    4:  "Carefulness",
    5:  "Guarding Awareness",
    6:  "The Perfection of Patience",
    7:  "The Perfection of Effort",
    8:  "The Perfection of Meditation",
    9:  "The Perfection of Wisdom",
    10: "Dedication",
}


# ---------------------------------------------------------------------------
# Rail reading
# ---------------------------------------------------------------------------

def parse_rail_synthesis(ch_num: int, verse_num: int) -> str | None:
    """
    Reads 2-RAILS/Verses/{ch_num}-{verse_num}.md and extracts the
    ## Synthesis section (actual Tibetan summary text, not transclusion refs).

    Returns the extracted synthesis text, or None if:
      - the rail file does not exist, or
      - the rail status is not 'complete'.
    """
    rail_path = os.path.join(RAILS_DIR, f"{ch_num}-{verse_num}.md")
    if not os.path.exists(rail_path):
        return None

    with open(rail_path, encoding="utf-8") as f:
        content = f.read()

    # Check status in YAML frontmatter
    status_match = re.search(r'^status:\s*(\w+)', content, re.MULTILINE)
    if not status_match or status_match.group(1) != 'complete':
        return None

    # Extract the ## Synthesis section (stop at next ## heading or end of file)
    synth_match = re.search(
        r'## Synthesis \((?:original language|Tibetan)\)\n(.*?)(?=^## |\Z)',
        content,
        re.MULTILINE | re.DOTALL,
    )
    if not synth_match:
        return None

    synthesis_raw = synth_match.group(1)

    # Keep only lines that contain actual text — skip:
    #   - Obsidian transclusion lines: ![[...]]
    #   - Subsection headings: ### ...
    #   - Blank lines
    lines = []
    for line in synthesis_raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('![['):
            continue  # transclusion ref — Obsidian-only, no inline text
        if stripped.startswith('###'):
            continue  # sub-heading (commentator name) — skip
        lines.append(stripped)

    return '\n'.join(lines) if lines else None


def build_verse_entry(block_id: str, sk_text: str) -> str:
    """
    Build the prompt block for a single verse, injecting rail synthesis
    if available.
    """
    m = re.match(r'\^(\d+)-(\d+)', block_id)
    if not m:
        return f"{block_id}:\n{sk_text}"

    ch_num, v_num = int(m.group(1)), int(m.group(2))
    synthesis = parse_rail_synthesis(ch_num, v_num)

    if synthesis:
        return (
            f"{block_id}:\n"
            f"Sanskrit root text:\n{sk_text}\n"
            f"Commentary synthesis (Tibetan):\n{synthesis}"
        )
    else:
        return f"{block_id}:\n{sk_text}"


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_chapters(source_text: str) -> dict[int, list[tuple[str, str]]]:
    """
    Returns {chapter_number: [(block_id, verse_text), ...]}
    Skips editorial notes and absent-verse markers.
    """
    chapters: dict[int, list[tuple[str, str]]] = {}
    current_ch = None

    # Match chapter headers like "## 1. बोधि..."
    ch_header = re.compile(r"^## (\d+)\.")

    # Match verse block IDs like ^1-1, ^2-33, ^3-2
    verse_end = re.compile(r"\^(\d+)-(\d+)\s*$")

    lines = source_text.splitlines()
    verse_lines: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect chapter change
        m = ch_header.match(line)
        if m:
            current_ch = int(m.group(1))
            if current_ch not in chapters:
                chapters[current_ch] = []
            verse_lines = []
            i += 1
            continue

        # Detect verse-end marker
        m = verse_end.search(line)
        if m and current_ch is not None:
            ch_num  = int(m.group(1))
            verse_n = int(m.group(2))
            block_id = f"^{ch_num}-{verse_n}"

            # Strip the block ID tag from the last line
            content_line = verse_end.sub("", line).strip()
            if content_line:
                verse_lines.append(content_line)

            full_verse = " ".join(verse_lines).strip()
            verse_lines = []

            # Skip editorial / absent-verse notes
            if "[Ed:" in full_verse or not full_verse:
                i += 1
                continue

            chapters.setdefault(current_ch, []).append((block_id, full_verse))
            i += 1
            continue

        # Accumulate verse lines
        if current_ch is not None and line.strip():
            # Skip markdown headers and comment lines
            if not line.startswith("#") and not line.startswith("---"):
                verse_lines.append(line.strip())

        i += 1

    return chapters


def read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def resolve_chapters(spec: str) -> list[int]:
    """Parse '1', '1-3', or 'all' into a list of chapter ints."""
    spec = spec.strip().lower()
    if spec == "all":
        return list(range(1, 11))
    if "-" in spec:
        a, b = spec.split("-", 1)
        return list(range(int(a), int(b) + 1))
    return [int(spec)]


# ---------------------------------------------------------------------------
# Claude translation call
# ---------------------------------------------------------------------------

def translate_chapter(
    ch_num: int,
    verses: list[tuple[str, str]],
    requirements: str,
    termbase: str,
) -> str:
    """Call Claude to translate a single chapter and return the markdown text."""
    try:
        import anthropic
    except ImportError:
        print("ERROR: 'anthropic' package not found. Run: pip install anthropic")
        sys.exit(1)

    client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from env

    title = CHAPTER_TITLES.get(ch_num, f"Chapter {ch_num}")

    # Build verse list, injecting rail synthesis where available
    rail_count = 0
    verse_entries = []
    for block_id, sk_text in verses:
        entry = build_verse_entry(block_id, sk_text)
        if "Commentary synthesis" in entry:
            rail_count += 1
        verse_entries.append(entry)

    verse_block = "\n\n".join(verse_entries)

    print(f"  Rail context loaded for {rail_count}/{len(verses)} verses.")

    system_prompt = f"""You are a skilled translator producing a plain-English Grade 8 translation
of Śāntideva's Bodhisattvacaryāvatāra from the Sanskrit.

## Style contract (requirements.md)
{requirements}

## Locked terminology (termbase.md)
{termbase}

## Your task
Translate the Sanskrit verses provided by the user into plain English following the style
contract exactly. For each verse:
- Output one prose paragraph (not poetry) per verse.
- Append the block ID (e.g. ^1-1) at the end of the paragraph, on the same line.
- Do not add any commentary, notes, or headings between verses.
- Do not transliterate any Sanskrit or Tibetan terms.
- Use the termbase for all locked terms.
- Target 15-20 words per sentence. Use active voice. Keep vocabulary simple.

## Using commentary context
For some verses a "Commentary synthesis (Tibetan)" block follows the Sanskrit. This
is a summary in Tibetan of what four traditional commentators say about that verse
(kunpal, ngulchu-thogmed, sabzang, prajnakaramati). Use it to resolve ambiguity in
the Sanskrit and to ensure the translation reflects the traditional understanding.
Do not translate the Tibetan directly — use it only as an interpretive guide.
If no synthesis block is present, translate from the Sanskrit alone.

Output ONLY the translated paragraphs with block IDs. Do not include a chapter header."""

    user_prompt = f"""Please translate the following {len(verses)} verses from Chapter {ch_num}
("{title}") of the Bodhisattvacaryāvatāra:

{verse_block}"""

    print(f"  Calling Claude for Chapter {ch_num} ({len(verses)} verses)...")

    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=8192,
        messages=[{"role": "user", "content": user_prompt}],
        system=system_prompt,
    )

    return message.content[0].text


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Translate BCA chapters to plain English.")
    parser.add_argument(
        "--chapter", "-c",
        default="1",
        help="Chapter number, range (e.g. 1-3), or 'all'",
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Output file path (default: auto-named in project root)",
    )
    args = parser.parse_args()

    # Read source files
    print("Reading source files...")
    source_text  = read_file(SOURCE_FILE)
    requirements = read_file(REQ_FILE)
    termbase     = read_file(TERM_FILE)

    # Parse all chapters from source
    print("Parsing Sanskrit verses...")
    all_chapters = parse_chapters(source_text)

    # Resolve which chapters to translate
    target_chapters = resolve_chapters(args.chapter)

    # Validate
    for ch in target_chapters:
        if ch not in all_chapters:
            print(f"WARNING: Chapter {ch} not found in source. Skipping.")
    target_chapters = [c for c in target_chapters if c in all_chapters]

    if not target_chapters:
        print("No valid chapters to translate. Exiting.")
        sys.exit(1)

    # Determine output path
    if args.output:
        out_path = args.output
    elif len(target_chapters) == 1:
        ch = target_chapters[0]
        out_path = os.path.join(OUTPUT_DIR, f"BCA-Chapter-{ch}-Plain-English.md")
    else:
        ch_range = f"{target_chapters[0]}-{target_chapters[-1]}"
        out_path = os.path.join(OUTPUT_DIR, f"BCA-Chapters-{ch_range}-Plain-English.md")

    # Build output document
    lines = [
        "# A Guide to the Bodhisattva's Way of Life",
        "### Plain English Translation (Grade 8)",
        "*Translated from the Sanskrit of Śāntideva, informed by Tibetan commentary*",
        "",
        "---",
        "",
    ]

    for ch_num in target_chapters:
        verses = all_chapters[ch_num]
        title  = CHAPTER_TITLES.get(ch_num, f"Chapter {ch_num}")

        print(f"\nTranslating Chapter {ch_num}: {title} ({len(verses)} verses)...")
        translated_body = translate_chapter(ch_num, verses, requirements, termbase)

        lines.append(f"## Chapter {ch_num}: {title}")
        lines.append("")
        lines.append(translated_body.strip())
        lines.append("")
        lines.append(f"_Thus ends Chapter {ch_num}: \"{title}.\"_")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Footer
    lines.append(
        "*Source: Sanskrit root text of the Bodhisattvacaryāvatāra by Śāntideva "
        f"({os.path.basename(SOURCE_FILE)}). Commentary context from 2-RAILS/Verses/ "
        "(Tibetan synthesis: kunpal, ngulchu-thogmed, sabzang, prajnakaramati). "
        "Translated at Grade 8 reading level following the en-plain-english style contract.*"
    )

    # Write output
    output_text = "\n".join(lines)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"\nDone! Output written to:\n  {out_path}")


if __name__ == "__main__":
    main()
