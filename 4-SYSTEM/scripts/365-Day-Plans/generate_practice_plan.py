#!/usr/bin/env python3
"""
generate_practice_plan.py — 365-Day Bodhisattvacharyavatara practice plan generator
using Google Gemini Flash.

This is a runnable version of the `bca-practice-plan` skill
(4-SYSTEM/Skills/365-day-practice-plan-generator/SKILL.md). It does the whole
pipeline end to end:

    1. Read the schedule file and look up the chapter + verse range for the given day.
    2. Read the root text and extract the exact verse text.
    3. Read all commentary files and extract the relevant commentary pipeline material.
    4. Send everything to Gemini with the full skill prompt (sections 1–7).
    5. Write the generated content into the correct target file under
       3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/.

--------------------------------------------------------------------------------
Setup
--------------------------------------------------------------------------------
    pip install google-genai
    set GEMINI_API_KEY=...        (Windows)   /   export GEMINI_API_KEY=...  (mac/Linux)

    Alternatively, place a .env file in the vault root (next to 4-SYSTEM/) with:
        GEMINI_API_KEY=your-key-here

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
    python 4-SYSTEM/scripts/365-Day-Plans/generate_practice_plan.py <day>

    # Generate today's practice plan (day 1):
    python 4-SYSTEM/scripts/365-Day-Plans/generate_practice_plan.py 1

    # Pass --dry-run to show what would be generated without calling Gemini:
    python 4-SYSTEM/scripts/365-Day-Plans/generate_practice_plan.py 45 --dry-run

    # Regenerate a day (overwrite existing content):
    python 4-SYSTEM/scripts/365-Day-Plans/generate_practice_plan.py 12 --force

Run with --help for the full option list.
"""

import argparse
import os
import random
import re
import sys
import time
from pathlib import Path

# ------------------------------------------------------------------------------
# .env loader
# ------------------------------------------------------------------------------

def _load_dotenv():
    """Load a .env file — searches cwd, vault root, script dir (first found wins)."""
    candidates = [Path.cwd()]
    for p in Path.cwd().parents:
        if (p / "4-SYSTEM").is_dir():
            candidates.append(p)
            break
    candidates.append(Path(__file__).parent)
    for base in candidates:
        env_file = base / ".env"
        if env_file.exists():
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


_load_dotenv()

# ------------------------------------------------------------------------------
# Defaults
# ------------------------------------------------------------------------------
DEFAULT_MODEL = "gemini-2.5-flash-preview-05-20"
DEFAULT_FALLBACK_MODEL = "gemini-2.0-flash"
MAX_RETRIES = 6
RETRY_BACKOFF_SECONDS = 6
MAX_BACKOFF_SECONDS = 90

# Vault paths (relative to vault root)
SCHEDULE_PATH = "3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/schedule-corrected.md"
ROOT_TEXT_PATH = "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
COMMENTARIES_DIR = "1-SOURCES/Commentaries"
PLANS_DIR = "3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo"

# ------------------------------------------------------------------------------
# Tibetan numeral conversion
# ------------------------------------------------------------------------------
TIB_DIGITS = "༠༡༢༣༤༥༦༧༨༩"

def to_tib_numeral(n: int) -> str:
    """Convert an integer to Tibetan numerals."""
    return "".join(TIB_DIGITS[int(d)] for d in str(n))

# Chapter ordinal forms for headers
CHAPTER_ORDINALS = {
    1:  "དང་པོ།",
    2:  "གཉིས་པ།",
    3:  "གསུམ་པ།",
    4:  "བཞི་པ།",
    5:  "ལྔ་པ།",
    6:  "དྲུག་པ།",
    7:  "བདུན་པ།",
    8:  "བརྒྱད་པ།",
    9:  "དགུ་པ།",
    10: "བཅུ་པ།",
}

VERSE_ORDINALS = {
    1:  "དང་པོ",    2:  "གཉིས་པ",   3:  "གསུམ་པ",   4:  "བཞི་པ",
    5:  "ལྔ་པ",     6:  "དྲུག་པ",    7:  "བདུན་པ",    8:  "བརྒྱད་པ",
    9:  "དགུ་པ",    10: "བཅུ་པ",     11: "བཅུ་གཅིག་པ", 12: "བཅུ་གཉིས་པ",
    13: "བཅུ་གསུམ་པ", 14: "བཅུ་བཞི་པ",  15: "བཅུ་ལྔ་པ",   16: "བཅུ་དྲུག་པ",
    17: "བཅུ་བདུན་པ",  18: "བཅུ་བརྒྱད་པ", 19: "བཅུ་དགུ་པ",  20: "ཉི་ཤུ་པ",
    21: "ཉི་ཤུ་རྩ་གཅིག་པ", 22: "ཉི་ཤུ་རྩ་གཉིས་པ", 23: "ཉི་ཤུ་རྩ་གསུམ་པ",
    24: "ཉི་ཤུ་རྩ་བཞི་པ", 25: "ཉི་ཤུ་རྩ་ལྔ་པ", 26: "ཉི་ཤུ་རྩ་དྲུག་པ",
    27: "ཉི་ཤུ་རྩ་བདུན་པ", 28: "ཉི་ཤུ་རྩ་བརྒྱད་པ", 29: "ཉི་ཤུ་རྩ་དགུ་པ",
    30: "སུམ་ཅུ་པ",
}

def verse_ordinal(n: int) -> str:
    """Return the Tibetan ordinal word for verse number n."""
    if n in VERSE_ORDINALS:
        return VERSE_ORDINALS[n]
    # For numbers beyond 30, fall back to numerals + པ
    return f"{to_tib_numeral(n)}་པ"


# ------------------------------------------------------------------------------
# Vault root detection
# ------------------------------------------------------------------------------

def find_vault_root(start: Path) -> Path:
    """Walk upward looking for the vault root (the dir containing 4-SYSTEM/)."""
    for parent in [start, *start.parents]:
        if (parent / "4-SYSTEM").is_dir():
            return parent
    return start.parent if start.is_file() else start


# ------------------------------------------------------------------------------
# Schedule parsing
# ------------------------------------------------------------------------------

def parse_schedule(schedule_path: Path) -> dict:
    """Parse the schedule file and return a dict mapping day int -> verse string.

    Verse string examples: "1.1–1.3", "Prologue, 1.1–1.3", "1.4–1.5"
    """
    schedule = {}
    text = schedule_path.read_text(encoding="utf-8")
    # Match table rows: | day | verses | ... |
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+)\|", text, re.MULTILINE):
        day = int(m.group(1))
        verses = m.group(2).strip()
        schedule[day] = verses
    return schedule


def parse_verse_entry(verse_str: str) -> tuple[int | None, int, int]:
    """Parse a verse entry like "1.4–1.5" or "Prologue, 1.1–1.3" into
    (chapter, verse_start, verse_end).

    Returns chapter=None for 'Prologue' entries.
    """
    # Handle "Prologue, ..." prefix
    verse_str = re.sub(r"Prologue[,\s]+", "", verse_str).strip()

    # Handle en-dash or hyphen range: "1.4–1.5" or "1.4-1.5"
    range_m = re.match(r"(\d+)\.(\d+)[–\-](\d+)\.(\d+)", verse_str)
    if range_m:
        chapter = int(range_m.group(1))
        v_start = int(range_m.group(2))
        v_end = int(range_m.group(4))
        return chapter, v_start, v_end

    # Single verse: "1.4"
    single_m = re.match(r"(\d+)\.(\d+)$", verse_str)
    if single_m:
        chapter = int(single_m.group(1))
        verse = int(single_m.group(2))
        return chapter, verse, verse

    # Cross-chapter or more complex — return raw
    print(f"  ! Could not parse verse entry: '{verse_str}' — returning as-is",
          file=sys.stderr)
    return None, 1, 1


# ------------------------------------------------------------------------------
# Root text extraction
# ------------------------------------------------------------------------------

def extract_verse_text(root_text_path: Path, chapter: int, verse_start: int,
                       verse_end: int) -> dict[str, str]:
    """Extract verse text from the root text file using block IDs ^chapter-verse.

    Returns a dict {f"{chapter}-{verse}": text} for each requested verse.
    """
    content = root_text_path.read_text(encoding="utf-8")
    results = {}
    for v in range(verse_start, verse_end + 1):
        block_id = f"^{chapter}-{v}"
        # Find the line with this block ID
        # Verses span up to the next block ID or blank line
        # Pattern: lines ending with ^ch-v
        pattern = re.compile(
            r"((?:.*\n)*?.*)" + re.escape(block_id) + r"\s*$",
            re.MULTILINE
        )
        # Simpler: split on block IDs
        # Find the verse block: text between preceding block and this block id
        idx = content.find(block_id)
        if idx == -1:
            print(f"  ! Block ID {block_id} not found in root text", file=sys.stderr)
            results[f"{chapter}-{v}"] = f"[Verse {chapter}.{v} not found]"
            continue

        # Walk back to find the start of this verse block (after previous block ID)
        # Find end of previous block
        before = content[:idx]
        prev_block_end = max(
            before.rfind("\n\n"),
            before.rfind("^"),
        )
        # Grab from last empty line before this block
        nl_idx = before.rfind("\n\n")
        if nl_idx == -1:
            nl_idx = 0
        else:
            nl_idx += 2  # skip the blank line itself

        verse_block = content[nl_idx:idx + len(block_id)].strip()
        # Remove the block ID itself from the end
        verse_block = verse_block[:verse_block.rfind(block_id)].strip()
        # Remove any trailing block IDs from previous verses that may be mixed in
        verse_block = re.sub(r"\^[\d\-]+\s*$", "", verse_block, flags=re.MULTILINE).strip()

        results[f"{chapter}-{v}"] = verse_block

    return results


# ------------------------------------------------------------------------------
# Commentary pipeline extraction
# ------------------------------------------------------------------------------

def extract_commentary_pipeline(commentary_dir: Path, chapter: int,
                                 verse_start: int, verse_end: int) -> list[dict]:
    """For each commentary file, extract the text between each verse's transclusion
    and the next verse transclusion.

    Returns a list of dicts:
      {
        "file": str (filename),
        "verse_key": "chapter-verse",
        "text": str (commentary text for that verse),
        "block_ids": [list of block IDs found in the text]
      }
    """
    results = []
    comm_files = sorted(commentary_dir.glob("*.md"))

    for comm_file in comm_files:
        content = comm_file.read_text(encoding="utf-8")
        # Find transclusion markers like ![[1-SOURCES/Text/...#^ch-v]]
        transclusion_re = re.compile(r"!\[\[[^\]]*#\^([\d\-]+)\]\]")

        # Split content into segments by transclusion
        segments = transclusion_re.split(content)
        # segments: [pre_text, block_id_1, text_1, block_id_2, text_2, ...]

        for v in range(verse_start, verse_end + 1):
            verse_key = f"{chapter}-{v}"
            # Find the segment following our verse transclusion
            i = 1  # start at first block_id
            while i < len(segments):
                seg_block_id = segments[i]
                if seg_block_id == verse_key and i + 1 < len(segments):
                    commentary_text = segments[i + 1]
                    # Trim at next transclusion (which is the next verse's transclusion
                    # line — already split out)
                    # But the text ends where the NEXT block_id begins, which is the
                    # next segment boundary — already clean.
                    # Collect block IDs from the commentary text itself
                    block_ids = re.findall(r"\^([\w\-]+)", commentary_text)
                    commentary_text = commentary_text.strip()
                    if commentary_text:
                        results.append({
                            "file": comm_file.name,
                            "verse_key": verse_key,
                            "text": commentary_text,
                            "block_ids": block_ids,
                        })
                    break
                i += 2

    return results


# ------------------------------------------------------------------------------
# Target file finder
# ------------------------------------------------------------------------------

def find_target_file(plans_dir: Path, day: int, chapter: int,
                     verse_start: int, verse_end: int) -> Path | None:
    """Find the target file for a given day in the plans directory.

    Filename format: Day-{day}-Ch{chapter}-V{verse_start}-{verse_end}.md
    or Day-{day}-Ch{chapter}-V{verse}.md for single-verse days.
    """
    if verse_start == verse_end:
        target_name = f"Day-{day}-Ch{chapter}-V{verse_start}.md"
    else:
        target_name = f"Day-{day}-Ch{chapter}-V{verse_start}-{verse_end}.md"

    # Search all subdirectories
    for path in plans_dir.rglob("*.md"):
        if path.name == target_name:
            return path

    return None


# ------------------------------------------------------------------------------
# Gemini client
# ------------------------------------------------------------------------------

def get_client():
    try:
        from google import genai  # type: ignore
    except ImportError:
        sys.exit(
            "Error: google-genai is not installed.\n"
            "  Install it with:  pip install google-genai"
        )
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "Error: no API key found.\n"
            "  Set the GEMINI_API_KEY environment variable to your Gemini API key.\n"
            "  Or add GEMINI_API_KEY=... to a .env file in the vault root."
        )
    return genai.Client(api_key=api_key)


def _is_overloaded(err) -> bool:
    s = str(err).upper()
    return any(tok in s for tok in (
        "503", "UNAVAILABLE", "OVERLOADED", "HIGH DEMAND",
        "429", "RESOURCE_EXHAUSTED",
    ))


def _generate(client, model: str, system_prompt: str, user_prompt: str,
              fallback_model: str = "", label: str = "request") -> str:
    """Call Gemini with exponential backoff + jitter, plus optional fallback model."""
    try:
        from google.genai import types  # type: ignore
    except ImportError:
        sys.exit("Error: google-genai is not installed.")

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0.7,
    )

    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)

    last_err = None
    for mi, mdl in enumerate(models_to_try):
        if mi > 0:
            print(f"    -> '{model}' still overloaded; falling back to '{mdl}'",
                  file=sys.stderr)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = client.models.generate_content(
                    model=mdl, contents=user_prompt, config=config,
                )
                return (resp.text or "").strip()
            except Exception as e:  # noqa: BLE001
                last_err = e
                if attempt < MAX_RETRIES:
                    base = min(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)),
                               MAX_BACKOFF_SECONDS)
                    wait = base + random.uniform(0, base * 0.25)
                    kind = "overloaded" if _is_overloaded(e) else "error"
                    print(f"    ! {label} attempt {attempt}/{MAX_RETRIES} {kind}: {e}; "
                          f"retrying in {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
        if not _is_overloaded(last_err):
            break
    raise RuntimeError(f"Gemini call failed after retries: {last_err}")


# ------------------------------------------------------------------------------
# Prompt builder
# ------------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are generating a daily practice plan document for the 365-Day Bodhisattvacharyavatara
(སྤྱོད་འཇུག) practice challenge. Your output must be in Tibetan (except Section 7).

Follow these rules exactly:
- All generated prose is in classical Tibetan with a warm, accessible register.
- Never invent or paraphrase root text verses — use only the provided verse texts.
- Never invent commentary — use only the provided commentary pipeline material.
- If content is missing, state this explicitly rather than improvising.
- Section 1 and Section 6 use the FIXED prayer texts provided — reproduce them verbatim.
- Section 2: first person (ངས་ / ང་རང་), 2–4 sentences, ≤60 words; practitioner's voice opening the day.
- Section 3: verse headers follow the specified format; verse text from provided source only.
- Section 4: neutral teacher tone; no first person (ངས་ / ང་རང་ / བདག་གིས་); 3–5 sentences;
  one combined explanation (not per-verse sub-sections); ends with **མཆན།** citation line.
- Section 5: first person singular (ངས་ / ང་རང་ / བདག་གིས་); never ང་ཚོས་; exactly 1 challenge
  in two-part format: bold Tibetan headline + **འགྲེལ་བཤད།** with 2–3 sentences.
- Section 7: English, single paragraph, 80–140 words; Pāla dynasty style; 4:5 portrait.
- Classical Tibetan grammar: avoid Dzongkha patterns, stacked nominalizations, and
  ending paragraphs on subordinate particles.
- Always refer to Śāntideva as རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ།
"""


def build_user_prompt(day: int, chapter: int, verse_start: int, verse_end: int,
                       verse_texts: dict, commentary_pipeline: list) -> str:
    """Build the full user prompt with all source material embedded."""

    tib_day = to_tib_numeral(day)
    chapter_ordinal = CHAPTER_ORDINALS.get(chapter, to_tib_numeral(chapter))
    tib_verse_start = to_tib_numeral(verse_start)
    tib_verse_end = to_tib_numeral(verse_end)

    # Build verse section text
    verse_section_parts = []
    for v in range(verse_start, verse_end + 1):
        key = f"{chapter}-{v}"
        v_text = verse_texts.get(key, f"[Verse {chapter}.{v} not found]")
        v_tib = to_tib_numeral(v)
        v_ord = verse_ordinal(v)
        verse_section_parts.append(
            f"#### **{v_tib}. ཤློཀ་{v_ord}།** (ལེའུ་ {to_tib_numeral(chapter)} ཤློཀ་ {v_tib})\n"
            f"> {v_text}"
        )

    verses_formatted = "\n\n".join(verse_section_parts)

    # Build commentary section text
    if commentary_pipeline:
        comm_parts = []
        for item in commentary_pipeline:
            block_refs = " ".join(f"[[1-SOURCES/Commentaries/{item['file']}#^{bid}|^{bid}]]"
                                  for bid in item["block_ids"][:3])  # sample up to 3
            comm_parts.append(
                f"--- Commentary from {item['file']} (verse {item['verse_key']}) ---\n"
                f"{item['text'][:2000]}\n"  # cap to keep prompt manageable
                f"Block IDs available: {block_refs if block_refs else '(none found)'}"
            )
        commentary_section = "\n\n".join(comm_parts)
    else:
        commentary_section = "(No commentary pipeline material found for these verses.)"

    prompt = f"""Generate a complete 7-section practice plan document for Day {day} of the 365-day Bodhisattvacharyavatara challenge.

DAY: {day}
CHAPTER: {chapter} ({chapter_ordinal})
VERSES: {verse_start}–{verse_end}

=== SOURCE MATERIAL — ROOT VERSES ===
(Use these exactly. Do not quote from memory or training data.)

{verses_formatted}

=== SOURCE MATERIAL — COMMENTARY PIPELINE ===
(All content in Section 4 must come from this material only.)

{commentary_section}

=== OUTPUT FORMAT ===

Generate the complete document below. Use this EXACT structure:

---
# ཉིན་ {tib_day} - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་{chapter_ordinal} ཤློཀ་ {tib_verse_start} - {tib_verse_end}

---

### ༡། སྐྱབས་འགྲོ་སེམས་བསྐྱེད།
#### **༡. ཚད་མེད་བཞི།**
> སེམས་ཅན་ཐམས་ཅད་བདེ་བ་དང་བདེ་བའི་རྒྱུ་དང་ལྡན་པར་གྱུར་ཅིག
> སེམས་ཅན་ཐམས་ཅད་སྡུག་བསྔལ་དང་སྡུག་བསྔལ་གྱི་རྒྱུ་དང་བྲལ་བར་གྱུར་ཅིག
> སེམས་ཅན་ཐམས་ཅད་སྡུག་བསྔལ་མེད་པའི་བདེ་བ་དང་མི་འབྲལ་བར་གྱུར་ཅིག
> སེམས་ཅན་ཐམས་ཅད་ཉེ་རིང་ཆགས་སྡང་གཉིས་དང་བྲལ་བའི་བཏང་སྙོམ་ལ་གནས་པར་གྱུར་ཅིག

#### **༡. སྐྱབས་འགྲོ།**

> བྱང་ཆུབ་སྙིང་པོར་མཆིས་ཀྱི་བར། །
> སངས་རྒྱས་རྣམས་ལ་སྐྱབས་སུ་མཆི། །
> ཆོས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཡི། །
> ཚོགས་ལའང་དེ་བཞིན་སྐྱབས་སུ་མཆི། །

#### **༢. སེམས་བསྐྱེད།**

> ཇི་ལྟར་སྔོན་གྱི་བདེ་གཤེགས་ཀྱིས། །
> བྱང་ཆུབ་ཐུགས་ནི་བསྐྱེད་པ་དང་། །
> བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ། །
> དེ་དག་རིམ་བཞིན་གནས་པ་ལྟར། །

> དེ་བཞིན་འགྲོ་ལ་ཕན་དོན་དུ། །
> བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་བགྱི་ཞིང་། །
> དེ་བཞིན་དུ་ནི་བསླབ་པ་ལའང་། །
> རིམ་པ་བཞིན་དུ་བསླབ་པར་བགྱི། །

---

### ༢། ངོ་སྤྲོད།

[GENERATE: 2–4 sentences, ≤60 words. First person (ངས་/ང་རང་). Practitioner's own voice opening the day and the verse(s) — engaging and drawing a direct living connection to life right now. Not an explanation of the verse.]

---

### ༣། དེ་རིང་གི་རྩ་ཚིག

[GENERATE: Copy the verse text exactly from the SOURCE MATERIAL above. Use the exact headers specified. No commentary here — verses only.]

---

### ༤། འགྲེལ་བཤད།

[GENERATE: 3–5 sentences. Neutral teacher tone (no ངས་/ང་རང་). One combined explanation covering all verses. Source everything from the COMMENTARY PIPELINE above. End with **མཆན།**: citation line listing all block IDs used.]

---

### ༥། ཉམས་སུ་ལེན་ཚུལ།

[GENERATE: Exactly 1 today's challenge.
**[Short Tibetan headline]**
**འགྲེལ་བཤད།** [2–3 sentences first person singular, practical and actionable for daily life.]]

---

### ༦། བསྔོ་བ་དང་སྨོན་ལམ།

####  **༡. བསྔོ་བ།**

> བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
>
> འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
>
> དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
>
> བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །

####  **༢. སྨོན་ལམ།**

> བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
>
> མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
>
> སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
>
> གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །

---

### ༧། Image Generation Prompt

[GENERATE: English, single paragraph, 80–140 words. Pāla dynasty style, jewel tones, 4:5 portrait. Synthesise verse themes, commentary, and today's challenge into one coherent visual story.]
"""
    return prompt


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate a single day's Bodhisattvacharyavatara practice plan.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("day", type=int,
                        help="Day number (1–365)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--fallback-model", default=DEFAULT_FALLBACK_MODEL,
                        help=f"Fallback model on overload (default: {DEFAULT_FALLBACK_MODEL})")
    parser.add_argument("--vault-root", default=None,
                        help="Vault root path (auto-detected if not given)")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing content in the target file")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show plan without calling Gemini or writing files")
    parser.add_argument("--print", action="store_true", dest="print_output",
                        help="Print the generated content to stdout as well as writing it")
    args = parser.parse_args()

    if not 1 <= args.day <= 365:
        sys.exit("Error: day must be between 1 and 365.")

    # --- Locate vault ---
    vault_root = Path(args.vault_root).resolve() if args.vault_root \
        else find_vault_root(Path(__file__).resolve())

    print(f"Vault root:  {vault_root}")
    print(f"Day:         {args.day}")
    print(f"Model:       {args.model}")
    print()

    # --- Read schedule ---
    schedule_path = vault_root / SCHEDULE_PATH
    if not schedule_path.exists():
        sys.exit(f"Error: schedule file not found: {schedule_path}")

    print("Reading schedule ...", end=" ", flush=True)
    schedule = parse_schedule(schedule_path)
    if args.day not in schedule:
        sys.exit(f"Error: Day {args.day} not found in schedule.")
    verse_entry = schedule[args.day]
    print(f"Day {args.day} → {verse_entry}")

    chapter, verse_start, verse_end = parse_verse_entry(verse_entry)
    if chapter is None:
        sys.exit(f"Error: could not parse verse entry '{verse_entry}' for day {args.day}.")

    print(f"Chapter {chapter}, verses {verse_start}–{verse_end}")

    # --- Find target file ---
    plans_dir = vault_root / PLANS_DIR
    target_file = find_target_file(plans_dir, args.day, chapter, verse_start, verse_end)

    if target_file is None:
        print(f"  ! Target file not found in {plans_dir}")
        print("  Creating a new file in the plans directory root ...")
        if verse_start == verse_end:
            fname = f"Day-{args.day}-Ch{chapter}-V{verse_start}.md"
        else:
            fname = f"Day-{args.day}-Ch{chapter}-V{verse_start}-{verse_end}.md"
        target_file = plans_dir / fname
    else:
        print(f"Target file: {target_file.relative_to(vault_root)}")

    # Check if already generated
    if target_file.exists() and not args.force:
        existing = target_file.read_text(encoding="utf-8")
        # Consider "placeholder" content if it lacks section 7 content
        if "### ༧།" in existing and len(existing) > 500:
            print()
            print(f"  Target file already has content. Use --force to regenerate.")
            print(f"  File: {target_file}")
            return

    # --- Read root text ---
    root_text_path = vault_root / ROOT_TEXT_PATH
    if not root_text_path.exists():
        sys.exit(f"Error: root text not found: {root_text_path}")

    print("Reading root text ...", end=" ", flush=True)
    verse_texts = extract_verse_text(root_text_path, chapter, verse_start, verse_end)
    found = sum(1 for v in verse_texts.values() if not v.startswith("[Verse"))
    print(f"{found}/{verse_end - verse_start + 1} verses found")

    # --- Read commentaries ---
    commentary_dir = vault_root / COMMENTARIES_DIR
    if not commentary_dir.exists():
        print(f"  ! Commentary directory not found: {commentary_dir}")
        commentary_pipeline = []
    else:
        comm_files = list(commentary_dir.glob("*.md"))
        print(f"Reading {len(comm_files)} commentary file(s) ...", end=" ", flush=True)
        commentary_pipeline = extract_commentary_pipeline(
            commentary_dir, chapter, verse_start, verse_end)
        print(f"{len(commentary_pipeline)} commentary segment(s) found")

    # --- Dry run ---
    if args.dry_run:
        print()
        print("=== DRY RUN ===")
        print(f"Would generate Day {args.day}: Ch {chapter}, V {verse_start}–{verse_end}")
        print(f"  Verse texts: {list(verse_texts.keys())}")
        print(f"  Commentary segments: {len(commentary_pipeline)}")
        print(f"  Target: {target_file}")
        print("No API call made. Pass without --dry-run to generate.")
        return

    # --- Generate via Gemini ---
    print()
    print("Building prompt ...", end=" ", flush=True)
    user_prompt = build_user_prompt(
        args.day, chapter, verse_start, verse_end,
        verse_texts, commentary_pipeline
    )
    print(f"({len(user_prompt)} chars)")

    print("Calling Gemini ...", flush=True)
    client = get_client()
    generated = _generate(
        client, args.model, SYSTEM_PROMPT, user_prompt,
        fallback_model=args.fallback_model,
        label=f"day-{args.day}"
    )

    # --- Write output ---
    target_file.parent.mkdir(parents=True, exist_ok=True)
    target_file.write_text(generated, encoding="utf-8")

    print()
    print(f"✓ Done. Written to: {target_file.relative_to(vault_root)}")
    print(f"  ({len(generated)} chars, {len(generated.splitlines())} lines)")

    if args.print_output:
        print()
        print("=== GENERATED CONTENT ===")
        print(generated)


if __name__ == "__main__":
    main()
