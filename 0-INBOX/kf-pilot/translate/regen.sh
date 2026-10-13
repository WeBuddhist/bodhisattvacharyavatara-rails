#!/bin/zsh -i
# Fix round for one track: regenerate the failing segments, then the minor-only ones (attempt 2).
#   zsh translate/regen.sh <lang> <variant> <factcheck-run-dir>     (from the kf-pilot dir; zsh -i reads the Gemini key)
cd /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails
PY=/Users/tashitsering/Desktop/work/Obsidian/KF-project/.venv/bin/python
T=0-INBOX/kf-pilot/translate/gm_variant_translate.py
$PY $T --variant $2 --lang $1 --feedback 0-INBOX/kf-pilot/factcheck/$3/feedback.json --attempt 2
$PY $T --variant $2 --lang $1 --feedback 0-INBOX/kf-pilot/factcheck/$3/feedback-minor.json --attempt 2
