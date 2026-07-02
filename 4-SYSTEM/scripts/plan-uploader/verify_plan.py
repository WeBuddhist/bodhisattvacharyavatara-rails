#!/usr/bin/env python3
"""Print the full day/task/sub-task tree of a plan, as the CMS sees it.

Usage:  python verify_plan.py <PLAN_ID>
Reads credentials from plan_uploader.env (same as upload_plan.py).
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from upload_plan import BASE_URL, CmsClient, load_config


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python verify_plan.py <PLAN_ID>")
    plan_id = sys.argv[1]

    cfg = load_config(Path(__file__).with_name("plan_uploader.env"))
    base_url = cfg.get("WEBUDDHIST_BASE_URL") or BASE_URL
    client = CmsClient(base_url)
    if cfg.get("WEBUDDHIST_ACCESS_TOKEN"):
        client.use_token(cfg["WEBUDDHIST_ACCESS_TOKEN"])
    else:
        client.login(cfg["WEBUDDHIST_EMAIL"], cfg["WEBUDDHIST_PASSWORD"])

    plan = client.get_plan(plan_id)
    print(f"\nPlan : {plan.get('title')}  (status: {plan.get('status')})")
    days = plan.get("days") or []
    print(f"Days : {len(days)}")
    for d in days:
        tasks = d.get("tasks") or []
        print(f"\nDay {d.get('day_number')}  ({len(tasks)} tasks)")
        for t in tasks:
            subs = t.get("sub_tasks") or t.get("subtasks") or []
            print(f"  Task: {t.get('title')}  -> {len(subs)} sub-task(s)")
            for s in subs:
                content = (s.get("content") or "")[:60].replace("\n", " ")
                print(f"    [{s.get('content_type')}] {content}...")

    print("\n--- raw JSON (first 3000 chars) ---")
    print(json.dumps(plan, ensure_ascii=False, indent=1)[:3000])


if __name__ == "__main__":
    main()
