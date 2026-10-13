#!/usr/bin/env python3
"""Fact-check loop helpers (the steps the Diamond Sutra did by hand).

  python3 loop.py render <run-dir> [--prompt factcheck-agent.md]
      fill the agent prompt for every <run-dir>/batches/batch-NN.json -> <run-dir>/rendered/batch-NN.md
  python3 loop.py feedback <run-dir> --variant academic [--lang en] [--minor]
      from <run-dir>/verdicts.json and the track's CURRENT text: feedback.json (segments that fail:
      their critical/major issues) or, with --minor, feedback-minor.json (passing segments with minor
      issues). Input of gm_variant_translate.py --feedback.
  python3 loop.py keep-best <recheck-run-dir> --variant academic [--lang en] --before <earlier-run-dir>
      keep-best rule: a segment that passed in the earlier run but fails in the re-check gets its
      earlier text back (ledger row with call_id "revert"); prints segments that failed both times.
"""
import argparse
import datetime as _dt
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("tr", HERE.parent / "translate" / "gm_variant_translate.py")
tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tr)


def render(a):
    run = pathlib.Path(a.run_dir).resolve()
    tpl = (HERE / "prompts" / a.prompt).read_text(encoding="utf-8")
    (run / "rendered").mkdir(exist_ok=True)
    (run / "agents").mkdir(exist_ok=True)
    names = sorted(f.stem for f in (run / "batches").glob("batch-*.json"))
    for n in names:
        (run / "rendered" / f"{n}.md").write_text(tpl.format(
            batch_path=run / "batches" / f"{n}.json", out_path=run / "agents" / f"{n}.json",
            batch_name=n, check_script=HERE / "check.py", lang_name=a.lang_name), encoding="utf-8")
    print(f"rendered {len(names)} prompts -> {run / 'rendered'}")


def checked_text(run):
    """{id: translation text the checker saw} from the run's batch files."""
    return {s["id"]: s["translation"] for f in (run / "batches").glob("batch-*.json")
            for s in json.loads(f.read_text(encoding="utf-8"))}


def feedback(a):
    run = pathlib.Path(a.run_dir)
    tr.LANG = a.lang
    rows = tr.latest(tr.work_file(a.lang, a.variant))
    seen = checked_text(run)
    out, skipped = {}, []
    for s in json.loads((run / "verdicts.json").read_text(encoding="utf-8")):
        if a.minor:
            iss = [i for i in s["issues"] if i["severity"] == "minor"] if s["verdict"] == "pass" else []
        else:
            iss = [i for i in s["issues"] if i["severity"] in ("critical", "major")] if s["verdict"] == "fail" else []
        if iss and s["id"] in seen and rows[s["id"]]["translation"] != seen[s["id"]]:
            skipped.append(s["id"])  # text changed since this check (e.g. keep-best revert): not this check's to fix
            continue
        if iss:
            out[s["id"]] = {"translation": seen.get(s["id"], rows[s["id"]]["translation"]), "issues": iss}
    name = "feedback-minor.json" if a.minor else "feedback.json"
    (run / name).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{name}: {len(out)} segments" + (f" (skipped, text changed since the check: {skipped})" if skipped else ""))


def keep_best(a):
    run, before = pathlib.Path(a.run_dir), pathlib.Path(a.before)
    tr.LANG = a.lang
    work = tr.work_file(a.lang, a.variant)
    v_now = {s["id"]: s for s in json.loads((run / "verdicts.json").read_text(encoding="utf-8"))}
    v_before = {s["id"]: s for s in json.loads((before / "verdicts.json").read_text(encoding="utf-8"))}
    text_before = checked_text(before)
    reverted, both = [], []
    with work.open("a", encoding="utf-8") as fh:
        for i, s in v_now.items():
            if s["verdict"] != "fail":
                continue
            if v_before.get(i, {}).get("verdict") == "pass":
                fh.write(json.dumps({"id": i, "translation": text_before[i], "variant": a.variant, "call_id": "revert",
                                     "attempt": 1, "model": "revert", "terms_required": None, "terms_missed": [],
                                     "batch": [i], "note": f"keep-best: re-check {run.name} failed; restored text checked in {before.name}",
                                     "ts": _dt.datetime.now().isoformat(timespec="seconds")}, ensure_ascii=False) + "\n")
                reverted.append(i)
            else:
                both.append(i)
    print(json.dumps({"reverted_to_earlier": reverted, "failed_both": both}))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("render")
    r.add_argument("run_dir")
    r.add_argument("--prompt", default="factcheck-agent.md")
    r.add_argument("--lang-name", default="English")
    r.set_defaults(func=render)
    f = sub.add_parser("feedback")
    f.add_argument("run_dir")
    f.add_argument("--variant", required=True)
    f.add_argument("--lang", default="en")
    f.add_argument("--minor", action="store_true")
    f.set_defaults(func=feedback)
    k = sub.add_parser("keep-best")
    k.add_argument("run_dir")
    k.add_argument("--variant", required=True)
    k.add_argument("--lang", default="en")
    k.add_argument("--before", required=True)
    k.set_defaults(func=keep_best)
    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    sys.exit(main())
