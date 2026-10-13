#!/bin/zsh -i
# Run (or resume) the translator for one track; extra args are passed through.
#   zsh -i translate/run.sh <lang> <variant> [--from-track academic] ...   (zsh -i reads the Gemini key)
cd /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails
lang=$1; variant=$2; shift 2
/Users/tashitsering/Desktop/work/Obsidian/KF-project/.venv/bin/python 0-INBOX/kf-pilot/translate/gm_variant_translate.py --variant $variant --lang $lang "$@"
