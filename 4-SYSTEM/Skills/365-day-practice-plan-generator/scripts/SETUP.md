# Gemini-backed practice plan generator — setup

This folder contains `generate_day.py`, which runs the 365-day practice plan
skill through the Gemini API instead of an interactive chat, and writes the
result straight into `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/`.

This script contains no secrets and is safe to commit to a public repo.
Your Gemini API key never lives in this vault — see below.

## 1. One-time setup (run in your own PowerShell, on your machine)

Create a key file **outside** this vault, so `git add` here can never see it:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.secrets" | Out-Null
"GEMINI_API_KEY=PASTE_YOUR_KEY_HERE" | Out-File -FilePath "$env:USERPROFILE\.secrets\gemini.env" -Encoding utf8
notepad "$env:USERPROFILE\.secrets\gemini.env"
```

Replace `PASTE_YOUR_KEY_HERE` with your real key in Notepad, save, and close.
That file now lives at `C:\Users\<you>\.secrets\gemini.env` — a sibling of
your Obsidian folder, never inside it.

Install the one dependency:

```powershell
pip install -r "C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\4-SYSTEM\Skills\365-day-practice-plan-generator\scripts\requirements.txt"
```

## 2. Check which days still need generating

```powershell
cd "C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\4-SYSTEM\Skills\365-day-practice-plan-generator\scripts"
python generate_day.py --status
```

Anything flagged `PLACEHOLDER?` is under 3KB and likely not yet written.

## 3. Preview a day before spending API credits

```powershell
python generate_day.py --day 45 --dry-run
```

This prints the exact system instructions + prompt that would be sent to
Gemini, and does **not** call the API or touch any file.

## 4. Generate for real

```powershell
python generate_day.py --day 45
python generate_day.py --days 45-50
python generate_day.py --days 45,46,47
```

Each run:
- looks up the day's chapter/verse range in `schedule-corrected.md`
- pulls the exact root verse text (by `^chapter-verse` block reference) from
  `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`
- pulls the matching `2-RAILS/Verses/<chapter>-<verse>-summary.md` file(s)
- sends all of that, plus the full Gem instructions from
  `BCA-Practice-Plan-Gemini-Gem.md`, to `gemini-2.5-pro`
- backs up the existing target file to `.bak` (unless `--no-backup`)
- writes Gemini's response into the correct
  `Day-N-ChC-Vstart-end.md` file

## Notes / limits worth knowing

- The key file and the script are two different things: the script is plain
  code (safe for GitHub), the key file is the one thing that must never be
  committed. Double-check `C:\Users\<you>\.secrets\` is *not* inside the
  vault before your next `git push`.
- Gemini's output quality/formatting adherence for this very detailed
  Tibetan style guide may vary — spot-check a generated file against the
  quality checklist in `SKILL.md` before considering a day final.
- If a verse's summary file doesn't exist yet, the script still runs but
  inserts a `[NO SUMMARY FILE FOUND ...]` placeholder in the prompt, and
  Gemini will likely flag it per the skill's own instructions.
