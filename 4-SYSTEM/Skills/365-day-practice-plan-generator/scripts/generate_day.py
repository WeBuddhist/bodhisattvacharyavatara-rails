#!/usr/bin/env python3
"""
generate_day.py — BCA 365-Day Practice Plan Generator (Gemini backend)

Reads a day's assigned verses from the vault, gathers the root verse text and
verse-context summaries, sends them to Gemini 2.5 Pro using the
"BCA-Practice-Plan-Gemini-Gem" instructions, and writes Gemini's output into
the matching file under 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/.

SECURITY:
  This script never contains your Gemini API key. It reads the key from
  (in order of preference):
    1. the GEMINI_API_KEY environment variable
    2. a local key file OUTSIDE this git repo (default: ~/.secrets/gemini.env,
       i.e. C:\\Users\\<you>\\.secrets\\gemini.env on Windows)
  Neither of those locations is inside the vault, so `git add` / `git push`
  can never pick up the key.

USAGE (run this yourself, in your own terminal — see the setup notes sent
alongside this script for the exact commands):
  python generate_day.py --day 45
  python generate_day.py --days 45-50
  python generate_day.py --days 45,46,47
  python generate_day.py --day 45 --dry-run          # preview prompt, no API call, no write
  python generate_day.py --status                    # list every day's file size so you can
                                                       # see which ones still look like placeholders
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# This script lives at: <vault>/4-SYSTEM/Skills/365-day-practice-plan-generator/scripts/generate_day.py
VAULT_ROOT_DEFAULT = Path(__file__).resolve().parents[4]

SKILL_DIR = "4-SYSTEM/Skills/365-day-practice-plan-generator"
ROOT_TEXT_REL = "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
VERSES_DIR_REL = "2-RAILS/Verses"
SCHEDULE_REL = "3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/schedule-corrected.md"
PLANS_DIR_REL = "3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo"
GEM_PROMPT_REL = f"{SKILL_DIR}/BCA-Practice-Plan-Gemini-Gem.md"

DEFAULT_KEY_FILE = Path.home() / ".secrets" / "gemini.env"


# ---------------------------------------------------------------------------
# Key loading
# ---------------------------------------------------------------------------

def load_api_key(key_file: Path) -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key.strip()

    if key_file.exists():
        # utf-8-sig strips a leading BOM if present (Windows PowerShell's
        # `Out-File -Encoding utf8` writes one) and behaves like plain utf-8
        # otherwise, so this is safe either way.
        for line in key_file.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip().lstrip("﻿")
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                name, _, value = line.partition("=")
                if name.strip() == "GEMINI_API_KEY":
                    return value.strip().strip('"').strip("'")

    raise SystemExit(
        f"No Gemini API key found.\n"
        f"Set the GEMINI_API_KEY environment variable, or create {key_file} "
        f"with a line: GEMINI_API_KEY=your-key-here\n"
        f"(That file must live OUTSIDE the vault so it never gets committed to git.)"
    )


# ---------------------------------------------------------------------------
# Schedule parsing
# ---------------------------------------------------------------------------

def parse_schedule(schedule_path: Path, day: int):
    """Return (chapter, verse_start, verse_end) for the given day number."""
    text = schedule_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        first = cells[0]
        if not first.isdigit():
            continue
        if int(first) != day:
            continue
        verses_cell = cells[1]
        pairs = re.findall(r"(\d+)\.(\d+)", verses_cell)
        if not pairs:
            raise ValueError(f"Could not parse verse range from schedule cell: {verses_cell!r}")
        chapter = int(pairs[0][0])
        verse_start = int(pairs[0][1])
        verse_end = int(pairs[-1][1])
        return chapter, verse_start, verse_end
    raise ValueError(f"Day {day} not found in {schedule_path}")


# ---------------------------------------------------------------------------
# Target file resolution
# ---------------------------------------------------------------------------

def find_target_file(plans_dir: Path, day: int, chapter: int, verse_start: int, verse_end: int) -> Path:
    """Find (or construct) the file this day's plan should be written to."""
    # Prefer an existing file for this day/chapter, whatever its exact verse
    # suffix is (keeps us consistent with any manual corrections already made).
    for chapter_dir in plans_dir.glob(f"Chapter-{chapter} *"):
        if not chapter_dir.is_dir():
            continue
        matches = list(chapter_dir.glob(f"Day-{day}-Ch{chapter}-*.md"))
        if matches:
            return matches[0]

    # Nothing exists yet — construct the expected filename and folder.
    candidates = list(plans_dir.glob(f"Chapter-{chapter} *"))
    if not candidates:
        raise FileNotFoundError(
            f"No 'Chapter-{chapter} ...' folder found under {plans_dir}; "
            f"create it first or check the chapter number."
        )
    chapter_dir = candidates[0]
    filename = f"Day-{day}-Ch{chapter}-V{verse_start}-{verse_end}.md"
    return chapter_dir / filename


# ---------------------------------------------------------------------------
# Root verse + summary extraction
# ---------------------------------------------------------------------------

def extract_verse_text(root_text: str, chapter: int, verse: int) -> str:
    lines = root_text.splitlines()
    marker = f"^{chapter}-{verse}"
    idx = None
    for i, line in enumerate(lines):
        if line.rstrip().endswith(marker):
            idx = i
            break
    if idx is None:
        return f"[COULD NOT FIND VERSE {chapter}-{verse} IN ROOT TEXT — block ref {marker} not found]"

    block = [lines[idx]]
    j = idx - 1
    while j >= 0:
        lj = lines[j]
        if lj.strip() == "" or lj.strip().startswith("![["):
            break
        block.insert(0, lj)
        j -= 1
    return "\n".join(block)


def load_summary(verses_dir: Path, chapter: int, verse: int) -> str:
    path = verses_dir / f"{chapter}-{verse}-summary.md"
    if not path.exists():
        return f"[NO SUMMARY FILE FOUND for {chapter}-{verse} — expected {path.name}]"
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Prompt assembly
# ---------------------------------------------------------------------------

def load_system_instructions(vault_root: Path) -> str:
    gem_path = vault_root / GEM_PROMPT_REL
    text = gem_path.read_text(encoding="utf-8")
    marker = "## Gem Instructions"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx:]


def build_user_prompt(day: int, chapter: int, verse_start: int, verse_end: int,
                       vault_root: Path) -> str:
    root_text = (vault_root / ROOT_TEXT_REL).read_text(encoding="utf-8")
    verses_dir = vault_root / VERSES_DIR_REL

    parts = [
        f"Day: {day}",
        f"Chapter: {chapter}",
        f"Verse range: {verse_start}-{verse_end}",
        "",
        "## Root verses (source: 1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md)",
        "",
    ]
    for v in range(verse_start, verse_end + 1):
        parts.append(f"### Verse {chapter}-{v}")
        parts.append(extract_verse_text(root_text, chapter, v))
        parts.append("")

    parts.append("## Verse-context summaries / commentary (source: 2-RAILS/Verses/<chapter>-<verse>-summary.md)")
    parts.append("")
    for v in range(verse_start, verse_end + 1):
        parts.append(f"### Summary for {chapter}-{v}")
        parts.append(load_summary(verses_dir, chapter, v))
        parts.append("")

    parts.append(
        "Generate the complete day's practice plan document now, following the "
        "instructions above exactly. Output ONLY the markdown document (including "
        "the mandatory header, with the required blank line before the first `---`), "
        "nothing else — no preamble, no meta-commentary about what you did."
    )
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Gemini call
# ---------------------------------------------------------------------------

def call_gemini(system_instructions: str, user_prompt: str, api_key: str, model: str) -> str:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model=model,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instructions,
                temperature=0.7,
            ),
        )
    except Exception as e:
        msg = str(e)
        if "NOT_FOUND" in msg or "404" in msg or "no longer available" in msg:
            raise SystemExit(
                f"Gemini rejected model '{model}':\n{msg}\n\n"
                f"Run `python generate_day.py --list-models` to see which models "
                f"your key can actually use, then pass one with --model, e.g.:\n"
                f"  python generate_day.py --day <N> --model gemini-3.5-flash"
            )
        raise
    return response.text


def list_models(api_key: str):
    from google import genai

    client = genai.Client(api_key=api_key)
    print("Models available to your key that support generateContent:\n")
    for m in client.models.list():
        actions = getattr(m, "supported_actions", None) or []
        if not actions or "generateContent" in actions:
            print(f"  {m.name}")


# ---------------------------------------------------------------------------
# Status mode
# ---------------------------------------------------------------------------

def run_status(vault_root: Path, threshold_bytes: int = 3000):
    plans_dir = vault_root / PLANS_DIR_REL
    schedule_path = vault_root / SCHEDULE_REL
    print(f"{'Day':>4}  {'Size':>8}  {'Status':<12}  File")
    for chapter_dir in sorted(plans_dir.glob("Chapter-* *"), key=lambda p: p.name):
        for f in sorted(chapter_dir.glob("Day-*.md"),
                         key=lambda p: int(re.search(r"Day-(\d+)-", p.name).group(1))):
            m = re.search(r"Day-(\d+)-", f.name)
            if not m:
                continue
            day = int(m.group(1))
            size = f.stat().st_size
            status = "filled" if size >= threshold_bytes else "PLACEHOLDER?"
            print(f"{day:>4}  {size:>8}  {status:<12}  {f.relative_to(plans_dir)}")


# ---------------------------------------------------------------------------
# Day range parsing
# ---------------------------------------------------------------------------

def parse_days_arg(days_arg: str):
    days = set()
    for chunk in days_arg.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            a, b = chunk.split("-", 1)
            days.update(range(int(a), int(b) + 1))
        else:
            days.add(int(chunk))
    return sorted(days)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--day", type=int, help="Single day number to generate")
    ap.add_argument("--days", type=str, help="Day range/list, e.g. '45-50' or '45,46,47'")
    ap.add_argument("--status", action="store_true", help="List every day's file size and exit")
    ap.add_argument("--list-models", action="store_true", help="List models your API key can use and exit")
    ap.add_argument("--dry-run", action="store_true", help="Build the prompt and print it, but do not call Gemini or write files")
    ap.add_argument("--no-backup", action="store_true", help="Skip writing a .bak copy of the existing file before overwriting")
    ap.add_argument("--model", default="gemini-2.5-pro", help="Gemini model name (default: gemini-2.5-pro)")
    ap.add_argument("--vault-root", type=str, default=str(VAULT_ROOT_DEFAULT), help="Override the vault root path (mainly for testing)")
    ap.add_argument("--key-file", type=str, default=str(DEFAULT_KEY_FILE), help="Path to the local key file (default: ~/.secrets/gemini.env)")
    args = ap.parse_args()

    vault_root = Path(args.vault_root)

    if args.status:
        run_status(vault_root)
        return

    if args.list_models:
        list_models(load_api_key(Path(args.key_file)))
        return

    if args.day:
        days = [args.day]
    elif args.days:
        days = parse_days_arg(args.days)
    else:
        ap.error("Specify --day, --days, or --status")
        return

    schedule_path = vault_root / SCHEDULE_REL
    plans_dir = vault_root / PLANS_DIR_REL
    system_instructions = load_system_instructions(vault_root)

    api_key = None
    if not args.dry_run:
        api_key = load_api_key(Path(args.key_file))

    for day in days:
        print(f"\n=== Day {day} ===")
        chapter, verse_start, verse_end = parse_schedule(schedule_path, day)
        print(f"  Chapter {chapter}, verses {verse_start}-{verse_end}")

        target_file = find_target_file(plans_dir, day, chapter, verse_start, verse_end)
        print(f"  Target file: {target_file}")

        user_prompt = build_user_prompt(day, chapter, verse_start, verse_end, vault_root)

        if args.dry_run:
            print("  --- SYSTEM INSTRUCTIONS (truncated) ---")
            print(system_instructions[:500] + "...\n")
            print("  --- USER PROMPT ---")
            print(user_prompt)
            continue

        print(f"  Calling {args.model} ...")
        output = call_gemini(system_instructions, user_prompt, api_key, args.model)

        if not output.lstrip().startswith("\n") and not output.startswith("\n---"):
            # Obsidian needs a blank line before a leading '---' or it reads as YAML frontmatter.
            if output.lstrip().startswith("---"):
                output = "\n" + output

        if target_file.exists() and not args.no_backup:
            backup_path = target_file.with_suffix(target_file.suffix + ".bak")
            backup_path.write_text(target_file.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"  Backed up existing file to {backup_path.name}")

        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(output, encoding="utf-8")
        print(f"  Wrote {len(output)} chars to {target_file}")

    print("\nDone.")


if __name__ == "__main__":
    main()
