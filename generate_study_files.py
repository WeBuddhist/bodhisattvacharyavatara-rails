#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
སྤྱོད་འཇུག་ཉིན་ ༣༦༥ ཀྱི་སློབ་སྦྱོང་འཆར་གཞི་བཟོ་བའི་ལས་རིམ། — Version 2

Each day file contains five sections:
  1. སྐྱབས་འགྲོ།      — fixed refuge prayer
  2. སེམས་བསྐྱེད།     — fixed bodhicitta aspiration/engagement prayer
  3. ཚིགས་བཅད།       — day's verse(s) with sa bcad heading
  4. འགྲེལ་བཤད།      — Kunpal commentary for those verses
  5. གནད་ཚིག         — key terms from the verse, explained by the commentary

Run from anywhere:
    python generate_study_files.py

No dependencies beyond the Python standard library.
"""

import re
import os

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT_TEXT = (
    r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails"
    r"\0-INBOX\bo-root versions"
    r"\bo-བློ་ལྡན་ཤེས་རབ།-ཀུན་དཔལ་སྤྱོད་འཇུག་རྩ་བ།.md"
)
COMMENTARY = (
    r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails"
    r"\1-SOURCES\Commentaries"
    r"\bo-མཁན་པོ་ཀུན་དཔལ།.md"
)
OUTPUT_DIR = (
    r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails"
    r"\3-TRANSFORMATIONS\སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།"
)

# ── Fixed opening prayers ─────────────────────────────────────────────────────

SKYABS_DRO = (
    "སངས་རྒྱས་ཆོས་དང་ཚོགས་ཀྱི་མཆོག་རྣམས་ལ། །\n"
    "བྱང་ཆུབ་བར་དུ་བདག་ནི་སྐྱབས་སུ་མཆི། །\n"
    "བདག་གིས་སྦྱིན་སོགས་བགྱིས་པའི་བསོད་ནམས་ཀྱིས། །\n"
    "འགྲོ་ལ་ཕན་ཕྱིར་སངས་རྒྱས་འགྲུབ་པར་ཤོག །"
)

SEMS_BSKYED = (
    "ཇི་ལྟར་སྔོན་གྱི་བདེ་གཤེགས་ཀྱིས། །\n"
    "བྱང་ཆུབ་ཐུགས་ནི་བསྐྱེད་པ་དང་། །\n"
    "བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ། །\n"
    "དེ་དག་རིམ་བཞིན་གནས་པ་ལྟར། །\n"
    "དེ་བཞིན་འགྲོ་ལ་ཕན་དོན་དུ། །\n"
    "བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་བགྱི་ཞིང་། །\n"
    "དེ་བཞིན་དུ་ནི་བསླབ་པ་ལའང་། །\n"
    "རིམ་པ་བཞིན་དུ་བསླབ་པར་བགྱི། །"
)

BSNGO_BA = (
    "བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །\n"
    "མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །\n"
    "སྐྱེས་པ་ཉམས་པ་མེད་པ་དང། །\n"
    "གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །\n"
    "\n"
    "འཇམ་དཔལ་དཔའ་བོས་ཇི་ལྟར་མཁྱེན་པ་དང༌། །\n"
    "ཀུན་ཏུ་བཟང་པོ་དེ་ཡང་དེ་བཞིན་ཏེ། །\n"
    "དེ་དག་ཀུན་གྱི་རྗེས་སུ་བདག་སློབ་ཅིང༌། །\n"
    "དགེ་བ་འདི་དག་ཐམས་ཅད་རབ་ཏུ་བསྔོ། །"
)

# ── Tibetan digit conversion ───────────────────────────────────────────────────
_TDIG = str.maketrans("0123456789", "༠༡༢༣༤༥༦༧༨༩")

def to_tib(n: int) -> str:
    return str(n).translate(_TDIG)


# ── Patterns ───────────────────────────────────────────────────────────────────
ITEM_RE      = re.compile(r"^(\d+)\.\s+(.*)")
HEADING_RE   = re.compile(r"^(#{2,4})\s+(.+)")
COLOPHON_RE  = re.compile(r"ལེའུ.{1,20}འོ།།")
SKIP_WORDS   = ["རྒྱ་གར་གྱི་མཁན་པོ", "རྫོགས་སོ།།"]


# ── Parse root text ────────────────────────────────────────────────────────────

def parse_root_text(path):
    """
    Return list of dicts: {num, text, heading}
    Tracks ## / ### / #### Markdown headings as sa bcad context.
    Skips items before the first heading, blanks, colophons, skip-words.
    """
    verses = []
    current_heading = ""
    first_heading_seen = False

    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")

            # Track headings
            hm = HEADING_RE.match(line)
            if hm:
                current_heading = line.strip()
                first_heading_seen = True
                continue

            if not first_heading_seen:
                continue

            # Numbered item
            im = ITEM_RE.match(line)
            if not im:
                continue

            num  = int(im.group(1))
            text = im.group(2).strip()

            if not text:
                continue
            if any(w in text for w in SKIP_WORDS):
                continue
            if COLOPHON_RE.search(text):
                continue

            verses.append({"num": num, "text": text, "heading": current_heading})

    return verses


# ── Parse commentary ────────────────────────────────────────────────────────────

def parse_commentary(path):
    """
    Return dict {item_num: text}.
    Root text item N -> commentary item N + 4  (offset due to root text renumbering).
    """
    comm = {}
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            m = ITEM_RE.match(raw.rstrip("\n"))
            if m:
                num  = int(m.group(1))
                text = m.group(2).strip()
                if text:
                    comm[num] = text
    return comm


# ── Format verse with pada line-breaks ────────────────────────────────────────

def format_verse(text):
    """Split on '། །' so each pada is on its own line."""
    parts = re.split(r"(། །)", text.strip())
    lines = []
    i = 0
    while i < len(parts):
        seg = parts[i].strip()
        sep = parts[i + 1] if i + 1 < len(parts) else ""
        i += 2
        if seg:
            lines.append(seg + (sep if sep else ""))
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) if lines else text


# ── Extract key terms from verse with commentary explanations ──────────────────

def extract_key_terms(verse_text, comm_text, max_terms=5):
    """
    Find meaningful sub-phrases from the verse that appear verbatim in the
    commentary, and return the surrounding commentary sentence as explanation.

    Rules:
    - Only terms that genuinely appear in the commentary are returned.
    - No fabrication: all explanations are verbatim excerpts from comm_text.
    - Tries 5->3 syllable phrases per pada, most specific first.
    - Extracts the shad-bounded sentence containing the matched phrase.

    Returns: list of (term_str, explanation_str)
    """
    if not comm_text:
        return []

    results = []
    seen    = set()

    # Process each pada of the verse
    padas = re.split(r"།\s*།|།།", verse_text)

    for pada in padas:
        pada = pada.strip().strip("།").strip()
        if not pada:
            continue

        # Syllables: split on tsek (་), ignore single-char fragments
        syllables = [s for s in re.split(r"་+", pada) if len(s) > 1]
        if len(syllables) < 3:
            continue

        matched = False
        for length in range(min(5, len(syllables)), 2, -1):
            for start in range(len(syllables) - length + 1):
                candidate = "་".join(syllables[start : start + length])

                if len(candidate) < 5 or candidate in seen:
                    continue

                pos = comm_text.find(candidate)
                if pos < 0:
                    continue

                # ── Extract surrounding sentence ───────────────────────────
                # Look back up to 100 chars for a sentence boundary
                look_back = max(0, pos - 100)
                preceding = comm_text[look_back:pos]
                last_bound = max(
                    preceding.rfind("།"),
                    preceding.rfind("ཏེ་"),
                    preceding.rfind("ནས་"),
                )
                sent_start = (look_back + last_bound + 1) if last_bound >= 0 else look_back

                # Look forward up to 200 chars for next shad
                look_fwd  = min(len(comm_text), pos + len(candidate) + 200)
                following = comm_text[pos + len(candidate) : look_fwd]
                next_shad = following.find("།")
                if next_shad >= 0:
                    sent_end = pos + len(candidate) + next_shad + 1
                else:
                    sent_end = look_fwd

                explanation = comm_text[sent_start:sent_end].strip()

                # Quality filters
                if 12 <= len(explanation) <= 400:
                    seen.add(candidate)
                    results.append((candidate, explanation))
                    matched = True
                    break  # one term per pada preferred

            if matched:
                break  # move to next pada

        if len(results) >= max_terms:
            break

    return results


# ── Day division ───────────────────────────────────────────────────────────────

def assign_days(verses):
    """
    Divide verse list into 365 day-batches.
    Days 1..extra get (base+1) verses; days (extra+1)..365 get base verses.
    """
    total = len(verses)
    base  = total // 365
    extra = total % 365
    days  = []
    idx   = 0
    for day in range(1, 366):
        count = base + (1 if day <= extra else 0)
        days.append(verses[idx : idx + count])
        idx += count
    return days


# ── Build one day file ─────────────────────────────────────────────────────────

def build_file(day_num, verse_list, comm_dict):
    tnum = to_tib(day_num)
    out  = []

    # ── Title ──────────────────────────────────────────────────────────────────
    out.append(f"# {tnum}། — སྤྱོད་འཇུག་སློབ་སྦྱོང་།")
    out.append("")

    # ── Section 1: Refuge ──────────────────────────────────────────────────────
    out.append("## ༡། སྐྱབས་འགྲོ།")
    out.append("")
    out.append(SKYABS_DRO)
    out.append("")

    # ── Section 2: Bodhicitta ──────────────────────────────────────────────────
    out.append("## ༢། སེམས་བསྐྱེད།")
    out.append("")
    out.append(SEMS_BSKYED)
    out.append("")

    # ── Section 3: Verse(s) with sa bcad heading ───────────────────────────────
    out.append("## ༣། དེ་རིང་གི་སྤྱོད་འཇུག་སློབ་ཚན།")
    out.append("")
    last_heading = None
    for v in verse_list:
        # Emit heading only when it changes
        if v["heading"] and v["heading"] != last_heading:
            out.append(v["heading"])
            out.append("")
            last_heading = v["heading"]
        out.append(format_verse(v["text"]))
        out.append("")

    # ── Section 4: Commentary ──────────────────────────────────────────────────
    out.append("## ༤། འགྲེལ་བཤད།")
    out.append("")
    for v in verse_list:
        comm_key = v["num"] + 4
        comm = comm_dict.get(comm_key, "")
        if comm:
            out.append(comm)
            out.append("")
        else:
            out.append("*(commentary not found)*")
            out.append("")

    # ── Section 5: Key terms ───────────────────────────────────────────────────
    # Collect terms across all verses for the day; deduplicate
    day_terms  = []
    seen_terms = set()
    for v in verse_list:
        comm_key = v["num"] + 4
        comm = comm_dict.get(comm_key, "")
        for (term, gloss) in extract_key_terms(v["text"], comm):
            if term not in seen_terms:
                seen_terms.add(term)
                day_terms.append((term, gloss))

    out.append("## ༥། གནད་ཚིག")
    out.append("")
    if day_terms:
        for (term, gloss) in day_terms:
            out.append(f"**{term}**")
            out.append(f"{gloss}")
            out.append("")
    else:
        out.append("*(གནད་ཚིག་གོང་གི་འགྲེལ་བཤད་ལས་ཞིབ་ཕྲར་གཟིགས་རོགས།)*")
        out.append("")

    # ── Section 6: Dedication ──────────────────────────────────────────────────
    out.append("## ༦། བསྔོ་བ།")
    out.append("")
    out.append(BSNGO_BA)
    out.append("")

    return "\n".join(out)


# ── Filename ───────────────────────────────────────────────────────────────────

def day_filename(day_num):
    return f"ཉིན་ {to_tib(day_num)}།.md"


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("སྤྱོད་འཇུག་སློབ་སྦྱོང་། ཉིན་ ༣༦༥། — ཡིག་ཆ་བཟོ་བཞིན་པ།")
    print()

    print("  རྩ་བ་ཀློག་བཞིན་པ།...")
    verses = parse_root_text(ROOT_TEXT)
    print(f"    -> ཚིགས་བཅད་གྲངས། {len(verses)}")

    print("  འགྲེལ་བ་ཀློག་བཞིན་པ།...")
    comm = parse_commentary(COMMENTARY)
    print(f"    -> འགྲེལ་བཤད་ཁག {len(comm)}")

    print("  ཉིན་ ༣༦༥ ལ་བགོ་བཞིན་པ།...")
    days  = assign_days(verses)
    total = len(verses)
    base  = total // 365
    extra = total % 365
    print(f"    -> ཉིན་རེར་ཚིགས་བཅད་ {base}-{base+1}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"  ཡིག་ཆ་འབྲི་བཞིན་པ།...")
    terms_total = 0
    for day_num, verse_list in enumerate(days, start=1):
        content = build_file(day_num, verse_list, comm)
        terms_total += content.count("\n**")
        filepath = os.path.join(OUTPUT_DIR, day_filename(day_num))
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)
        if day_num % 50 == 0 or day_num == 365:
            print(f"    ཉིན་ {to_tib(day_num)} ལེགས་གྲུབ།")

    print()
    print("ལེགས་གྲུབ། ཡིག་ཆ་ ༣༦༥ བཀོད་ཟིན།")
    print()
    print("གྲུབ་འབྲས་གཞི་གྲངས།:")
    print(f"  ཚིགས་བཅད་གྲངས།          {total}")
    print(f"  འགྲེལ་བཤད་གྲངས།          {len(comm)}")
    print(f"  གནད་ཚིག་རྙེད་པའི་གྲངས།  {terms_total}")
    print(f"  ཁ་ཕྱོགས།                 {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
