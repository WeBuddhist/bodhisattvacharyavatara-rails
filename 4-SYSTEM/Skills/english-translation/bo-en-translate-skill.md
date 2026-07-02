---
name: bo-en-translate
description: >
  Translates Buddhist source text (Tibetan, or the existing base English verse
  translation) into graded English at a specified audience level — beginner, general,
  intermediate, or advanced — while enforcing term consistency across the entire
  translation by drawing on a pre-built keyword termbase. Outputs a clean English
  markdown file with one line per verse followed by its block ID. Use this skill
  whenever the user asks to "translate to English by audience level", "produce a
  beginner English version", "academic English translation", "grade this English
  translation", "use keyword termbase for English translation", or "generate graded
  English md" for any passage from the Bodhisattvacharyavatara (BCA). Also triggers
  for: "make this plain English", "scholarly English translation", "general audience
  English", "term-consistent English".
---

# bo-en-translate

Produces an English translation of BCA verses that reads naturally **and** uses
Buddhist terms consistently at the target audience register. The result is saved as
a clean markdown file — one verse per line followed by its block ID — mirroring the
structure of the source translation files.

This skill mirrors `4-SYSTEM/Skills/hindi-translation/bo-en-translate-skill.md`'s
sibling `bo-hi-translate`, with English in place of Hindi as the target language.
Where Hindi grading swaps registers of Devanagari vocabulary (plain Hindi ↔ Sanskrit
loanwords), English grading swaps registers of English vocabulary (plain English
gloss ↔ untranslated Sanskrit/Pali/Tibetan technical terms).

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Source text** | ✓ | Tibetan text, or the existing base English verse translation, to translate/regrade. May be one verse or many. |
| **Audience grade** | ✓ | `beginner`, `general`, `intermediate`, or `advanced` |
| **Verse IDs** | recommended | e.g. `1-1`, `3-4` — used to write results back to the JSON |
| **Output path** | optional | Markdown file to also save the translation to |

If the user does not specify an audience grade, ask before proceeding.

---

## Dependency — English-graded termbase

This skill depends on an English-graded keyword termbase analogous to the
`bo_hi_keyword_*.json` files that `bo-hi-translate` reads. Those English-graded
files (`bo_en_keyword_beginner.json`, `…general.json`, `…intermediate.json`,
`…advanced.json`) do not exist yet in this vault as of this writing. Build them
first with a companion skill mirroring `bo-hi-keyword-grade` — call it
`bo-en-keyword-grade` — before running this skill. That companion skill has not
been created; ask the user to confirm before scaffolding it, since it was not part
of this request.

---

## Termbase + output files (one per grade)

| Grade | File | Keyword rank cutoff |
|---|---|---|
| beginner | `4-SYSTEM/scripts/english_keyword/output/bo_en_keyword_beginner.json` | rank ≤ 200 |
| general | `4-SYSTEM/scripts/english_keyword/output/bo_en_keyword_general.json` | rank ≤ 500 |
| intermediate | `4-SYSTEM/scripts/english_keyword/output/bo_en_keyword_intermediate.json` | rank ≤ 500 |
| advanced | `4-SYSTEM/scripts/english_keyword/output/bo_en_keyword_advanced.json` | all ranks |

Each file uses this structure — which is also the write-back target:

```json
{
  "verse_id": {
    "text": "Base English translation (David Karma Choephel), unchanged",
    "bo_text": "Tibetan source lines",
    "en_text": "Graded English translation at this grade",
    "keywords": [
      {
        "key": "english_term",
        "rank": 0,
        "score": 0.0,
        "count": 0,
        "bo": "Tibetan meaning",
        "en": "Graded English rendering of this term at this grade",
        "grade": "beginner"
      }
    ]
  }
}
```

**Keyword filtering per file:**
- `beginner` file: include only keywords with `rank ≤ 200`
- `general` / `intermediate` files: include only keywords with `rank ≤ 500`
- `advanced` file: include all keywords regardless of rank

---

## Procedure

### Step 1 — Load termbase

Open the grade's keyword JSON and build a flat `key → en` dict (first occurrence wins). This is the single source of truth for term consistency.

```python
import json
OUT = "4-SYSTEM/scripts/english_keyword/output"
grade = "<target grade>"
GRADE_FILE = {"beginner": "bo_en_keyword_beginner.json", "general": "bo_en_keyword_general.json",
               "intermediate": "bo_en_keyword_intermediate.json", "advanced": "bo_en_keyword_advanced.json"}

with open(f"{OUT}/{GRADE_FILE[grade]}", encoding="utf-8") as f:
    kw_data = json.load(f)

termbase = {}
for verse in kw_data.values():
    for kw in verse.get("keywords", []):
        key = kw["key"].lower()
        en  = kw.get("en", "")
        if en and en != key and key not in termbase:
            termbase[key] = en
```

### Step 2 — Fetch verses by chapter

Group verses by chapter (first segment of verse ID). Process chapters in order: 0, I, 1–10, colophon.

```python
from collections import defaultdict
chapters = defaultdict(list)
for vid, entry in kw_data.items():
    ch = vid.split("-")[0]
    chapters[ch].append((vid, entry))
```

### Step 3 — Translate chapter by chapter

For each chapter:
1. **Identify locked terms** — scan the chapter's verses for termbase matches. These English forms are fixed; do not substitute synonyms.
2. **Translate each verse** — from the Tibetan `bo_text` field (or regrade the base `text` field), applying locked terms and the grade register:

| Grade | Style |
|---|---|
| **beginner** | Plain modern English. No unglossed Sanskrit/Pali/Tibetan. Gloss any unavoidable technical term inline: "the wish to awaken for the sake of all beings (bodhichitta)". |
| **general** | Standard English prose. Common Buddhist loanwords used freely (bodhichitta, karma, nirvana) without gloss. |
| **intermediate** | English + untransliterated Sanskrit/Pali terms for technical concepts (kleśas, prajñā) used without gloss. |
| **advanced** | Sanskrit/Pali-rich technical register. Full Abhidharma/Madhyamaka vocabulary; parenthetical Sanskrit/Tibetan given for key terms. |

Rules: locked terms override register · translate line-by-line · never add content · inflection is allowed.

### Step 4 — Consistency check

After all chapters, re-scan output for locked terms. Fix any verse using a non-termbase form.

### Step 5 — Write markdown output

One block per verse: English text followed by its block ID on the same line. Blank line between blocks.

```
{en_text} ^{verse_id}
```

Headings (`verse_id` ends in `-0`): `## {en_text} ^{verse_id}`

```python
out_lines = []
for vid, verse in sorted(kw_data.items()):
    en = verse.get("en_text", "").strip()
    if not en:
        continue
    is_heading = vid.split("-")[-1] == "0"
    prefix = "## " if is_heading else ""
    out_lines.append(f"{prefix}{en} ^{vid}")
    out_lines.append("")

md_path = f"3-TRANSFORMATIONS/Translations/en-{grade}/bca-en-{grade}.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
```

No Tibetan, no metadata — English only.

---

## Adapting between grades

When the user wants a grade that has no existing `en_text`:

- **general → beginner**: Strip parenthetical/unglossed Sanskrit. Replace technical loanwords with plain English equivalents from the beginner termbase. Gloss on first use if unavoidable.
- **general → advanced**: Add Sanskrit/Pali technical terms in parentheses. Use the advanced termbase for more precise equivalents.
- When adapting, always switch to the **target grade's termbase** — do not mix termbase entries from different grades.

---

## Examples of grade-register differences

| Concept | beginner | general | advanced |
|---|---|---|---|
| bodhichitta | the wish to awaken for the sake of all beings | bodhichitta | bodhichitta (bodhicitta) |
| suffering | suffering | suffering | suffering (duḥkha; three types of duḥkhatā) |
| emptiness | the lack of any fixed, separate self in things | emptiness | emptiness (śūnyatā; niḥsvabhāvatā) |
| merit | good karma from virtuous action | merit | merit (puṇya) |
| liberation | freedom from suffering | liberation | liberation (mokṣa; vimokṣa) |

---

## Completion check

- [ ] Grade specified; correct termbase file loaded (`bo_en_keyword_<grade>.json`).
- [ ] If the termbase file does not yet exist, stop and tell the user it must be built first (see Dependency section) rather than improvising term choices ad hoc.
- [ ] Global termbase built from all verses in the file.
- [ ] Verses grouped by chapter; chapters processed in order.
- [ ] All verses in each chapter translated together.
- [ ] Locked terms identified per chapter before translating.
- [ ] Translation produced at correct grade register.
- [ ] Consistency check passed: same English form for same term across all verses.
- [ ] Markdown file written: one verse per block, English text followed by `^{verse_id}`.
- [ ] Heading verses rendered as `## {en_text} ^{verse_id}`.
- [ ] No JSON files modified except the grade's own termbase write-back.
