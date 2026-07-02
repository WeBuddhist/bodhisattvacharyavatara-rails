#!/usr/bin/env python3
"""Upload a Bodhisattva Challenge day file to the WeBuddhist Studio CMS.

Implements the workflow documented in
`3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/Plan Uploader.md`:

    Login -> Create plan (series_id + language) -> Add day
          -> Create tasks (one per ### section)
          -> Create sub-tasks (TEXT content, HTML)

The plan is left in DRAFT status unless --publish is passed.

Usage
-----
# Dry run — parse only, no network calls:
python upload_plan.py "path/to/Day-1-Ch1-V1-3.md" --dry-run

# Create a new plan in the series and upload Day 1:
python upload_plan.py "path/to/Day-1-Ch1-V1-3.md" \
    --title "སྤྱོད་འཇུག་ཉིན་རེའི་ཉམས་ལེན། ལེའུ་དང་པོ།" \
    --description "ཉིན་ ༡ - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང་།" \
    --total-days 14

# Add another day to an existing plan:
python upload_plan.py "path/to/Day-2-Ch1-V4-5.md" --plan-id <PLAN_ID>

Credentials & IDs
-----------------
Read from environment variables, or from a key=value file passed with
--env (default: `plan_uploader.env` next to this script):

    WEBUDDHIST_EMAIL=author@example.com
    WEBUDDHIST_PASSWORD=...
    WEBUDDHIST_SERIES_ID=<uuid>
    WEBUDDHIST_GROUP_ID=<uuid>

Requires: pip install requests
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

BASE_URL = "https://api.webuddhist.com/api/v1"

# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------

REQUIRED_KEYS = [
    "WEBUDDHIST_EMAIL",
    "WEBUDDHIST_PASSWORD",
    "WEBUDDHIST_SERIES_ID",
    "WEBUDDHIST_GROUP_ID",
]


def load_config(env_path: Path) -> dict:
    """Environment variables win; fall back to key=value lines in env_path."""
    cfg = {}
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            cfg[key.strip()] = val.strip()
    for key in REQUIRED_KEYS:
        if os.environ.get(key):
            cfg[key] = os.environ[key]
    missing = [k for k in REQUIRED_KEYS if not cfg.get(k)]
    if missing:
        sys.exit(
            "Missing config: " + ", ".join(missing)
            + f"\nSet them as environment variables or in {env_path}"
        )
    return cfg


# --------------------------------------------------------------------------
# Markdown parsing
# --------------------------------------------------------------------------

TIBETAN_NUMERAL_PREFIX = re.compile(r"^[༠-༩]+[།.]\s*")
SECTION_RE = re.compile(r"^###\s+(?!#)(.+?)\s*$")
SUBSECTION_RE = re.compile(r"^####\s+(.+?)\s*$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def strip_md_inline(text: str) -> str:
    """Convert inline markdown (bold) to HTML."""
    return BOLD_RE.sub(r"<strong>\1</strong>", text)


def md_block_to_html(lines: list[str]) -> str:
    """Convert a section's markdown lines to simple HTML."""
    html: list[str] = []
    para: list[str] = []
    quote: list[str] = []

    def flush_para():
        if para:
            html.append("<p>" + "<br/>".join(strip_md_inline(l) for l in para) + "</p>")
            para.clear()

    def flush_quote():
        if quote:
            html.append(
                "<blockquote>"
                + "<br/>".join(strip_md_inline(l) for l in quote)
                + "</blockquote>"
            )
            quote.clear()

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_para()
            flush_quote()
            continue
        if stripped == "---":
            flush_para()
            flush_quote()
            continue
        m = SUBSECTION_RE.match(stripped)
        if m:
            flush_para()
            flush_quote()
            title = BOLD_RE.sub(r"\1", m.group(1)).strip()
            html.append(f"<h4>{title}</h4>")
            continue
        if stripped.startswith(">"):
            flush_para()
            quote.append(stripped.lstrip(">").strip())
            continue
        flush_quote()
        para.append(stripped)

    flush_para()
    flush_quote()
    return "\n".join(html)


def parse_day_file(path: Path) -> dict:
    """Split a day markdown file into sections (-> tasks with one TEXT sub-task)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    day_title = None
    for line in lines:
        if line.startswith("## ") and day_title is None:
            day_title = line[3:].strip()

    sections: list[dict] = []
    current_title = None
    current_lines: list[str] = []

    for line in lines:
        m = SECTION_RE.match(line)
        if m:
            if current_title is not None:
                sections.append({"title": current_title, "lines": current_lines})
            current_title = TIBETAN_NUMERAL_PREFIX.sub("", m.group(1)).strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections.append({"title": current_title, "lines": current_lines})

    if not sections:
        sys.exit(f"No '### ' sections found in {path} — nothing to upload.")

    tasks = [
        {"title": s["title"], "html": md_block_to_html(s["lines"])} for s in sections
    ]
    return {"day_title": day_title or path.stem, "tasks": tasks}


# --------------------------------------------------------------------------
# API client
# --------------------------------------------------------------------------


class CmsClient:
    def __init__(self, base_url: str):
        import requests  # deferred so --dry-run works without requests

        self.requests = requests
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _call(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        resp = self.session.request(method, url, timeout=60, **kwargs)
        if resp.status_code >= 400:
            sys.exit(
                f"API error {resp.status_code} on {method} {path}:\n{resp.text[:2000]}"
            )
        return resp.json() if resp.text else {}

    def login(self, email: str, password: str):
        data = self._call(
            "POST", "/cms/auth/login", json={"email": email, "password": password}
        )
        token = data["auth"]["access_token"]
        self.session.headers["Authorization"] = f"Bearer {token}"
        print(f"Logged in as: {data['user']['name']}")

    def create_plan(self, **fields) -> str:
        data = self._call("POST", "/cms/plans", json=fields)
        plan_id = data["id"]
        print(f"Created plan: {fields['title']}  (PLAN_ID={plan_id})")
        return plan_id

    def add_day(self, plan_id: str) -> dict:
        data = self._call(
            "POST",
            f"/cms/plans/{plan_id}/days",
            json={"number_of_days": 1, "source_day_id": None},
        )
        day = data[0] if isinstance(data, list) else data
        print(f"Added day {day.get('day_number')}  (DAY_ID={day['id']})")
        return day

    def create_task(self, plan_id: str, day_id: str, title: str) -> str:
        data = self._call(
            "POST",
            "/cms/tasks",
            json={
                "plan_id": plan_id,
                "day_id": day_id,
                "title": title,
                "description": "",
                "estimated_time": 5,
            },
        )
        return data["id"]

    def create_text_subtask(self, task_id: str, html: str) -> str:
        data = self._call(
            "POST",
            "/cms/sub-tasks",
            json={
                "task_id": task_id,
                "sub_tasks": [
                    {
                        "content_type": "TEXT",
                        "content": html,
                        "duration": None,
                        "source_text_id": None,
                        "pecha_segment_id": None,
                        "segment_ids": None,
                        "start_ms": None,
                        "end_ms": None,
                    }
                ],
            },
        )
        return data["sub_tasks"][0]["id"]

    def set_status(self, plan_id: str, status: str):
        self._call("PATCH", f"/cms/plans/{plan_id}/status", json={"status": status})
        print(f"Plan status set to {status}")

    def get_plan(self, plan_id: str) -> dict:
        return self._call("GET", f"/cms/plans/{plan_id}")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("day_file", type=Path, help="Markdown day file to upload")
    ap.add_argument("--title", help="Plan title (required when creating a new plan)")
    ap.add_argument("--description", help="Plan description")
    ap.add_argument("--difficulty", default="BEGINNER",
                    choices=["BEGINNER", "INTERMEDIATE", "ADVANCED"])
    ap.add_argument("--language", default="BO",
                    choices=["EN", "BO", "ZH", "HI", "NE", "MN"])
    ap.add_argument("--total-days", type=int, default=1)
    ap.add_argument("--display-order", type=int, default=None)
    ap.add_argument("--plan-id", help="Add the day to this existing plan "
                                      "instead of creating a new one")
    ap.add_argument("--publish", action="store_true",
                    help="Set plan status to PUBLISHED after upload")
    ap.add_argument("--dry-run", action="store_true",
                    help="Parse and print structure; no API calls")
    ap.add_argument("--env", type=Path,
                    default=Path(__file__).with_name("plan_uploader.env"),
                    help="Path to key=value credentials file")
    args = ap.parse_args()

    if not args.day_file.exists():
        sys.exit(f"File not found: {args.day_file}")

    parsed = parse_day_file(args.day_file)

    print(f"\nDay file : {args.day_file.name}")
    print(f"Day title: {parsed['day_title']}")
    print(f"Tasks    : {len(parsed['tasks'])}")
    for i, t in enumerate(parsed["tasks"], 1):
        print(f"  {i}. {t['title']}  ({len(t['html'])} chars HTML)")

    if args.dry_run:
        print("\n--- HTML preview ---")
        for t in parsed["tasks"]:
            print(f"\n===== {t['title']} =====")
            print(t["html"])
        print("\nDry run complete. No API calls made.")
        return

    cfg = load_config(args.env)
    client = CmsClient(BASE_URL)
    client.login(cfg["WEBUDDHIST_EMAIL"], cfg["WEBUDDHIST_PASSWORD"])

    if args.plan_id:
        plan_id = args.plan_id
        print(f"Using existing plan PLAN_ID={plan_id}")
    else:
        if not args.title:
            sys.exit("--title is required when creating a new plan "
                     "(or pass --plan-id to use an existing one).")
        plan_id = client.create_plan(
            title=args.title,
            description=args.description or args.title,
            difficulty_level=args.difficulty,
            total_days=args.total_days,
            language=args.language,
            group_id=cfg["WEBUDDHIST_GROUP_ID"],
            series_id=cfg["WEBUDDHIST_SERIES_ID"],
            display_order=args.display_order,
            image_url=None,
            tag_ids=[],
            start_date=None,
        )

    day = client.add_day(plan_id)

    for i, t in enumerate(parsed["tasks"], 1):
        task_id = client.create_task(plan_id, day["id"], t["title"])
        sub_id = client.create_text_subtask(task_id, t["html"])
        print(f"  Task {i}/{len(parsed['tasks'])}: {t['title']}"
              f"  (TASK_ID={task_id}, SUB_TASK_ID={sub_id})")

    if args.publish:
        client.set_status(plan_id, "PUBLISHED")
    else:
        print("Plan left in DRAFT status (use --publish to go live).")

    # Verify
    plan = client.get_plan(plan_id)
    days = plan.get("days", [])
    print(f"\nVerification: plan '{plan.get('title')}' now has {len(days)} day(s).")
    for d in days:
        n_tasks = len(d.get("tasks", []))
        print(f"  Day {d.get('day_number')}: {n_tasks} task(s)")
    print(f"\nPLAN_ID={plan_id}")


if __name__ == "__main__":
    main()
