# Plans — per-plan convention

This folder holds calendar-driven study and practice arcs: daily readings, weekly retreat sessions, year-long courses, chanting schedules. Each plan organises engagement with the text along a calendar, generating per-session content from rails (and often from completed Translation or Adaptation outputs).

See [`../About Transformations.md`](../About%20Transformations.md) for the top-level rules that govern all transformation categories.

---

## Plan structure

Each plan is one subfolder. Inside that folder, language streams are completely separate — one subfolder per language code. The plan root holds only the cross-language overview document.

```
Plans/
└── <plan-name>/
    ├── About <plan-name>.md    # plan overview, cross-language structure, session shape
    └── <lang>/                 # one folder per published language (e.g. en/, bn/, pi/)
        ├── requirements.md     # style contract for this language stream (in target language)
        ├── schedule.md         # day-by-day calendar for this language
        ├── termbase.md         # vocabulary contract for this language
        ├── days/               # per-session output files
        │   ├── day-1.md        # intro day: plan overview + text of day + notifications
        │   ├── day-2.md
        │   └── ...
        ├── communication/      # outreach content for this language
        │   ├── announcements.md
        │   └── ...
        └── assets/
            ├── images/
            └── ...
```

### Why per-language subfolders

Keeping each language stream self-contained lets teams work independently — the English drafters don't touch the Bengali folder, and vice versa. It also means each language stream can be at a different completion stage: `en/` may be `complete` while `bn/` is still `draft`, with no risk of mixing content.

---

## The plan root: `About <plan-name>.md`

The single file at the plan root is the cross-language overview. It covers:

- **What the plan is** — purpose, duration, intended audience (across all languages).
- **Per-session shape** — the structure every day-file follows regardless of language (e.g. liturgy → text of the day → commentary → reflection → notifications). This is the binding template; individual language `requirements.md` files fill in the language-specific rendering of each step.
- **Languages published** — list of `<lang>/` subfolders and their status.
- **Source-rail dependencies** — which `2-RAILS/` packages each session draws from.
- **Status rules** — what `draft / partial / complete` mean for plan sessions specifically.
- **Reading path** — links to each language stream's `requirements.md` and `schedule.md`.

---

## Per-language files

### `requirements.md` — language-stream style contract

Written **in the target language**. Covers:

- Target audience and register for this language stream.
- Rendering conventions for the session steps defined in `About <plan-name>.md`.
- Communications style (tone, length, platform conventions for announcements and notifications).
- Cultural-adaptation rules (what to translate, gloss, leave untranslated, or omit).
- Source-rail dependencies (which rails and which completed outputs from other tracks feed this stream).

### `termbase.md` — vocabulary contract

One chosen rendering per keyword, scoped to the terms that actually appear in the plan's day files. Built by the `glossary-select` skill from the consolidated `2-RAILS/Bilingual-Glossaries/<src>-<tgt>.md`, guided by `requirements.md`.

### `schedule.md` — day-by-day calendar

The complete ordered list of days for this language stream: date, day number, verse or section reference, and any language-specific notes (public holidays, local events that affect delivery). One row per session.

---

## Day files (`days/day-N.md`)

Each day file is a self-contained publishing unit. Minimum structure:

```yaml
---
day: 1
ref: [verse-id or section-id]
transformation_type: plan-session
context_packages:
  - 2-RAILS/Verses/[verse-id].md
  - 2-RAILS/Sections/[node-id].md
generation_date: [ISO date]
status: draft | partial | complete
---
```

```markdown
## [Day title / theme]

[Plan introduction — only on day-1; omitted from subsequent days.]

## Text of the Day

![[3-TRANSFORMATIONS/Translations/[track]/[output].md#^[verse-ref]]]

## [Commentary step, reflection, or practice instruction]

[Content drawn from the verse-context rail, rendered for this audience.]

## Notifications

**Push notification (short):** [~100 characters]
**Social media:** [~280 characters]
**Email subject:** [~60 characters]
```

- Transclude the text of the day from the relevant Translation track output — never copy-paste.
- All content traces to `2-RAILS/` packages listed in `context_packages:`.
- The notifications block gives communicators ready-to-send copy for each channel; it is generated alongside the day content, not separately.

---

## Communications folder

`communication/` holds cross-day outreach content for this language stream — material that spans multiple sessions or the plan as a whole:

- `announcements.md` — launch announcement, milestone announcements, closing announcement.
- Additional files as needed (e.g. `social-media-kit.md`, `email-series.md`).

Per-day notifications live in each `days/day-N.md` file, not here.

---

## Starting a new plan

1. Create `Plans/<plan-name>/`.
2. Author `About <plan-name>.md` — define the session shape and languages before any language stream begins.
3. For each language stream: create `Plans/<plan-name>/<lang>/` and author `requirements.md` (in the target language), then run `glossary-select` to produce `termbase.md`.
4. Build `schedule.md` for each language stream.
5. Create the `days/` folder; generate day-1 as `draft` using the verse/section rails; iterate through review until `complete` before moving to day-2.
6. Add communications content as the plan rolls out.

---

## Citation rules for plan sessions

Plan sessions may cite:
- `2-RAILS/` packages — always.
- Completed outputs from Translation or Adaptation tracks — when transcluding the text of the day or embedding a commentary rendering. Record these in `context_packages:` the same way as rail packages.

Plan sessions may **not** cite `1-SOURCES/` directly. All source-text content reaches the day file through a Translation track output, never raw.
