#!/usr/bin/env python3
"""Render the extraction-agent prompt for each batch of a term-extract run.

  python3 render_prompts.py <run-dir> [batch-01 batch-02 ...]   -> <run-dir>/prompts/batch-NN.md

Without batch names, renders every batch in <run-dir>/batches/.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
run = pathlib.Path(sys.argv[1]).resolve()
names = sys.argv[2:] or sorted(f.stem for f in (run / "batches").glob("batch-*.json"))
tpl = (HERE / "prompts/extract-agent.md").read_text(encoding="utf-8")
(run / "prompts").mkdir(exist_ok=True)
(run / "agents").mkdir(exist_ok=True)
for n in names:
    (run / "prompts" / f"{n}.md").write_text(tpl.format(
        batch_path=run / "batches" / f"{n}.json", out_path=run / "agents" / f"{n}.json",
        batch_name=n, check_script=HERE / "verify.py"), encoding="utf-8")
print(f"rendered {len(names)} prompts -> {run / 'prompts'}")
