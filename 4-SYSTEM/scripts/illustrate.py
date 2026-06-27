"""Batch illustration generator using Gemini 3 Pro Image.

Parses a single Verse_and_challenge.md file, splits it by verse headings,
extracts verse/practice/explanation, and submits a batch image generation
job. Saves three illustration variants per verse into individual folders.
"""

import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from google import genai

TIBETAN_DIGITS = {
    "༠": 0, "༡": 1, "༢": 2, "༣": 3, "༤": 4,
    "༥": 5, "༦": 6, "༧": 7, "༨": 8, "༩": 9,
}

SYSTEM_INSTRUCTION = (
    "You are a strict layout and style enforcer. Generate exactly ONE illustration "
    "image per request. The image must strictly follow these constraints:\n\n"
    "1. **The 75/25 Spatial Rule:** The upper 75% of the portrait canvas *must* be "
    "completely empty, showing nothing but the blank, cream-colored texture of rice "
    "paper. The illustration *must* be contained entirely within the bottom 25%.\n"
    "2. **Style Fidelity:** Execute a clean, unbusy fusion of Anand Pai\u2019s comic "
    "linework (dominant) with subtle Madhubani art accents (subdominant) in a single "
    "monochrome blue ink. No borders.\n"
    "3. **Single Image:** Output exactly one image. Do NOT combine multiple scenes, "
    "do NOT create a collage, grid, or tiled layout. One scene, one image."
)

IMAGES_PER_VERSE = 3

VARIATION_HINTS = [
    "Focus on a wide establishing shot of the village scene.",
    "Focus on a close-up of one or two characters in the scene.",
    "Focus on a symbolic or abstract interpretation of the theme.",
]

PROMPT_TEMPLATE = """\
Let's illustrate this:

Verse: {verse}; Practice: {practice}; Explanation: {explanation}

Pick one theme from the above text to illustrate. {variation_hint}

Generate exactly one single illustration. Do NOT create multiple scenes or a \
collage — just one clean image.

The illustration should be a fusion of mostly Anand Pai comic line illustration \
and a hint of "Madhubani art style" in monochrome blue line on rice paper drawing \
of a rural Indian village scene in bihar. The illustration is at the bottom of a \
portrait page, it covers less than a quarter of the page. The top of the page is \
empty for a quote. The drawing has no borders and is not busy.\
"""

POLL_INTERVAL_SECONDS = 30

COMPLETED_STATES = {
    "JOB_STATE_SUCCEEDED",
    "JOB_STATE_FAILED",
    "JOB_STATE_CANCELLED",
    "JOB_STATE_EXPIRED",
}


@dataclass
class VerseEntry:
    """Parsed content from one verse section of the markdown."""

    number: int
    verse: str
    practice: str
    explanation: str


def parse_tibetan_number(raw: str) -> int:
    """Convert Tibetan numeral string (e.g. ༡༤) to an integer."""
    digits = [str(TIBETAN_DIGITS[ch]) for ch in raw if ch in TIBETAN_DIGITS]
    if not digits:
        raise ValueError(f"No Tibetan digits found in: {raw!r}")
    return int("".join(digits))


def parse_verses(md_path: Path) -> list[VerseEntry]:
    """Split the markdown by verse headings and extract fields."""
    text = md_path.read_text(encoding="utf-8")

    heading_pattern = r"###\s*ཚིགས་བཅད་\s+([༠-༩]+)\s*།"
    headings = list(re.finditer(heading_pattern, text))

    if not headings:
        raise ValueError("No verse headings found in the markdown file")

    entries: list[VerseEntry] = []

    for idx, match in enumerate(headings):
        num = parse_tibetan_number(match.group(1))
        start = match.end()
        end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
        section = text[start:end]

        verse = _extract_verse(section)
        practice, explanation = _extract_english(section)

        entries.append(VerseEntry(
            number=num,
            verse=verse,
            practice=practice,
            explanation=explanation,
        ))

    return entries


def _extract_verse(section: str) -> str:
    """Extract the Tibetan verse lines (before the first **Tibetan** marker)."""
    match = re.search(r"^(.+?)(?=\*\*Tibetan)", section, re.DOTALL)
    return match.group(1).strip() if match else ""


def _extract_english(section: str) -> tuple[str, str]:
    """Extract English Practice/Action and Explanation from a section."""
    eng_match = re.search(
        r"\*\*English[:\s]*\*\*[:\s]*\n(.+?)(?=\*\*Hindi|\n---|\Z)",
        section,
        re.DOTALL,
    )
    if not eng_match:
        return "", ""

    eng_block = eng_match.group(1).strip()

    practice_match = re.search(
        r"\*\*(?:Practice|Action)\*\*[:\s]*(.+?)(?=\*\*Explanation|\Z)",
        eng_block,
        re.DOTALL,
    )
    practice = practice_match.group(1).strip() if practice_match else ""

    explanation_match = re.search(
        r"\*\*Explanation\*\*[:\s]*(.+?)$",
        eng_block,
        re.DOTALL,
    )
    explanation = explanation_match.group(1).strip() if explanation_match else ""

    return practice, explanation


def is_processed(verse_dir: Path) -> bool:
    """A verse is processed if illustration_1.png already exists."""
    return (verse_dir / "illustration_1.png").exists()


def build_requests_for_verse(entry: VerseEntry) -> list[dict]:
    """Build IMAGES_PER_VERSE batch request entries for one verse."""
    requests: list[dict] = []
    for var_idx in range(IMAGES_PER_VERSE):
        prompt = PROMPT_TEMPLATE.format(
            verse=entry.verse,
            practice=entry.practice,
            explanation=entry.explanation,
            variation_hint=VARIATION_HINTS[var_idx],
        )
        requests.append({
            "contents": [{"parts": [{"text": prompt}], "role": "user"}],
            "config": {
                "response_modalities": ["TEXT", "IMAGE"],
                "system_instruction": SYSTEM_INSTRUCTION,
                "tools": [{"google_search": {}}],
                "temperature": 1,
                "max_output_tokens": 32768,
                "top_p": 0.95,
            },
        })
    return requests


def submit_batch(client: genai.Client, requests: list[dict]) -> str:
    """Submit inline batch job and return the job name."""
    batch_job = client.batches.create(
        model="gemini-3-pro-image",
        src=requests,
        config={"display_name": "challenge-illustrations"},
    )
    print(f"Batch job created: {batch_job.name}")
    return batch_job.name


def poll_until_done(client: genai.Client, job_name: str):
    """Poll batch job until it reaches a terminal state."""
    while True:
        batch_job = client.batches.get(name=job_name)
        state = batch_job.state.name if hasattr(batch_job.state, "name") else str(batch_job.state)
        print(f"  Status: {state}")

        if state in COMPLETED_STATES:
            return batch_job

        time.sleep(POLL_INTERVAL_SECONDS)


def save_images(batch_job, verse_dirs: list[Path]) -> None:
    """Extract images from batch responses and save to verse folders.

    Responses are ordered as IMAGES_PER_VERSE consecutive entries per verse.
    """
    responses = batch_job.dest.inlined_responses

    for resp_idx, inline_response in enumerate(responses):
        verse_idx = resp_idx // IMAGES_PER_VERSE
        img_num = (resp_idx % IMAGES_PER_VERSE) + 1

        if verse_idx >= len(verse_dirs):
            break

        verse_dir = verse_dirs[verse_idx]

        if inline_response.error:
            print(f"  ERROR for {verse_dir.name} image {img_num}: {inline_response.error}")
            continue

        if not inline_response.response:
            print(f"  No response for {verse_dir.name} image {img_num}")
            continue

        for part in inline_response.response.candidates[0].content.parts:
            if part.inline_data:
                image = part.as_image()
                output_path = verse_dir / f"illustration_{img_num}.png"
                image.save(str(output_path))
                print(f"  Saved: {output_path}")
            elif part.text:
                text_path = verse_dir / "illustration_notes.txt"
                with text_path.open("a", encoding="utf-8") as f:
                    f.write(f"--- Variation {img_num} ---\n{part.text}\n\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python illustrate.py <path/to/Verse_and_challenge.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1]).resolve()
    if not md_path.is_file():
        print(f"Error: {md_path} is not a file")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_KEY")
    if not api_key:
        print("Error: GEMINI_KEY environment variable not set")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    entries = parse_verses(md_path)
    print(f"Parsed {len(entries)} verses from {md_path.name}")

    output_dir = md_path.parent
    unprocessed_dirs: list[Path] = []
    requests: list[dict] = []

    for entry in entries:
        verse_dir = output_dir / f"verse_{entry.number}"
        verse_dir.mkdir(exist_ok=True)

        if is_processed(verse_dir):
            print(f"  Skipping verse {entry.number} (already has illustrations)")
            continue

        print(f"  Verse {entry.number}: practice='{entry.practice[:60]}...'")
        unprocessed_dirs.append(verse_dir)
        requests.extend(build_requests_for_verse(entry))

    if not requests:
        print("All verses already processed. Nothing to do.")
        return

    print(f"\nSubmitting batch: {len(unprocessed_dirs)} verses, {len(requests)} requests...")
    job_name = submit_batch(client, requests)

    print("Polling for completion...")
    batch_job = poll_until_done(client, job_name)

    state = batch_job.state.name if hasattr(batch_job.state, "name") else str(batch_job.state)
    if state == "JOB_STATE_SUCCEEDED":
        print("\nBatch succeeded! Saving images...")
        save_images(batch_job, unprocessed_dirs)
        print("\nDone.")
    else:
        print(f"\nBatch job ended with state: {state}")
        if hasattr(batch_job, "error") and batch_job.error:
            print(f"Error: {batch_job.error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
