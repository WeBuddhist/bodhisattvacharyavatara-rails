#!/usr/bin/env python3
"""Read-only inspector for CMS plans.

Usage:
  python verify_plan.py                    # list all plans in your series
  python verify_plan.py <PLAN_ID>          # full day/task/sub-task tree
  python verify_plan.py <PLAN_ID> --day 3  # one day only
  python verify_plan.py <PLAN_ID> --json   # full raw JSON of the plan

Reads credentials from plan_uploader.env (same as upload_plan.py).
Never writes anything.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from upload_plan import BASE_URL, CmsClient, load_config


def get_client():
    cfg = load_config(Path(__file__).with_name("plan_uploader.env"))
    base_url = cfg.get("WEBUDDHIST_BASE_URL") or BASE_URL
    client = CmsClient(base_url)
    if cfg.get("WEBUDDHIST_ACCESS_TOKEN"):
        client.use_token(cfg["WEBUDDHIST_ACCESS_TOKEN"])
    else:
        client.login(cfg["WEBUDDHIST_EMAIL"], cfg["WEBUDDHIST_PASSWORD"])
    return client, cfg


def list_plans(client, cfg, series_id=None):
    series_id = series_id or cfg["WEBUDDHIST_SERIES_ID"]
    print(f"Series: {series_id}")
    for lang in ["BO", "EN", "ZH", "HI", "NE", "MN"]:
        plans = client.list_series_plans(series_id, lang)
        if plans:
            print(f"\n{lang} plans in series:")
            for p in plans:
                print(f"  {p.get('id')}  '{p.get('title')}'  "
                      f"status={p.get('status')}  days={p.get('total_days')}")


def show_plan(client, plan_id, only_day=None, as_json=False):
    plan = client.get_plan(plan_id)
    if as_json:
        print(json.dumps(plan, ensure_ascii=False, indent=1))
        return
    print(f"\nPlan : {plan.get('title')}  (status: {plan.get('status')})")
    days = plan.get("days") or []
    print(f"Days : {len(days)}")
    for d in days:
        if only_day is not None and d.get("day_number") != only_day:
            continue
        tasks = sorted(d.get("tasks") or [],
                       key=lambda t: t.get("display_order") or 0)
        print(f"\nDay {d.get('day_number')}  ({len(tasks)} tasks)")
        for t in tasks:
            subs = t.get("sub_tasks") or t.get("subtasks") or []
            print(f"  Task: {t.get('title')}  -> {len(subs)} sub-task(s)")
            for s in subs:
                ct = s.get("content_type")
                if ct == "SOURCE_REFERENCE":
                    print(f"    [{ct}] source_text_id={s.get('source_text_id')} "
                          f"pecha_segment_id={s.get('pecha_segment_id')} "
                          f"segment_ids={s.get('segment_ids')}")
                else:
                    content = (s.get("content") or "")[:70].replace("\n", " ")
                    print(f"    [{ct}] {content}...")


def main():
    args = [a for a in sys.argv[1:]]
    as_json = "--json" in args
    only_day = None
    series_id = None
    if "--day" in args:
        i = args.index("--day")
        only_day = int(args[i + 1])
        del args[i:i + 2]
    if "--series" in args:
        i = args.index("--series")
        series_id = args[i + 1]
        del args[i:i + 2]
    args = [a for a in args if a != "--json"]

    client, cfg = get_client()
    if not args:
        list_plans(client, cfg, series_id=series_id)
    else:
        show_plan(client, args[0], only_day=only_day, as_json=as_json)


if __name__ == "__main__":
    main()
