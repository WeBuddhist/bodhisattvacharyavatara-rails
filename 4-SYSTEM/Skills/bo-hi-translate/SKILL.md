---
name: bo-hi-translate
description: >
  Translates Buddhist source text (English verse translation or Tibetan) into Hindi at a
  specified audience grade level — beginner, general, intermediate, or advanced — while
  enforcing term consistency across the entire translation by drawing on a pre-built
  keyword termbase. Stores results back into the grade-specific keyword JSON file in the
  same structure as the existing bo_hi_keyword_*.json files. Use this skill whenever the
  user asks to "translate to Hindi", "render in Hindi", "produce a Hindi version",
  "write Hindi translation", "store Hindi translation", or "update keyword JSON with Hindi"
  for any passage from the Bodhisattvacharyavatara (BCA). Also triggers for: "make this
  beginner Hindi", "academic Hindi translation", "general audience Hindi", "use keyword
  termbase for translation", "term-consistent Hindi", "save to keyword JSON".
---

# bo-hi-translate

Produces a Hindi translation of BCA verses that reads naturally **and** uses Buddhist
terms consistently. The result is written back into the grade-specific keyword JSON file
(`bo_hi_keyword_<grade>.json`), updating `hi_text` per verse and `hi` per keyword, so
the entire corpus stays in sync at that audience level.

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

### Step 1 — Build the termbase

Load the grade-appropriate keyword JSON. Extract every unique `key → hi` pair across
**all verses** to form the global termbase for this grade:

```python
import json

GRADE_FILE = {
    "beginner":     "bo_hi_keyword_beginner.json",
    "general":      "bo_hi_keyword_general.json",
    "intermediate": "bo_hi_keyword_intermediate.json",
    "advanced":     "bo_hi_keyword_advanced.json",
}

OUT = "4-SYSTEM/scripts/english_keyword/output"
grade = "<target grade>"

with open(f"{OUT}/{GRADE_FILE[grade]}", encoding="utf-8") as f:
    kw_data = json.load(f)

# Global termbase: first occurrence of each key wins
termbase = {}
for verse in kw_data.values():
    for kw in verse.get("keywords", []):
        key = kw["key"].lower()
        hi  = kw.get("hi", "")
        if hi and hi != key and key not in termbase:
            termbase[key] = hi

print(f"Termbase: {len(termbase)} terms for grade={grade}")
```

This termbase is the single source of truth for Hindi term equivalents at this grade.
It is consistent across the whole file, so every verse will use the same Hindi word
for the same concept.

### Step 2 — Identify verses to translate

If verse IDs are provided, look them up in `kw_data` to get:
- `text` (English) — source for translation
- `bo_text` (Tibetan) — include in output unchanged
- `keywords` — list of keyword entries to update with `hi`
- existing `hi_text` — use as reference draft if present

If no verse IDs are given, treat the supplied source text as a free passage and skip
the JSON write-back (translate only, no update).

### Step 3 — Scan source for locked terms

Before translating each verse, scan its English text for keywords that appear in the
termbase. These become **locked terms** — their Hindi equivalent is fixed for this
translation:

```
Locked terms for verse 1-1:
  bodhisattva → बोधिसत्त्व
  suffering   → दुःख
  merit       → पुण्य
```

Do not substitute synonyms for locked terms. Consistency across the corpus outweighs
per-verse elegance.

### Step 4 — Translate

**If `hi_text` already exists in the JSON:** use it as a base draft, then adapt the
register to the target grade (up or down). This is faster and preserves any
human-reviewed text.

**If `hi_text` is empty or absent:** translate from the English `text` field directly,
applying locked terms and the grade register below.

#### Grade registers

| Grade | Audience | Hindi style |
|---|---|---|
| **beginner** | New to Buddhism, general public | Plain everyday Hindustani. Short sentences. No unglossed Sanskrit. Buddhist terms get a brief plain gloss on first use: बोधिचित्त (सबके भले की इच्छा). |
| **general** | Educated general reader | Modern standard Hindi. Common Sanskrit Buddhist terms (बोधिचित्त, करुणा, धर्म) used freely without glosses. Flowing prose. |
| **intermediate** | Students with basic Buddhist study | Mix of Hindi and classical Sanskrit. Terms like क्लेश, प्रज्ञा, समाधि used without full glosses. Precise but readable. |
| **advanced** | Scholars, monks, serious practitioners | Sanskrit-rich. Technical Abhidharma / Madhyamaka vocabulary: सम्यकसम्बुद्ध, कुशलकर्म, परिणामना, प्रतीत्यसमुत्पाद. Parenthetical Sanskrit expansions welcome. |

#### Universal translation rules

1. **Locked terms override register.** The termbase value IS the grade's preferred form.
2. **Preserve verse structure.** Translate line-by-line; keep line breaks.
3. **Never add content.** Translate what is there; do not expand or explain beyond
   the one-word gloss allowed for beginner grade.
4. **Grammatical inflection is allowed.** `बोधिसत्त्व` may become `बोधिसत्त्व को`
   etc. — inflection is not a consistency violation.

### Step 5 — Consistency check

After drafting all translations:

1. Re-scan every output verse for locked terms. Verify each uses the correct Hindi form.
2. If any term appears in two different Hindi forms across verses, fix both to the
   termbase value.
3. For beginner: confirm no unglossed Sanskrit term survived.

### Step 6 — Write back to the keyword JSON

For each translated verse, update the entry in `kw_data` in memory:

```python
for vid, translation in translated_verses.items():
    if vid not in kw_data:
        continue  # verse not in base JSON; skip write-back

    entry = kw_data[vid]

    # Update hi_text
    entry["hi_text"] = translation

    # Update hi field on each keyword using the termbase
    for kw in entry.get("keywords", []):
        key_lower = kw["key"].lower()
        if key_lower in termbase:
            kw["hi"] = termbase[key_lower]
        # grade field stays as set in the original file

# Save updated JSON (write to /tmp first, then copy to avoid filesystem issues)
import shutil, tempfile

tmp = f"/tmp/{GRADE_FILE[grade]}"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(kw_data, f, ensure_ascii=False, indent=2)
shutil.copy2(tmp, f"{OUT}/{GRADE_FILE[grade]}")

# Verify
with open(f"{OUT}/{GRADE_FILE[grade]}", encoding="utf-8") as f:
    check = json.load(f)
print(f"Saved {len(check)} verses. Updated hi_text for {len(translated_verses)} verses.")
```

**Important:** Only update `hi_text` and keyword `hi` fields. Never modify `text`,
`bo_text`, `key`, `rank`, `score`, `count`, `bo`, or `grade` fields — those are managed
by other skills.

### Step 7 — Markdown output

Also write a clean markdown file for human reading:

```markdown
# Hindi Translation — <grade> grade
## Verse <id>

**Tibetan:** <bo_text>
**English:** <text>
**Hindi (<grade>):** <translation>

---
```

Save to the user-specified path or `3-TRANSFORMATIONS/Translations/hi-<grade>/`.

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
- [ ] Locked terms identified per verse before translation.
- [ ] Translation produced at correct grade register.
- [ ] Consistency check passed: same Hindi form for same term across all verses.
- [ ] `hi_text` updated in `kw_data` for each translated verse.
- [ ] `hi` field updated on every keyword entry using the termbase.
- [ ] JSON file saved (via /tmp to avoid filesystem issues); verified with `json.load`.
- [ ] Markdown file written if output path provided.
- [ ] No `text`, `bo_text`, `key`, `rank`, `score`, `count`, `bo`, or `grade` fields modified.
