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
        ├── communications/     # outreach content for this language
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
- **Per-session shape** — the structure every day-file follows regardless of language (e.g. liturgy → text of the day → commentary → reflection → notif