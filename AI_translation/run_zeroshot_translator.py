#!/usr/bin/env python3
"""
run_zeroshot_translator.py
==========================

Batch-run the AI_translation zero-shot path via Gemini.

Governed by AI_translation/skills/requirements.md (workspace contract) and
AI_translation/skills/zeroshot-translator.md (path skill). Output naming,
audience profiles, and structural invariants come from those docs — this
script is the mechanical runner, not a second source of policy.

Translates every file in a Tibetan (or other) split_chapters folder into a
target language guided by an audience profile under
AI_translation/audience_profile/.

Pacing note: requirements.md §3 requires one chapter per turn when an agent
runs the skill interactively. This batch script intentionally runs files in
parallel (no per-chapter approval gate) for unattended API jobs — use
--workers 1 if you want sequential file translation.

Usage (venv activated, from vault root):
    python AI_translation/run_zeroshot_translator.py \\
        --target-language english --audience-profile plain

    python AI_translation/run_zeroshot_translator.py \\
        --target-language hindi --audience-profile children --workers 6

    python AI_translation/run_zeroshot_translator.py \\
        --target-language english --audience-profile plain --resume

Requires GEMINI_API_KEY (or GOOGLE_API_KEY) in the environment or a vault-root
.env file. Install: pip install google-genai
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_TEXT_SLUG = "bca"
DEFAULT_WORKERS = 4
DEFAULT_SOURCE_GLOB = "bo-*_split_chapters"
DEFAULT_CHUNK_CHARS = 22000
DEFAULT_OVERLAP_LINES = 20
DEFAULT_MAX_OUTPUT_TOKENS = 65536
SOURCE_FILE_GLOBS = ("*.md", "frontmatter.txt")
LINE_BLOCK_ID_RE = re.compile(
    r"^(?P<body>.*?)[ \t]*\^(?P<id>[^\s^]+)\s*$"
)

AI_TRANSLATION_DIR = Path(__file__).resolve().parent
VAULT_ROOT = AI_TRANSLATION_DIR.parent
AUDIENCE_DIR = AI_TRANSLATION_DIR / "audience_profile"

LANG_TAGS = {
    "english": "en",
    "hindi": "hi",
    "marathi": "mr",
    "chinese": "zh",
    "tibetan": "bo",
    "sanskrit": "sk",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "nepali": "ne",
    "bhutanese": "dz",
}


# ---------------------------------------------------------------------------
# .env
# ---------------------------------------------------------------------------

def _load_dotenv() -> None:
    """Load a .env file — searches cwd, vault root, script dir (first found wins)."""
    candidates = [Path.cwd(), VAULT_ROOT, AI_TRANSLATION_DIR]
    for parent in Path.cwd().parents:
        if (parent / "4-SYSTEM").is_dir():
            candidates.append(parent)
            break

    seen: set[Path] = set()
    for base in candidates:
        base = base.resolve()
        if base in seen:
            continue
        seen.add(base)
        env_file = base / ".env"
        if not env_file.is_file():
            continue
        with open(env_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = val
        return


# ---------------------------------------------------------------------------
# Paths / inputs
# ---------------------------------------------------------------------------

def resolve_source_dir(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.is_dir():
            sys.exit(f"Error: source dir not found: {path}")
        return path.resolve()

    matches = sorted(AI_TRANSLATION_DIR.glob(DEFAULT_SOURCE_GLOB))
    matches = [p for p in matches if p.is_dir()]
    if not matches:
        sys.exit(
            f"Error: no default source folder matching "
            f"AI_translation/{DEFAULT_SOURCE_GLOB}"
        )
    if len(matches) > 1:
        listed = "\n  ".join(str(p.relative_to(VAULT_ROOT)) for p in matches)
        sys.exit(
            "Error: multiple source folders match the default glob; "
            f"pass --source-dir explicitly:\n  {listed}"
        )
    return matches[0]


def resolve_audience_profile(slug: str) -> tuple[str, Path, str]:
    slug = slug.strip().removesuffix(".md")
    path = AUDIENCE_DIR / f"{slug}.md"
    if not path.is_file():
        available = sorted(p.stem for p in AUDIENCE_DIR.glob("*.md"))
        sys.exit(
            f"Error: audience profile not found: {path}\n"
            f"  Available: {', '.join(available) or '(none)'}"
        )
    return slug, path, path.read_text(encoding="utf-8")


def list_source_files(source_dir: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in SOURCE_FILE_GLOBS:
        files.extend(source_dir.glob(pattern))
    # Dedupe + stable order: frontmatter, intro, chapters numeric, colophon, rest
    unique = {p.resolve(): p for p in files}
    paths = list(unique.values())

    def sort_key(p: Path) -> tuple[int, int, str]:
        name = p.name.lower()
        if name == "frontmatter.txt":
            return (0, 0, name)
        if name == "intro.md":
            return (1, 0, name)
        if name.startswith("ch") and name.endswith(".md"):
            num = name[2:-3]
            return (2, int(num) if num.isdigit() else 999, name)
        if name == "colophon.md":
            return (3, 0, name)
        return (4, 0, name)

    return sorted(paths, key=sort_key)


def output_dir_for(
    target_language: str,
    audience_slug: str,
    text_slug: str,
) -> Path:
    folder = (
        f"{text_slug}-{target_language}-{audience_slug}-zeroshot_split_chapters"
    )
    return AI_TRANSLATION_DIR / target_language / folder


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

# Structural / pacing / naming policy: AI_translation/skills/requirements.md
# Path-specific rules: AI_translation/skills/zeroshot-translator.md
# The audience profile body is supplied in the user prompt — do not invent register.
SYSTEM_INSTRUCTION = """\
You are a careful literary translator for Buddhist verse texts on the
AI_translation zero-shot path (no termbase).

Follow these invariants (from the workspace requirements):
- No termbase. Choose terminology with your best judgment; stay consistent
  within this file.
- Apply the audience profile in the user prompt exactly for register, style,
  explanatory latitude, and priority order. Do not invent a different register.
- Preserve every segment/block ID (e.g. ^1-1, ^I-3, ^a-0) exactly, in the same
  position as the source (typically at the end of the segment's last line).
  No renumbering, additions, or omissions.
- Per-segment line count must mirror the source: each target line carries its
  source line's content. Do not collapse verses into prose or word-wrap to hit
  a count. Atypical line counts (2 or 5 in a mostly-4 chapter) match that
  segment's own count.
- Separate consecutive segments with exactly one blank line (normalize even if
  the source uses two or more).
- No structural additions — no new sub-headers, no reordering, no filler, and
  nothing the source does not state (clarification only via word choice if the
  audience profile allows it).
- Preserve markdown heading markers (# ## ### ####).
- Preserve Obsidian/wiki links and transclusions (![[...]], [[...]]) byte-for-byte
  if present.
- Output ONLY the translated markdown/text for this file. No preamble, no
  commentary, no code fences.
"""


def build_user_prompt(
    *,
    source_text: str,
    filename: str,
    target_language: str,
    lang_tag: str,
    audience_slug: str,
    audience_body: str,
    preceding_context: str = "",
) -> str:
    frontmatter_extra = ""
    if filename.lower() == "frontmatter.txt":
        frontmatter_extra = f"""
FRONTMATTER RULES (this file only):
- Keep the YAML structure and every key name unchanged.
- Keep IDs and URLs unchanged (bdrc_work_id, text_id, edition_id, toc_id,
  category_id, source, license, verse_id_format, root_text, covers_verses).
- Translate human-readable string values where natural (e.g. title,
  source_description, translation_basis) into {target_language}.
- Set language to the English name "{target_language.capitalize()}" (or the
  conventional English language name) and lang_tag to "{lang_tag}".
- Keep translator names and BDRC person IDs as in the source.
"""

    context_block = ""
    if preceding_context.strip():
        context_block = f"""
=== PRECEDING CONTEXT (already translated — for continuity only;
DO NOT include any of this context in your output) ===
{preceding_context.rstrip()}
=== END PRECEDING CONTEXT ===
"""

    translate_note = (
        "Translate ONLY the SOURCE section below into "
        f"{target_language}. Do not repeat the preceding context. "
        "Return only the translated SOURCE section contents."
        if preceding_context.strip()
        else f"Translate the following source file into {target_language}. "
        "Return only the translated file contents."
    )

    return f"""\
TARGET LANGUAGE: {target_language}
AUDIENCE PROFILE SLUG: {audience_slug}
SOURCE FILENAME: {filename}

=== AUDIENCE PROFILE (follow closely) ===
{audience_body.strip()}
=== END AUDIENCE PROFILE ===
{frontmatter_extra}{context_block}
{translate_note}

=== SOURCE ===
{source_text}
=== END SOURCE ===
"""


def split_source_segments(text: str) -> list[str]:
    """Split text into verse/segment blocks ending at each trailing ^id line."""
    segments: list[str] = []
    buf: list[str] = []
    for line in text.splitlines():
        buf.append(line)
        if LINE_BLOCK_ID_RE.match(line):
            segments.append("\n".join(buf) + "\n")
            buf = []
    if buf:
        trailing = "\n".join(buf)
        if trailing.strip():
            # Keep trailing non-id text attached to last segment if possible
            if segments:
                segments[-1] = segments[-1].rstrip("\n") + "\n" + trailing + "\n"
            else:
                segments.append(trailing + "\n")
    return segments


def build_chunks(
    source_text: str,
    *,
    chunk_chars: int,
    overlap_lines: int,
) -> list[tuple[str, str]]:
    """
    Split source into (preceding_context, chunk_text) pairs.

    preceding_context is the last `overlap_lines` lines before this chunk
    (empty for the first chunk). chunk_text is the new material to translate.
    """
    if chunk_chars <= 0 or len(source_text) <= chunk_chars:
        return [("", source_text if source_text.endswith("\n") else source_text + "\n")]

    segments = split_source_segments(source_text)
    if len(segments) <= 1:
        return [("", source_text if source_text.endswith("\n") else source_text + "\n")]

    chunks: list[tuple[str, str]] = []
    i = 0
    n = len(segments)
    while i < n:
        start = i
        size = 0
        while i < n:
            seg_len = len(segments[i])
            if size > 0 and size + seg_len > chunk_chars:
                break
            size += seg_len
            i += 1
            # Always take at least one segment
            if size >= chunk_chars:
                break
        chunk_text = "".join(segments[start:i])
        if start == 0:
            context = ""
        else:
            prior = "".join(segments[:start])
            prior_lines = prior.splitlines()
            context = "\n".join(prior_lines[-overlap_lines:]) + "\n"
        chunks.append((context, chunk_text))
    return chunks


def strip_code_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


# ---------------------------------------------------------------------------
# Gemini
# ---------------------------------------------------------------------------

def make_client():
    try:
        from google import genai
    except ImportError:
        sys.exit(
            "Error: google-genai is not installed.\n"
            "  Activate your venv, then: pip install google-genai"
        )
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "Error: no API key found.\n"
            "  Set GEMINI_API_KEY (or GOOGLE_API_KEY), or put it in a .env "
            "file at the vault root."
        )
    return genai.Client(api_key=api_key)


def _call_gemini(
    client,
    *,
    model: str,
    prompt: str,
    temperature: float,
    max_retries: int,
    max_output_tokens: int,
) -> str:
    from google.genai import types

    config_kwargs: dict = {
        "system_instruction": SYSTEM_INSTRUCTION,
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
    }
    # Gemini 2.5: thinking_budget=0 disables thinking.
    # Gemini 3.x: thinking_budget is invalid / returns 400; use thinking_level.
    try:
        model_l = (model or "").lower()
        if model_l.startswith("gemini-3"):
            config_kwargs["thinking_config"] = types.ThinkingConfig(
                thinking_level="minimal"
            )
        else:
            config_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
    except Exception:  # noqa: BLE001
        pass

    config = types.GenerateContentConfig(**config_kwargs)
    last_err: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            resp = client.models.generate_content(
                model=model,
                contents=prompt,
                config=config,
            )
            text = strip_code_fences(getattr(resp, "text", None) or "")
            if not text:
                raise RuntimeError("empty response from Gemini")
            return text
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            time.sleep(min(60, 4 * attempt))
    raise RuntimeError(f"failed after {max_retries} tries: {last_err}")


def translate_one(
    client,
    *,
    model: str,
    source_path: Path,
    out_path: Path,
    target_language: str,
    lang_tag: str,
    audience_slug: str,
    audience_body: str,
    temperature: float,
    max_retries: int,
    chunk_chars: int = DEFAULT_CHUNK_CHARS,
    overlap_lines: int = DEFAULT_OVERLAP_LINES,
    max_output_tokens: int = DEFAULT_MAX_OUTPUT_TOKENS,
) -> tuple[str, bool, str]:
    """Returns (filename, ok, message)."""
    name = source_path.name
    source_text = source_path.read_text(encoding="utf-8")
    chunks = build_chunks(
        source_text,
        chunk_chars=chunk_chars,
        overlap_lines=overlap_lines,
    )

    try:
        parts: list[str] = []
        for idx, (context, chunk_text) in enumerate(chunks, 1):
            prompt = build_user_prompt(
                source_text=chunk_text,
                filename=name,
                target_language=target_language,
                lang_tag=lang_tag,
                audience_slug=audience_slug,
                audience_body=audience_body,
                preceding_context=context,
            )
            part = _call_gemini(
                client,
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_retries=max_retries,
                max_output_tokens=max_output_tokens,
            )
            if not part.endswith("\n"):
                part += "\n"
            parts.append(part)
            if len(chunks) > 1:
                print(
                    f"  chunk {idx}/{len(chunks)} for {name} "
                    f"({len(chunk_text)} chars, overlap_ctx={len(context.splitlines())} lines)",
                    file=sys.stderr,
                )

        text = "".join(parts)
        if not text.endswith("\n"):
            text += "\n"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text, encoding="utf-8")
        extra = f" ({len(chunks)} chunks)" if len(chunks) > 1 else ""
        return name, True, f"wrote {out_path}{extra}"
    except Exception as exc:  # noqa: BLE001
        return name, False, str(exc)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Batch-run AI_translation zero-shot path via Gemini. "
            "Governed by skills/requirements.md and skills/zeroshot-translator.md "
            "(parallel over split_chapters files; use --workers 1 for sequential)."
        )
    )
    p.add_argument(
        "--target-language",
        required=True,
        help="Target language folder name, e.g. english, hindi, marathi",
    )
    p.add_argument(
        "--audience-profile",
        required=True,
        help="Audience profile slug under AI_translation/audience_profile/ "
        "(e.g. plain, children, scholars)",
    )
    p.add_argument(
        "--source-dir",
        default=None,
        help=f"Split-chapters source folder "
        f"(default: sole AI_translation/{DEFAULT_SOURCE_GLOB})",
    )
    p.add_argument(
        "--text-slug",
        default=DEFAULT_TEXT_SLUG,
        help=f"Short text id for output folder name (default: {DEFAULT_TEXT_SLUG})",
    )
    p.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini model (default: {DEFAULT_MODEL})",
    )
    p.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Parallel workers (default: {DEFAULT_WORKERS})",
    )
    p.add_argument(
        "--temperature",
        type=float,
        default=0.3,
        help="Sampling temperature (default: 0.3)",
    )
    p.add_argument(
        "--max-retries",
        type=int,
        default=5,
        help="Retries per file on API errors (default: 5)",
    )
    p.add_argument(
        "--resume",
        action="store_true",
        help="Skip files that already have a non-empty output",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="List planned work without calling the API",
    )
    p.add_argument(
        "--only",
        nargs="+",
        metavar="FILE",
        help="Only translate these filenames (e.g. ch1.md intro.md)",
    )
    p.add_argument(
        "--chunk-chars",
        type=int,
        default=DEFAULT_CHUNK_CHARS,
        help=(
            f"Split source files longer than this many characters into "
            f"chunked Gemini calls (default: {DEFAULT_CHUNK_CHARS}; 0=disable)"
        ),
    )
    p.add_argument(
        "--overlap-lines",
        type=int,
        default=DEFAULT_OVERLAP_LINES,
        help=(
            f"Preceding source lines included as non-output context when "
            f"chunking (default: {DEFAULT_OVERLAP_LINES})"
        ),
    )
    p.add_argument(
        "--max-output-tokens",
        type=int,
        default=DEFAULT_MAX_OUTPUT_TOKENS,
        help=f"Gemini max_output_tokens (default: {DEFAULT_MAX_OUTPUT_TOKENS})",
    )
    return p.parse_args()


def _configure_stdio() -> None:
    """Avoid UnicodeEncodeError on Windows cp1252 consoles (Tibetan paths)."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                pass


def main() -> int:
    _configure_stdio()
    args = parse_args()
    _load_dotenv()

    target_language = args.target_language.strip().lower()
    audience_slug, audience_path, audience_body = resolve_audience_profile(
        args.audience_profile
    )
    source_dir = resolve_source_dir(args.source_dir)
    out_dir = output_dir_for(target_language, audience_slug, args.text_slug)
    lang_tag = LANG_TAGS.get(target_language, target_language[:2])

    files = list_source_files(source_dir)
    if args.only:
        wanted = {name.lower() for name in args.only}
        files = [f for f in files if f.name.lower() in wanted]
        missing = wanted - {f.name.lower() for f in files}
        if missing:
            sys.exit(f"Error: --only not found in source: {', '.join(sorted(missing))}")

    if not files:
        sys.exit(f"Error: no source files in {source_dir}")

    print(f"Source:    {source_dir}")
    print(f"Audience:  {audience_path}")
    print(f"Target:    {target_language} (lang_tag={lang_tag})")
    print(f"Output:    {out_dir}")
    print(f"Model:     {args.model}")
    print(f"Workers:   {args.workers}")
    print(f"Chunking:  chars>{args.chunk_chars} overlap_lines={args.overlap_lines}")
    print(f"Files:     {len(files)}")
    for f in files:
        print(f"  - {f.name}")

    todo: list[tuple[Path, Path]] = []
    for src in files:
        dest = out_dir / src.name
        if args.resume and dest.is_file() and dest.stat().st_size > 0:
            print(f"skip (resume): {src.name}")
            continue
        todo.append((src, dest))

    if not todo:
        print("Nothing to do.")
        return 0

    if args.dry_run:
        print(f"Dry run — would translate {len(todo)} file(s) in parallel.")
        return 0

    client = make_client()
    ok_count = 0
    fail_count = 0

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(
                translate_one,
                client,
                model=args.model,
                source_path=src,
                out_path=dest,
                target_language=target_language,
                lang_tag=lang_tag,
                audience_slug=audience_slug,
                audience_body=audience_body,
                temperature=args.temperature,
                max_retries=args.max_retries,
                chunk_chars=args.chunk_chars,
                overlap_lines=args.overlap_lines,
                max_output_tokens=args.max_output_tokens,
            ): src.name
            for src, dest in todo
        }
        for fut in as_completed(futures):
            name, ok, msg = fut.result()
            if ok:
                ok_count += 1
                print(f"OK  {name}: {msg}")
            else:
                fail_count += 1
                print(f"ERR {name}: {msg}", file=sys.stderr)

    print(f"Done. ok={ok_count} failed={fail_count} output={out_dir}")
    return 1 if fail_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
