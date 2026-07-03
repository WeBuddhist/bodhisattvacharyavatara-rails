#!/usr/bin/env python3
"""Replace a task's sub-tasks with SOURCE_REFERENCE sub-tasks pointing at a
WeBuddhist edition (Pecha text) by edition ID and segment numbers.

Recreates the task (the CMS has no delete-sub-task endpoint), adds one
SOURCE_REFERENCE sub-task per segment, links the edition to each sub-task
as a preset, and restores the task's position in the day.

Usage
-----
python set_source_ref.py --plan-id <PLAN_ID> --day 1 --task 3 \
    --edition 3rCvwAoWrzKGlIQdtLjCu --segments 1-3

Options:
  --task         1-based task position in the day (or exact task title)
  --segments     "1-3" or "1,2,3"
  --language     preset language (default BO)
  --single       one sub-task carrying all segments in segment_ids,
                 instead of one sub-task per segment (default: per-segment)
  --edition-as-source-text
                 put the edition ID in source_text_id instead of the preset
  --no-preset    skip the preset call

Credentials: same plan_uploader.env as upload_plan.py.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from upload_plan import BASE_URL, CmsClient, load_config, _sorted_tasks, _titles_equal


def parse_segments(spec: str) -> list[str]:
    segs: list[str] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            segs.extend(str(n) for n in range(int(a), int(b) + 1))
        elif part:
            segs.append(part)
    if not segs:
        sys.exit(f"No segments parsed from '{spec}'")
    return segs


def make_subtask_fields(edition: str, segments: list[str], single: bool,
                        edition_as_source_text: bool) -> list[dict]:
    base = {
        "content_type": "SOURCE_REFERENCE",
        "content": "",
        "duration": None,
        "source_text_id": edition if edition_as_source_text else None,
        "pecha_segment_id": None,
        "segment_ids": None,
        "start_ms": None,
        "end_ms": None,
    }
    if single:
        st = dict(base)
        st["segment_ids"] = segments
        return [st]
    out = []
    for seg in segments:
        st = dict(base)
        st["pecha_segment_id"] = seg
        out.append(st)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--plan-id", required=True)
    ap.add_argument("--day", type=int, required=True)
    ap.add_argument("--task", required=True,
                    help="1-based task position in the day, or exact title")
    ap.add_argument("--create", action="store_true",
                    help="If the task doesn't exist, create it (requires "
                         "--task to be a title, not a position)")
    ap.add_argument("--position", type=int, default=None,
                    help="1-based position for a newly created task "
                         "(default: append at the end)")
    ap.add_argument("--edition", required=True, help="WeBuddhist edition ID")
    ap.add_argument("--segments", required=True, help='e.g. "1-3" or "1,2,3"')
    ap.add_argument("--language", default="BO")
    ap.add_argument("--single", action="store_true")
    ap.add_argument("--edition-as-source-text", action="store_true")
    ap.add_argument("--no-preset", action="store_true")
    ap.add_argument("--env", type=Path,
                    default=Path(__file__).with_name("plan_uploader.env"))
    args = ap.parse_args()

    segments = parse_segments(args.segments)

    cfg = load_config(args.env)
    base_url = cfg.get("WEBUDDHIST_BASE_URL") or BASE_URL
    print(f"API base : {base_url}")
    client = CmsClient(base_url)
    if cfg.get("WEBUDDHIST_ACCESS_TOKEN"):
        client.use_token(cfg["WEBUDDHIST_ACCESS_TOKEN"])
    else:
        client.login(cfg["WEBUDDHIST_EMAIL"], cfg["WEBUDDHIST_PASSWORD"])

    plan = client.get_plan(args.plan_id)
    day = next((d for d in plan.get("days") or []
                if d.get("day_number") == args.day), None)
    if day is None:
        sys.exit(f"Day {args.day} not found in plan.")
    tasks = _sorted_tasks(day)

    # locate target task by index or title
    target_idx = None
    old = None
    if args.task.isdigit():
        idx = int(args.task) - 1
        if not 0 <= idx < len(tasks):
            sys.exit(f"Day has {len(tasks)} tasks; no position {args.task}. "
                     "(To create a new task, pass --create with a title.)")
        target_idx = idx
    else:
        for i, t in enumerate(tasks):
            if _titles_equal(t.get("title") or "", args.task):
                target_idx = i
                break
        if target_idx is None and not args.create:
            sys.exit(f"No task titled '{args.task}' in day {args.day} "
                     "(pass --create to create it).")

    n_subs_desc = "1 combined" if args.single else str(len(segments))
    if target_idx is not None:
        old = tasks[target_idx]
        title = old.get("title") or args.task
        print(f"Target: day {args.day}, task {target_idx + 1} '{title}' "
              f"(replace)")
        print(f"Replacing with {n_subs_desc} SOURCE_REFERENCE sub-task(s): "
              f"edition={args.edition}, segments={','.join(segments)}")
        client.delete_task(old["id"])
        new_task_id = client.create_task(args.plan_id, day["id"], title)
        print(f"Recreated task (TASK_ID={new_task_id})")
    else:
        title = args.task
        target_idx = (args.position - 1 if args.position
                      else len(tasks))
        target_idx = max(0, min(target_idx, len(tasks)))
        print(f"Target: day {args.day}, NEW task '{title}' at position "
              f"{target_idx + 1}")
        print(f"Creating with {n_subs_desc} SOURCE_REFERENCE sub-task(s): "
              f"edition={args.edition}, segments={','.join(segments)}")
        new_task_id = client.create_task(args.plan_id, day["id"], title)
        print(f"Created task (TASK_ID={new_task_id})")

    # 2. create SOURCE_REFERENCE sub-tasks
    fields = make_subtask_fields(args.edition, segments, args.single,
                                 args.edition_as_source_text)
    data = client._call("POST", "/cms/sub-tasks",
                        json={"task_id": new_task_id, "sub_tasks": fields})
    subs = (data or {}).get("sub_tasks") or (data or {}).get("subtasks") or []
    sub_ids = [s.get("id") for s in subs]
    print(f"Created {len(sub_ids)} sub-task(s): {sub_ids}")

    # 3. link the edition as a preset on each sub-task
    if not args.no_preset:
        for sid in sub_ids:
            r = client._call(
                "POST", f"/cms/sub-tasks/{sid}/preset",
                tolerate=(400, 404, 422),
                json={"version_id": args.edition, "language": args.language},
            )
            if r is not None:
                print(f"  preset linked on {sid}")

    # 4. restore task order (new/recreated task was appended to the end)
    if old is not None:
        final_ids = [new_task_id if t["id"] == old["id"] else t["id"]
                     for t in tasks]
    else:
        final_ids = [t["id"] for t in tasks]
        final_ids.insert(target_idx, new_task_id)
    client.reorder_tasks(day["id"], final_ids)
    print("Task order restored.")

    # 5. verify
    plan = client.get_plan(args.plan_id)
    day = next(d for d in plan.get("days") or []
               if d.get("day_number") == args.day)
    tasks = _sorted_tasks(day)
    t = tasks[target_idx]
    subs = t.get("sub_tasks") or t.get("subtasks") or []
    print(f"\nVerification: task {target_idx + 1} '{t.get('title')}' "
          f"now has {len(subs)} sub-task(s):")
    ok = True
    for s in subs:
        ct = s.get("content_type")
        print(f"  [{ct}] source_text_id={s.get('source_text_id')} "
              f"pecha_segment_id={s.get('pecha_segment_id')} "
              f"segment_ids={s.get('segment_ids')}")
        ok = ok and ct == "SOURCE_REFERENCE"
    expected = 1 if args.single else len(segments)
    if ok and len(subs) == expected:
        print("\nVerification passed.")
    else:
        sys.exit("\nVerification FAILED — inspect output above.")


if __name__ == "__main__":
    main()
