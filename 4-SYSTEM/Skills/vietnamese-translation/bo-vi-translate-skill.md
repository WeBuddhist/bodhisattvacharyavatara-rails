---
name: bo-vi-translate
description: >
  Translates Buddhist source text (English verse translation or Tibetan) into Vietnamese at a
  specified audience grade level — beginner, general, intermediate, or advanced — while
  enforcing term consistency across the entire translation by drawing on a pre-built
  keyword termbase. Outputs a clean Vietnamese markdown file with one line per verse followed
  by its block ID. Use this skill whenever the user asks to "translate to Vietnamese", "render
  in Vietnamese", "produce a Vietnamese version", "write Vietnamese translation", or "generate
  Vietnamese md" for any passage from the Bodhisattvacharyavatara (BCA). Also triggers for:
  "make this beginner Vietnamese", "academic Vietnamese translation", "general audience
  Vietnamese", "use keyword termbase for translation", "term-consistent Vietnamese".
---

# bo-vi-translate

Produces a Vietnamese translation of BCA verses that reads naturally **and** uses Buddhist
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

Note: a beginner-grade full translation already exists at
`3-TRANSFORMATIONS/Translations/vi-beginner-audience/BCA-Full-Beginner-Vietnamese.md` — check
whether the requested verses are already covered there before regenerating them, and treat its
attested renderings as authoritative locked terms for the beginner termbase.

---

## Termbase + output files (one per grade)

| Grade | File | Keyword rank cutoff |
|---|---|---|
| beginner | `4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_beginner.json` | rank ≤ 200 |
| general | `4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_general.json` | rank ≤ 500 |
| intermediate | `4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_intermediate.json` | rank ≤ 500 |
| advanced | `4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_advanced.json` | all ranks |

Each file uses this structure — which is also the write-back target:

```json
{
  "verse_id": {
    "text": "English translation",
    "bo_text": "Tibetan source lines",
    "vi_text": "Vietnamese translation at this grade",
    "keywords": [
      {
        "key": "english_term",
        "rank": 0,
        "score": 0.0,
        "count": 0,
        "bo": "Tibetan meaning",
        "vi": "Vietnamese meaning at this grade",
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

These files are produced by the `bo-vi-keyword-grade` skill — run it first if they don't
exist yet for the target grade.

---

## Procedure

### Step 1 — Load termbase

Open the grade's keyword JSON and build a flat `key → vi` dict (first occurrence wins). This is the single source of truth for term consistency.

```python
import json
OUT = "4-SYSTEM/scripts/english_keyword/output"
grade = "<target grade>"
GRADE_FILE = {"beginner": "bo_vi_keyword_beginner.json", "general": "bo_vi_keyword_general.json",
               "intermediate": "bo_vi_keyword_intermediate.json", "advanced": "bo_vi_keyword_advanced.json"}

with open(f"{OUT}/{GRADE_FILE[grade]}", encoding="utf-8") as f:
    kw_data = json.load(f)

termbase = {}
for verse in kw_data.values():
    for kw in verse.get("keywords", []):
        key = kw["key"].lower()
        vi  = kw.get("vi", "")
        if vi and vi != key and key not in termbase:
            termbase[key] = vi
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
1. **Identify locked terms** — scan the chapter's verses for termbase matches. These Vietnamese forms are fixed; do not substitute synonyms.
2. **Translate each verse** — from the English `text` field, applying locked terms and the grade register:

| Grade | Style |
|---|---|
| **beginner** | Plain modern Vietnamese, short sentences. Gloss Sino-Vietnamese/Sanskrit terms on first use: tâm bồ đề (lòng mong muốn giúp tất cả chúng sinh thoát khổ). |
| **general** | Modern standard Vietnamese. Common Sino-Vietnamese Buddhist terms used freely (Phật, Pháp, Bồ Tát, từ bi, hồi hướng). Flowing prose. |
| **intermediate** | Vietnamese + precise Sino-Vietnamese terms. Terms like phiền não, ba-la-mật used without glosses. |
| **advanced** | Sino-Vietnamese/Sanskrit-rich. Full Abhidharma/Madhyamaka vocabulary, Sanskrit terms transliterated or parenthesised. |

Rules: locked terms override register · translate line-by-line · never add content · natural Vietnamese word order and particles (rồi, thì, mà, vậy) are allowed.

### Step 4 — Consistency check

After all chapters, re-scan output for locked terms. Fix any verse using a non-termbase form.

### Step 5 — Write markdown output

One block per verse: Vietnamese text followed by its block ID on the same line. Blank line between blocks.

```
{vi_text} ^{verse_id}
```

Headings (`verse_id` ends in `-0`): `## {vi_text} ^{verse_id}`

```python
out_lines = []
for vid, verse in sorted(kw_data.items()):
    vi = verse.get("vi_text", "").strip()
    if not vi:
        continue
    is_heading = vid.split("-")[-1] == "0"
    prefix = "## " if is_heading else ""
    out_lines.append(f"{prefix}{vi} ^{vid}")
    out_lines.append("")

md_path = f"3-TRANSFORMATIONS/Translations/vi-{grade}/bca-vi-{grade}.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
```

No English, no Tibetan, no metadata — Vietnamese only.

---

## Adapting between grades

When the user wants a grade that has no existing `vi_text`:

- **general → beginner**: Strip parenthetical glosses. Replace technical Sino-Vietnamese/Sanskrit
  with plain Vietnamese equivalents from the beginner termbase. Gloss on first use.
- **general → advanced**: Add Sanskrit/Pali technical terms in parentheses. Use the advanced
  termbase for more precise equivalents.
- When adapting, always switch to the **target grade's termbase** — do not mix
  termbase entries from different grades.

---

## Examples of grade-register differences

| Concept | beginner | general | advanced |
|---|---|---|---|
| bodhichitta | tâm muốn giúp tất cả mọi người (tâm bồ đề) | tâm bồ đề | tâm bồ đề (bồ đề tâm) |
| suffering | khổ, nỗi khổ | khổ đau | khổ đau (khổ đế) |
| emptiness | sự trống rỗng của mọi thứ | tánh không | tánh không (vô tự tính) |
| merit | việc tốt, phước đức | công đức | công đức, phước đức |
| liberation | thoát khỏi khổ đau hoàn toàn | giải thoát | giải thoát (mokṣa) |

---

## Completion check

- [ ] Grade specified; correct termbase file loaded.
- [ ] Global termbase built from all verses in the file.
- [ ] Verses grouped by chapter; chapters processed in order.
- [ ] All verses in each chapter translated together.
- [ ] Locked terms identified per chapter before translating.
- [ ] Existing `vi-beginner-audience` translation checked for already-covered verses/terms.
- [ ] Translation produced at correct grade register.
- [ ] Consistency check passed: same Vietnamese form for same term across all verses.
- [ ] Markdown file written: one verse per block, Vietnamese text followed by `^{verse_id}`.
- [ ] Heading verses rendered as `## {vi_text} ^{verse_id}`.
- [ ] No JSON files modified.
