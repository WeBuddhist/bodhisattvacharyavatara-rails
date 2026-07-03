#!/usr/bin/env python3
"""Give a task SOURCE_REFERENCE sub-tasks pointing at a WeBuddhist edition
(Pecha text) by edition ID and segment numbers.

Resolves the edition's real segment IDs from the public WeBuddhist API
(segment numbers -> segment IDs), then creates the sub-tasks, trying the
known field mappings until the CMS accepts one.

Usage
-----
python set_source_ref.py --plan-id <PLAN_ID> --day 1 \
    --task "TITLE" --create --position 3 \
    --edition 3rCvwAoWrzKGlIQdtLjCu --segments 1-3

Credentials: same plan_uploader.env as upload_plan.py.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from upload_plan import BASE_URL, CmsClient, load_config, _sorted_tasks, _titles_equal

PUBLIC_BASE = "https://api.webuddhist.com/api/v1"


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


# ---------------------------------------------------------------------------
# Segment resolution against the public Pecha API
# ---------------------------------------------------------------------------


def _get_json(requests, url, params=None):
    try:
        r = requests.get(url, params=params or {}, timeout=30)
        print(f"  GET {r.url} -> {r.status_code}")
        if r.status_code == 200 and r.text:
            return r.json()
    except Exception as e:
        print(f"  GET {url} failed: {e}")
    return None


def _walk(node, found: dict):
    """Recursively collect {segment_number: segment_id} pairs."""
    if isinstance(node, dict):
        num = node.get("segment_number", node.get("number"))
        sid = node.get("segment_id") or node.get("id")
        if num is not None and sid and str(num).isdigit():
            found.setdefault(str(num), str(sid))
        for v in node.values():
            _walk(v, found)
    elif isinstance(node, list):
        for v in node:
            _walk(v, found)


def resolve_segments(requests, edition: str, numbers: list[str]) -> dict:
    """Return {number: segment_id}. Prints its trail for debugging."""
    print(f"Resolving segments {numbers} of edition {edition} "
          f"via {PUBLIC_BASE} ...")
    found: dict = {}
    candidates = [
        (f"{PUBLIC_BASE}/texts/versions/{edition}/info", None),
        (f"{PUBLIC_BASE}/texts/{edition}/contents", {"limit": 100}),
    ]
    text_id = None
    for url, params in candidates:
        data = _get_json(requests, url, params)
        if data is None:
            continue
        _walk(data, found)
        if isinstance(data, dict):
            text_id = text_id or data.get("text_id") or (
                (data.get("text") or {}).get("id")
                if isinstance(data.get("text"), dict) else None)
        if all(n in found for n in numbers):
            break
    if text_id and not all(n in found for n in numbers):
        data = _get_json(requests,
                         f"{PUBLIC_BASE}/texts/{text_id}/contents",
                         {"version_id": edition, "limit": 100})
        if data is not None:
            _walk(data, found)

    hits = {n: found[n] for n in numbers if n in found}
    if hits:
        print(f"  resolved: {hits}")
    else:
        print("  no segment IDs resolved (will fall back to raw numbers)")
    return hits


# ---------------------------------------------------------------------------
# Sub-task creation variants
# ---------------------------------------------------------------------------


def _st(content_type="SOURCE_REFERENCE", **over):
    base = {
        "content_type": content_type,
        "content": "",
        "duration": None,
        "source_text_id": None,
        "pecha_segment_id": None,
        "segment_ids": None,
        "start_ms": None,
        "end_ms": None,
    }
    base.update(over)
    return base


def build_variants(edition: str, numbers: list[str], resolved: dict) -> list:
    """Ordered list of (name, sub_tasks_payload) to try against the CMS."""
    variants = []
    if resolved and all(n in resolved for n in numbers):
        ids = [resolved[n] for n in numbers]
        variants += [
            ("per-segment: pecha_segment_id=<uuid>, source_text_id=<edition>",
             [_st(pecha_segment_id=i, source_text_id=edition) for i in ids]),
            ("per-segment: pecha_segment_id=<uuid>",
             [_st(pecha_segment_id=i) for i in ids]),
            ("single: segment_ids=<uuids>, source_text_id=<edition>",
             [_st(segment_ids=ids, source_text_id=edition)]),
            ("single: segment_ids=<uuids>",
             [_st(segment_ids=ids)]),
        ]
    variants += [
        ("per-segment: pecha_segment_id=<number>, source_text_id=<edition>",
         [_st(pecha_segment_id=n, source_text_id=edition) for n in numbers]),
        ("per-segment: pecha_segment_id=<number>",
         [_st(pecha_segment_id=n) for n in numbers]),
    ]
    return variants


def create_subtasks(client, task_id: str, variants: list) -> list:
    for name, fields in variants:
        data = client._call("POST", "/cms/sub-tasks",
                            tolerate=(400, 422, 500),
                            json={"task_id": task_id, "sub_tasks": fields})
        if data is not None:
            subs = data.get("sub_tasks") or data.get("subtasks") or []
            if subs:
                print(f"Accepted variant: {name}")
                return subs
        print(f"Rejected variant: {name}")
    sys.exit("The CMS rejected every sub-task variant — paste this output "
             "back so the field mapping can be corrected.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


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
                    help="1-based position for the task (default: keep "
                         "current position, or append when creating)")
    ap.add_argument("--edition", required=True, help="WeBuddhist edition ID")
    ap.add_argument("--segments", required=True, help='e.g. "1-3" or "1,2,3"')
    ap.add_argument("--language", default="BO")
    ap.add_argument("--no-preset", action="store_true")
    ap.add_argument("--env", type=Path,
                    default=Path(__file__).with_name("plan_uploader.env"))
    args = ap.parse_args()

    numbers = parse_segments(args.segments)

    cfg = load_config(args.env)
    base_url = cfg.get("WEBUDDHIST_BASE_URL") or BASE_URL
    print(f"API base : {base_url}")
    client = CmsClient(base_url)
    if cfg.get("WEBUDDHIST_ACCESS_TOKEN"):
        client.use_token(cfg["WEBUDDHIST_ACCESS_TOKEN"])
    else:
        client.login(cfg["WEBUDDHIST_EMAIL"], cfg["WEBUDDHIST_PASSWORD"])

    resolved = resolve_segments(client.requests, args.edition, numbers)

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

    if target_idx is not None:
        old = tasks[target_idx]
        title = old.get("title") or args.task
        print(f"Target: day {args.day}, task {target_idx + 1} '{title}' "
              f"(replace)")
        client.delete_task(old["id"])
        new_task_id = client.create_task(args.plan_id, day["id"], title)
        print(f"Recreated task (TASK_ID={new_task_id})")
    else:
        title = args.task
        print(f"Target: day {args.day}, NEW task '{title}'")
        new_task_id = client.create_task(args.plan_id, day["id"], title)
        print(f"Created task (TASK_ID={new_task_id})")

    # create SOURCE_REFERENCE sub-tasks, trying field mappings in order
    variants = build_variants(args.edition, numbers, resolved)
    subs = create_subtasks(client, new_task_id, variants)
    sub_ids = [s.get("id") for s in subs]
    print(f"Created {len(sub_ids)} sub-task(s): {sub_ids}")

    # best-effort preset link (endpoint 500s on some servers)
    if not args.no_preset:
        for sid in sub_ids:
            r = client._call(
                "POST", f"/cms/sub-tasks/{sid}/preset",
                tolerate=(400, 404, 422, 500),
                json={"version_id": args.edition, "language": args.language},
            )
            print(f"  preset {'linked' if r is not None else 'FAILED (non-fatal)'}"
                  f" on {sid}")

    # restore task order (new/recreated task was appended to the end)
    final_ids = [t["id"] for t in tasks]
    if old is not None:
        final_ids.remove(old["id"])
    pos = (args.position - 1) if args.position else (
        target_idx if old is not None else len(final_ids))
    pos = max(0, min(pos, len(final_ids)))
    final_ids.insert(pos, new_task_id)
    client.reorder_tasks(day["id"], final_ids)
    print(f"Task order restored (task placed at position {pos + 1}).")

    # verify
    plan = client.get_plan(args.plan_id)
    day = next(d for d in plan.get("days") or []
               if d.get("day_number") == args.day)
    tasks = _sorted_tasks(day)
    t = tasks[pos]
    subs = t.get("sub_tasks") or t.get("subtasks") or []
    print(f"\nVerification: task {pos + 1} '{t.get('title')}' "
          f"now has {len(subs)} sub-task(s):")
    for s in subs:
        print(f"  [{s.get('content_type')}] "
              f"source_text_id={s.get('source_text_id')} "
              f"pecha_segment_id={s.get('pecha_segment_id')} "
              f"segment_ids={s.get('segment_ids')}")
    if subs and all(s.get("content_type") == "SOURCE_REFERENCE" for s in subs):
        print("\nVerification passed.")
    else:
        sys.exit("\nVerification FAILED — no SOURCE_REFERENCE sub-tasks "
                 "visible. Paste this full output back.")


if __name__ == "__main__":
    main()
