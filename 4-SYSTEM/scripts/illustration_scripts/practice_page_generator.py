"""Compose Bodhisattva Challenge social posts from a daily folder.

Each input folder should contain:
- A date markdown file (e.g. ``06_July.md``) with practice, verse, and verse id
- One illustration PNG (any filename except ``background.png``)

Usage::

    python compose.py path/to/06_July_folder
    python compose.py path/to/06_July.md path/to/illustration.png
"""

from __future__ import annotations

import calendar
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONTS_DIR = Path(__file__).parent / "fonts"
BACKGROUND_PATH = Path(__file__).parent / "data" / "background.png"
HANDLE = "@WeBuddhist"

COLOR_HEADER = "#6979A6"
COLOR_PRIMARY = "#183380"
COLOR_BODY = "#6C6B67"

CANVAS_SIZE = (1080, 1920)
TOP_Y = 54
MARGIN_X = 70
MAX_PRACTICE_WIDTH = 940
MAX_VERSE_WIDTH = 920
ILLUSTRATION_MAX_WIDTH = 900
ILLUSTRATION_MAX_HEIGHT = 620

FONT_LEAGUE_GOTHIC = FONTS_DIR / "LeagueGothic-Regular.otf"
FONT_INTER_BOLD = FONTS_DIR / "Inter-Bold.ttf"
FONT_INTER_REGULAR = FONTS_DIR / "Inter-Regular.ttf"
FONT_CORMORANT = FONTS_DIR / "CormorantGaramond-Regular.ttf"
FONT_CORMORANT_ITALIC = FONTS_DIR / "CormorantGaramond-Italic.ttf"

SIZE_HEADER = 108
SIZE_PRACTICE = 84
SIZE_VERSE = 52
SIZE_VERSE_ID = 52
SIZE_HANDLE = 24

LINE_GAP = 8
SECTION_GAP = 72
ILLUSTRATION_GAP = 23
POST_ILLUSTRATION_GAP = 92
BOTTOM_MARGIN = 50

MONTH_ABBR = {
    name.lower(): name[:3] for name in calendar.month_name[1:]
}
MONTH_ABBR.update(
    {name.lower(): name[:3] for name in calendar.month_abbr[1:]}
)


@dataclass
class ChallengeContent:
    """Parsed challenge text fields."""

    practice: str
    verse: str
    verse_id: str


@dataclass
class ChallengeDate:
    """Date extracted from a filename like ``06_July.md``."""

    day: int
    month: str

    @property
    def title(self) -> str:
        """Return the header title, e.g. ``JUL 6 BODHISATTVA CHALLENGE``."""
        month_abbr = MONTH_ABBR.get(self.month.lower(), self.month[:3]).upper()
        return f"{month_abbr} {self.day} BODHISATTVA CHALLENGE"


def parse_date_from_filename(path: Path) -> ChallengeDate:
    """Parse day and month from filenames like ``06_July.md``."""
    match = re.match(r"(\d{1,2})_(\w+)\.md$", path.name, re.IGNORECASE)
    if not match:
        raise ValueError(
            f"Expected date markdown named like 06_July.md, got: {path.name}"
        )

    day = int(match.group(1))
    month = match.group(2)
    if day < 1 or day > 31:
        raise ValueError(f"Invalid day in filename: {path.name}")
    if month.lower() not in MONTH_ABBR:
        raise ValueError(f"Unknown month in filename: {path.name}")

    return ChallengeDate(day=day, month=month)


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


def parse_challenge_md(md_path: Path) -> ChallengeContent:
    """Parse practice, verse, and verse id from a daily markdown file."""
    text = md_path.read_text(encoding="utf-8")

    practice = _extract_section(
        text,
        ("Practice of the day", "Practice of day", "Parctice of the day", "Practice"),
    )
    verse = _extract_section(text, ("Verse of the day", "Verse of day", "Verse"))
    verse_id = _extract_section(text, ("Verse id", "Verse ID", "Verse Id"))

    missing = [
        name
        for name, value in (
            ("practice", practice),
            ("verse", verse),
            ("verse id", verse_id),
        )
        if not value
    ]
    if missing:
        raise ValueError(
            f"Missing required field(s) in {md_path.name}: {', '.join(missing)}"
        )

    return ChallengeContent(practice=practice, verse=verse, verse_id=verse_id)


def find_illustration(folder: Path, md_path: Path) -> Path:
    """Find the illustration PNG in a daily folder."""
    candidates = sorted(
        path
        for path in folder.iterdir()
        if path.suffix.lower() == ".png"
        and path.name.lower() != "background.png"
        and not path.name.endswith("_challenge.png")
        and path.resolve() != BACKGROUND_PATH.resolve()
    )

    if not candidates:
        raise FileNotFoundError(f"No illustration PNG found in {folder}")

    if len(candidates) == 1:
        return candidates[0]

    preferred = [path for path in candidates if path != md_path.with_suffix(".png")]
    if len(preferred) == 1:
        return preferred[0]

    names = ", ".join(path.name for path in candidates)
    raise ValueError(f"Multiple illustration PNG files found in {folder}: {names}")


def _load_font(path: Path, size: float, *, index: int | None = None) -> ImageFont.FreeTypeFont:
    """Load a TrueType/OpenType font."""
    if not path.is_file():
        raise FileNotFoundError(f"Font not found: {path}")

    if index is None:
        return ImageFont.truetype(str(path), size)
    return ImageFont.truetype(str(path), size, index=index)


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


def _text_block_height(lines: list[str], font: ImageFont.FreeTypeFont) -> int:
    """Return total pixel height for a wrapped text block."""
    if not lines:
        return 0

    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    line_height = draw.textbbox((0, 0), "Ag", font=font)[3]
    return len(lines) * line_height + (len(lines) - 1) * LINE_GAP


def _draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    *,
    y: int,
    font: ImageFont.FreeTypeFont,
    fill: str,
    canvas_width: int,
) -> int:
    """Draw centered lines and return the y-position after the block."""
    if not lines:
        return y

    line_height = draw.textbbox((0, 0), "Ag", font=font)[3]
    for line in lines:
        width = draw.textbbox((0, 0), line, font=font)[2]
        x = (canvas_width - width) // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height + LINE_GAP

    return y


def _draw_left_aligned_block(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    *,
    y: int,
    font: ImageFont.FreeTypeFont,
    fill: str,
    canvas_width: int,
) -> tuple[int, int]:
    """Draw lines left-aligned as a centred block; return (y_after, block_right_x).

    All lines share the same left edge, computed so the widest line is centred
    on the canvas.  Returns the right x-coordinate of the widest line so
    callers can right-align the verse citation flush to the block.
    """
    if not lines:
        return y, canvas_width // 2

    line_height = draw.textbbox((0, 0), "Ag", font=font)[3]
    block_width = max(draw.textbbox((0, 0), line, font=font)[2] for line in lines)
    x = (canvas_width - block_width) // 2
    block_right = x + block_width

    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height + LINE_GAP

    return y, block_right


def _strip_panel_border(image: Image.Image) -> Image.Image:
    """Crop away a rectangular comic-panel border baked into an illustration.

    Scans only the outer 15% strip on each side for strong blue lines that
    span >50% of the image dimension.  This avoids mistaking interior art
    lines for frame borders.  If all four sides have such a line, the image
    is cropped to the inner content box.  Returns the image unchanged when
    no four-sided frame is detected.
    """
    import numpy as np

    arr = np.array(image.convert("RGB"))
    h, w = arr.shape[:2]
    edge = max(int(min(h, w) * 0.15), 20)

    def _is_blue(pixel: np.ndarray) -> bool:
        return int(pixel[2]) > 100 and int(pixel[0]) < 80

    # Scan only the edge strips for border lines
    top_candidates = [
        y for y in range(edge)
        if sum(1 for x in range(w) if _is_blue(arr[y, x])) / w > 0.5
    ]
    bottom_candidates = [
        y for y in range(h - edge, h)
        if sum(1 for x in range(w) if _is_blue(arr[y, x])) / w > 0.5
    ]
    left_candidates = [
        x for x in range(edge)
        if sum(1 for y in range(h) if _is_blue(arr[y, x])) / h > 0.5
    ]
    right_candidates = [
        x for x in range(w - edge, w)
        if sum(1 for y in range(h) if _is_blue(arr[y, x])) / h > 0.5
    ]

    if not top_candidates or not bottom_candidates or not left_candidates or not right_candidates:
        return image

    crop_left = max(left_candidates) + 1
    crop_top = max(top_candidates) + 1
    crop_right = min(right_candidates)
    crop_bottom = min(bottom_candidates)

    if crop_right <= crop_left or crop_bottom <= crop_top:
        return image

    return image.crop((crop_left, crop_top, crop_right, crop_bottom))


def _fit_illustration(image: Image.Image) -> Image.Image:
    """Resize an illustration to fit the layout bounds, stripping any panel border."""
    image = _strip_panel_border(image)
    width, height = image.size
    scale = min(
        ILLUSTRATION_MAX_WIDTH / width,
        ILLUSTRATION_MAX_HEIGHT / height,
        1.0,
    )
    if scale == 1.0:
        return image

    new_size = (int(width * scale), int(height * scale))
    return image.resize(new_size, Image.Resampling.LANCZOS)


def compose_challenge(
    content: ChallengeContent,
    challenge_date: ChallengeDate,
    illustration_path: Path,
    output_path: Path,
    *,
    background_path: Path = BACKGROUND_PATH,
) -> Path:
    """Compose the final challenge image and save it to ``output_path``."""
    canvas = Image.open(background_path).convert("RGBA").crop(
        (0, 0, CANVAS_SIZE[0], CANVAS_SIZE[1])
    )
    draw = ImageDraw.Draw(canvas)
    width, _height = canvas.size

    font_header = _load_font(FONT_LEAGUE_GOTHIC, SIZE_HEADER)
    font_practice = _load_font(FONT_INTER_BOLD, SIZE_PRACTICE)
    font_verse = _load_font(FONT_CORMORANT, SIZE_VERSE)
    font_verse_id = _load_font(FONT_CORMORANT_ITALIC, SIZE_VERSE_ID)
    font_handle = _load_font(FONT_INTER_REGULAR, SIZE_HANDLE)

    y = TOP_Y

    title = challenge_date.title
    title_width = draw.textbbox((0, 0), title, font=font_header)[2]
    draw.text(
        ((width - title_width) // 2, y),
        title,
        font=font_header,
        fill=COLOR_HEADER,
    )
    y += draw.textbbox((0, 0), title, font=font_header)[3] + SECTION_GAP

    practice_lines = _wrap_text(content.practice, font_practice, MAX_PRACTICE_WIDTH)
    y = _draw_centered_lines(
        draw,
        practice_lines,
        y=y,
        font=font_practice,
        fill=COLOR_PRIMARY,
        canvas_width=width,
    )
    y += ILLUSTRATION_GAP

    illustration = _fit_illustration(Image.open(illustration_path).convert("RGBA"))
    illu_x = (width - illustration.width) // 2
    canvas.paste(illustration, (illu_x, y), illustration)
    y += illustration.height + POST_ILLUSTRATION_GAP

    verse_lines = _wrap_text(content.verse, font_verse, MAX_VERSE_WIDTH)
    y, block_right = _draw_left_aligned_block(
        draw,
        verse_lines,
        y=y,
        font=font_verse,
        fill=COLOR_BODY,
        canvas_width=width,
    )
    y += 12

    verse_id_width = draw.textbbox((0, 0), content.verse_id, font=font_verse_id)[2]
    draw.text(
        (block_right - verse_id_width, y),
        content.verse_id,
        font=font_verse_id,
        fill=COLOR_BODY,
    )
    y += _text_block_height([content.verse_id], font_verse_id) + SECTION_GAP

    handle_y = canvas.height - BOTTOM_MARGIN - SIZE_HANDLE
    draw.text((MARGIN_X, handle_y), HANDLE, font=font_handle, fill=COLOR_PRIMARY)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output_path, "PNG")
    return output_path


def resolve_inputs(
    arg1: Path,
    arg2: Path | None = None,
) -> tuple[Path, Path, Path]:
    """Resolve markdown, illustration, and output paths from CLI arguments."""
    if arg2 is not None:
        md_path = arg1
        illustration_path = arg2
        output_path = md_path.with_name(f"{md_path.stem}_challenge.png")
        return md_path, illustration_path, output_path

    folder = arg1
    md_files = sorted(folder.glob("*_*.md"))
    if not md_files:
        raise FileNotFoundError(
            f"No date markdown file like 06_July.md found in {folder}"
        )
    if len(md_files) > 1:
        names = ", ".join(path.name for path in md_files)
        raise ValueError(f"Multiple date markdown files found in {folder}: {names}")

    md_path = md_files[0]
    illustration_path = find_illustration(folder, md_path)
    output_path = folder / f"{md_path.stem}_challenge.png"
    return md_path, illustration_path, output_path


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) not in {2, 3}:
        print(
            "Usage:\n"
            "  python compose.py <folder>\n"
            "  python compose.py <06_July.md> <illustration.png>"
        )
        sys.exit(1)

    arg1 = Path(sys.argv[1]).resolve()
    arg2 = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else None

    try:
        md_path, illustration_path, output_path = resolve_inputs(arg1, arg2)
        content = parse_challenge_md(md_path)
        challenge_date = parse_date_from_filename(md_path)
        result = compose_challenge(
            content,
            challenge_date,
            illustration_path,
            output_path,
        )
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print(f"Created: {result}")


if __name__ == "__main__":
    main()
