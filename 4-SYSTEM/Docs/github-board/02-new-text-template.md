# Template — onboarding a new text onto the board

For each new text, create 1 parent issue + 15 sub-issues by copying below and replacing `{{TEXT}}` with the text name. (The gh script in `03-setup-script.md` automates this.)

## Parent issue

**Title:** `[TEXT] {{TEXT}}`
**Labels:** `text` · **Status:** Backlog
**Body:**

> Master tracking issue for the full processing pipeline of {{TEXT}}.
>
> ### Stage overview
> - [ ] 1 · Sources: Root Text (S1–S2)
> - [ ] 1 · Sources: Translations & Commentaries (S3–S4)
> - [ ] 2 · Rails: Sections & Verses (R1–R3)
> - [ ] 2 · Rails: Claims & Wiki (R4–R7)
> - [ ] 3 · Transformations (T1–T4)

## Sub-issues (same bodies as in `01-issues-bodhicharyavatara.md`, with `{{TEXT}}` swapped in)

| ID | Title | Labels |
|---|---|---|
| S1 | `S1 [{{TEXT}}] Sanskrit root text: source high-quality edition + assign IDs` | `artifact` `stage:sources` `root-text` |
| S2 | `S2 [{{TEXT}}] Tibetan root text: multi-edition sourcing, proofread edition, IDs, verse-level Sanskrit alignment` | `artifact` `stage:sources` `root-text` |
| S3 | `S3 [{{TEXT}}] Existing human translations: source, assign IDs, link to root text` | `artifact` `stage:sources` `translations` |
| S4 | `S4 [{{TEXT}}] Commentaries: gather all, assign IDs, link to root text at verse level` | `artifact` `stage:sources` `commentaries` |
| R1 | `R1 [{{TEXT}}] Sections/RAW: extract table of contents for every text` | `artifact` `stage:rails` `sections` |
| R2 | `R2 [{{TEXT}}] Sections: one file per TOC level with section summaries` | `artifact` `stage:rails` `sections` |
| R3 | `R3 [{{TEXT}}] Verses: one file per root verse compiled from all commentaries` | `artifact` `stage:rails` `verses` |
| R4 | `R4 [{{TEXT}}] Claims/RAW: one file per commentary with all relevant claims/facts` | `artifact` `stage:rails` `claims` |
| R5 | `R5 [{{TEXT}}] Claims: one file per claim/question with answers from all commentaries` | `artifact` `stage:rails` `claims` |
| R6 | `R6 [{{TEXT}}] Local-Wiki/RAW: TF-IDF + YAKE keyword lists, combined en + bo lists` | `artifact` `stage:rails` `local-wiki` |
| R7 | `R7 [{{TEXT}}] Local-Wiki: one article per keyword (claims → TOC → draft → polished Tibetan)` | `artifact` `stage:rails` `local-wiki` |
| T1 | `T1 [{{TEXT}}] Transformations: plans` | `artifact` `stage:transformations` `plans` |
| T2 | `T2 [{{TEXT}}] Transformations: translations` | `artifact` `stage:transformations` `translation-out` |
| T3 | `T3 [{{TEXT}}] Transformations: short videos` | `artifact` `stage:transformations` `video` |
| T4 | `T4 [{{TEXT}}] Transformations: e-learning course` | `artifact` `stage:transformations` `elearning` |

> Note for prose-only texts (no verses / no Sanskrit original): drop S1, rename S2 to "root text edition", and R3 becomes per-section rather than per-verse compilations. Everything else applies unchanged.

## Upcoming-text placeholder cards (Backlog)

Seed the board with these as `[TEXT]`-labeled parent issues in **Backlog** (no sub-issues until work starts):

1. `[TEXT] ཀུན་བཟང་བླ་མའི་ཞལ་ལུང (Words of My Perfect Teacher)` — already appearing in `0-INBOX/`; note: prose text, no Sanskrit root (see note above)
2. `[TEXT] <next text — TBD>`

*(Confirm/replace with your actual upcoming texts.)*
