---
name: bo-hi-translate
description: >
  Translates Buddhist source text (English verse translation or Tibetan) into Hindi at a
  specified audience grade level — beginner, general, intermediate, or advanced — while
  enforcing term consistency across the entire translation by drawing on a pre-built
  keyword termbase. Outputs a clean Hindi markdown file with one line per verse followed
  by its block ID. Use this skill whenever the user asks to "translate to Hindi", "render
  in Hindi", "produce a Hindi version", "write Hindi translation", or "generate Hindi md"
  for any passage from the Bodhisattvacharyavatara (BCA). Also triggers for: "make this
  beginner Hindi", "academic Hindi translation", "general audience Hindi", "use keyword
  termbase for translation", "term-consistent Hindi".
---

# bo-hi-translate

Produces a Hindi translation of BCA verses that reads naturally **and** uses Buddhist
terms consistently. The result is saved as a clean markdown file — one verse per line
followed by its block ID — mirroring the structure of the source translation files.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Source text** | ✓ | English verse translation or Tibetan text to translate. May be one verse or many. |
| **Audience grade** | ✓ | `beginner`, `general`, `intermediate`, or `advanced` |
| **Verse IDs** | recommended | e.g. `1-1`, `3-4` — used to write results back to the JSON |
| **Output path** | optional | Markdown file to also save the translation to |

If the user does not specify an audience grade, ask before proceeding.

---

## Termbase + output files (one per grade)

| Grade | File | Keyword rank cutoff |
|---|---|---|
| beginner | `4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_beginner.json` | rank ≤ 200 |
| general | `4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_general.json` | rank ≤ 500 |
| intermediate | `4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_intermediate.json` | rank ≤ 500 |
| advanced | `4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_advanced.json` | all ranks |

Each file uses this structure — which is also the write-back target:

```json
{
  "verse_id": {
    "text": "English translation",
    "bo_text": "Tibetan source lines",
    "hi_text": "Hindi translation at this grade",
    "keywords": [
      {
        "key": "english_term",
        "rank": 0,
        "score": 0.0,
        "count": 0,
        "bo": "Tibetan meaning",
        "hi": "Hindi meaning at this grade",
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

Open the grade's keyword JSON and build a flat `key → hi` dict (first occurrence wins). This is the single source of truth for term consistency.

```python
import json
OUT = "4-SYSTEM/scripts/english_keyword/output"
grade = "<target grade>"
GRADE_FILE = {"beginner": "bo_hi_keyword_beginner.json", "general": "bo_hi_keyword_general.json",
               "intermediate": "bo_hi_keyword_intermediate.json", "advanced": "bo_hi_keyword_advanced.json"}

with open(f"{OUT}/{GRADE_FILE[grade]}", encoding="utf-8") as f:
    kw_data = json.load(f)

termbase = {}
for verse in kw_data.values():
    for kw in verse.get("keywords", []):
        key = kw["key"].lower()
        hi  = kw.get("hi", "")
        if hi and hi != key and key not in termbase:
            termbase[key] = hi
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
1. **Identify locked terms** — scan the chapter's verses for termbase matches. These Hindi forms are fixed; do not substitute synonyms.
2. **Translate each verse** — from the English `text` field, applying locked terms and the grade register:

| Grade | Style |
|---|---|
| **beginner** | Plain Hindustani. Gloss Sanskrit on first use: बोधिचित्त (सबके भले की इच्छा). |
| **general** | Modern standard Hindi. Sanskrit Buddhist terms used freely. Flowing prose. |
| **intermediate** | Hindi + classical Sanskrit. Terms like क्लेश, प्रज्ञा used without glosses. |
| **advanced** | Sanskrit-rich. Full Abhidharma/Madhyamaka vocabulary. Parenthetical expansions welcome. |

Rules: locked terms override register · translate line-by-line · never add content · inflection is allowed.

### Step 4 — Consistency check

After all chapters, re-scan output for locked terms. Fix any verse using a non-termbase form.

### Step 5 — Write markdown output

One block per verse: Hindi text followed by its block ID on the same line. Blank line between blocks.

```
{hi_text} ^{verse_id}
```

Headings (`verse_id` ends in `-0`): `## {hi_text} ^{verse_id}`

```python
out_lines = []
for vid, verse in sorted(kw_data.items()):
    hi = verse.get("hi_text", "").strip()
    if not hi:
        continue
    is_heading = vid.split("-")[-1] == "0"
    prefix = "## " if is_heading else ""
    out_lines.append(f"{prefix}{hi} ^{vid}")
    out_lines.append("")

md_path = f"3-TRANSFORMATIONS/Translations/hi-{grade}/bca-hi-{grade}.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
```

No English, no Tibetan, no metadata — Hindi only.

---

## Adapting between grades

When the user wants a grade that has no existing `hi_text`:

- **general → beginner**: Strip parenthetical glosses. Replace technical Sanskrit with
  plain Hindi equivalents from the beginner termbase. Gloss on first use.
- **general → advanced**: Add Sanskrit technical terms in parentheses. Use the advanced
  termbase for more precise equivalents.
- When adapting, always switch to the **target grade's termbase** — do not mix
  termbase entries from different grades.

---

## Examples of grade-register differences

| Concept | beginner | general | advanced |
|---|---|---|---|
| bodhichitta | सबके भले की इच्छा (बोधिचित्त) | बोधिचित्त | बोधिचित्त (संवोधिचित्त) |
| suffering | दुःख | दुःख | दुःख (त्रिविधदुःखता) |
| emptiness | खालीपन | शून्यता | शून्यता (निःस्वभावता) |
| merit | पुण्य | पुण्य | कुशलकर्म |
| liberation | मुक्ति | मुक्ति | विमोक्ष |

---

## Completion check

- [ ] Grade specified; correct termbase file loaded.
- [ ] Global termbase built from all verses in the file.
- [ ] Verses grouped by chapter; chapters processed in order.
- [ ] All verses in each chapter translated together.
- [ ] Locked terms identified per chapter before translating.
- [ ] Translation produced at correct grade register.
- [ ] Consistency check passed: same Hindi form for same term across all verses.
- [ ] Markdown file written: one verse per block, Hindi text followed by `^{verse_id}`.
- [ ] Heading verses rendered as `## {hi_text} ^{verse_id}`.
- [ ] No JSON files modified.
