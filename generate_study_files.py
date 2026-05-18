#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
སྤྱོད་འཇུག་ཉིན་ ༣༦༥ ཀྱི་སློབ་སྦྱོང་འཆར་གཞི་བཟོ་བའི་ལས་རིམ། — Version 3

Each day file contains six sections:
  1. སྐྱབས་འགྲོ།      — fixed refuge prayer
  2. སེམས་བསྐྱེད།     — fixed bodhicitta prayer
  3. ཚིགས་བཅད།       — day's verse(s) with sa bcad heading
  4. འགྲེལ་བཤད།      — Kunpal commentary for those verses
  5. གནད་ཚིག         — key terms from the verse, explained by the commentary
  6. བསྔོ་བ།          — fixed dedication

SOURCE FILE FORMAT:
  Root text: Markdown headings (## / ### / ####) + plain verse blocks.
  No item numbers. One verse per blank-line-delimited block.

COMMENTARY OFFSET:
  Root text has 3 visible preamble blocks (Sanskrit title, Tibetan title,
  homage). The commentary retains 5 preamble items (two were removed from
  the root text by a previous edit). So for study verses:
      commentary_key = seq_number + 2
  where seq_number counts ALL blocks from 1, including the 3 preamble blocks.

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

# Commentary offset: commentary_key = block_seq + COMM_OFFSET
# Derived from: block seq 4 (intro verse 1) -> commentary item 6  => offset 2
#               block seq 8 (Ch1 verse 1)   -> commentary item 10 => offset 2
COMM_OFFSET = 2

# ── Fixed prayers ─────────────────────────────────────────────────────────────

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

def to_tib(n):
    return str(n).translate(_TDIG)

# ── Patterns ───────────────────────────────────────────────────────────────────
HEADING_RE  = re.compile(r"^(#{1,4})\s+(.+)")
COLOPHON_RE = re.compile(r"ལེའུ.{1,20}འོ།།")
SKIP_WORDS  = ["རྒྱ་གར་གྱི་མཁན་པོ", "རྫོགས་སོ།།"]

# Preamble blocks: these text patterns identify items to skip entirely
PREAMBLE_MARKERS = [
    "རྒྱ་གར་སྐད་དུ།",   # Sanskrit title line
    "བོད་སྐད་དུ།",       # Tibetan title line
    "ཕྱག་འཚལ་ལོ།",      # Translator homage
]

# Commentary item-line pattern
COMM_ITEM_RE = re.compile(r"^(\d+)\.\s+(.*)")

# ── Parse root text ────────────────────────────────────────────────────────────

def parse_root_text(path):
    """
    Parse root text in heading + verse-block format (no item numbers).

    Groups consecutive non-blank, non-heading lines into blocks.
    Assigns a sequential block number (seq) starting from 1, counting
    ALL blocks including preamble.

    Returns list of dicts: {seq, text, heading}
    - seq      : sequential block number (used to compute commentary key)
    - text     : raw verse text (padas separated by newlines)
    - heading  : the most recent Markdown heading line above this block

    Skipped automatically:
    - Preamble blocks (Sanskrit title, Tibetan title, homage)
    - Chapter colophons
    - Blocks containing skip-words
    """
    result       = []
    current_head = ""
    buf          = []     # lines accumulating for the current block
    seq          = 0      # global block counter (counts skipped blocks too)

    def flush():
        nonlocal seq
        if not buf:
            return
        seq += 1
        text = "\n".join(buf)
        # Skip preamble
        if any(m in text for m in PREAMBLE_MARKERS):
            return
        # Skip colophons
        if COLOPHON_RE.search(text):
            return
        # Skip translator notes
        if any(w in text for w in SKIP_WORDS):
            return
        result.append({"seq": seq, "text": text, "heading": current_head})

    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")

            hm = HEADING_RE.match(line)
            if hm:
                flush()
                buf = []
                current_head = line.strip()
                continue

            stripped = line.strip()
            if not stripped:
                flush()
                buf = []
                continue

            buf.append(stripped)

    flush()
    return result


# ── Parse commentary ────────────────────────────────────────────────────────────

def parse_commentary(path):
    """
    Return dict {item_num: text}.
    Commentary file uses numbered items: 'NNN. commentary text...'
    Commentary key for root verse = verse.seq + COMM_OFFSET
    """
    comm = {}
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            m = COMM_ITEM_RE.match(raw.rstrip("\n"))
            if m:
                num  = int(m.group(1))
                text = m.group(2).strip()
                if text:
                    comm[num] = text
    return comm


# ── Format verse ───────────────────────────────────────────────────────────────

def format_verse(text):
    """
    Ensure each pada is on its own line ending with '། །'.
    Input may already be multi-line (one pada per line).
    """
    # Split on pada boundary marker, keeping the separator
    parts = re.split(r"(། །)", text.strip())
    lines = []
    i = 0
    while i < len(parts):
        seg = parts[i].strip()
        sep = parts[i + 1] if i + 1 < len(parts) else ""
        i  += 2
        if seg:
            lines.append(seg + (sep if sep else ""))
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) if lines else text.strip()


# ── Extract key terms ──────────────────────────────────────────────────────────

def extract_key_terms(verse_text, comm_text, max_terms=5):
    """
    Find meaningful sub-phrases from the verse that appear verbatim in the
    commentary. Returns surrounding commentary context as explanation.

    All explanations are direct verbatim excerpts — no fabrication.
    Returns: list of (term_str, explanation_str)
    """
    if not comm_text:
        return []

    results = []
    seen    = set()

    padas = re.split(r"།\s*།|།།", verse_text)

    for pada in padas:
        pada = pada.strip().strip("།").strip()
        if not pada:
            continue

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

                # Extract surrounding sentence
                look_back  = max(0, pos - 100)
                preceding  = comm_text[look_back:pos]
                last_bound = max(
                    preceding.rfind("།"),
                    preceding.rfind("ཏེ་"),
                    preceding.rfind("ནས་"),
                )
                sent_start = (look_back + last_bound + 1) if last_bound >= 0 else look_back

                look_fwd   = min(len(comm_text), pos + len(candidate) + 200)
                following  = comm_text[pos + len(candidate) : look_fwd]
                next_shad  = following.find("།")
                sent_end   = pos + len(candidate) + next_shad + 1 if next_shad >= 0 else look_fwd

                explanation = comm_text[sent_start:sent_end].strip()

                if 12 <= len(explanation) <= 400:
                    seen.add(candidate)
                    results.append((candidate, explanation))
                    matched = True
                    break

            if matched:
                break

        if len(results) >= max_terms:
            break

    return results


# ── Day division ───────────────────────────────────────────────────────────────

def assign_days(verses):
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

    # Title
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
        comm_key = v["seq"] + COMM_OFFSET
        comm = comm_dict.get(comm_key, "")
        if comm:
            out.append(comm)
            out.append("")
        else:
            out.append(f"*(commentary not found — key {comm_key})*")
            out.append("")

    # ── Section 5: Key terms ───────────────────────────────────────────────────
    day_terms  = []
    seen_terms = set()
    for v in verse_list:
        comm_key = v["seq"] + COMM_OFFSET
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
            out.append(gloss)
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

def day_filename(n):
    return f"ཉིན་ {to_tib(n)}།.md"


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("སྤྱོད་འཇུག་སློབ་སྦྱོང་། ཉིན་ ༣༦༥།")
    print()

    print(f"  རྩ་བ་ཀློག་བཞིན་པ།  {ROOT_TEXT}")
    verses = parse_root_text(ROOT_TEXT)
    print(f"    -> ཚིགས་བཅད་གྲངས། {len(verses)}")
    if verses:
        print(f"    -> seq range: {verses[0]['seq']} .. {verses[-1]['seq']}")
        print(f"    -> first verse: {verses[0]['text'][:60]}")

    print(f"  འགྲེལ་བ་ཀློག་བཞིན་པ།  {COMMENTARY}")
    comm = parse_commentary(COMMENTARY)
    print(f"    -> འགྲེལ་བཤད་གྲངས། {len(comm)}")

    # Verify offset: first verse should match commentary key = seq + COMM_OFFSET
    if verses and comm:
        v0 = verses[0]
        ckey = v0["seq"] + COMM_OFFSET
        sample = comm.get(ckey, "NOT FOUND")[:80]
        print(f"    -> offset check: verse seq={v0['seq']} "
              f"-> commentary[{ckey}]: {sample}")

    total = len(verses)
    base  = total // 365
    extra = total % 365
    print(f"  ཉིན་རེར་ཚིགས་བཅད་ {base}-{base+1} (ཉིན་ {extra} ལ་ {base+1})")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"  ཡིག་ཆ་འབྲི་བཞིན་པ།  {OUTPUT_DIR}")
    days = assign_days(verses)
    terms_total = 0
    comm_found  = 0
    for day_num, verse_list in enumerate(days, start=1):
        content = build_file(day_num, verse_list, comm)
        terms_total += content.count("\n**")
        # Count days where commentary was found
        for v in verse_list:
            if comm.get(v["seq"] + COMM_OFFSET):
                comm_found += 1
        filepath = os.path.join(OUTPUT_DIR, day_filename(day_num))
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)
        if day_num % 50 == 0 or day_num == 365:
            print(f"    ཉིན་ {to_tib(day_num)} ལེགས་གྲུབ།")

    print()
    print("ལེགས་གྲུབ། ཡིག་ཆ་ ༣༦༥ བཀོད་ཟིན།")
    print()
    print("གྲུབ་འབྲས་གཞི་གྲངས།:")
    print(f"  ཚིགས་བཅད་གྲངས།               {total}")
    print(f"  འགྲེལ་བཤད་རྙེད་ཚིགས་བཅད།     {comm_found}")
    print(f"  གནད་ཚིག་རྙེད་པའི་གྲངས།        {terms_total}")
    print(f"  ཁ་ཕྱོགས།                       {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
