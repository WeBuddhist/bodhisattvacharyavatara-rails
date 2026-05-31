# The Bodhisattva Challenge: One Year Training in the Way of the Bodhisattva

*སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།* — a daily practice plan covering the entire Bodhisattvacharyavatara over one year.

## Purpose

A morning practice arc delivered by phone notification. Each day opens with a short hook, moves through a fixed liturgy (four immeasurables, refuge, bodhisattva vow), presents two to four verses from the *Bodhisattvacaryāvatāra* with a brief commentary note, closes with the aspiration and dedication, and ends with one concrete practice instruction for the day. The whole session takes five to ten minutes.

## Audience

Lay Buddhists who are new to Buddhist philosophy but already oriented to the bodhisattva path. They know about taking refuge and renewing the bodhisattva vow; they have not studied Śāntideva or the Mahāyāna sūtric tradition. They are time-poor, sceptical of formulaic spiritual content, and want authentic engagement with a primary text delivered efficiently.

## Per-session shape (all language streams)

Each day file contains exactly six elements, in this order:

1. **Opening** — a short notification text (max 12 words, the push notification) plus an introductory paragraph (max 60 words) that contextualises the day's verses within the training arc. The reader sees this first when they tap in.
2. **Renewing the Bodhisattva Vow** — four immeasurables, refuge, and bodhisattva vow. Identical text every day; presented as a recitation, not as new content.
3. **Today's verses** — root text passage(s) in Tibetan with English.
4. **From the Tradition** — one focused note (max 150 words) from the commentary tradition on a single topic from the day's verses. The verses are self-explanatory; this section is enrichment, not explanation.
5. **Aspiration and dedication** — aspiration prayer and dedication verses. Identical text every day.
6. **Today's Practice Challenge** — one concrete instruction derived from the commentary material, grounded in a recognisable real-life situation.

## Languages

| Folder | Language | Status |
| ------ | -------- | ------ |
| `bo/` | Tibetan | active — 365 days generated |
| `en/` | English | in progress — 12 days generated |

## Source-rail dependencies

- `2-RAILS/Verses/<verse-id>.md` — verse-level context packages (status: `complete` required before use)
- `2-RAILS/Sections/<section-id>.md` — section context (for transition days)

## Status rules

Day files are generated as `draft`. A domain specialist sets `complete` after reviewing the day's content against the source rails. Only `complete` day files are published.

## Notes

- The `bo/schedule.md` file is the master day-by-day calendar for the Tibetan stream. Day files follow the naming convention `ཉིན་ ༡།.md` through `ཉིན་ ༣༦༥།.md`.
- The `en/schedule.md` file is the master calendar for the English stream. Day files follow the naming convention `1.md` through `365.md`.
- Per-stream style contracts and vocabulary contracts live at `<lang>/requirements.md` and `<lang>/termbase.md` respectively.
