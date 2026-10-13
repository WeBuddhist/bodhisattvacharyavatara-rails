#!/bin/zsh -i
# Gemini MQM annotation of every blind sample (resumes).  zsh -i blind-eval/run_gemini.sh  (from kf-pilot)
cd /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/blind-eval
/Users/tashitsering/Desktop/work/Obsidian/KF-project/.venv/bin/python judge_gemini.py "$@"
