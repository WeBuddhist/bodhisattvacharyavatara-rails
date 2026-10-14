#!/usr/bin/env python3
"""Render the fact-check agent prompt for every batch of a fact-check run (after prep.py).

  python3 render_prompts.py <run-dir>     # e.g. academic-a1, zh-academic-a1, hi-children-a2
      -> <run-dir>/rendered/batch-NN.md   (the agent writes <run-dir>/agents/batch-NN.json)

The run dir's name picks the template: a `zh-`/`hi-` prefix selects the -lang prompt,
`children` in the name the children's prompt.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
LANG_NAMES = {"zh": "Chinese (Traditional characters)", "hi": "Hindi (Devanagari)"}
run = pathlib.Path(sys.argv[1]).resolve()
lang = run.name.split("-")[0] if run.name.split("-")[0] in LANG_NAMES else "en"
kind = "factcheck-children" if "children" in run.name else "factcheck-agent"
tpl = (HERE / "prompts" / (f"{kind}-lang.md" if lang != "en" else f"{kind}.md")).read_text(encoding="utf-8")
(run / "rendered").mkdir(exist_ok=True)
(run / "agents").mkdir(exist_ok=True)
names = sorted(f.stem for f in (run / "batches").glob("batch-*.json"))
for n in names:
    (run / "rendered" / f"{n}.md").write_text(tpl.format(
        batch_path=run / "batches" / f"{n}.json", out_path=run / "agents" / f"{n}.json", batch_name=n,
        check_script=HERE / "check.py", lang_name=LANG_NAMES.get(lang, "English")), encoding="utf-8")
print(f"rendered {len(names)} {kind} prompts ({lang}) -> {run / 'rendered'}")
