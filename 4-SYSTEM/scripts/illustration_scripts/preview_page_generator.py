"""Generate a daily post image matching the data/17.jpg template.

Layout (top to bottom on a white 1080×1920 canvas):

1. Verse of the day — bold sans-serif, dark blue, centred
2. Verse explanation — serif body text, grey, centred
3. Illustration — blue line art, bottom-anchored

Reads content from a daily folder (e.g. ``data/06_July/``) containing a date
markdown file and one illustration PNG.

Usage::

    python generate_day.py data/06_July
    python generate_day.py data/06_July/06_july.md data/06_July/illustration_2.png
    python generate_day.py data/06_July --compare data/17.jpg
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from compose import find_illustration, parse_date_from_filename

FONTS_DIR = Path(__file__).parent / "fonts"

CANVAS_SIZE = (1080, 1920)
COLOR_PRIMARY = "#183380"
COLOR_BODY = "#4D4C4A"

TOP_Y = 80
BOTTOM_MARGIN = 105
ILLUSTRATION_MAX_WIDTH = 900
ILLUSTRATION_HEIGHT = 640
ILLUSTRATION_GAP = 100

MAX_VERSE_WIDTH = 920
MAX_EXPLANATION_WIDTH = 860

SIZE_VERSE = 90
SIZE_EXPLANATION = 78

VERSE_LINE_GAP = 14
EXPLANATION_LINE_GAP = 10
SECTION_GAP = 85

FONT_INTER_BOLD = FONTS_DIR / "Inter-Bold.ttf"
FONT_CORMORANT = FONTS_DIR / "CormorantGaramond-Regular.ttf"


@dataclass
class DayContent:
    """Parsed daily post text fields."""

    verse: str
    explanation: str


def _extract_section(text: str, labels: tuple[str, ...]) -> str:
    """Extract content under a markdown heading or bold label."""
    label_pattern = "|".join(re.escape(label) for label in labels)
    patterns = [
        rf"(?:^|\n)#{{1,3}}\s*(?:{label_pattern})\s*\n+(.+?)(?=\n#{{1,3}}\s|\Z)",
        rf"\*\*(?:{label_pattern})\*\*[:\s]*\n?(.+?)(?=\n\*\*|\Z)",
        rf"(?:^|\n)(?:{label_pattern})[:\s]+\n?(.+?)(?=\n(?:#{{1,3}}|\*\*|[A-Za-z ]+ of the day)|\Z)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()

    return ""


def parse_day_md(md_path: Path) -> DayContent:
    """Parse verse and explanation fields from a daily markdown file."""
    text = md_path.read_text(encoding="utf-8")

    verse = _extract_section(
        text,
        (
            "Practice of the day",
            "Practice of day",
            "Parctice of the day",
            "Practice",
            "Verse of the day",
            "Verse of day",
            "Verse",
        ),
    )
    explanation = _extract_section(
        text,
        (
            "Practice Explaination",
            "Practice Explanation",
            "Verse explanation",
            "Verse Explanation",
            "Explanation",
        ),
    )

    missing = [
        name
        for name, value in (("verse of the day", verse), ("explanation", explanation))
        if not value
    ]
    if missing:
        raise ValueError(
            f"Missing required field(s) in {md_path.name}: {', '.join(missing)}"
        )

    return DayContent(verse=verse, explanation=explanation)


def _load_font(path: Path, size: float) -> ImageFont.FreeTypeFont:
    """Load a TrueType/OpenType font."""
    if not path.is_file():
        raise FileNotFoundError(f"Font not found: {path}")
    return ImageFont.truetype(str(path), size)


def _wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    """Wrap text to fit within ``max_width``."""
    words = text.split()
    if not words:
        return []

    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    lines: list[str] = []
    current: list[str] = []

    for word in words:
        candidate = " ".join(current + [word])
        width = draw.textbbox((0, 0), candidate, font=font)[2]
        if width <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]

    if current:
        lines.append(" ".join(current))

    return lines


def _line_height(font: ImageFont.FreeTypeFont) -> int:
    """Return the pixel height of one line for ``font``."""
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    return draw.textbbox((0, 0), "Ag", font=font)[3]


def _block_height(lines: list[str], font: ImageFont.FreeTypeFont, line_gap: int) -> int:
    """Return total pixel height for a wrapped text block."""
    if not lines:
        return 0
    return len(lines) * _line_height(font) + (len(lines) - 1) * line_gap


def _draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    *,
    y: int,
    font: ImageFont.FreeTypeFont,
    fill: str,
    canvas_width: int,
    line_gap: int,
) -> int:
    """Draw centred lines and return the y-position after the block."""
    if not lines:
        return y

    line_height = _line_height(font)
    for line in lines:
        width = draw.textbbox((0, 0), line, font=font)[2]
        x = (canvas_width - width) // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height + line_gap

    return y


def _fit_illustration(image: Image.Image) -> Image.Image:
    """Scale an illustration to fit within template bounds, preserving aspect ratio."""
    img_w, img_h = image.size
    scale = min(ILLUSTRATION_MAX_WIDTH / img_w, ILLUSTRATION_HEIGHT / img_h)
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    return image.resize((new_w, new_h), Image.Resampling.LANCZOS)


def _layout_text(
    content: DayContent,
    *,
    verse_size: float = SIZE_VERSE,
    explanation_size: float = SIZE_EXPLANATION,
    verse_width: int = MAX_VERSE_WIDTH,
    explanation_width: int = MAX_EXPLANATION_WIDTH,
) -> tuple[list[str], list[str], ImageFont.FreeTypeFont, ImageFont.FreeTypeFont, int]:
    """Wrap text and compute y-offset, shrinking fonts if content overflows.

    Text always starts at ``TOP_Y``.  If the block is too tall to clear the
    illustration, font sizes are reduced by 2px and layout is retried.
    """
    font_verse = _load_font(FONT_INTER_BOLD, verse_size)
    font_explanation = _load_font(FONT_CORMORANT, explanation_size)

    verse_lines = _wrap_text(content.verse, font_verse, verse_width)
    explanation_lines = _wrap_text(content.explanation, font_explanation, explanation_width)

    illustration_y = CANVAS_SIZE[1] - BOTTOM_MARGIN - ILLUSTRATION_HEIGHT
    text_target_bottom = illustration_y - ILLUSTRATION_GAP
    block_height = (
        _block_height(verse_lines, font_verse, VERSE_LINE_GAP)
        + SECTION_GAP
        + _block_height(explanation_lines, font_explanation, EXPLANATION_LINE_GAP)
    )
    start_y = TOP_Y
    text_bottom = start_y + block_height

    if text_bottom > text_target_bottom:
        if verse_size > 48 or explanation_size > 32:
            return _layout_text(
                content,
                verse_size=verse_size - 2,
                explanation_size=explanation_size - 2,
                verse_width=verse_width,
                explanation_width=explanation_width,
            )
        raise ValueError("Daily text is too long for the template layout")

    return verse_lines, explanation_lines, font_verse, font_explanation, start_y


def generate_day_image(
    content: DayContent,
    illustration_path: Path,
    output_path: Path,
) -> Path:
    """Compose the daily post image and save it to ``output_path``."""
    canvas = Image.new("RGB", CANVAS_SIZE, "white")
    draw = ImageDraw.Draw(canvas)
    width, _height = canvas.size

    verse_lines, explanation_lines, font_verse, font_explanation, y = _layout_text(
        content
    )

    y = _draw_centered_lines(
        draw,
        verse_lines,
        y=y,
        font=font_verse,
        fill=COLOR_PRIMARY,
        canvas_width=width,
        line_gap=VERSE_LINE_GAP,
    )
    y += SECTION_GAP
    _draw_centered_lines(
        draw,
        explanation_lines,
        y=y,
        font=font_explanation,
        fill=COLOR_BODY,
        canvas_width=width,
        line_gap=EXPLANATION_LINE_GAP,
    )

    illustration = _fit_illustration(Image.open(illustration_path).convert("RGBA"))
    illustration_x = (width - illustration.width) // 2
    illustration_y = CANVAS_SIZE[1] - BOTTOM_MARGIN - illustration.height
    canvas.paste(illustration, (illustration_x, illustration_y), illustration)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=95)
    return output_path


def compare_with_reference(generated_path: Path, reference_path: Path) -> float:
    """Return mean absolute pixel difference against a reference image."""
    import numpy as np

    generated = np.array(Image.open(generated_path).convert("RGB"), dtype=float)
    reference = np.array(Image.open(reference_path).convert("RGB"), dtype=float)
    if generated.shape != reference.shape:
        raise ValueError(
            f"Size mismatch: generated {generated.shape[:2]}, "
            f"reference {reference.shape[:2]}"
        )
    return float(np.abs(generated - reference).mean())


def resolve_inputs(
    arg1: Path,
    arg2: Path | None = None,
) -> tuple[Path, Path, Path]:
    """Resolve markdown, illustration, and output paths from CLI arguments."""
    if arg2 is not None:
        md_path = arg1
        illustration_path = arg2
        output_path = md_path.with_name(f"{md_path.stem}_generated.jpg")
        return md_path, illustration_path, output_path

    folder = arg1
    md_files = sorted(folder.glob("*_*.md"))
    if not md_files:
        raise FileNotFoundError(
            f"No date markdown file like 06_july.md found in {folder}"
        )
    if len(md_files) > 1:
        names = ", ".join(path.name for path in md_files)
        raise ValueError(f"Multiple date markdown files found in {folder}: {names}")

    md_path = md_files[0]
    illustration_path = find_illustration(folder, md_path)
    output_path = folder / f"{md_path.stem}_generated.jpg"
    return md_path, illustration_path, output_path


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate a daily post image (17.jpg template)."
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Daily folder or markdown file",
    )
    parser.add_argument(
        "illustration",
        nargs="?",
        type=Path,
        help="Illustration PNG (required when input is a markdown file)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output image path (default: <date>_generated.jpg in the folder)",
    )
    parser.add_argument(
        "--compare",
        type=Path,
        metavar="REFERENCE",
        help="Compare output to a reference image and print MAE",
    )
    args = parser.parse_args()

    arg1 = args.input.resolve()
    arg2 = args.illustration.resolve() if args.illustration else None

    try:
        md_path, illustration_path, output_path = resolve_inputs(arg1, arg2)
        if args.output:
            output_path = args.output.resolve()

        content = parse_day_md(md_path)
        parse_date_from_filename(md_path)
        result = generate_day_image(content, illustration_path, output_path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Created: {result}")

    if args.compare:
        mae = compare_with_reference(result, args.compare.resolve())
        print(f"Reference MAE: {mae:.2f} (lower is closer to template)")


if __name__ == "__main__":
    main()
