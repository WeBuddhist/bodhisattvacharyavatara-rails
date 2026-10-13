#!/bin/zsh -i
# Recompute the before/after pairs and run the blind pairwise judge with the keep-best revert.
#   zsh -i factcheck/judge.sh <track> [<track> ...]     e.g. zh-academic   (from the kf-pilot dir)
# Judge a track only after its re-check and keep-best step. Pairs already judged are skipped.
cd /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot
PY=/Users/tashitsering/Desktop/work/Obsidian/KF-project/.venv/bin/python
R=reports
$PY factcheck/improvement.py --json $R/improvement-bodhicaryavatara.json --pairs $R/improvement-pairs-bodhicaryavatara.json > /dev/null
$PY -c "
import json, sys
p = json.load(open('$R/improvement-pairs-bodhicaryavatara.json'))
keep = [x for x in p if x['track'] in sys.argv[1:]]
json.dump(keep, open('$R/improvement-pairs-judge-batch.json', 'w'), ensure_ascii=False, indent=1)
print('pairs to judge:', len(keep))" "$@"
$PY factcheck/pairwise_judge.py $R/improvement-pairs-judge-batch.json --out $R/pairwise-langs-bodhicaryavatara.json --revert-losses
