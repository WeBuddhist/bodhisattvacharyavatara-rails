#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format the Tibetan root text of Bodhisattvacharyavatara (BCA).
Run this script from anywhere:
    python format_bca.py

It modifies the .md file in 1-SOURCES/Translations/ in place.
"""

import re, os, sys

# ─── Locate the file ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(SCRIPT_DIR, '1-SOURCES', 'Translations')
files = [f for f in os.listdir(BASE) if f.endswith('.md')]
print("MD files found:", files)
if not files:
    sys.exit("No .md file found in " + BASE)
INPUT = os.path.join(BASE, files[0])
print(f"Processing: {INPUT}")

# ─── Chapter start verse numbers (absolute, 1-indexed) ───────────────────────
# Chapter N begins at this absolute verse number.
CHAPTER_STARTS = {
    1: 1,   2: 40,  3: 107, 4: 142, 5: 192,
    6: 304, 7: 444, 8: 523, 9: 710, 10: 885
}

def ch_for_abs(n):
    """Return which chapter absolute verse n belongs to."""
    ch = 1
    for num in sorted(CHAPTER_STARTS):
        if n >= CHAPTER_STARTS[num]:
            ch = num
        else:
            break
    return ch

def rel_verse(abs_v, ch):
    """Chapter-relative verse number."""
    return abs_v - CHAPTER_STARTS[ch] + 1

# ─── Colophon detection ───────────────────────────────────────────────────────
COLOPHON_MARKER = 'འཇུག་པ་ལས'   # appears in every chapter colophon

SHAD_PAIR = '། །'               # verse-line separator

# Matches a mid-verse line break: space + shad directly followed by Tibetan text.
# Examples: "ཞིག །ན", "གི །ས", "གོ །བ" — two half-verses merged onto one line.
# Lookbehind (?<![།]) prevents matching the 2nd shad inside a '། །' pair.
# Lookahead (?=[^\s།]) prevents matching a shad at end-of-line or before another shad.
MID_LINE_SHAD = re.compile(r'(?<![།]) །(?=[^\s།])')

# ─── Helpers ──────────────────────────────────────────────────────────────────
def has_tibetan(line):
    return bool(re.search(r'[ༀ-࿿]', line))

def is_number_only(line):
    return bool(re.match(r'^\s*\d+\s*$', line.strip()))

def clean_existing_id(line):
    """Remove old block IDs from the end of a line (e.g. ^1-2 or bare 1-2)."""
    line = re.sub(r'\s*\^\S+\s*$', '', line)
    line = re.sub(r'\s+\d+-\d+\s*$', '', line)
    return line.rstrip()

def block_id(ch, rel):
    return f'^{ch}-{rel}'

def split_stanza(text):
    """Split a merged verse into individual lines.

    Handles two separators:
      1. SHAD_PAIR '། །' — standard verse-line end (shad-space-shad).
      2. MID_LINE_SHAD: a single shad immediately preceded by a space and
         followed by a Tibetan syllable (no space/shad after). This is the
         mid-verse line break — e.g. 'ཞིག །ན', 'གི །ས', 'གོ །བ'.
         The first half-line keeps its trailing ' །'; the second starts fresh.

    A null-byte sentinel (\x00) is inserted at mid-verse break points before
    the SHAD_PAIR split so both split types are handled cleanly.
    """
    text = text.strip()
    if not text:
        return []

    # Insert sentinel after each mid-verse break (the ' །' is kept; \x00 marks split)
    text = MID_LINE_SHAD.sub(r' །\x00', text)

    parts = text.split(SHAD_PAIR)
    lines = []

    for seg in parts[:-1]:
        s = seg.strip()
        if not s:
            continue
        sub = s.split('\x00')
        for j, piece in enumerate(sub):
            piece = piece.strip()
            if not piece:
                continue
            if j < len(sub) - 1:
                lines.append(piece)            # already ends with ' །'
            else:
                lines.append(piece + SHAD_PAIR)  # restore full verse-line ending

    last = parts[-1].strip()
    if last:
        sub = last.split('\x00')
        for j, piece in enumerate(sub):
            piece = piece.strip()
            if not piece:
                continue
            lines.append(piece)  # last segment: keep as-is (may end with ' །' or nothing)

    return lines

def format_stanza(raw_lines, ch, rel):
    """Combine accumulated lines, split if merged, and append block ID."""
    combined = ' '.join(l.strip() for l in raw_lines if l.strip())
    combined = clean_existing_id(combined).strip()
    if not combined:
        return []
    bid = block_id(ch, rel)
    vlines = split_stanza(combined)
    if not vlines:
        return [combined + ' ' + bid]
    result = []
    for i, vl in enumerate(vlines):
        result.append(vl + ' ' + bid if i == len(vlines) - 1 else vl)
    return result

def strip_colophon(line):
    """Remove chapter colophon text from a line, returning only the verse portion."""
    # Try the full colophon opener first (most specific, avoids false positives)
    full_opener = 'བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་ལས'
    idx = line.find(full_opener)
    if idx != -1:
        return line[:idx].rstrip()
    # Fallback: cut at the COLOPHON_MARKER
    idx = line.find(COLOPHON_MARKER)
    if idx != -1:
        return line[:idx].rstrip()
    return line

def make_heading(ch_num, leu, ordinal, name):
    return f'## {ch_num}. {leu}{ordinal}། {name} ^TOC-{ch_num}'

def extract_chapter_info(col_text):
    """Extract (leu_word, ordinal, chapter_name) from a colophon line."""
    m_ord = re.search(r'(ལེའུ་)(?:སྟེ་)?(\S+?)འོ', col_text)
    if m_ord:
        leu     = m_ord.group(1)
        ordinal = m_ord.group(2).rstrip('་།')
    else:
        leu     = 'ལེའུ་'
        ordinal = '?'
    m_name = re.search(
        r'འཇུག་པ་ལས[་།\s]+([\s\S]+?)(?:་ཞེས་བྱ་བ་སྟེ་|་སྟེ་ལེའུ་|འི་ལེའུ་|་ལེའུ་)',
        col_text
    )
    if m_name:
        name = m_name.group(1).strip().rstrip('་').strip() + '།'
    else:
        name = ordinal + '།'
    return leu, ordinal, name

# ─── Read the file ─────────────────────────────────────────────────────────────
with open(INPUT, 'r', encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f.readlines()]
print(f"Read {len(lines)} lines")

# ─── Pass 1: extract chapter headings from colophons ──────────────────────────
chapter_headings = {}
colophon_count = 0
for line in lines:
    if COLOPHON_MARKER in line and '།།' in line:
        colophon_count += 1
        if colophon_count <= 10:
            try:
                leu, ordinal, name = extract_chapter_info(line)
                chapter_headings[colophon_count] = make_heading(colophon_count, leu, ordinal, name)
                print(f"  Ch.{colophon_count}: {chapter_headings[colophon_count]}")
            except Exception as e:
                print(f"  Ch.{colophon_count} extraction error: {e}")
                chapter_headings[colophon_count] = f'## {colophon_count}. ^TOC-{colophon_count}'

print(f"Found {colophon_count} colophons")
if colophon_count < 10:
    print("WARNING: fewer than 10 colophons found — check file encoding.")

# ─── Pass 2: reformat lines 34+ (keep intro lines 1-33 unchanged) ─────────────
# The intro (lines 1-33) already contains: TOC, title, 0.1/0.2 stanzas with
# block IDs, and the Chapter 1 heading. We do not touch those.
INTRO_END = 33
output = list(lines[:INTRO_END])
process_lines = lines[INTRO_END:]

current_chapter  = 1
chapters_headed  = {1}       # ch.1 heading already present in intro
pending_abs      = None      # absolute verse# for the stanza being accumulated
stanza_lines     = []
last_abs_verse   = 0
colophons_seen   = 0
past_all_chapters = False
prev_was_blank   = False

def flush(out, s_lines, abs_v, last_abs, ch):
    """Format and append the accumulated stanza to out."""
    if not s_lines:
        return last_abs
    if abs_v is None:
        abs_v = last_abs + 1
    r = rel_verse(abs_v, ch)
    for fl in format_stanza(s_lines, ch, r):
        out.append(fl)
    return abs_v

for line in process_lines:

    # After all 10 chapter colophons: pass remaining lines through verbatim
    if past_all_chapters:
        output.append(line)
        prev_was_blank = (line.strip() == '')
        continue

    # ── Blank line ──────────────────────────────────────────────────────────
    if line.strip() == '':
        if stanza_lines:
            last_abs_verse = flush(output, stanza_lines, pending_abs,
                                   last_abs_verse, current_chapter)
            stanza_lines = []
            pending_abs  = None
        if not prev_was_blank:
            output.append('')
        prev_was_blank = True
        continue

    prev_was_blank = False

    # ── Standalone verse number ─────────────────────────────────────────────
    if is_number_only(line):
        if stanza_lines:
            last_abs_verse = flush(output, stanza_lines, pending_abs,
                                   last_abs_verse, current_chapter)
            stanza_lines = []
            pending_abs  = None
        abs_v   = int(line.strip())
        pending_abs = abs_v
        new_ch  = ch_for_abs(abs_v)
        if new_ch != current_chapter:
            current_chapter = new_ch
            if new_ch not in chapters_headed:
                while output and output[-1] == '':
                    output.pop()
                output.append('')
                output.append(chapter_headings.get(new_ch, f'## {new_ch}. ^TOC-{new_ch}'))
                output.append('')
                chapters_headed.add(new_ch)
                prev_was_blank = True
        continue   # discard the number line itself

    # ── Markdown heading ────────────────────────────────────────────────────
    if line.strip().startswith('#'):
        if stanza_lines:
            last_abs_verse = flush(output, stanza_lines, pending_abs,
                                   last_abs_verse, current_chapter)
            stanza_lines = []
            pending_abs  = None
        output.append(line)
        continue

    # ── Tibetan text ────────────────────────────────────────────────────────
    if has_tibetan(line):
        if COLOPHON_MARKER in line and '།།' in line:
            # ── Chapter-end colophon ──────────────────────────────────────
            colophons_seen += 1
            stanza_part = strip_colophon(line).strip()
            if stanza_part:
                stanza_lines.append(stanza_part)
            if stanza_lines:
                last_abs_verse = flush(output, stanza_lines, pending_abs,
                                       last_abs_verse, current_chapter)
                stanza_lines = []
                pending_abs  = None
            if colophons_seen >= 10:
                past_all_chapters = True
        else:
            stanza_lines.append(line)

    else:
        # Non-Tibetan, non-number, non-blank, non-heading line
        if stanza_lines:
            last_abs_verse = flush(output, stanza_lines, pending_abs,
                                   last_abs_verse, current_chapter)
            stanza_lines = []
            pending_abs  = None
        output.append(line)

# Flush any stanza remaining at end of file
if stanza_lines:
    flush(output, stanza_lines, pending_abs, last_abs_verse, current_chapter)

# ─── Remove consecutive blank lines ───────────────────────────────────────────
cleaned = []
pb = False
for line in output:
    if line == '':
        if not pb:
            cleaned.append(line)
        pb = True
    else:
        cleaned.append(line)
        pb = False

# ─── Write back to the original file ──────────────────────────────────────────
with open(INPUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(cleaned) + '\n')

print(f"\nDone! {len(cleaned)} lines written (was {len(lines)}).")
print(f"File: {INPUT}")
