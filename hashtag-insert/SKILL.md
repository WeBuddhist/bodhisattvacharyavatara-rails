---
name: hashtag-insert
description: Insert contextual Tibetan practice hashtags (མཚན་རྟགས།) into root-verse translation files by matching each verse's meaning against a categorized hashtag/application list. Use this whenever the user wants root verses (e.g. from Shantideva's Bodhicaryavatara/སྤྱོད་འཇུག, or any similarly-structured Tibetan root text with ^chapter-verse block references) tagged with a provided list of hashtags, wants to "add hashtags to verses according to context," mentions མཚན་རྟགས།, or asks to match verses in an Obsidian vault to a tag/application table for later topical retrieval. Make sure to trigger this even if the user just says "tag the root verses" or pastes/points to a hashtag list without spelling out the full workflow.
---

# Hashtag Insert

Insert hashtags under root verses of a Tibetan text, choosing which tag(s) (if any) apply to each verse based on genuine thematic/contextual overlap with a user-supplied hashtag definition list — not keyword matching.

## Why this needs care

The hashtag lists this skill works with (see `references/tag-list-format.md` for a real example) are not generic topic tags — they're **practical-application tags**: each one names a specific real-life coping situation ("enduring harsh words," "losing wealth to theft," "facing a life-threatening illness," "calming anxiety about the future") together with a short description of when it applies. Only a minority of verses in any root text will genuinely speak to one of these situations. **It is correct and expected for most verses to receive zero tags.** Force-fitting a tag onto every verse defeats the purpose — the tags exist so a practitioner in a specific kind of distress can jump straight to verses that speak to it. A wrong or over-eager tag is worse than a missing one.

## Inputs you need

1. **The root-text file** — a markdown translation with `^chapter-verse` block references at the end of each verse (see `references/root-text-format.md`). Check its YAML frontmatter for `verse_id_format: chapter-verse` to confirm it follows this convention.
2. **The hashtag list file** — a markdown file with one or more `###` category sections, each containing a two-column pipe table: tag (backtick-quoted, starts with `#`) and application/context description. The user may point you at a specific file (e.g. a "... Tags.md" note) or paste the list directly.

If either input is ambiguous (multiple candidate files, or the user hasn't said which chapters to cover), ask before doing a full run — but if you already have a specific file path from the conversation, don't stop to ask, just proceed and state your interpretation.

## Workflow

### 1. Extract structured data with the bundled scripts

Don't hand-parse a large root-text file yourself — these files can run to hundreds of verses and it's easy to miscount lines or corrupt spacing by editing directly. Use the scripts:

```bash
python scripts/extract_tags.py "<tags_file.md>" -o tags.json
python scripts/extract_verses.py "<root_file.md>" -o verses.json
```

`extract_tags.py` walks the file top to bottom, tracks the current `###` category heading, and pulls out every `| \`#tag\` | application text |` row — tolerant of stray blank lines between rows (a common Obsidian export artifact). `extract_verses.py` walks the file and treats every line ending in `^<digits>-<digits>` as the close of one verse block; everything since the previous block boundary (heading, transclusion embed, or prior anchor) is that verse's text. Non-numeric anchors (like `^I-1` homage lines before chapter 1, or `^b-1` colophon lines at the very end) are recognized as boundaries but correctly excluded from the verse list, since they aren't root verses.

Inspect the JSON output (`tag_count`, `categories`, `verse_count`, `chapters`) and sanity-check it against what you'd expect from skimming the source files. If counts look wrong (e.g. way fewer verses than the frontmatter's `covers_verses` range implies), look at the raw file for a formatting quirk the parser didn't anticipate before proceeding.

### 2. Match verses to tags, chapter by chapter

Work through the verses in batches (one chapter at a time is a good default) rather than trying to hold the whole text and tag list in your head at once. For each verse:

- Read the verse's `text` and think about what it is actually saying — its doctrinal point, the situation it addresses, the practice it's teaching.
- Compare that against each tag's `application` description. Ask: would someone going through *this specific* situation be helped by being pointed at *this specific* verse?
- Assign a tag only when the match is clear and specific — not just thematically adjacent. A verse about patience in general doesn't automatically get every patience-related tag; match to the specific situation described in the application text (e.g. "enduring harsh words" vs. "not retaliating against harm" are different tags even though both are about anger/patience).
- A verse can get more than one tag if it genuinely addresses more than one situation, but keep this rare — most tagged verses will get exactly one.
- It's fine, and expected, for a verse to get zero tags.

Build a mapping file as you go, e.g. `mapping.json`:

```json
{
  "6-14": ["#ཚིག་ངན་བཟོད་པ།"],
  "6-21": ["#གནོད་ལན་མི་སློག་པ།", "#དགྲ་བོ་སློབ་དཔོན་དུ་ལྟ་བ།"]
}
```

Only include verse_ids that actually received a tag — don't add empty-array entries.

### 3. Apply the tags with the insert script

```bash
python scripts/insert_tags.py "<root_file.md>" mapping.json -o "<root_file>-tagged.md"
```

This never edits the input file in place — it always writes a new file, so the original stays untouched and the user can diff before accepting. It re-locates each verse's block-reference line using the same parser as step 1, then inserts the tags as their own paragraph directly beneath it, e.g.:

```
དེང་ནས་བཟུང་སྟེ་གཉིད་ལོག་གམ། །
བག་མེད་གྱུར་ཀྱང་བསོད་ནམས་ཤུགས། །
རྒྱུན་མི་འཆད་པར་དུ་མ་ཞིག །
ནམ་མཁའ་མཉམ་པར་རབ་ཏུ་འབྱུང་། ། #བྱང་ཆུབ་ཀྱི་སེམས། ^1-19

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-19]]
```

Everything else in the file — frontmatter, headings, transclusion embeds, verse text, spacing — is left byte-for-byte identical. If the user wants the original file edited in place rather than a new "-tagged" copy, do that as an explicit final step only after they've reviewed the output (e.g. by replacing the original once confirmed) — don't silently overwrite their source file.

### 4. Report back

Give the user a short summary: how many verses were tagged out of how many total, a breakdown of tag usage counts (so they can spot a tag that's suspiciously never used, or one used implausibly often), and call out any verses where you were genuinely unsure and made a judgment call, so they can double check those specifically.

## Working across a large text

A full root text can have 900+ verses across 10 chapters. Don't try to tag everything in one pass held in context — process and report chapter by chapter (or in similarly sized batches), building up `mapping.json` incrementally, and merge/apply at the end (or apply per-chapter as you go with separate `-o` outputs, whichever the user prefers). This keeps each matching decision grounded in a manageable amount of context rather than skimming under time/context pressure.

## Reference files

- `references/tag-list-format.md` — annotated real example of the hashtag list table format, including the categories/tags actually seen in this project.
- `references/root-text-format.md` — annotated real example of the root-text verse block format, including how frontispiece/homage and colophon material differs from numbered root verses.
