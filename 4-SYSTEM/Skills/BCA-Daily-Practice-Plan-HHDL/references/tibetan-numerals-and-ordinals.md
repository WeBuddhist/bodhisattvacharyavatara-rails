# Tibetan numeral, ordinal, and cardinal reference

Used to build the chapter/verse citation phrase in Section 2 (ངོ་སྤྲོད།), the
document title line, and anywhere else a number must appear in Tibetan script
rather than Arabic digits. **Anchors** (`^chapter-verse`) are the one
exception — the vault's citation convention (CLAUDE.md §5) requires Arabic
numerals there, and filenames also use plain Arabic digits. Everything else
that is prose content of the plan must use Tibetan digits/words.

---

## Tibetan digits (for the document title line only)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| ༠ | ༡ | ༢ | ༣ | ༤ | ༥ | ༦ | ༧ | ༨ | ༩ |

Combine digits normally: 35 → ༣༥, 134 → ༡༣༤.

---

## Cardinal numbers 1–10 (for "N verses" phrasing, e.g. verse-count in Section 2)

| # | Cardinal |
|---|----------|
| 1 | གཅིག་ |
| 2 | གཉིས་ |
| 3 | གསུམ་ |
| 4 | བཞི་ |
| 5 | ལྔ་ |
| 6 | དྲུག་ |
| 7 | བདུན་ |
| 8 | བརྒྱད་ |
| 9 | དགུ་ |
| 10 | བཅུ་ |

A day's verse count is almost always in this range (schedule days cover 1–4
verses). If a day ever exceeds 10, spell it compositionally (e.g. 11 →
བཅུ་གཅིག་).

---

## Ordinal numbers — the compositional rule

Tibetan ordinals are built as **[cardinal root] + པ**, with irregular forms
for 1 and set "decade" prefixes that replace the cardinal root for 20–99.
Chapters only need 1–10; verses can run to ~185 (Chapter 8 has the highest
verse count), so the decade-prefix system below is required for verse
ordinals.

### 1–10 (irregular/base forms)

| N | Ordinal |
|---|---------|
| 1 | དང་པོ། |
| 2 | གཉིས་པ། |
| 3 | གསུམ་པ། |
| 4 | བཞི་པ། |
| 5 | ལྔ་པ། |
| 6 | དྲུག་པ། |
| 7 | བདུན་པ། |
| 8 | བརྒྱད་པ། |
| 9 | དགུ་པ། |
| 10 | བཅུ་པ། |

### 11–19: བཅུ་ + [ones digit] + པ — except 15 and 18, which are irregular

11 → བཅུ་གཅིག་པ། · 12 → བཅུ་གཉིས་པ། · 13 → བཅུ་གསུམ་པ། · 14 → བཅུ་བཞི་པ། ·
**15 → བཅོ་ལྔ་པ།** (not བཅུ་ལྔ་པ — "bco", not "bcu") · 16 → བཅུ་དྲུག་པ། ·
17 → བཅུ་བདུན་པ། · **18 → བཅོ་བརྒྱད་པ།** (not བཅུ་བརྒྱད་པ — likewise irregular) ·
19 → བཅུ་དགུ་པ།

This bcu→bco irregularity is confined to 15 and 18 within the teens. It does
not recur at 25/28, 35/38, etc. — there the decade prefix replaces bcu/bco
entirely and the ones-digit is regular (25 → ཉེར་ལྔ་པ།, 28 → ཉེར་བརྒྱད་པ།).

### Decade prefixes (20–99): [decade-prefix] + [ones digit] + པ

Each decade has its own combining prefix — do not use the plain cardinal root
(e.g. ཉི་ཤུ་) when forming 21–29; use the prefix (ཉེར་) instead.

| Decade | Round number | Combining prefix | Example (round+5) |
|---|---|---|---|
| 20s | ཉི་ཤུ་པ། (20th) | ཉེར་ | ཉེར་ལྔ་པ། (25th) |
| 30s | སུམ་ཅུ་པ། (30th) | སོ་ | སོ་ལྔ་པ། (35th) |
| 40s | བཞི་བཅུ་པ། (40th) | ཞེ་ | ཞེ་ལྔ་པ། (45th) |
| 50s | ལྔ་བཅུ་པ། (50th) | ང་ | ང་ལྔ་པ། (55th) |
| 60s | དྲུག་ཅུ་པ། (60th) | རེ་ | རེ་ལྔ་པ། (65th) |
| 70s | བདུན་ཅུ་པ། (70th) | དོན་ | དོན་ལྔ་པ། (75th) |
| 80s | བརྒྱད་ཅུ་པ། (80th) | གྱ་ | གྱ་ལྔ་པ། (85th) |
| 90s | དགུ་བཅུ་པ། (90th) | གོ་ | གོ་ལྔ་པ། (95th) |

Worked check against the example in the skill instructions: 35th → སོ་ + ལྔ་
+ པ། = སོ་ལྔ་པ། ✓. 37th → སོ་ + བདུན་ + པ། = སོ་བདུན་པ། ✓.

### 100+: བརྒྱ་དང་ + [remainder ordinal]

100th → བརྒྱ་པ། . For 101–199, say "hundred and [remainder]-th":
185th → བརྒྱ་དང་གྱ་ལྔ་པ།

---

## Chapter name table (ordinal form for the document title line)

| # | Ordinal | Chapter title (Tibetan) |
|---|---------|---------------------------|
| 1 | དང་པོ། | བྱང་ཆུབ་ཀྱི་ཕན་ཡོན། |
| 2 | གཉིས་པ། | སྡིག་པ་བཤགས་པ། |
| 3 | གསུམ་པ། | བྱང་ཆུབ་སེམས་ཀྱི་བདག་ཉིད་ལེན་པ། |
| 4 | བཞི་པ། | བྱང་ཆུབ་སེམས་ལ་མི་བརྟེན་པ། |
| 5 | ལྔ་པ། | བག་ཡོད་པ། |
| 6 | དྲུག་པ། | བཟོད་པ། |
| 7 | བདུན་པ། | བརྩོན་འགྲུས། |
| 8 | བརྒྱད་པ། | བསམ་གཏན། |
| 9 | དགུ་པ། | ཤེས་རབ། |
| 10 | བཅུ་པ། | བསྔོ་བ། |

---

## Chapter → folder map (for locating/writing day files)

| Chapter | Folder |
|---|---|
| 1 | `Chapter-1 D1-D14` |
| 2 | `Chapter-2 D15-D40` |
| 3 | `Chapter-3 D41-D54` |
| 4 | `Chapter-4 D55-D73` |
| 5 | `Chapter-5 D74-D116` |
| 6 | `Chapter-6 D117-D170` |
| 7 | `Chapter-7 D171-D201` |
| 8 | `Chapter-8 D202-D274` |
| 9 | `Chapter-9 D275-D341` |
| 10 | `Chapter-10 D342-D365` |

All under `3-TRANSFORMATIONS/Plans/Dalai Lama/`. Pick the folder whose `D<s>-D<e>`
range contains the day number — do not derive it from the chapter number alone,
confirm against this table since it is also how the Tibetan-schedule-corrected.md
`Ch.Day` resets are keyed.
