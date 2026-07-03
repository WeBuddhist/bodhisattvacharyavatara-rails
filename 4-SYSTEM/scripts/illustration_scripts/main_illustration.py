"""Batch illustration generator using Gemini 3 Pro Image.

Parses a single Verse_and_challenge.md file, splits it by verse headings,
extracts verse/practice/explanation, and submits a batch image generation
job. Generates three illustrations per verse — one from the verse alone, one
from the practice + explanation, and one from all three combined — and saves
them into individual folders.
"""

import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from google.genai._gaos.types.interactions.vertexaisearchconfig import List
import numpy as np
from PIL import Image
from google import genai

TIBETAN_DIGITS = {
    "༠": 0, "༡": 1, "༢": 2, "༣": 3, "༤": 4,
    "༥": 5, "༦": 6, "༧": 7, "༨": 8, "༩": 9,
}

IMAGES_PER_VERSE = 3

_STYLE_BLOCK = """\
The line drawing illustration should be a Anand Pai comic illustration combined with features of "Madhubani art style".
The drawing is done exclusively as a heavy blue line drawing in monochrome blue line. \
The scene happens in a rural Indian village scene in Buddhist Bihar. \
The scene can show the buddha and bodhisattvas when relevant. \
The scene should be a single scene, with a clear action happening in the scene. \
The composition of the scene should be like a comic panel without text bubbles. \
Comic book spot illustration, plain white background. \
The drawing has no borders and is not busy."""

_RULES_BLOCK = """\
STRICT RULES — follow all of them without exception:
- NO text, letters, words, labels, captions, or inscriptions anywhere in the image. \
- The drawing is done exclusively with a 2mm drawing pen line in monochrome blue lines. \
- Don't use snakes of fishes in the trees.
- NO Hindu gods, goddesses, deities, or hindu iconography of any kind \
(no Ganesha, Krishna, Shiva, Durga, Hanuman, or any other deity).
- NO symbols associated with Hinduism. No bindu on people's foreheads.
- The scene must show only ordinary rural people of various ages, animals, nature, or everyday \
village life.
- The illustration should make people smile or gasp.
- The image has one single clear scene, with a clear action happening in the scene.
- The illustration shouldn't be in a square box. The image panel shouldn't have side borders.
"""

VERSE_PROMPT_TEMPLATE = f"""\
Let's illustrate a scene for a buddhist verse.

Generate exactly one single illustration. Do NOT create multiple scenes or a \
collage — just one clean image.

{_RULES_BLOCK}

Here's the verse to illustrate:

{{verse}}

Identify the main character(s) of the scene, and the action happening in the scene. \
Illustrate the main action and feeling evoked by the verse itself. 

{_STYLE_BLOCK}
"""

PRACTICE_PROMPT_TEMPLATE = f"""\
Let's illustrate a scene for a buddhist daily practice.

Generate exactly one single illustration. Do NOT create multiple scenes or a \
collage — just one clean image.

{_RULES_BLOCK}

Here's the practice and its explanation:

Practice: {{practice}}

Identify the main character(s) of the scene, and the action happening in the scene. \
The illustration should trigger the viewer to remember and perform the practice.

{_STYLE_BLOCK}
"""

COMBINED_PROMPT_TEMPLATE = f"""\
Let's illustrate a scene for a buddhist text.

Generate exactly one single illustration. Do NOT create multiple scenes or a \
collage — just one clean image.

{_RULES_BLOCK}

Here's the text to illustrate:

Verse: {{verse}}; Practice: {{practice}}; Explanation: {{explanation}}

Pick a common theme to the above texts to illustrate. \
Identify the main character(s) of the scene, and the action happening in the scene. \
The illustration should trigger the main feeling of the theme.

{_STYLE_BLOCK}
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


def make_background_transparent(
    image_path: Path,
    output_path: Path | None = None,
    threshold: int = 240,
) -> Path:
    """Replace near-white background pixels with transparency.

    Args:
        image_path: Path to the source PNG image.
        output_path: Where to save the result. Defaults to overwriting image_path.
        threshold: RGB channel minimum to consider a pixel as background (0-255).

    Returns:
        Path to the saved transparent image.
    """
    output_path = output_path or image_path
    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)

    rgb = data[:, :, :3]
    is_background = np.all(rgb > threshold, axis=2)
    data[is_background, 3] = 0

    Image.fromarray(data).save(output_path, "PNG")
    return output_path


def _make_request(prompt: str) -> dict:
    """Wrap a prompt string into a batch request entry."""
    return {
        "contents": [{"parts": [{"text": prompt}], "role": "user"}],
        "config": {
            "response_modalities": ["TEXT", "IMAGE"],
            "tools": [{"google_search": {}}],
            "image_config": {
                "aspect_ratio": "3:2",
                "image_size": "2K",
            },
        },
    }


def build_requests_for_verse(entry: VerseEntry) -> list[dict]:
    """Build three batch requests per verse: verse-only, practice-only, combined."""
    verse_prompt = VERSE_PROMPT_TEMPLATE.format(verse=entry.verse)
    practice_prompt = PRACTICE_PROMPT_TEMPLATE.format(
        practice=entry.practice,
    )
    combined_prompt = COMBINED_PROMPT_TEMPLATE.format(
        verse=entry.verse,
        practice=entry.practice,
        explanation=entry.explanation,
    )
    return [
        _make_request(verse_prompt),
        _make_request(practice_prompt),
        _make_request(combined_prompt),
    ]


def submit_batch(client: genai.Client, requests: list[dict]) -> str:
    """Submit inline batch job and return the job name."""
    batch_job = client.batches.create(
        model="gemini-3-pro-image-preview",
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


_PROMPT_LABELS = {0: "verse", 1: "practice", 2: "combined"}


def save_images(batch_job, verse_dirs: list[Path]) -> None:
    """Extract images from batch responses and save to verse folders.

    Responses are ordered as IMAGES_PER_VERSE consecutive entries per verse:
    index 0 → verse, index 1 → practice, index 2 → combined.
    """
    responses = batch_job.dest.inlined_responses

    for resp_idx, inline_response in enumerate(responses):
        verse_idx = resp_idx // IMAGES_PER_VERSE
        prompt_idx = resp_idx % IMAGES_PER_VERSE
        img_num = prompt_idx + 1
        label = _PROMPT_LABELS.get(prompt_idx, str(img_num))

        if verse_idx >= len(verse_dirs):
            break

        verse_dir = verse_dirs[verse_idx]

        if inline_response.error:
            print(f"  ERROR for {verse_dir.name} ({label}): {inline_response.error}")
            continue

        if not inline_response.response:
            print(f"  No response for {verse_dir.name} ({label})")
            continue

        for part in inline_response.response.candidates[0].content.parts:
            if part.inline_data:
                image = part.as_image()
                output_path = verse_dir / f"illustration_{img_num}.png"
                image.save(str(output_path))
                make_background_transparent(output_path)
                print(f"  Saved: {output_path} ({label})")
            elif part.text:
                text_path = verse_dir / "illustration_notes.txt"
                with text_path.open("a", encoding="utf-8") as f:
                    f.write(f"--- {label} ---\n{part.text}\n\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python illustrate.py <path/to/v2.md>")
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
    # main()

    verse_dirs = [
        Path("data/Verse10"), 
        Path("data/Verse13"), 
        Path("data/Verse14")
        ]
    for verse_dir in verse_dirs:
        img_paths = list(verse_dir.iterdir())
        print(f"Found {len(img_paths)} images in {verse_dir}")
        for img_path in img_paths:
            #convert imaage background to transparent by calling make_background_transparent
            make_background_transparent(img_path)
            print(f"  Saved: {img_path}")