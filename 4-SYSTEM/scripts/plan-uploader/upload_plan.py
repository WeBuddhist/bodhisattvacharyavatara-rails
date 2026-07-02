#!/usr/bin/env python3
"""Idempotently sync a Bodhisattva Challenge day file to the WeBuddhist Studio CMS.

Implements the workflow documented in
`3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/Plan Uploader.md`:

    Login -> resolve plan (existing --plan-id or create new)
          -> ensure day N exists -> diff desired vs remote tasks
          -> create / update / delete tasks to converge -> reorder
          -> verify remote state matches the file

**Idempotent:** running the same command twice makes no changes the second
time. Existing tasks are updated in place (title via PUT /cms/tasks/{id},
content via PUT /cms/sub-tasks); tasks no longer in the file are deleted;
missing tasks are created. Task order is enforced with
PUT /cms/tasks/{day_id}/order.

The plan is left in DRAFT status unless --publish is passed.

Usage
-----
# Dry run — parse only, no network calls:
python upload_plan.py "path/to/Day-1-Ch1-V1-3.md" --dry-run

# Read-only diff against the server (no writes):
python upload_plan.py "path/to/Day-1-Ch1-V1-3.md" --plan-id <PLAN_ID> --check

# Create a new plan in the series and sync Day 1:
python upload_plan.py "path/to/Day-1-Ch1-V1-3.md" \
    --title "སྤྱོད་འཇུག་ཉིན་རེའི་ཉམས་ལེན། ལེའུ་དང་པོ།" \
    --description "ཉིན་ ༡ - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང་།" \
    --total-days 14

# Sync a day into an existing plan (day number taken from the filename):
python upload_plan.py "path/to/Day-2-Ch1-V4-5.md" --plan-id <PLAN_ID>

Credentials & IDs
-----------------
Read from environment variables, or from a key=value file passed with
--env (default: `plan_uploader.env` next to this script):

    WEBUDDHIST_EMAIL=author@example.com
    WEBUDDHIST_PASSWORD=...
    WEBUDDHIST_SERIES_ID=<uuid>
    WEBUDDHIST_GROUP_ID=<uuid>
    WEBUDDHIST_BASE_URL=https://api.webuddhist.com/api/v1   # optional

Requires: pip install requests
"""

import argparse
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

OPTIONAL_KEYS = ["WEBUDDHIST_BASE_URL", "WEBUDDHIST_ACCESS_TOKEN"]


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
    for key in REQUIRED_KEYS + OPTIONAL_KEYS:
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
DAY_NUMBER_RE = re.compile(r"day[-_ ]?(\d+)", re.IGNORECASE)


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

    m = DAY_NUMBER_RE.search(path.stem)
    day_number = int(m.group(1)) if m else None

    return {
        "day_title": day_title or path.stem,
        "day_number": day_number,
        "tasks": tasks,
    }


# --------------------------------------------------------------------------
# API client
# --------------------------------------------------------------------------


class CmsClient:
    def __init__(self, base_url: str):
        import requests  # deferred so --dry-run works without requests

        self.requests = requests
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _call(self, method: str, path: str, tolerate=(), **kwargs):
        url = f"{self.base_url}{path}"
        resp = self.session.request(method, url, timeout=60, **kwargs)
        if resp.status_code >= 400:
            if resp.status_code in tolerate:
                print(f"  (tolerated {resp.status_code} on {method} {path})")
                return None
            sys.exit(
                f"API error {resp.status_code} on {method} {path}:\n{resp.text[:2000]}"
            )
        return resp.json() if resp.text else {}

    def use_token(self, token: str):
        self.session.headers["Authorization"] = f"Bearer {token}"
        print("Using provided access token (login skipped).")

    def login(self, email: str, password: str):
        data = self._call(
            "POST", "/cms/auth/login", json={"email": email, "password": password}
        )
        token = data["auth"]["access_token"]
        self.session.headers["Authorization"] = f"Bearer {token}"
        print(f"Logged in as: {data['user']['name']}")

    # -- plan ---------------------------------------------------------------

    def create_plan(self, **fields) -> str:
        data = self._call("POST", "/cms/plans", json=fields)
        plan_id = data["id"]
        print(f"Created plan: {fields['title']}  (PLAN_ID={plan_id})")
        return plan_id

    def get_plan(self, plan_id: str) -> dict:
        return self._call("GET", f"/cms/plans/{plan_id}")

    def list_series_plans(self, series_id: str, language: str) -> list:
        data = self._call("GET", f"/cms/series/{series_id}?language={language}")
        return data.get("plans") or []

    def set_status(self, plan_id: str, status: str):
        self._call("PATCH", f"/cms/plans/{plan_id}/status", json={"status": status})
        print(f"Plan status set to {status}")

    # -- days ---------------------------------------------------------------

    def add_days(self, plan_id: str, number_of_days: int = 1) -> list:
        data = self._call(
            "POST",
            f"/cms/plans/{plan_id}/days",
            json={"number_of_days": number_of_days, "source_day_id": None},
        )
        return data if isinstance(data, list) else [data]

    # -- tasks --------------------------------------------------------------

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

    def update_task_title(self, task_id: str, title: str):
        self._call("PUT", f"/cms/tasks/{task_id}", json={"title": title})

    def delete_task(self, task_id: str):
        self._call("DELETE", f"/cms/tasks/{task_id}")

    def reorder_tasks(self, day_id: str, task_ids: list[str]):
        self._call(
            "PUT",
            f"/cms/tasks/{day_id}/order",
            json={
                "tasks": [
                    {"id": tid, "display_order": i}
                    for i, tid in enumerate(task_ids, 1)
                ]
            },
        )

    # -- sub-tasks ----------------------------------------------------------

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

    def update_text_subtask(self, task_id: str, sub_task_id: str, html: str):
        self._call(
            "PUT",
            "/cms/sub-tasks",
            json={
                "task_id": task_id,
                "sub_tasks": [
                    {
                        "id": sub_task_id,
                        "content_type": "TEXT",
                        "content": html,
                        "display_order": 1,
                        "duration": None,
                        "image_url": None,
                        "audio_url": None,
                        "source_text_id": None,
                        "pecha_segment_id": None,
                        "segment_ids": None,
                        "start_ms": None,
                        "end_ms": None,
                    }
                ],
            },
        )


# --------------------------------------------------------------------------
# Idempotent sync
# --------------------------------------------------------------------------


def _norm(text) -> str:
    """Whitespace-insensitive comparison form for HTML content."""
    import unicodedata
    return unicodedata.normalize(
        "NFC", re.sub(r"\s+", " ", (text or ""))
    ).strip()


def _titles_equal(server_title: str, want_title: str) -> bool:
    """Compare titles ignoring Unicode form, whitespace, and a leading
    Tibetan-numeral prefix (e.g. '༡། ') that older uploads may carry."""
    a, b = _norm(server_title), _norm(want_title)
    if a == b:
        return True
    return TIBETAN_NUMERAL_PREFIX.sub("", a) == TIBETAN_NUMERAL_PREFIX.sub("", b)


def _sorted_tasks(day: dict) -> list:
    return sorted(day.get("tasks") or [], key=lambda t: t.get("display_order") or 0)


def _first_text_subtask(task: dict):
    # The CMS uses both spellings across endpoints ("sub_tasks" in POST/PUT
    # bodies, "subtasks" in GET /cms/plans responses) — accept either.
    raw = task.get("sub_tasks") or task.get("subtasks") or []
    subs = sorted(raw, key=lambda s: s.get("display_order") or 0)
    for s in subs:
        if (s.get("content_type") or "TEXT") == "TEXT":
            return s, len(subs)
    return None, len(subs)


def ensure_day(client, plan_id: str, day_number: int, actions: list, apply: bool):
    """Return the day dict for day_number, appending days if needed."""
    plan = client.get_plan(plan_id)
    days = plan.get("days") or []
    by_number = {d.get("day_number"): d for d in days}
    if day_number in by_number:
        return by_number[day_number]
    max_day = max((d.get("day_number") or 0 for d in days), default=0)
    if day_number <= max_day:
        sys.exit(
            f"Day {day_number} not found in plan but higher-numbered days exist — "
            "day numbering on the server is inconsistent; fix manually."
        )
    n_missing = day_number - max_day
    actions.append(f"add {n_missing} day(s) (server has {max_day}, need {day_number})")
    if not apply:
        return None
    client.add_days(plan_id, n_missing)
    plan = client.get_plan(plan_id)
    for d in plan.get("days") or []:
        if d.get("day_number") == day_number:
            return d
    sys.exit(f"Added days but day {day_number} still not found in plan — aborting.")


def sync_day(client, plan_id: str, day_number: int, desired: list[dict],
             apply: bool = True, update_only: bool = False) -> list[str]:
    """Converge the remote day to the desired tasks. Returns action log.

    desired: [{"title": str, "html": str}, ...] in file order.
    apply=False → read-only: report what would change, write nothing.
    update_only=True → never delete or recreate tasks; only update
    titles/content in place and create missing tasks.
    """
    actions: list[str] = []
    day = ensure_day(client, plan_id, day_number, actions, apply)
    if day is None:  # check mode and day missing: every task is a create
        for t in desired:
            actions.append(f"create task '{t['title']}' + TEXT sub-task")
        return actions

    day_id = day["id"]
    existing = _sorted_tasks(day)
    final_ids: list[str] = []
    order_dirty = False

    for i, want in enumerate(desired):
        if i < len(existing):
            task = existing[i]
            task_id = task["id"]
            sub, n_subs = _first_text_subtask(task)
            # A task whose sub-task layout we can't converge in place
            # (no TEXT sub-task, or extra sub-tasks) is recreated.
            if sub is None or n_subs != 1:
                if update_only:
                    if sub is None:
                        actions.append(
                            f"SKIP task {i + 1} '{want['title']}': no TEXT "
                            "sub-task to update (--update-only, not recreating)"
                        )
                        final_ids.append(task_id)
                        continue
                    # extra sub-tasks: update the first TEXT one, leave the rest
                else:
                    actions.append(
                        f"recreate task '{want['title']}' "
                        f"(position {i + 1} has {n_subs} sub-task(s), no single TEXT)"
                    )
                    if apply:
                        client.delete_task(task_id)
                        task_id = client.create_task(plan_id, day_id, want["title"])
                        client.create_text_subtask(task_id, want["html"])
                    order_dirty = True
                    final_ids.append(task_id)
                    continue
            if not _titles_equal(task.get("title") or "", want["title"]):
                actions.append(
                    f"retitle task {i + 1}: '{task.get('title')}' -> '{want['title']}'"
                )
                if apply:
                    client.update_task_title(task_id, want["title"])
            if _norm(sub.get("content")) != _norm(want["html"]):
                actions.append(f"update content of task {i + 1} '{want['title']}'")
                if apply:
                    client.update_text_subtask(task_id, sub["id"], want["html"])
            final_ids.append(task_id)
        else:
            actions.append(f"create task '{want['title']}' + TEXT sub-task")
            if apply:
                task_id = client.create_task(plan_id, day_id, want["title"])
                client.create_text_subtask(task_id, want["html"])
                final_ids.append(task_id)
            order_dirty = True

    for task in existing[len(desired):]:
        if update_only:
            actions.append(
                f"KEEP extra task '{task.get('title')}' (--update-only)"
            )
            continue
        actions.append(f"delete extra task '{task.get('title')}'")
        if apply:
            client.delete_task(task["id"])
        order_dirty = True

    if order_dirty and apply and len(final_ids) > 1:
        actions.append("reorder tasks to file order")
        client.reorder_tasks(day_id, final_ids)

    return actions


def verify_day(client, plan_id: str, day_number: int, desired: list[dict]) -> bool:
    """Re-fetch the plan and confirm the day matches the file. Prints a report."""
    plan = client.get_plan(plan_id)
    day = next(
        (d for d in plan.get("days") or [] if d.get("day_number") == day_number), None
    )
    print(f"\nVerification — plan '{plan.get('title')}', day {day_number}:")
    if day is None:
        print("  ✗ day not found on server")
        return False
    existing = _sorted_tasks(day)
    ok = True
    if len(existing) != len(desired):
        print(f"  ✗ task count: server {len(existing)}, file {len(desired)}")
        ok = False
    for i, want in enumerate(desired):
        if i >= len(existing):
            print(f"  ✗ {i + 1}. '{want['title']}' missing on server")
            ok = False
            continue
        task = existing[i]
        sub, _ = _first_text_subtask(task)
        t_ok = _titles_equal(task.get("title") or "", want["title"])
        c_ok = sub is not None and _norm(sub.get("content")) == _norm(want["html"])
        mark = "✓" if (t_ok and c_ok) else "✗"
        detail = "" if (t_ok and c_ok) else (
            " [title mismatch]" if not t_ok else " [content mismatch]"
        )
        print(f"  {mark} {i + 1}. {want['title']}{detail}")
        ok = ok and t_ok and c_ok
    return ok


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("day_file", type=Path, help="Markdown day file to sync")
    ap.add_argument("--title", help="Plan title (required when creating a new plan)")
    ap.add_argument("--description", help="Plan description")
    ap.add_argument("--difficulty", default="BEGINNER",
                    choices=["BEGINNER", "INTERMEDIATE", "ADVANCED"])
    ap.add_argument("--language", default="BO",
                    choices=["EN", "BO", "ZH", "HI", "NE", "MN"])
    ap.add_argument("--total-days", type=int, default=1)
    ap.add_argument("--display-order", type=int, default=None)
    ap.add_argument("--plan-id", help="Sync into this existing plan "
                                      "instead of creating a new one")
    ap.add_argument("--day-number", type=int, default=None,
                    help="Day number to sync (default: parsed from filename "
                         "'Day-N-...')")
    ap.add_argument("--check", action="store_true",
                    help="Read-only: diff against the server, write nothing")
    ap.add_argument("--update-only", action="store_true",
                    help="Never delete or recreate tasks — only update "
                         "titles/sub-task content in place (and create "
                         "missing tasks)")
    ap.add_argument("--publish", action="store_true",
                    help="Set plan status to PUBLISHED after sync")
    ap.add_argument("--dry-run", action="store_true",
                    help="Parse and print structure; no API calls")
    ap.add_argument("--base-url", default=None,
                    help="Override API base URL (or set WEBUDDHIST_BASE_URL "
                         f"in the env file). Default: {BASE_URL}")
    ap.add_argument("--env", type=Path,
                    default=Path(__file__).with_name("plan_uploader.env"),
                    help="Path to key=value credentials file")
    args = ap.parse_args()

    if not args.day_file.exists():
        sys.exit(f"File not found: {args.day_file}")

    parsed = parse_day_file(args.day_file)
    day_number = args.day_number or parsed["day_number"]

    print(f"\nDay file  : {args.day_file.name}")
    print(f"Day title : {parsed['day_title']}")
    print(f"Day number: {day_number if day_number else '?? (pass --day-number)'}")
    print(f"Tasks     : {len(parsed['tasks'])}")
    for i, t in enumerate(parsed["tasks"], 1):
        print(f"  {i}. {t['title']}  ({len(t['html'])} chars HTML)")

    if args.dry_run:
        print("\n--- HTML preview ---")
        for t in parsed["tasks"]:
            print(f"\n===== {t['title']} =====")
            print(t["html"])
        print("\nDry run complete. No API calls made.")
        return

    if day_number is None:
        sys.exit("Could not parse a day number from the filename — "
                 "pass --day-number explicitly.")

    cfg = load_config(args.env)
    base_url = args.base_url or cfg.get("WEBUDDHIST_BASE_URL") or BASE_URL
    print(f"API base  : {base_url}")
    client = CmsClient(base_url)
    if cfg.get("WEBUDDHIST_ACCESS_TOKEN"):
        client.use_token(cfg["WEBUDDHIST_ACCESS_TOKEN"])
    else:
        client.login(cfg["WEBUDDHIST_EMAIL"], cfg["WEBUDDHIST_PASSWORD"])

    if args.plan_id:
        plan_id = args.plan_id
        print(f"Using existing plan PLAN_ID={plan_id}")
    else:
        # No --plan-id: look for an existing plan in the series first.
        found = client.list_series_plans(cfg["WEBUDDHIST_SERIES_ID"],
                                         args.language)
        if len(found) == 1:
            plan_id = found[0]["id"]
            print(f"Found existing plan in series: '{found[0].get('title')}' "
                  f"(PLAN_ID={plan_id})")
        elif len(found) > 1:
            print(f"Series has {len(found)} {args.language} plans — "
                  "pass --plan-id to pick one:")
            for p in found:
                print(f"  {p.get('id')}  '{p.get('title')}'  "
                      f"status={p.get('status')}")
            sys.exit(1)
        elif args.check:
            sys.exit("--check: no plan found in series and nothing to create.")
        elif not args.title:
            sys.exit("No plan found in series. --title is required to create "
                     "a new one (or pass --plan-id).")
        else:
            plan_id = None
    if not args.plan_id and plan_id is None:
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

    actions = sync_day(client, plan_id, day_number, parsed["tasks"],
                       apply=not args.check, update_only=args.update_only)

    label = "Would apply" if args.check else "Applied"
    if actions:
        print(f"\n{label} {len(actions)} change(s):")
        for a in actions:
            print(f"  - {a}")
    else:
        print("\nNo changes — server already matches the file.")

    if args.check:
        print("\nCheck complete. Nothing written.")
        return

    if args.publish:
        client.set_status(plan_id, "PUBLISHED")
    else:
        print("Plan left in DRAFT status (use --publish to go live).")

    ok = verify_day(client, plan_id, day_number, parsed["tasks"])
    print(f"\nPLAN_ID={plan_id}")
    if not ok:
        sys.exit("Verification FAILED — server does not match the file.")
    print("Verification passed — server matches the file.")


if __name__ == "__main__":
    main()
