#!/usr/bin/env python3
"""Render the termbase-step agent prompts for a non-English run dir (after prep_lang.py).

  python3 render_prompts_lang.py <run-dir>      # run dir name ends in -zh or -hi
      -> <run-dir>/rendered/style-sheet.md   (writes <run-dir>/style-sheet.md)
      -> <run-dir>/rendered/batch-NN.md      (writes <run-dir>/agents/batch-NN.json)

The Diamond Sutra filled these templates by hand; this does the same, without the
Kumārajīva notes (the Bodhicaryāvatāra's human Chinese versions stay out of the pipeline).
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
LANG = {
    "zh": {"name": "Chinese (Traditional characters)", "zs": "modern Chinese"},
    "hi": {"name": "Hindi (Devanagari)", "zs": "Hindi"},
}
run = pathlib.Path(sys.argv[1]).resolve()
lang = run.name.rsplit("-", 1)[-1]
L = LANG[lang]
example_note = f" and a Gemini zero-shot {L['zs']} line (`gemini_zero_shot`)"
common = dict(lang_name=L["name"], registers=HERE / f"registers-{lang}.md")
(run / "rendered").mkdir(exist_ok=True)
(run / "agents").mkdir(exist_ok=True)
(run / "rendered" / "style-sheet.md").write_text(
    (HERE / "prompts/style-sheet-lang.md").read_text(encoding="utf-8").format(
        **common, overview=run / "overview.md", examples=run / "terms.json",
        example_note=example_note,
        policy_note=f" (established {L['zs']} Buddhist usage vs the Gemini zero-shot)",
        out_path=run / "style-sheet.md"), encoding="utf-8")
tpl = (HERE / "prompts/terms-agent-lang.md").read_text(encoding="utf-8")
names = sorted(f.stem for f in (run / "batches").glob("batch-*.json"))
for n in names:
    (run / "rendered" / f"{n}.md").write_text(tpl.format(
        **common, style_sheet=run / "style-sheet.md", batch_path=run / "batches" / f"{n}.json",
        example_note=example_note,
        basis_note='"zero-shot" if you took the Gemini line\'s term, "style-sheet" if from the style sheet, '
                   '"english-pivot" if you translated the English rendering, "new" otherwise;',
        out_path=run / "agents" / f"{n}.json", batch_name=n, check_script=HERE / "check.py"), encoding="utf-8")
print(f"rendered style-sheet + {len(names)} batch prompts -> {run / 'rendered'}")
