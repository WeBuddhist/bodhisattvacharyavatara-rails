#!/usr/bin/env python3
"""Render the termbase-step agent prompts for a run dir (English).

  python3 render_prompts.py <run-dir>
      -> <run-dir>/rendered/style-sheet.md   (writes <run-dir>/style-sheet.md)
      -> <run-dir>/rendered/batch-NN.md      (writes <run-dir>/agents/batch-NN.json)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
run = pathlib.Path(sys.argv[1]).resolve()
(run / "rendered").mkdir(exist_ok=True)
(run / "agents").mkdir(exist_ok=True)
registers = HERE / "registers.md"
(run / "rendered" / "style-sheet.md").write_text(
    (HERE / "prompts/style-sheet.md").read_text(encoding="utf-8").format(
        registers=registers, overview=run / "overview.md", out_path=run / "style-sheet.md"), encoding="utf-8")
tpl = (HERE / "prompts/terms-agent.md").read_text(encoding="utf-8")
names = sorted(f.stem for f in (run / "batches").glob("batch-*.json"))
for n in names:
    (run / "rendered" / f"{n}.md").write_text(tpl.format(
        registers=registers, style_sheet=run / "style-sheet.md", batch_path=run / "batches" / f"{n}.json",
        out_path=run / "agents" / f"{n}.json", batch_name=n, check_script=HERE / "check.py"), encoding="utf-8")
print(f"rendered style-sheet + {len(names)} batch prompts -> {run / 'rendered'}")
