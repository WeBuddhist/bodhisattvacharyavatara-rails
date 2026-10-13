#!/bin/zsh
# Re-render the Gemini en ledger (partial is fine), rebuild segments/batches, report which batches have both baselines.
cd /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails
PY=/Users/tashitsering/Desktop/work/Obsidian/KF-project/.venv/bin/python; STEM="bo-བློ་ལྡན་ཤེས་རབ།"; G=3-TRANSFORMATIONS/Translations/Gemini/en
$PY 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py --source "1-SOURCES/Translations/$STEM.md" --lang english --lang-tag en --out $G --extra-fm "$G/work/extra-fm-$STEM.json" --render-only >/dev/null
$PY 0-INBOX/kf-pilot/term-extract/prep.py --root "1-SOURCES/Translations/$STEM.md" --baseline dm=3-TRANSFORMATIONS/Translations/Dharmamitra/en/$STEM-en.md --baseline gm=$G/$STEM-en.md --out 0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en | cut -c1-60
cd 0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en
$PY -c "
import json,glob,os
for f in sorted(glob.glob('batches/*.json')):
    b=json.load(open(f)); n=os.path.basename(f)[:-5]
    miss=[s['id'] for s in b if not s['gm'] and not s['heading']]
    print(n, 'READY' if not miss else f'waiting ({len(miss)} gm missing)', 'done' if os.path.exists(f'agents/{n}.json') else '')
"
