# About spyod-jug-365 — སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།

*Bodhisattvacaryāvatāra in 365 Days* — a daily study plan covering the entire text over one year.

## Purpose

A structured daily engagement with the *Bodhisattvacaryāvatāra*, providing five minutes of content per day. Each day covers one or more verses, with supporting context drawn from the commentary tradition.

## Per-session shape (all language streams)

Each day file contains:
1. **Daily notification text** — a short phrase suitable for a push notification
2. **Verse** — the root text passage(s) for the day, in the source language
3. **Reading for meaning** — the passage in the target language, generated from `2-RAILS/` verse packages
4. **Commentary note** — a brief gloss from the principal commentary tradition, drawn from the rails

## Languages

| Folder | Language | Status |
| ------ | -------- | ------ |
| `bo/` | Tibetan | active — 365 days generated |

## Source-rail dependencies

- `2-RAILS/Verses/<verse-id>.md` — verse-level context packages (status: `complete` required before use)
- `2-RAILS/Sections/<section-id>.md` — section context (for transition days)

## Status rules

Day files are generated as `draft`. A domain specialist sets `complete` after reviewing the day's content against the source rails. Only `complete` day files are published.

## Notes

- The `bo/schedule.md` file is the master day-by-day calendar for the Tibetan stream.
- Day files in `bo/days/` follow the naming convention: `ཉིན་ ༡།.md` through `ཉིན་ ༣༦༥།.md`.
