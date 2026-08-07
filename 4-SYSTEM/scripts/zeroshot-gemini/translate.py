#!/usr/bin/env python3
"""
translate.py — zero-shot translation driver (Gemini).

Translates a block-ID'd Railroads source file into any target language, using a
track's `requirements.md` as the sole style authority and a second source file
as a disambiguation reference. Output is structurally interchangeable with the
source: same block IDs, same order, same line counts.

Default source pair for this vault
----------------------------------
    meaning base   1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md   (Tibetan)
    reference      1-SOURCES/Text/BCAV08_SH_sk.md                (Sanskrit)

Both are overridable, so the same driver serves any text in any vault that
follows the block-ID convention.

Quick start
-----------
    # See what would be sent, spend nothing
    python 4-SYSTEM/scripts/zeroshot-gemini/translate.py \
        --requirements 3-TRANSFORMATIONS/Translations/en-verse-plain/requirements.md \
        --target-lang English \
        --track en-verse-plain \
        --chapters 1 \
        --dry-run

    # Translate chapter 1 for real
    python 4-SYSTEM/scripts/zeroshot-gemini/translate.py \
        --requirements 3-TRANSFORMATIONS/Translations/en-verse-plain/requirements.md \
        --target-lang English \
        --track en-verse-plain \
        --chapters 1

    # Resume an interrupted run (finished windows are reused from cache)
    ... --chapters 1-10 --resume

Design notes
------------
* One API call per *window* of blocks, never larger than --max-blocks, never
  crossing a chapter boundary. Chapters 5, 6, 8 and 9 are long; a whole-chapter
  call invites truncation and drift.
* Every window is validated against the source before it is accepted. A failing
  window is sent back to the model with the specific errors, up to
  --repair-attempts times, before the run stops. It never silently ships a
  chapter with missing verses.
* Every accepted window is cached to the work directory, so --resume costs
  nothing and an interrupted 10-chapter run picks up where it stopped.
* Nothing is ever written to 1-SOURCES/. Generated chapters are always
  `status: draft` — only a domain specialist promotes to complete.

Requires: pip install google-genai  (python-dotenv optional, for .env loading)
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from prompt import SYSTEM_INSTRUCTION, build_prompt, window_label  # noqa: E402
from structure import Block, Section, parse_block_map, parse_document  # noqa: E402
from validate import render_blocks, validate_window  # noqa: E402

DEFAULT_MODEL = "gemini-2.5-pro"

DEFAULT_SOURCE = "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
DEFAULT_REFERENCE = "1-SOURCES/Text/BCAV08_SH_sk.md"


class TranslationError(RuntimeError):
    pass


# ---------------------------------------------------------------------------
# environment
# ---------------------------------------------------------------------------


def load_env(project_root: Path) -> None:
    """Load .env without requiring python-dotenv."""
    try:
        from dotenv import load_dotenv

        load_dotenv(project_root / ".env")
        return
    except ImportError:
        pass
    env_file = project_root / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def find_project_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "1-SOURCES").is_dir() and (candidate / "4-SYSTEM").is_dir():
            return candidate
    return Path.cwd()


# ---------------------------------------------------------------------------
# gemini backend
# ---------------------------------------------------------------------------


class GeminiClient:
    def __init__(self, model: str, temperature: float, thinking_budget: int | None):
        try:
            from google import genai
            from google.genai import types
        except ImportError as exc:  # pragma: no cover
            raise TranslationError(
                "google-genai is not installed. Run: pip install google-genai"
            ) from exc

        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise TranslationError(
                "No GEMINI_API_KEY found. Add it to the project .env file or "
                "export it in your shell."
            )
        self._types = types
        self._client = genai.Client(api_key=api_key)
        self._model = model
        self._temperature = temperature
        self._thinking_budget = thinking_budget

    def generate(self, prompt: str) -> str:
        kwargs = {
            "system_instruction": SYSTEM_INSTRUCTION,
            "temperature": self._temperature,
        }
        if self._thinking_budget is not None:
            try:
                kwargs["thinking_config"] = self._types.ThinkingConfig(
                    thinking_budget=self._thinking_budget
                )
            except AttributeError:  # older SDK without thinking config
                pass
        config = self._types.GenerateContentConfig(**kwargs)
        response = self._client.models.generate_content(
            model=self._model, contents=prompt, config=config
        )
        text = getattr(response, "text", None)
        if not text:
            raise TranslationError("Gemini returned an empty response.")
        return text.strip()


# ---------------------------------------------------------------------------
# windowing
# ---------------------------------------------------------------------------


def make_windows(section: Section, max_blocks: int, max_chars: int) -> list[list[Block]]:
    """Split one section into API-sized windows without breaking a block."""
    windows: list[list[Block]] = []
    current: list[Block] = []
    chars = 0
    for block in section.blocks:
        size = len(block.text)
        if current and (len(current) >= max_blocks or chars + size > max_chars):
            windows.append(current)
            current, chars = [], 0
        current.append(block)
        chars += size
    if current:
        windows.append(current)
    return windows or [[]]


def parse_chapter_scope(spec: str, available: list[str]) -> list[str]:
    """'1', '1-3', '1,4,7', 'all', 'front', 'back' -> list of section keys."""
    spec = spec.strip().lower()
    if spec in ("all", "*"):
        return available
    keys: list[str] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if part == "front":
            keys.append("I")
            continue
        if part == "back":
            keys.extend(k for k in available if not k.isdigit() and k != "I")
            continue
        m = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", part)
        if m:
            lo, hi = int(m.group(1)), int(m.group(2))
            keys.extend(str(n) for n in range(lo, hi + 1))
            continue
        keys.append(part.upper() if part in ("i",) else part)
    seen, out = set(), []
    for k in keys:
        if k in available and k not in seen:
            seen.add(k)
            out.append(k)
    return out


# ---------------------------------------------------------------------------
# output assembly
# ---------------------------------------------------------------------------


def chapter_frontmatter(
    *,
    section: Section,
    track: str,
    target_lang: str,
    source_path: str,
    reference_path: str | None,
    requirements_path: str,
    model: str,
) -> str:
    ids = section.block_ids
    span = f"^{ids[0]}–^{ids[-1]}" if ids else ""
    packages = [f"  - {source_path} ({span})"]
    if reference_path:
        packages.append(f"  - {reference_path} ({span})")
    title = section.heading.lines[0] if section.heading else f"Section {section.key}"
    title = re.sub(r"\s*\^\S+\s*$", "", title).lstrip("# ").strip()
    return "\n".join(
        [
            "---",
            f"ref: {section.key}",
            f'title: "{title}"',
            "transformation_type: translation",
            f"track: {track}",
            f"target_language: {target_lang}",
            f"style_contract: {requirements_path}",
            f"generated_by: 4-SYSTEM/scripts/zeroshot-gemini/translate.py ({model})",
            "context_packages:",
            *packages,
            f"generation_date: {_dt.date.today().isoformat()}",
            "status: draft",
            "---",
            "",
        ]
    )


def cache_key(prompt: str, model: str) -> str:
    return hashlib.sha256((model + "\n" + prompt).encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def run(args: argparse.Namespace) -> int:
    root = Path(args.project_root).resolve() if args.project_root else find_project_root(
        Path(__file__).resolve().parent
    )
    load_env(root)

    def resolve(p: str) -> Path:
        path = Path(p)
        return path if path.is_absolute() else (root / path)

    source_path = resolve(args.source)
    reference_path = resolve(args.reference) if args.reference else None
    requirements_path = resolve(args.requirements)

    for label, path in (("source", source_path), ("requirements", requirements_path)):
        if not path.exists():
            raise TranslationError(f"{label} file not found: {path}")
    if reference_path and not reference_path.exists():
        raise TranslationError(f"reference file not found: {reference_path}")

    doc = parse_document(source_path)
    reference_map = parse_block_map(reference_path) if reference_path else None
    requirements_text = requirements_path.read_text(encoding="utf-8")
    termbase_text = None
    if args.termbase:
        tb = resolve(args.termbase)
        if tb.exists():
            termbase_text = tb.read_text(encoding="utf-8")
        else:
            print(f"  ! termbase not found, continuing without it: {tb}")

    available = [s.key for s in doc.sections]
    scope = parse_chapter_scope(args.chapters, available)
    if not scope:
        raise TranslationError(
            f"chapter scope '{args.chapters}' matched nothing. Available: "
            + ", ".join(available)
        )

    out_dir = resolve(args.output_dir) if args.output_dir else (
        root / "3-TRANSFORMATIONS" / "Translations" / args.track
    )
    work_dir = resolve(args.work_dir) if args.work_dir else (
        root / "0-INBOX" / "zeroshot-gemini" / args.track
    )
    if not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)

    rel_source = str(source_path.relative_to(root)) if source_path.is_relative_to(root) else str(source_path)
    rel_reference = (
        str(reference_path.relative_to(root))
        if reference_path and reference_path.is_relative_to(root)
        else (str(reference_path) if reference_path else None)
    )
    rel_requirements = (
        str(requirements_path.relative_to(root))
        if requirements_path.is_relative_to(root)
        else str(requirements_path)
    )

    # --- run banner ---------------------------------------------------------
    print("zero-shot translation (Gemini)")
    print(f"  project root   : {root}")
    print(f"  source         : {rel_source}  ({doc.path.name})")
    print(f"  reference      : {rel_reference or '— none —'}")
    print(f"  style contract : {rel_requirements}")
    print(f"  termbase       : {args.termbase or '— none —'}")
    print(f"  target         : {args.target_lang}")
    print(f"  track          : {args.track}")
    print(f"  model          : {args.model}")
    print(f"  scope          : {', '.join('^' + k for k in scope)}")
    print(f"  output dir     : {out_dir}")
    print(f"  work dir       : {work_dir}")

    if reference_map:
        src_ids = {b for s in doc.sections for b in s.block_ids}
        matched = src_ids & set(reference_map)
        print(
            f"  reference alignment: {len(matched)}/{len(src_ids)} source blocks "
            f"have a parallel ({len(src_ids - set(reference_map))} without)"
        )

    client = None
    if not args.dry_run:
        client = GeminiClient(args.model, args.temperature, args.thinking_budget)

    total_calls = 0
    for key in scope:
        section = doc.section(key)
        if section is None or not section.blocks:
            print(f"\n^{key}: no blocks, skipped")
            continue

        windows = make_windows(section, args.max_blocks, args.max_chars)
        label = f"Chapter-{int(key):02d}" if key.isdigit() else f"Section-{key}"
        out_file = out_dir / f"{label}.md"

        if out_file.exists() and not args.overwrite and not args.resume:
            print(f"\n{label}: already exists, skipped (pass --overwrite to replace)")
            continue

        print(f"\n{label}  ({len(section.blocks)} blocks, {section.char_count} chars, "
              f"{len(windows)} window{'s' if len(windows) != 1 else ''})")

        pieces: list[str] = []
        carryover: str | None = None

        for i, window in enumerate(windows):
            wlabel = window_label(section, i, len(windows))
            base_prompt = build_prompt(
                blocks=window,
                reference_map=reference_map,
                requirements_text=requirements_text,
                requirements_path=rel_requirements,
                source_lang=args.source_lang,
                target_lang=args.target_lang,
                reference_lang=args.reference_lang,
                termbase_text=termbase_text,
                carryover=carryover,
            )
            ckey = cache_key(base_prompt, args.model)
            cache_file = work_dir / f"{wlabel}.{ckey}.md"
            prompt_file = work_dir / f"{wlabel}.prompt.txt"
            prompt_file.write_text(base_prompt, encoding="utf-8")

            ids = [b.block_id for b in window]
            span = f"^{ids[0]}–^{ids[-1]}" if ids else "—"
            print(f"  [{i + 1}/{len(windows)}] {span}  {len(base_prompt):,} prompt chars", end="")

            if args.dry_run:
                print("  (dry run — prompt written, no API call)")
                continue

            if args.resume and cache_file.exists():
                accepted = cache_file.read_text(encoding="utf-8")
                print("  (cached)")
                pieces.append(accepted)
                carryover = accepted.split("\n\n")[-1]
                continue

            accepted = None
            errors: list[str] = []
            previous = None
            for attempt in range(args.repair_attempts + 1):
                prompt = base_prompt if attempt == 0 else build_prompt(
                    blocks=window,
                    reference_map=reference_map,
                    requirements_text=requirements_text,
                    requirements_path=rel_requirements,
                    source_lang=args.source_lang,
                    target_lang=args.target_lang,
                    reference_lang=args.reference_lang,
                    termbase_text=termbase_text,
                    carryover=carryover,
                    repair_errors=errors,
                    previous_attempt=previous,
                )
                raw = call_with_retry(client, prompt, args)
                total_calls += 1
                blocks, errors = validate_window(
                    source_blocks=window,
                    output_text=raw,
                    hard_breaks=not args.no_hard_breaks,
                    allow_editorial=args.allow_editorial,
                )
                if not errors:
                    accepted = render_blocks(blocks)
                    print("  ok" if attempt == 0 else f"  ok (after {attempt} repair)")
                    break
                previous = raw
                print(f"\n      ✗ {len(errors)} structural error(s) on attempt {attempt + 1}:")
                for e in errors[:6]:
                    print(f"        {e}")
                (work_dir / f"{wlabel}.attempt{attempt + 1}.failed.md").write_text(
                    raw, encoding="utf-8"
                )

            if accepted is None:
                raise TranslationError(
                    f"{label} window {i + 1} still failed after "
                    f"{args.repair_attempts} repair attempt(s). Failed outputs are "
                    f"in {work_dir}. Fix the prompt or lower --max-blocks and rerun "
                    "with --resume."
                )

            cache_file.write_text(accepted, encoding="utf-8")
            pieces.append(accepted)
            carryover = accepted.split("\n\n")[-1]
            if args.delay:
                time.sleep(args.delay)

        if args.dry_run:
            continue

        body = "\n\n".join(pieces)
        header = chapter_frontmatter(
            section=section,
            track=args.track,
            target_lang=args.target_lang,
            source_path=rel_source,
            reference_path=rel_reference,
            requirements_path=rel_requirements,
            model=args.model,
        )
        out_file.write_text(header + "\n" + body + "\n", encoding="utf-8")
        print(f"  → {out_file.relative_to(root) if out_file.is_relative_to(root) else out_file}")

    print(f"\ndone — {total_calls} API call(s)")
    if args.dry_run:
        print(f"prompts written to {work_dir}; no quota spent")
    else:
        print("all generated files are `status: draft` — a domain specialist "
              "promotes them to complete after translation-qa runs clean")
    return 0


def call_with_retry(client: GeminiClient, prompt: str, args) -> str:
    last: Exception | None = None
    for attempt in range(args.retries):
        try:
            return client.generate(prompt)
        except Exception as exc:  # transient API failure
            last = exc
            wait = args.backoff * (2 ** attempt)
            print(f"\n      ! API error ({exc}); retrying in {wait:.0f}s")
            time.sleep(wait)
    raise TranslationError(f"Gemini failed after {args.retries} attempts: {last}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--requirements", required=True,
                   help="Path to the track's requirements.md — the style contract. "
                        "This file is authoritative for register and layout.")
    p.add_argument("--target-lang", required=True,
                   help='Target language name, e.g. "English", "Hindi".')
    p.add_argument("--track", required=True,
                   help="Track name; output goes to "
                        "3-TRANSFORMATIONS/Translations/<track>/ by default.")

    p.add_argument("--source", default=DEFAULT_SOURCE,
                   help=f"Meaning-base source file (default: {DEFAULT_SOURCE}).")
    p.add_argument("--source-lang", default="Tibetan",
                   help="Language name of the source, for the prompt.")
    p.add_argument("--reference", default=DEFAULT_REFERENCE,
                   help=f"Disambiguation reference file (default: {DEFAULT_REFERENCE}). "
                        "Pass an empty string to disable.")
    p.add_argument("--reference-lang", default="Sanskrit",
                   help="Language name of the reference, for the prompt.")
    p.add_argument("--termbase", default=None,
                   help="Optional termbase.md with locked renderings.")

    p.add_argument("--chapters", default="all",
                   help="Scope: 'all', '1', '1-3', '1,4,7', 'front', 'back'.")
    p.add_argument("--output-dir", default=None,
                   help="Override the output directory.")
    p.add_argument("--work-dir", default=None,
                   help="Override the checkpoint/prompt directory.")

    p.add_argument("--model", default=DEFAULT_MODEL, help=f"Default: {DEFAULT_MODEL}.")
    p.add_argument("--temperature", type=float, default=0.3)
    p.add_argument("--thinking-budget", type=int, default=None,
                   help="Gemini thinking token budget (omit for the model default).")

    p.add_argument("--max-blocks", type=int, default=25,
                   help="Max source blocks per API call (default: 25).")
    p.add_argument("--max-chars", type=int, default=6000,
                   help="Max source characters per API call (default: 6000).")
    p.add_argument("--repair-attempts", type=int, default=2,
                   help="Structural repair round-trips before giving up (default: 2).")
    p.add_argument("--retries", type=int, default=3,
                   help="Retries per API call on transient failure (default: 3).")
    p.add_argument("--backoff", type=float, default=5.0)
    p.add_argument("--delay", type=float, default=1.0,
                   help="Seconds to pause between accepted windows (default: 1).")

    p.add_argument("--no-hard-breaks", action="store_true",
                   help="Do not append two trailing spaces to non-final lines. "
                        "Use for prose tracks; leave off for verse tracks.")
    p.add_argument("--allow-editorial", action="store_true",
                   help="Permit `[Ed: …]` notes in the output.")
    p.add_argument("--resume", action="store_true",
                   help="Reuse cached windows and continue an interrupted run.")
    p.add_argument("--overwrite", action="store_true",
                   help="Replace existing chapter files.")
    p.add_argument("--dry-run", action="store_true",
                   help="Build and save every prompt, make no API call, spend nothing.")
    p.add_argument("--project-root", default=None,
                   help="Vault root (auto-detected from 1-SOURCES/ + 4-SYSTEM/).")
    return p


def main() -> int:
    args = build_parser().parse_args()
    if args.reference in ("", "none", "None"):
        args.reference = None
    try:
        return run(args)
    except TranslationError as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\ninterrupted — rerun with --resume to continue", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
