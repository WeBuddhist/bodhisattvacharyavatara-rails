#!/usr/bin/env python3
"""Log the exact usage of every Claude agent listed in an agents-map.json into the usage ledger.

  python3 harvest.py <run-dir>/agents-map.json [...]

The map holds session_dir, step, text, and optionally lang / variant / attempt, plus
{"agents": {batch-name: agent-id}}. Segment counts come from <run-dir>/batches/<batch>.json
where it exists. A map is harvested once: its run dir gets a `.harvested` marker.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
LEDGER = HERE.parents[1] / "4-SYSTEM/scripts/usage-ledger/usage_ledger.py"

for arg in sys.argv[1:]:
    mp = pathlib.Path(arg).resolve()
    run = mp.parent
    if (run / ".harvested").exists():
        print(f"{run.name}: already harvested")
        continue
    m = json.loads(mp.read_text(encoding="utf-8"))
    ok = 0
    for batch, aid in m["agents"].items():
        cmd = ["python3", str(LEDGER), "harvest-agent", "--session-dir", m["session_dir"], "--agent-id", aid,
               "--step", m["step"], "--text", m["text"], "--batch", batch, "--attempt", str(m.get("attempt", 1))]
        for k in ("lang", "variant"):
            if m.get(k):
                cmd += [f"--{k}", m[k]]
        bf = run / "batches" / f"{batch}.json"
        if bf.exists():
            cmd += ["--segments", str(len(json.loads(bf.read_text(encoding="utf-8"))))]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            ok += 1
        else:
            print(f"  {batch}: {r.stderr.strip()[-200:]}")
    (run / ".harvested").write_text(f"{ok} agents\n")
    print(f"{run.name}: harvested {ok}/{len(m['agents'])}")
