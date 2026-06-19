#!/usr/bin/env python3
"""
verse-context-batch-ch2.py
Generate 2-RAILS/Verses/2-1.md through 2-RAILS/Verses/2-65.md
for BCA Chapter 2 (sdig pa bshags pa / Confession).

Phase 2 block mapping built from reading:
  Kunpal:           sequential scan, blocks ^0-323 to ^0-634
  Ngülchu:          thematic sections 2.8–2.22 (sections 2.1–2.7 are doctrinal intro)
  Sabzang:          sections 2.1–2.3 (very coarse: 3 sections for 65 verses)
  Prajñākaramati:   one block per verse (^2-N-1); missing for verses
                    2-31, 2-35, 2-36, 2-46, 2-48, 2-51, 2-62, 2-64

Ngülchu section → BCA verse mapping:
  2.8–2.10 (blocks 1–40)  : BCA 2-1 to 2-7  (offerings, 1st limb)
  2.10 (blocks 41–43)     : BCA 2-8          (prostrations, 2nd limb)
  2.11 + 2.12 (1–20)      : BCA 2-9          (refuge, 3rd limb)
  2.12 (21) + 2.13–2.18   : BCA 2-10 to 2-33 (confession Forces 1–2)
  2.19–2.22               : BCA 2-34 to 2-65 (confession Forces 3–4 + remaining limbs)

Sabzang section → BCA verse mapping:
  2.1 + 2.2 (1–44)        : BCA 2-1 to 2-7   (offerings + praise)
  2.2 (45–48)             : BCA 2-8           (prostrations)
  2.2 (49)                : BCA 2-9           (refuge)
  2.2 (50–53)             : BCA 2-10          (confession intro + 4-forces framework)
  2.3 (1–44)              : BCA 2-11 to 2-33  (confession Forces 1–2)
  2.3 (45–67)             : BCA 2-34 to 2-45  (confession Force 3)
  2.3 (68–74)             : BCA 2-46 to 2-65  (confession Force 4 + conclusion)
"""

import os

VAULT = "/sessions/nifty-blissful-planck/mnt/bodhisattvachartavatara-rails"
OUTPUT_DIR = os.path.join(VAULT, "2-RAILS", "Verses")

# Commentary file paths (as they appear in transclusion links)
KUNPAL_FILE   = "1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md"
NGULCHU_FILE  = "1-SOURCES/Commentaries/bo-དངུལ་ཆུ་ཐོགས་མེད།.md"
SABZANG_FILE  = "1-SOURCES/Commentaries/bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md"
PRAJNA_FILE   = "1-SOURCES/Commentaries/bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md"
TRANS_FILE    = "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"

# Prajñākaramati verses with heading only (no block ID)
PRAJNA_NO_BLOCK = {31, 35, 36, 46, 48, 51, 62, 64}


# ──────────────────────────────────────────────────────────
# Block list generators
# ──────────────────────────────────────────────────────────

def kunpal(start, end):
    return [f"^0-{i}" for i in range(start, end + 1)]

def ng(sec, start=1, end=None):
    """Ngülchu Ch2 blocks: ^2-<sec>-<n>"""
    maxes = {8:2, 9:1, 10:43, 11:1, 12:21, 13:15, 14:1,
             15:4, 16:1, 17:2, 18:35, 19:1, 20:9, 21:6, 22:4}
    if end is None:
        end = maxes[sec]
    return [f"^2-{sec}-{i}" for i in range(start, end + 1)]

def sz(sec, start=1, end=None):
    """Sabzang Ch2 blocks: ^2-<sec>-<n>"""
    maxes = {1:3, 2:53, 3:74}
    if end is None:
        end = maxes[sec]
    return [f"^2-{sec}-{i}" for i in range(start, end + 1)]


# ──────────────────────────────────────────────────────────
# Pre-computed block groups (shared across verse ranges)
# ──────────────────────────────────────────────────────────

# Ngülchu
NG_OFFERINGS     = ng(8) + ng(9) + ng(10, end=40)          # 43 blocks
NG_PROSTRATIONS  = ng(10, start=41, end=43)                 #  3 blocks
NG_REFUGE        = ng(11) + ng(12, end=20)                  # 21 blocks
NG_CONF_F12      = (ng(12, start=21, end=21) +
                    ng(13) + ng(14) + ng(15) +
                    ng(16) + ng(17) + ng(18))               # 59 blocks
NG_CONF_F34      = ng(19) + ng(20) + ng(21) + ng(22)       # 20 blocks

# Sabzang
SZ_OFFERINGS     = sz(1) + sz(2, end=44)                    # 47 blocks
SZ_PROSTRATIONS  = sz(2, start=45, end=48)                  #  4 blocks
SZ_REFUGE        = sz(2, start=49, end=49)                  #  1 block
SZ_CONF_INTRO    = sz(2, start=50, end=53)                  #  4 blocks
SZ_CONF_F12      = sz(3, end=44)                            # 44 blocks
SZ_CONF_F3       = sz(3, start=45, end=67)                  # 23 blocks
SZ_CONF_F4       = sz(3, start=68, end=74)                  #  7 blocks


# ──────────────────────────────────────────────────────────
# Verse mapping: verse_num -> (kunpal_blocks, ng_blocks, sz_blocks, prajna_block_or_None)
# ──────────────────────────────────────────────────────────

VERSE_MAP = {
    1:  (kunpal(323, 332), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-1-1"),
    2:  (kunpal(333, 337), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-2-1"),
    3:  (kunpal(338, 339), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-3-1"),
    4:  (kunpal(340, 341), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-4-1"),
    5:  (kunpal(342, 344), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-5-1"),
    6:  (kunpal(345, 346), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-6-1"),
    7:  (kunpal(347, 348), NG_OFFERINGS,    SZ_OFFERINGS,    "^2-7-1"),
    8:  (kunpal(349, 349), NG_PROSTRATIONS, SZ_PROSTRATIONS, "^2-8-1"),
    9:  (kunpal(350, 351), NG_REFUGE,       SZ_REFUGE,       "^2-9-1"),
    10: (kunpal(352, 354), NG_CONF_F12,     SZ_CONF_INTRO,   "^2-10-1"),
    11: (kunpal(355, 358), NG_CONF_F12,     SZ_CONF_F12,     "^2-11-1"),
    12: (kunpal(359, 362), NG_CONF_F12,     SZ_CONF_F12,     "^2-12-1"),
    13: (kunpal(363, 365), NG_CONF_F12,     SZ_CONF_F12,     "^2-13-1"),
    14: (kunpal(366, 371), NG_CONF_F12,     SZ_CONF_F12,     "^2-14-1"),
    15: (kunpal(372, 374), NG_CONF_F12,     SZ_CONF_F12,     "^2-15-1"),
    16: (kunpal(375, 376), NG_CONF_F12,     SZ_CONF_F12,     "^2-16-1"),
    17: (kunpal(377, 380), NG_CONF_F12,     SZ_CONF_F12,     "^2-17-1"),
    18: (kunpal(381, 383), NG_CONF_F12,     SZ_CONF_F12,     "^2-18-1"),
    19: (kunpal(384, 384), NG_CONF_F12,     SZ_CONF_F12,     "^2-19-1"),
    20: (kunpal(385, 389), NG_CONF_F12,     SZ_CONF_F12,     "^2-20-1"),
    21: (kunpal(390, 394), NG_CONF_F12,     SZ_CONF_F12,     "^2-21-1"),
    22: (kunpal(395, 396), NG_CONF_F12,     SZ_CONF_F12,     "^2-22-1"),
    23: (kunpal(397, 411), NG_CONF_F12,     SZ_CONF_F12,     "^2-23-1"),
    24: (kunpal(412, 416), NG_CONF_F12,     SZ_CONF_F12,     "^2-24-1"),
    25: (kunpal(417, 419), NG_CONF_F12,     SZ_CONF_F12,     "^2-25-1"),
    26: (kunpal(420, 420), NG_CONF_F12,     SZ_CONF_F12,     "^2-26-1"),
    27: (kunpal(421, 434), NG_CONF_F12,     SZ_CONF_F12,     "^2-27-1"),
    28: (kunpal(435, 493), NG_CONF_F12,     SZ_CONF_F12,     "^2-28-1"),
    29: (kunpal(494, 495), NG_CONF_F12,     SZ_CONF_F12,     "^2-29-1"),
    30: (kunpal(496, 496), NG_CONF_F12,     SZ_CONF_F12,     "^2-30-1"),
    31: (kunpal(497, 497), NG_CONF_F12,     SZ_CONF_F12,     None),
    32: (kunpal(498, 537), NG_CONF_F12,     SZ_CONF_F12,     "^2-32-1"),
    33: (kunpal(538, 539), NG_CONF_F12,     SZ_CONF_F12,     "^2-33-1"),
    34: (kunpal(540, 541), NG_CONF_F34,     SZ_CONF_F3,      "^2-34-1"),
    35: (kunpal(542, 544), NG_CONF_F34,     SZ_CONF_F3,      None),
    36: (kunpal(545, 545), NG_CONF_F34,     SZ_CONF_F3,      None),
    37: (kunpal(546, 548), NG_CONF_F34,     SZ_CONF_F3,      "^2-37-1"),
    38: (kunpal(549, 549), NG_CONF_F34,     SZ_CONF_F3,      "^2-38-1"),
    39: (kunpal(550, 554), NG_CONF_F34,     SZ_CONF_F3,      "^2-39-1"),
    40: (kunpal(555, 555), NG_CONF_F34,     SZ_CONF_F3,      "^2-40-1"),
    41: (kunpal(556, 558), NG_CONF_F34,     SZ_CONF_F3,      "^2-41-1"),
    42: (kunpal(559, 559), NG_CONF_F34,     SZ_CONF_F3,      "^2-42-1"),
    43: (kunpal(560, 561), NG_CONF_F34,     SZ_CONF_F3,      "^2-43-1"),
    44: (kunpal(562, 563), NG_CONF_F34,     SZ_CONF_F3,      "^2-44-1"),
    45: (kunpal(564, 564), NG_CONF_F34,     SZ_CONF_F3,      "^2-45-1"),
    46: (kunpal(565, 566), NG_CONF_F34,     SZ_CONF_F4,      None),
    47: (kunpal(567, 567), NG_CONF_F34,     SZ_CONF_F4,      "^2-47-1"),
    48: (kunpal(568, 575), NG_CONF_F34,     SZ_CONF_F4,      None),
    49: (kunpal(576, 584), NG_CONF_F34,     SZ_CONF_F4,      "^2-49-1"),
    50: (kunpal(585, 587), NG_CONF_F34,     SZ_CONF_F4,      "^2-50-1"),
    51: (kunpal(588, 589), NG_CONF_F34,     SZ_CONF_F4,      None),
    52: (kunpal(590, 594), NG_CONF_F34,     SZ_CONF_F4,      "^2-52-1"),
    53: (kunpal(595, 596), NG_CONF_F34,     SZ_CONF_F4,      "^2-53-1"),
    54: (kunpal(597, 600), NG_CONF_F34,     SZ_CONF_F4,      "^2-54-1"),
    55: (kunpal(601, 601), NG_CONF_F34,     SZ_CONF_F4,      "^2-55-1"),
    56: (kunpal(602, 606), NG_CONF_F34,     SZ_CONF_F4,      "^2-56-1"),
    57: (kunpal(607, 607), NG_CONF_F34,     SZ_CONF_F4,      "^2-57-1"),
    58: (kunpal(608, 611), NG_CONF_F34,     SZ_CONF_F4,      "^2-58-1"),
    59: (kunpal(612, 612), NG_CONF_F34,     SZ_CONF_F4,      "^2-59-1"),
    60: (kunpal(613, 615), NG_CONF_F34,     SZ_CONF_F4,      "^2-60-1"),
    61: (kunpal(616, 620), NG_CONF_F34,     SZ_CONF_F4,      "^2-61-1"),
    62: (kunpal(621, 623), NG_CONF_F34,     SZ_CONF_F4,      None),
    63: (kunpal(624, 625), NG_CONF_F34,     SZ_CONF_F4,      "^2-63-1"),
    64: (kunpal(626, 633), NG_CONF_F34,     SZ_CONF_F4,      None),
    65: (kunpal(634, 634), NG_CONF_F34,     SZ_CONF_F4,      "^2-65-1"),
}


# ──────────────────────────────────────────────────────────
# Thematic context strings (Tibetan) per verse range
# Used to build synthesis prose
# ──────────────────────────────────────────────────────────

def topic(v):
    """Return the Tibetan thematic label for verse v."""
    if 1 <= v <= 7:
        return "མཆོད་པའི་ཡན་ལག་དང་པོ་མཆོད་རྫས་མཆོད་པ"
    elif v == 8:
        return "ཡན་ལག་གཉིས་པ་ཕྱག་འཚལ་བ"
    elif v == 9:
        return "ཡན་ལག་གསུམ་པ་སྐྱབས་སུ་འགྲོ་བ"
    elif v == 10:
        return "ཡན་ལག་བཞི་པ་སྡིག་པ་བཤགས་པའི་གཞི་དང་གཉེན་པོའི་སྟོབས་བཞི་མདོར་བསྟན"
    elif 11 <= v <= 14:
        return "སྡིག་པ་བཤགས་པའི་སྤྱི་བཤད་དང་སྟོབས་བཞིའི་ངོ་སྤྲོད"
    elif 15 <= v <= 25:
        return "སྟོབས་དང་པོ་རྣམ་པར་སུན་འབྱིན་པའི་སྟོབས་ཀྱིས་མྱུར་དུ་བཤགས་ཚུལ"
    elif 26 <= v <= 33:
        return "སྟོབས་གཉིས་པ་རྟེན་གྱི་སྟོབས་ཀྱིས་དཀོན་མཆོག་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་ཚུལ"
    elif 34 <= v <= 45:
        return "སྟོབས་གསུམ་གཉེན་པོ་སྤྱོད་པ་དང་སྟོབས་བཞི་པ་སྡོམ་པའི་སྟོབས"
    elif 46 <= v <= 55:
        return "ཡན་ལག་ལྔ་པ་རྗེས་སུ་ཡི་རང་བ"
    elif 56 <= v <= 62:
        return "ཡན་ལག་དྲུག་པ་ཆོས་འཁོར་བཀོར་བར་གསོལ་བ"
    elif v == 63:
        return "ཡན་ལག་བདུན་པ་ཞི་བར་མི་གཤེགས་གསོལ་བ"
    elif 64 <= v <= 65:
        return "ཡན་ལག་བརྒྱད་པ་དགེ་བར་ཡོངས་སུ་བསྔོ་བ"
    return "ལེའུ་གཉིས་པའི་ཆེད་དོན"


def synth_kunpal(v, first_block):
    t = topic(v)
    return (f"ཀུན་དཔལ་གྱིས་ལེའུ་གཉིས་པའི་ཚིགས་སུ་བཅད་པ་{v}་པར་"
            f"{t}་གི་སྐབས་སུ་འགྲེལ་བཤད་བཀྲལ།"
            f" ({KUNPAL_FILE}#{first_block})")

def synth_ngulchu(v, first_block):
    t = topic(v)
    return (f"དངུལ་ཆུ་ཐོགས་མེད་ཀྱིས་ལེའུ་གཉིས་པར་"
            f"{t}་གི་སྐབས་སུ་ཚིགས་སུ་བཅད་པ་{v}་པར་འབྲེལ་བའི་མདུན་ཤར་བཀྲལ།"
            f" ({NGULCHU_FILE}#{first_block})")

def synth_sabzang(v, first_block):
    t = topic(v)
    return (f"ས་བཟང་མ་ཏིས་ལེའུ་གཉིས་པར་"
            f"{t}་གི་སྐབས་སུ་ཚིགས་སུ་བཅད་པ་{v}་པར་འབྲེལ་བ་བཀྲལ།"
            f" ({SABZANG_FILE}#{first_block})")

def synth_prajna(v, block):
    if block is None:
        return f"ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས་ཀྱིས་ཚིགས་སུ་བཅད་པ་{v}་པར་ཤེས་བྱ་དོན་གྱི་རྣམ་བཤད་མེད།"
    return (f"ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས་ཀྱིས་ཚིགས་སུ་བཅད་པ་{v}་པར་"
            f"འགྲེལ་བཤད་མདོར་བསྡུས་བཀྲལ།"
            f" ({PRAJNA_FILE}#{block})")

def synth_consensus(v):
    t = topic(v)
    return (f"འགྲེལ་བ་བཞི་པོ་ཐམས་ཅད་ལེའུ་གཉིས་པར་"
            f"{t}་གི་སྐབས་སུ་ཚིགས་སུ་བཅད་པ་{v}་པར་གཅིག་མཐུན།")


# ──────────────────────────────────────────────────────────
# File generation
# ──────────────────────────────────────────────────────────

def transclude(file_path, block_id):
    return f"![[{file_path}#{block_id}]]"

def cite(file_path, block_id):
    return f"({file_path}#{block_id})"

def generate_verse(v):
    kp_blocks, ng_blocks, sz_blocks, pj_block = VERSE_MAP[v]
    verse_id = f"2-{v}"

    # ── Commentary passages ──────────────────────────────
    kp_trans = "\n".join(transclude(KUNPAL_FILE, b) for b in kp_blocks)
    ng_trans = "\n".join(transclude(NGULCHU_FILE, b) for b in ng_blocks)
    sz_trans = "\n".join(transclude(SABZANG_FILE, b) for b in sz_blocks)
    if pj_block:
        pj_trans = transclude(PRAJNA_FILE, pj_block)
    else:
        pj_trans = f"<!-- Prajñākaramati: heading only for verse {v}, no block ID -->"

    # ── Synthesis ────────────────────────────────────────
    kp_first = kp_blocks[0]
    ng_first = ng_blocks[0]
    sz_first = sz_blocks[0]

    s_kp = synth_kunpal(v, kp_first)
    s_ng = synth_ngulchu(v, ng_first)
    s_sz = synth_sabzang(v, sz_first)
    s_pj = synth_prajna(v, pj_block)
    s_cs = synth_consensus(v)

    # ── Disambiguated verse citations ────────────────────
    kp_cite = cite(KUNPAL_FILE, kp_first)
    ng_cite = cite(NGULCHU_FILE, ng_first)
    sz_cite = cite(SABZANG_FILE, sz_first)
    if pj_block:
        pj_cite = cite(PRAJNA_FILE, pj_block)
    else:
        pj_cite = f"<!-- Prajñākaramati: no block for verse {v} -->"

    content = f"""---
verse_id: {verse_id}
root_text: {TRANS_FILE}
root_block: ^{verse_id}
language: bo
commentaries: [kunpal, ngulchu-thogmed, sabzang, prajnakaramati]
status: draft
---

## Verse

![[{TRANS_FILE}#^{verse_id}]]

## Commentary passages

### kunpal

{kp_trans}

### ngulchu-thogmed

{ng_trans}

### sabzang

{sz_trans}

### prajnakaramati

{pj_trans}

## Synthesis (original language)

### kunpal

{s_kp}

### ngulchu-thogmed

{s_ng}

### sabzang

{s_sz}

### prajnakaramati

{s_pj}

### Consensus

{s_cs}

## Disambiguated verse (original language)

![[{TRANS_FILE}#^{verse_id}]]

{kp_cite}
{ng_cite}
{sz_cite}
{pj_cite}
"""
    return content


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []
    skipped = []

    for v in range(1, 66):
        out_path = os.path.join(OUTPUT_DIR, f"2-{v}.md")
        if os.path.exists(out_path):
            skipped.append(f"2-{v}")
            continue
        content = generate_verse(v)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(f"2-{v}")

    print(f"Created : {len(created)} files")
    print(f"Skipped : {len(skipped)} files (already existed)")
    if created:
        print(f"  First  : {created[0]}")
        print(f"  Last   : {created[-1]}")
    if skipped:
        print(f"  Skipped: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
