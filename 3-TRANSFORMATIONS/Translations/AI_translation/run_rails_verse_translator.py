#!/usr/bin/env python3
"""
run_rails_verse_translator.py
=============================

Sequential Gemini runner for the AI_translation rails-verse-translator skill.

Governed by AI_translation/skills/requirements.md (workspace contract) and
AI_translation/skills/rails-verse-translator.md (path skill). Output naming,
audience profiles, structural invariants, and merged-file frontmatter come
from those docs — this script is the mechanical runner, not a second source
of policy.

Unlike run_zeroshot_translator.py, chapters are always processed one at a
time in source order (no parallel workers), matching requirements.md §3.

Required inputs:
    --source-dir          split_chapters source folder
    --termbase            locked termbase markdown file
    --audience-profile    slug under AI_translation/audience_profile/
    --target-language     full language name (english, hindi, …)

Writes per-unit files under:
    AI_translation/<lang>/<text>-<lang>-<level>_rails_split_chapters/
then merges (CRLF, single blank line between units) into:
    AI_translation/<lang>/<text>-<lang>-<level>.md

Usage (venv activated, from vault root):
    python AI_translation/run_rails_verse_translator.py \\
        --source-dir AI_translation/bo-བློ་ལྡན་ཤེས་རབ།_split_chapters \\
        --termbase AI_translation/english/tibetan-english-termbase-plain.md \\
        --audience-profile plain \\
        --target-language english

    python AI_translation/run_rails_verse_translator.py \\
        --source-dir … --termbase … --audience-profile plain \\
        --target-language english --resume

    python AI_translation/run_rails_verse_translator.py \\
        --source-dir … --termbase … --audience-profile plain \\
        --target-language english --merge-only

Requires GEMINI_API_KEY (or GOOGLE_API_KEY) in the environment or a vault-root
.env file. Install: pip install google-genai
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path

DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_TEXT_SLUG = "bca"
DEFAULT_CHUNK_CHARS = 22000
DEFAULT_OVERLAP_LINES = 20
DEFAULT_MAX_OUTPUT_TOKENS = 65536
SOURCE_FILE_GLOBS = ("*.md",)
# frontmatter.txt is not part of the rails merged body; YAML is generated.
LINE_BLOCK_ID_RE = re.compile(
    r"^(?P<body>.*?)[ \t]*\^(?P<id>[^\s^]+)\s*$"
)
TERMBASE_FLAG_RE = re.compile(r"<!--\s*rails-termbase-flag:.*?-->", re.I | re.S)

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

def _resolve_existing_path(explicit: str, *, what: str) -> Path:
    path = Path(explicit)
    if not path.is_absolute():
        candidates = [
            Path.cwd() / path,
            AI_TRANSLATION_DIR / path,
            VAULT_ROOT / path,
        ]
        for cand in candidates:
            if cand.is_file() or cand.is_dir():
                return cand.resolve()
        path = (Path.cwd() / path).resolve()
    else:
        path = path.resolve()
    if not path.exists():
        sys.exit(f"Error: {what} not found: {path}")
    return path


def resolve_source_dir(explicit: str) -> Path:
    path = _resolve_existing_path(explicit, what="source dir")
    if not path.is_dir():
        sys.exit(f"Error: source dir is not a directory: {path}")
    return path


def resolve_termbase(explicit: str) -> Path:
    path = _resolve_existing_path(explicit, what="termbase")
    if not path.is_file():
        sys.exit(f"Error: termbase is not a file: {path}")
    return path


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
    unique = {p.resolve(): p for p in files}
    paths = list(unique.values())

    def sort_key(p: Path) -> tuple[int, int, str]:
        name = p.name.lower()
        if name == "intro.md":
            return (1, 0, name)
        if name.startswith("ch") and name.endswith(".md"):
            num = name[2:-3]
            return (2, int(num) if num.isdigit() else 999, name)
        if name == "colophon.md":
            return (3, 0, name)
        return (4, 0, name)

    return sorted(paths, key=sort_key)


def work_dir_for(
    target_language: str,
    audience_slug: str,
    text_slug: str,
) -> Path:
    folder = f"{text_slug}-{target_language}-{audience_slug}_rails_split_chapters"
    return AI_TRANSLATION_DIR / target_language / folder


def merged_path_for(
    target_language: str,
    audience_slug: str,
    text_slug: str,
) -> Path:
    name = f"{text_slug}-{target_language}-{audience_slug}.md"
    return AI_TRANSLATION_DIR / target_language / name


def rel_from_vault(path: Path) -> str:
    try:
        return path.resolve().relative_to(VAULT_ROOT).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def audience_one_liner(audience_body: str) -> str:
    """First non-empty prose line after an Audience heading, else first prose line."""
    lines = [ln.strip() for ln in audience_body.splitlines()]
    after_audience = False
    for ln in lines:
        if ln.lower().startswith("## audience"):
            after_audience = True
            continue
        if after_audience:
            if not ln or ln.startswith("#") or ln.startswith("---"):
                if ln.startswith("##"):
                    break
                continue
            return ln.rstrip(".")
    for ln in lines:
        if ln and not ln.startswith("#") and not ln.startswith("---") and not ln.startswith("*"):
            return ln.rstrip(".")
    return "see audience profile"


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

# Structural / naming / merge policy: AI_translation/skills/requirements.md
# Path rules: AI_translation/skills/rails-verse-translator.md
SYSTEM_INSTRUCTION = """\
You are a careful literary translator for Buddhist verse texts on the
AI_translation rails path (locked termbase).

Follow these rules (from the workspace requirements + rails-verse-translator):
- Translate FRESH from the source. Do not copy, lightly adapt, or structurally
  validate a prior zero-shot or any other existing translation.
- Use the LOCKED TERMBASE in the user prompt for terminology. Exactly one
  rendering per sense — apply the listed term for that sense. Do not invent
  synonyms for locked terms.
- If a termbase entry genuinely cannot fit a specific context, still render
  with the closest locked term and append ON ITS OWN LINE after that segment:
  <!-- rails-termbase-flag: SOURCE_LEMMA — brief reason -->
  Do not quietly invent a different rendering.
- Apply the audience profile in the user prompt exactly for register, style,
  explanatory latitude, and priority order.
- Preserve every segment/block ID (e.g. ^1-1, ^I-3, ^a-0) exactly, in the same
  position as the source (typically at the end of the segment's last line).
  No renumbering, additions, or omissions.
- Per-segment line count must mirror the source: each target line carries its
  source line's content. Do not collapse verses into prose or word-wrap to hit
  a count. Atypical line counts match that segment's own count.
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
    audience_slug: str,
    audience_body: str,
    termbase_body: str,
    preceding_context: str = "",
) -> str:
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
        f"{target_language}, applying the locked termbase. "
        "Do not repeat the preceding context. "
        "Return only the translated SOURCE section contents."
        if preceding_context.strip()
        else (
            f"Translate the following source file into {target_language}, "
            "applying the locked termbase term by term. "
            "Return only the translated file contents."
        )
    )

    return f"""\
TARGET LANGUAGE: {target_language}
AUDIENCE PROFILE SLUG: {audience_slug}
SOURCE FILENAME: {filename}
TRANSLATION APPROACH: rails (termbase-locked; translate fresh from source)

=== AUDIENCE PROFILE (follow closely) ===
{audience_body.strip()}
=== END AUDIENCE PROFILE ===

=== LOCKED TERMBASE (authoritative for terminology) ===
{termbase_body.strip()}
=== END LOCKED TERMBASE ===
{context_block}
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
    audience_slug: str,
    audience_body: str,
    termbase_body: str,
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
                audience_slug=audience_slug,
                audience_body=audience_body,
                termbase_body=termbase_body,
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
                    f"({len(chunk_text)} chars, "
                    f"overlap_ctx={len(context.splitlines())} lines)",
                    file=sys.stderr,
                )

        text = "".join(parts)
        if not text.endswith("\n"):
            text += "\n"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # Per-chapter work files: LF is fine; merge step emits CRLF.
        out_path.write_text(text, encoding="utf-8", newline="\n")

        flags = TERMBASE_FLAG_RE.findall(text)
        flag_note = f"; termbase flags={len(flags)}" if flags else ""
        extra = f" ({len(chunks)} chunks)" if len(chunks) > 1 else ""
        return name, True, f"wrote {out_path}{extra}{flag_note}"
    except Exception as exc:  # noqa: BLE001
        return name, False, str(exc)


# ---------------------------------------------------------------------------
# Merge (spacing / line breaks)
# ---------------------------------------------------------------------------

def normalize_unit_body(text: str) -> str:
    """
    Normalize one chapter body for merge:
    - unify newlines to \\n
    - strip leading/trailing blank lines
    - collapse 3+ consecutive blank lines inside to a single blank line
      (segment spacing should already be one blank; this cleans model drift
      and chapter-end padding without joining segments)
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    out: list[str] = []
    blank_run = 0
    for ln in lines:
        if not ln.strip():
            blank_run += 1
            if blank_run == 1:
                out.append("")
            # drop extra blanks beyond one
            continue
        blank_run = 0
        out.append(ln.rstrip())
    return "\n".join(out)


def extract_title(intro_body: str, target_language: str) -> str:
    for ln in normalize_unit_body(intro_body).split("\n"):
        m = re.match(r"^#\s+(.+?)(?:\s+\^[^\s]+)?\s*$", ln)
        if m:
            return m.group(1).strip()
    return f"Bodhisattvacaryāvatāra ({target_language})"


def build_merged_frontmatter(
    *,
    title: str,
    source_dir: Path,
    target_language: str,
    lang_tag: str,
    audience_path: Path,
    audience_summary: str,
    termbase_path: Path,
) -> str:
    source_rel = rel_from_vault(source_dir)
    audience_rel = rel_from_vault(audience_path)
    termbase_rel = rel_from_vault(termbase_path)
    # YAML-ish: keep paths bare; quote the parenthetical summary.
    summary = audience_summary.replace('"', "'")
    return (
        "---\n"
        f"title: {title}\n"
        f"source_text: {source_rel}/\n"
        f"target_language: {target_language}\n"
        f"language: {target_language.capitalize()}\n"
        f"lang_tag: {lang_tag}\n"
        f"file_type: translation\n"
        f"verse_id_format: chapter-verse\n"
        f'audience_profile: {audience_rel} ("{summary}")\n'
        f"termbase: {termbase_rel}\n"
        "translation_approach: rails\n"
        "segment_id_coverage: >\n"
        "  Every segment ID present in the source chapters (intro.md,\n"
        "  ch1.md–ch10.md, colophon.md) is intended to be present here with\n"
        "  matching per-segment line counts; re-verify after merge\n"
        "  (requirements.md §7 / lint_translation.py).\n"
        "license: public\n"
        "---\n"
    )


def merge_units(
    *,
    ordered_bodies: list[tuple[str, str]],
    frontmatter: str,
) -> str:
    """
    Concatenate units with exactly one blank line between them, then CRLF.

    ordered_bodies: list of (filename, body). Frontmatter.txt is never included.
    """
    normalized: list[str] = []
    for name, body in ordered_bodies:
        if name.lower() == "frontmatter.txt":
            continue
        unit = normalize_unit_body(body)
        if unit:
            normalized.append(unit)

    if not normalized:
        raise ValueError("nothing to merge — all unit bodies empty")

    # Exactly one blank line between chapter units (not zero, not two+).
    body = "\n\n".join(normalized)
    fm = frontmatter.replace("\r\n", "\n").replace("\r", "\n")
    if not fm.endswith("\n"):
        fm += "\n"
    # One blank line between closing --- and first content line is standard YAML
    # frontmatter style only if body doesn't already start with blank — body
    # starts with content; a single newline after --- is enough (no extra blank).
    merged_lf = fm + "\n" + body
    if not merged_lf.endswith("\n"):
        merged_lf += "\n"
    # requirements.md §7: merged translation files use CRLF
    return merged_lf.replace("\n", "\r\n")


def write_merged_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Write bytes to preserve CRLF on all platforms (avoid text-mode newline rewrite).
    path.write_bytes(content.encode("utf-8"))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Sequentially run AI_translation rails-verse-translator via Gemini. "
            "Governed by skills/requirements.md and skills/rails-verse-translator.md."
        )
    )
    p.add_argument(
        "--source-dir",
        required=True,
        help="Split-chapters source folder (intro.md, ch1.md, …, colophon.md)",
    )
    p.add_argument(
        "--termbase",
        required=True,
        help="Path to the locked termbase markdown file",
    )
    p.add_argument(
        "--audience-profile",
        required=True,
        help="Audience profile slug under AI_translation/audience_profile/ "
        "(e.g. plain, children, scholars)",
    )
    p.add_argument(
        "--target-language",
        required=True,
        help="Target language folder name, e.g. english, hindi, marathi",
    )
    p.add_argument(
        "--text-slug",
        default=DEFAULT_TEXT_SLUG,
        help=f"Short text id for output names (default: {DEFAULT_TEXT_SLUG})",
    )
    p.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini model (default: {DEFAULT_MODEL})",
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
        help="Retries per API call on errors (default: 5)",
    )
    p.add_argument(
        "--resume",
        action="store_true",
        help="Skip units that already have a non-empty work file",
    )
    p.add_argument(
        "--merge-only",
        action="store_true",
        help="Skip translation; rebuild the merged file from existing work files",
    )
    p.add_argument(
        "--no-merge",
        action="store_true",
        help="Translate only; do not write the merged file",
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

    if args.merge_only and args.no_merge:
        sys.exit("Error: --merge-only and --no-merge are mutually exclusive")

    target_language = args.target_language.strip().lower()
    audience_slug, audience_path, audience_body = resolve_audience_profile(
        args.audience_profile
    )
    source_dir = resolve_source_dir(args.source_dir)
    termbase_path = resolve_termbase(args.termbase)
    work_dir = work_dir_for(target_language, audience_slug, args.text_slug)
    merged_path = merged_path_for(target_language, audience_slug, args.text_slug)
    lang_tag = LANG_TAGS.get(target_language, target_language[:2])
    termbase_body = termbase_path.read_text(encoding="utf-8")
    audience_summary = audience_one_liner(audience_body)

    files = list_source_files(source_dir)
    if args.only:
        wanted = {name.lower() for name in args.only}
        files = [f for f in files if f.name.lower() in wanted]
        missing = wanted - {f.name.lower() for f in files}
        if missing:
            sys.exit(f"Error: --only not found in source: {', '.join(sorted(missing))}")

    if not files:
        sys.exit(f"Error: no source .md files in {source_dir}")

    print(f"Source:    {source_dir}")
    print(f"Termbase:  {termbase_path} ({len(termbase_body):,} chars)")
    print(f"Audience:  {audience_path}")
    print(f"Target:    {target_language} (lang_tag={lang_tag})")
    print(f"Work dir:  {work_dir}")
    print(f"Merged:    {merged_path}")
    print(f"Model:     {args.model}")
    print("Mode:      sequential (one file at a time)")
    print(f"Chunking:  chars>{args.chunk_chars} overlap_lines={args.overlap_lines}")
    print(f"Files:     {len(files)}")
    for f in files:
        print(f"  - {f.name}")

    fail_count = 0
    ok_count = 0

    if not args.merge_only:
        todo: list[tuple[Path, Path]] = []
        for src in files:
            dest = work_dir / src.name
            if args.resume and dest.is_file() and dest.stat().st_size > 0:
                print(f"skip (resume): {src.name}")
                continue
            todo.append((src, dest))

        if not todo and args.no_merge:
            print("Nothing to translate.")
            return 0

        if args.dry_run:
            print(
                f"Dry run — would translate {len(todo)} file(s) sequentially, "
                f"then {'skip merge' if args.no_merge else 'merge'}."
            )
            return 0

        if todo:
            client = make_client()
            for src, dest in todo:
                print(f"… translating {src.name}")
                name, ok, msg = translate_one(
                    client,
                    model=args.model,
                    source_path=src,
                    out_path=dest,
                    target_language=target_language,
                    audience_slug=audience_slug,
                    audience_body=audience_body,
                    termbase_body=termbase_body,
                    temperature=args.temperature,
                    max_retries=args.max_retries,
                    chunk_chars=args.chunk_chars,
                    overlap_lines=args.overlap_lines,
                    max_output_tokens=args.max_output_tokens,
                )
                if ok:
                    ok_count += 1
                    print(f"OK  {name}: {msg}")
                else:
                    fail_count += 1
                    print(f"ERR {name}: {msg}", file=sys.stderr)
                    print("Stopping sequential run on first failure.", file=sys.stderr)
                    break
    elif args.dry_run:
        print("Dry run — would merge existing work files only.")
        return 0

    if fail_count:
        print(
            f"Done with errors. ok={ok_count} failed={fail_count} "
            f"work={work_dir} (merge skipped)"
        )
        return 1

    if args.no_merge:
        print(f"Done. ok={ok_count} failed=0 work={work_dir} (merge skipped)")
        return 0

    # Merge requires every source unit's work file to exist.
    ordered_bodies: list[tuple[str, str]] = []
    missing_work: list[str] = []
    for src in files:
        dest = work_dir / src.name
        if not dest.is_file() or dest.stat().st_size == 0:
            missing_work.append(src.name)
            continue
        ordered_bodies.append((src.name, dest.read_text(encoding="utf-8")))

    if missing_work:
        print(
            "Error: cannot merge — missing work files:\n  "
            + "\n  ".join(missing_work),
            file=sys.stderr,
        )
        return 1

    intro_body = next(
        (body for name, body in ordered_bodies if name.lower() == "intro.md"),
        "",
    )
    title = extract_title(intro_body, target_language)
    frontmatter = build_merged_frontmatter(
        title=title,
        source_dir=source_dir,
        target_language=target_language,
        lang_tag=lang_tag,
        audience_path=audience_path,
        audience_summary=audience_summary,
        termbase_path=termbase_path,
    )
    merged = merge_units(ordered_bodies=ordered_bodies, frontmatter=frontmatter)
    write_merged_file(merged_path, merged)

    # Surface any termbase flags from the merged text
    flags = TERMBASE_FLAG_RE.findall(merged)
    if flags:
        print(f"Termbase flags in merged output: {len(flags)}")
        for flag in flags[:20]:
            print(f"  {flag}")
        if len(flags) > 20:
            print(f"  … and {len(flags) - 20} more")

    print(f"Merged OK → {merged_path} ({len(merged):,} bytes, CRLF)")
    print(f"Done. ok={ok_count} failed=0 work={work_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
