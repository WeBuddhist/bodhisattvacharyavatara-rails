#!/usr/bin/env python3
"""
run_keyword_equivalence_mapper.py
=================================

Run the AI_translation keyword-equivalence-mapper skill via Gemini.

Maps each source-language keyword (from a per-segment keyword reference
file) to its equivalent in a target-language translation of the same text.

Skill: AI_translation/skills/keyword-equivalence-mapper.md

Arguments
---------
  translation     Target-language text: one Markdown file, OR a folder of
                  split chapter files (*.md + frontmatter.txt).
  keyword_file    Source-language keywords, one line per segment:
                    [id] word1, word2, word3

Required flags
--------------
  --source-language     Language of the keyword file (e.g. tibetan)
  --target-language     Language of the translation (e.g. english)
  --audience-profile    Audience slug used for the translation (e.g. plain)

Usage
-----
    python AI_translation/run_keyword_equivalence_mapper.py \\
        AI_translation/english/bca-english-plain-zeroshot.md \\
        AI_translation/keywords-by-reference-tibetan-only.md \\
        --source-language tibetan \\
        --target-language english \\
        --audience-profile plain

    python AI_translation/run_keyword_equivalence_mapper.py \\
        AI_translation/english/bca-english-plain-zeroshot_split_chapters \\
        AI_translation/keywords-by-reference-tibetan-only.md \\
        --source-language tibetan \\
        --target-language english \\
        --audience-profile plain \\
        --workers 6

Output
------
    AI_translation/<target-language>/keywords-by-reference-<src>-<tgt>-<audience>.md

    [id] source_word1=target_equiv1, source_word2=target_equiv2, ...

Requires GEMINI_API_KEY (or GOOGLE_API_KEY) in the environment or vault-root
.env. Install: pip install google-genai
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_WORKERS = 4
SOURCE_FILE_GLOBS = ("*.md", "frontmatter.txt")

AI_TRANSLATION_DIR = Path(__file__).resolve().parent
VAULT_ROOT = AI_TRANSLATION_DIR.parent

KEYWORD_LINE_RE = re.compile(
    r"^\[(?P<id>[^\]]+)\]\s*(?P<body>.*)$"
)
# Trailing Obsidian block id on a line: "... text ^1-1" or "... text^1-1"
LINE_BLOCK_ID_RE = re.compile(
    r"^(?P<body>.*?)[ \t]*\^(?P<id>[^\s^]+)\s*$"
)


# ---------------------------------------------------------------------------
# Stdio / .env
# ---------------------------------------------------------------------------

def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                pass


def _load_dotenv() -> None:
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
# Parsers
# ---------------------------------------------------------------------------

def parse_keyword_file(path: Path) -> OrderedDict[str, list[str]]:
    """Parse `[id] w1, w2, ...` into an ordered id → keywords map."""
    text = path.read_text(encoding="utf-8")
    out: OrderedDict[str, list[str]] = OrderedDict()
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = KEYWORD_LINE_RE.match(line)
        if not m:
            continue
        seg_id = m.group("id").strip()
        body = m.group("body").strip()
        if not body:
            out[seg_id] = []
            continue
        words = [w.strip() for w in body.split(",") if w.strip()]
        out[seg_id] = words
    if not out:
        sys.exit(f"Error: no keyword lines found in {path}")
    return out


def load_translation_text(path: Path) -> str:
    """Load a single file, or concatenate a split_chapters-style folder."""
    if path.is_file():
        return path.read_text(encoding="utf-8")
    if not path.is_dir():
        sys.exit(f"Error: translation path not found: {path}")

    files: list[Path] = []
    for pattern in SOURCE_FILE_GLOBS:
        files.extend(path.glob(pattern))
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

    paths = sorted(paths, key=sort_key)
    if not paths:
        sys.exit(f"Error: no translation files in folder: {path}")
    parts = [p.read_text(encoding="utf-8") for p in paths]
    return "".join(parts)


def parse_translation_segments(text: str) -> OrderedDict[str, str]:
    """
    Split translation into id → segment body (including the trailing ^id line
    content, without the caret id itself).
    """
    segments: OrderedDict[str, str] = OrderedDict()
    buf: list[str] = []
    for line in text.splitlines():
        m = LINE_BLOCK_ID_RE.match(line)
        if m:
            body_line = m.group("body")
            seg_id = m.group("id")
            buf.append(body_line)
            segments[seg_id] = "\n".join(buf).strip()
            buf = []
        else:
            buf.append(line)
    return segments


def chapter_key(seg_id: str) -> str:
    if "-" not in seg_id:
        return seg_id
    return seg_id.split("-", 1)[0]


def group_ids_by_chapter(ids: list[str]) -> OrderedDict[str, list[str]]:
    groups: OrderedDict[str, list[str]] = OrderedDict()
    for seg_id in ids:
        key = chapter_key(seg_id)
        groups.setdefault(key, []).append(seg_id)
    return groups


# ---------------------------------------------------------------------------
# Gemini
# ---------------------------------------------------------------------------

SYSTEM_INSTRUCTION = """\
You are a bilingual philological assistant for Buddhist texts.

Your task is keyword equivalence mapping, verse by verse:
- You receive source-language keywords already extracted for each segment ID.
- You also receive the target-language translation text for that same segment.
- For EACH source keyword, name the word or short phrase in the target text
  that carries its meaning in that verse's context.
- If there is no direct equivalent (particles, honorifics, implicit renderings),
  use exactly: (no direct equivalent)
- Do NOT drop or reorder keywords. Output one pair per source keyword, same order.
- The same source keyword may map to different target phrases in different verses.
- Target equivalents may be multi-word phrases when needed.
- Output ONLY mapping lines, one per segment, in this exact format:
  [id] source1=target1, source2=target2, ...
- No commentary, no code fences, no blank lines between entries.
"""


def make_client():
    try:
        from google import genai
    except ImportError:
        sys.exit(
            "Error: google-genai is not installed.\n"
            "  Activate this project's venv, then:\n"
            "  python -m pip install google-genai"
        )
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "Error: no API key found.\n"
            "  Set GEMINI_API_KEY (or GOOGLE_API_KEY), or put it in vault-root .env"
        )
    return genai.Client(api_key=api_key)


def build_chapter_prompt(
    *,
    chapter: str,
    ids: list[str],
    keywords: OrderedDict[str, list[str]],
    verses: OrderedDict[str, str],
    source_language: str,
    target_language: str,
) -> str:
    blocks: list[str] = []
    for seg_id in ids:
        kws = keywords.get(seg_id, [])
        verse = verses.get(seg_id, "").strip()
        kw_line = ", ".join(kws) if kws else "(none)"
        verse_block = verse if verse else "(SEGMENT NOT FOUND IN TRANSLATION)"
        blocks.append(
            f"### [{seg_id}]\n"
            f"SOURCE KEYWORDS ({source_language}): {kw_line}\n"
            f"TARGET VERSE ({target_language}):\n{verse_block}\n"
        )

    return f"""\
SOURCE LANGUAGE (keywords): {source_language}
TARGET LANGUAGE (translation): {target_language}
CHAPTER / GROUP: {chapter}
SEGMENTS IN THIS BATCH: {len(ids)}

For every segment below, output exactly one line:
[id] source_keyword=target_equivalent, ...

Use (no direct equivalent) when needed. Keep every source keyword, same order.

=== SEGMENTS ===
{"".join(blocks)}
=== END SEGMENTS ===
"""


def parse_mapping_response(
    text: str,
    expected_ids: list[str],
    keywords: OrderedDict[str, list[str]],
) -> dict[str, str]:
    """
    Parse model output into id → full `[id] pairs...` line.
    Falls back to marking missing keywords if model skips an id.
    """
    found: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("```"):
            continue
        m = KEYWORD_LINE_RE.match(line)
        if not m:
            continue
        seg_id = m.group("id").strip()
        body = m.group("body").strip()
        found[seg_id] = f"[{seg_id}] {body}"

    out: dict[str, str] = {}
    for seg_id in expected_ids:
        if seg_id in found:
            out[seg_id] = found[seg_id]
            continue
        # Fallback: preserve keywords with no-equivalent markers
        kws = keywords.get(seg_id, [])
        if kws:
            pairs = ", ".join(f"{w}=(no direct equivalent)" for w in kws)
            out[seg_id] = f"[{seg_id}] {pairs}"
        else:
            out[seg_id] = f"[{seg_id}]"
    return out


def map_chapter(
    client,
    *,
    model: str,
    chapter: str,
    ids: list[str],
    keywords: OrderedDict[str, list[str]],
    verses: OrderedDict[str, str],
    source_language: str,
    target_language: str,
    temperature: float,
    max_retries: int,
) -> tuple[str, bool, dict[str, str], str]:
    from google.genai import types

    prompt = build_chapter_prompt(
        chapter=chapter,
        ids=ids,
        keywords=keywords,
        verses=verses,
        source_language=source_language,
        target_language=target_language,
    )
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=temperature,
    )

    last_err: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            resp = client.models.generate_content(
                model=model,
                contents=prompt,
                config=config,
            )
            text = (getattr(resp, "text", None) or "").strip()
            if not text:
                raise RuntimeError("empty response from Gemini")
            mapped = parse_mapping_response(text, ids, keywords)
            return chapter, True, mapped, f"{len(mapped)} segments"
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            time.sleep(min(60, 4 * attempt))

    return chapter, False, {}, f"failed after {max_retries} tries: {last_err}"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Map source-language keywords to target-language equivalents "
            "(keyword-equivalence-mapper skill via Gemini)."
        )
    )
    p.add_argument(
        "translation",
        type=Path,
        help="Target-language translation: a .md/.txt file OR a split_chapters folder",
    )
    p.add_argument(
        "keyword_file",
        type=Path,
        help="Source-language keyword reference file ([id] word1, word2, ...)",
    )
    p.add_argument(
        "--source-language",
        required=True,
        help="Language of the keyword file (e.g. tibetan)",
    )
    p.add_argument(
        "--target-language",
        required=True,
        help="Language of the translation (e.g. english)",
    )
    p.add_argument(
        "--audience-profile",
        required=True,
        help="Audience slug for the translation being mapped (e.g. plain)",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional explicit output path (default under AI_translation/<target>/)",
    )
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    p.add_argument("--temperature", type=float, default=0.2)
    p.add_argument("--max-retries", type=int, default=5)
    p.add_argument(
        "--only-chapters",
        nargs="+",
        metavar="KEY",
        help="Only process these chapter keys (e.g. 1 I a)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse inputs and list chapter batches without calling the API",
    )
    return p.parse_args()


def default_output_path(
    source_language: str,
    target_language: str,
    audience: str,
) -> Path:
    name = (
        f"keywords-by-reference-{source_language}-"
        f"{target_language}-{audience}.md"
    )
    return AI_TRANSLATION_DIR / target_language / name


def main() -> int:
    _configure_stdio()
    args = parse_args()
    _load_dotenv()

    translation_path = args.translation
    if not translation_path.is_absolute():
        translation_path = (Path.cwd() / translation_path).resolve()
    keyword_path = args.keyword_file
    if not keyword_path.is_absolute():
        keyword_path = (Path.cwd() / keyword_path).resolve()

    if not keyword_path.is_file():
        sys.exit(f"Error: keyword file not found: {keyword_path}")
    if not translation_path.exists():
        sys.exit(f"Error: translation path not found: {translation_path}")

    source_language = args.source_language.strip().lower()
    target_language = args.target_language.strip().lower()
    audience = args.audience_profile.strip().removesuffix(".md").lower()

    out_path = args.output
    if out_path is None:
        out_path = default_output_path(source_language, target_language, audience)
    elif not out_path.is_absolute():
        out_path = (Path.cwd() / out_path).resolve()

    keywords = parse_keyword_file(keyword_path)
    translation_text = load_translation_text(translation_path)
    verses = parse_translation_segments(translation_text)

    ids = list(keywords.keys())
    overlap = sum(1 for i in ids if i in verses)
    missing_in_translation = [i for i in ids if i not in verses]
    extra_in_translation = [i for i in verses if i not in keywords]

    groups = group_ids_by_chapter(ids)
    if args.only_chapters:
        wanted = {k.strip() for k in args.only_chapters}
        groups = OrderedDict((k, v) for k, v in groups.items() if k in wanted)
        if not groups:
            sys.exit(f"Error: --only-chapters matched nothing: {sorted(wanted)}")

    print(f"Keywords:     {keyword_path}  ({len(ids)} segments)")
    print(f"Translation:  {translation_path}  ({len(verses)} segments with ^ids)")
    print(f"Overlap:      {overlap}/{len(ids)} keyword IDs found in translation")
    if missing_in_translation[:8]:
        preview = ", ".join(missing_in_translation[:8])
        more = "" if len(missing_in_translation) <= 8 else "…"
        print(f"Missing in translation ({len(missing_in_translation)}): {preview}{more}")
    if extra_in_translation and len(extra_in_translation) <= 12:
        print(f"Translation-only IDs: {', '.join(extra_in_translation)}")
    print(f"Languages:    {source_language} → {target_language}  (audience={audience})")
    print(f"Output:       {out_path}")
    print(f"Model:        {args.model}")
    print(f"Workers:      {args.workers}")
    print(f"Chapters:     {len(groups)}")
    for key, seg_ids in groups.items():
        print(f"  - {key}: {len(seg_ids)} segments")

    if args.dry_run:
        print("Dry run — no API calls.")
        return 0

    if overlap == 0:
        sys.exit(
            "Error: no segment ID overlap between keyword file and translation. "
            "Check that both use the same ^id convention."
        )

    client = make_client()
    results: dict[str, str] = {}
    fail_count = 0

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(
                map_chapter,
                client,
                model=args.model,
                chapter=chapter,
                ids=seg_ids,
                keywords=keywords,
                verses=verses,
                source_language=source_language,
                target_language=target_language,
                temperature=args.temperature,
                max_retries=args.max_retries,
            ): chapter
            for chapter, seg_ids in groups.items()
        }
        for fut in as_completed(futures):
            chapter, ok, mapped, msg = fut.result()
            if ok:
                results.update(mapped)
                print(f"OK  chapter {chapter}: {msg}")
            else:
                fail_count += 1
                print(f"ERR chapter {chapter}: {msg}", file=sys.stderr)

    # Emit in keyword-file order
    lines: list[str] = []
    for seg_id in ids:
        if seg_id in results:
            lines.append(results[seg_id])
        else:
            kws = keywords.get(seg_id, [])
            if kws:
                pairs = ", ".join(f"{w}=(no direct equivalent)" for w in kws)
                lines.append(f"[{seg_id}] {pairs}")
            else:
                lines.append(f"[{seg_id}]")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Done. wrote={out_path} lines={len(lines)} failed_chapters={fail_count}")
    return 1 if fail_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
