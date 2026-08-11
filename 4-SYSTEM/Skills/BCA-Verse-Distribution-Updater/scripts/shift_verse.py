#!/usr/bin/env python3
"""
shift_verse.py — move a verse boundary between two adjacent-in-sequence days
in the Dalai Lama track schedule (Tibetan-schedule-corrected.md), rippling
the "Verses" and "Studio Verse" columns through every day in between, and
rename the affected day files under the Dalai Lama plan folder to match.

Subcommands:
  audit   — structural health check of the schedule file (no changes)
  plan    — dry run: show exactly what would change (no changes)
  apply   — perform the edit: rewrite the schedule file and rename day files

Usage:
  python shift_verse.py audit --schedule "<path-to-schedule.md>"
  python shift_verse.py plan  --schedule "<path>" --verse 3.22 --to-day 50
  python shift_verse.py apply --schedule "<path>" --verse 3.22 --to-day 50 \
      --plan-root "<path-to-Dalai Lama plan folder>"

Model
-----
Each chapter's verses are partitioned into contiguous, non-overlapping,
gap-free day-buckets (Y.Day rows sharing the same chapter). A verse can only
move to a *different* day by pushing it across the boundary it currently
sits on:

  - If the verse is the LAST verse of its day, it may move FORWARD to any
    later day in the same chapter. Every day strictly between the source and
    target loses one verse from its front and gains one at its back (net
    size unchanged, whole range shifts down by one); the source day shrinks
    by one verse at its end; the target day grows by one verse at its front.

  - If the verse is the FIRST verse of its day, it may move BACKWARD to any
    earlier day in the same chapter, by the mirror-image rule.

  - A single-verse day's verse is both first and last, so it may move either
    direction.

A verse in the *middle* of a day cannot be moved this way without splitting
that day's range in two, which this script does not support — it stops and
reports the problem instead of guessing.

"Studio Verse" tracks the root text's global verse numbering. Within one
chapter, studio_verse - chapter_verse is a constant offset (verified by
`audit`), so once the Verses column is recomputed the Studio Verse column
follows by simply re-adding that offset. This script never touches Y.Day,
Ch.Day, or Date — only Verses and Studio Verse cells for the rows between
(and including) the source and target day, plus the day-file names for
those same rows.
"""

import argparse
import glob
import os
import re
import subprocess
import sys

DASH = "–"  # en dash, matches the schedule file's existing convention

ROW_RE = re.compile(r"^\s*\|.*\|\s*$")


def parse_row(line):
    """Split a markdown table row into its 5 cells, stripping ==highlight==
    markers and recording which cells were highlighted."""
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    inner = stripped.strip("|")
    cells = [c.strip() for c in inner.split("|")]
    if len(cells) != 5:
        return None
    values, highlighted = [], []
    for c in cells:
        h = False
        if c.startswith("==") and c.endswith("==") and len(c) >= 4:
            h = True
            c = c[2:-2]
        values.append(c)
        highlighted.append(h)
    return values, highlighted


def parse_verse_cell(cell):
    """Return (prefix, chapter, start, end) from a Verses cell.

    Handles: "3.20–23.22"-style ranges, "10.58"-style single verses,
    "Prologue, 1.1–1.3"-style prefixed rows, and tolerates the known
    "3.32-3-33" typo (hyphen used instead of a dot before the end verse).
    """
    tokens = list(re.finditer(r"(\d+)\.(\d+)", cell))
    if not tokens:
        raise ValueError(f"cannot find a chapter.verse token in {cell!r}")
    first = tokens[0]
    chapter = int(first.group(1))
    start = int(first.group(2))
    prefix = cell[: first.start()]

    if len(tokens) >= 2:
        second = tokens[1]
        if int(second.group(1)) != chapter:
            raise ValueError(f"range spans two chapters in {cell!r}")
        end = int(second.group(2))
        return prefix, chapter, start, end, True  # True = well-formed

    rest = cell[first.end():].strip()
    if not rest:
        return prefix, chapter, start, start, True  # genuine single verse

    # Something follows the first token but wasn't a second "C.V" — try to
    # recover it (typo tolerance) and flag as not well-formed.
    rest = rest.lstrip("–-").strip()
    m = re.match(r"(\d+)-(\d+)", rest)  # e.g. "3-33" meant as "3.33"
    if m and int(m.group(1)) == chapter:
        return prefix, chapter, start, int(m.group(2)), False
    m = re.match(r"(\d+)", rest)
    if m:
        return prefix, chapter, start, int(m.group(1)), False

    raise ValueError(f"cannot parse end of range in {cell!r}")


def parse_studio_cell(cell):
    nums = re.findall(r"\d+", cell)
    if not nums:
        raise ValueError(f"cannot find a number in Studio Verse cell {cell!r}")
    start = int(nums[0])
    end = int(nums[1]) if len(nums) > 1 else start
    return start, end


def format_verse_cell(prefix, chapter, start, end):
    body = f"{chapter}.{start}" if start == end else f"{chapter}.{start}{DASH}{chapter}.{end}"
    return prefix + body


def format_studio_cell(start, end):
    return str(start) if start == end else f"{start}{DASH}{end}"


def load_schedule(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    header_idx = next(
        (i for i, l in enumerate(lines) if l.strip().startswith("| Y.Day")), None
    )
    if header_idx is None:
        raise SystemExit(f"Could not find the '| Y.Day' header row in {path}")
    sep_idx = header_idx + 1

    sep_cells = [c.strip() for c in lines[sep_idx].strip().strip("|").split("|")]
    col_widths = [len(c) for c in sep_cells]
    if len(col_widths) != 5:
        raise SystemExit("Header separator row does not have 5 columns as expected")

    rows = []
    for i in range(sep_idx + 1, len(lines)):
        line = lines[i]
        if not line.strip().startswith("|"):
            continue
        parsed = parse_row(line)
        if parsed is None:
            continue
        values, hl = parsed
        try:
            yday = int(values[0])
            chday = int(values[1])
            vprefix, chapter, vstart, vend, verse_ok = parse_verse_cell(values[2])
            sstart, send = parse_studio_cell(values[3])
        except ValueError as e:
            print(f"WARNING: skipping unparseable row at line {i+1}: {e}", file=sys.stderr)
            continue
        rows.append(
            {
                "line_idx": i,
                "yday": yday,
                "chday": chday,
                "chapter": chapter,
                "vprefix": vprefix,
                "vstart": vstart,
                "vend": vend,
                "verse_well_formed": verse_ok,
                "sstart": sstart,
                "send": send,
                "date": values[4],
                "highlighted": hl,
            }
        )
    return lines, rows, col_widths


def render_row(row, col_widths):
    cells = [
        str(row["yday"]),
        str(row["chday"]),
        format_verse_cell(row["vprefix"], row["chapter"], row["vstart"], row["vend"]),
        format_studio_cell(row["sstart"], row["send"]),
        row["date"],
    ]
    out = []
    for c, w, h in zip(cells, col_widths, row["highlighted"]):
        content = f"=={c}==" if h else c
        out.append(" " + content.ljust(w) + " ")
    return "|" + "|".join(out) + "|\n"


def find_source_row(rows, chapter, verse):
    for r in rows:
        if r["chapter"] == chapter and r["vstart"] <= verse <= r["vend"]:
            return r
    return None


def find_row_by_day(rows, yday):
    for r in rows:
        if r["yday"] == yday:
            return r
    return None


def chapter_offset(rows, chapter):
    offsets = {r["sstart"] - r["vstart"] for r in rows if r["chapter"] == chapter}
    return offsets


def compute_shift(rows, chapter, verse, to_day):
    src = find_source_row(rows, chapter, verse)
    if src is None:
        raise SystemExit(f"Verse {chapter}.{verse} was not found in any day of the schedule.")

    dst = find_row_by_day(rows, to_day)
    if dst is None:
        raise SystemExit(f"Day {to_day} was not found in the schedule (Y.Day column).")

    if dst["yday"] == src["yday"]:
        print(f"Verse {chapter}.{verse} is already on day {to_day}. Nothing to do.")
        return None

    if dst["chapter"] != src["chapter"]:
        raise SystemExit(
            f"Verse {chapter}.{verse} is in chapter {src['chapter']} (day {src['yday']}), "
            f"but day {to_day} is in chapter {dst['chapter']}. This script only supports "
            f"shifts within a single chapter — a cross-chapter move also changes each "
            f"chapter's total verse count, the chapter folder's day range (e.g. "
            f"'Chapter-{src['chapter']} D..-D..'), and the studio-verse offset, and needs "
            f"a human to adjudicate. Stopping without making any changes."
        )

    is_last = verse == src["vend"]
    is_first = verse == src["vstart"]

    if to_day > src["yday"]:
        if not is_last:
            raise SystemExit(
                f"Verse {chapter}.{verse} is not the LAST verse of day {src['yday']} "
                f"(that day covers {chapter}.{src['vstart']}–{chapter}.{src['vend']}). "
                f"Only the first or last verse of a day can move to another day without "
                f"splitting that day's range. Stopping without making any changes."
            )
        direction = "forward"
    elif to_day < src["yday"]:
        if not is_first:
            raise SystemExit(
                f"Verse {chapter}.{verse} is not the FIRST verse of day {src['yday']} "
                f"(that day covers {chapter}.{src['vstart']}–{chapter}.{src['vend']}). "
                f"Only the first or last verse of a day can move to another day without "
                f"splitting that day's range. Stopping without making any changes."
            )
        direction = "backward"
    else:
        return None  # unreachable, guarded above

    offsets = chapter_offset(rows, chapter)
    if len(offsets) != 1:
        raise SystemExit(
            f"Chapter {chapter}'s studio-verse offset is not constant across its rows "
            f"({sorted(offsets)}). Refusing to guess the new Studio Verse numbers — "
            f"fix the schedule's Studio Verse column for chapter {chapter} first, or "
            f"compute the shift by hand."
        )
    offset = next(iter(offsets))

    lo, hi = (src["yday"], dst["yday"]) if direction == "forward" else (dst["yday"], src["yday"])
    day_list = sorted([r for r in rows if lo <= r["yday"] <= hi], key=lambda r: r["yday"])

    changes = []
    if direction == "forward":
        for i, r in enumerate(day_list):
            new_vstart, new_vend = r["vstart"], r["vend"]
            if i == 0:  # source day
                new_vend -= 1
            elif i == len(day_list) - 1:  # target day
                new_vstart -= 1
            else:
                new_vstart -= 1
                new_vend -= 1
            changes.append((r, new_vstart, new_vend))
    else:
        for i, r in enumerate(day_list):
            new_vstart, new_vend = r["vstart"], r["vend"]
            if i == 0:  # target day (smallest yday)
                new_vend += 1
            elif i == len(day_list) - 1:  # source day
                new_vstart += 1
            else:
                new_vstart += 1
                new_vend += 1
            changes.append((r, new_vstart, new_vend))

    for r, new_vstart, new_vend in changes:
        if new_vend < new_vstart:
            raise SystemExit(
                f"Day {r['yday']} (currently {chapter}.{r['vstart']}–{chapter}.{r['vend']}) "
                f"would become empty under this shift. This script does not support "
                f"collapsing a day to zero verses. Stopping without making any changes."
            )

    result = []
    for r, new_vstart, new_vend in changes:
        result.append(
            {
                "row": r,
                "old_vstart": r["vstart"],
                "old_vend": r["vend"],
                "new_vstart": new_vstart,
                "new_vend": new_vend,
                "new_sstart": new_vstart + offset,
                "new_send": new_vend + offset,
            }
        )
    return {
        "chapter": chapter,
        "verse": verse,
        "direction": direction,
        "source_day": src["yday"],
        "target_day": dst["yday"],
        "changes": result,
    }


def print_plan(plan):
    print(
        f"Move verse {plan['chapter']}.{plan['verse']} from day {plan['source_day']} "
        f"to day {plan['target_day']} ({plan['direction']} shift, "
        f"{len(plan['changes'])} day(s) affected):\n"
    )
    for c in plan["changes"]:
        r = c["row"]
        old_v = format_verse_cell(r["vprefix"], plan["chapter"], c["old_vstart"], c["old_vend"])
        new_v = format_verse_cell(r["vprefix"], plan["chapter"], c["new_vstart"], c["new_vend"])
        old_s = format_studio_cell(r["sstart"], r["send"])
        new_s = format_studio_cell(c["new_sstart"], c["new_send"])
        print(f"  Day {r['yday']:>3}  Verses: {old_v!r:>24} -> {new_v!r:<24}  "
              f"Studio: {old_s!r:>10} -> {new_s!r}")

    print("\nDay files to rename:")
    for c in plan["changes"]:
        r = c["row"]
        old_name = f"Day-{r['yday']}-Ch{plan['chapter']}-V{c['old_vstart']}"
        if c["old_vend"] != c["old_vstart"]:
            old_name += f"-{c['old_vend']}"
        old_name += ".md"
        new_name = f"Day-{r['yday']}-Ch{plan['chapter']}-V{c['new_vstart']}"
        if c["new_vend"] != c["new_vstart"]:
            new_name += f"-{c['new_vend']}"
        new_name += ".md"
        print(f"  {old_name}  ->  {new_name}")


def apply_schedule(schedule_path, lines, col_widths, plan):
    for c in plan["changes"]:
        r = c["row"]
        r["vstart"], r["vend"] = c["new_vstart"], c["new_vend"]
        r["sstart"], r["send"] = c["new_sstart"], c["new_send"]
        lines[r["line_idx"]] = render_row(r, col_widths)
    with open(schedule_path, "w", encoding="utf-8", newline="") as f:
        f.writelines(lines)
    print(f"\nSchedule file updated: {schedule_path}")


def find_chapter_folder(plan_root, chapter):
    matches = glob.glob(os.path.join(plan_root, f"Chapter-{chapter} D*"))
    matches = [m for m in matches if os.path.isdir(m)]
    if len(matches) != 1:
        raise SystemExit(
            f"Expected exactly one 'Chapter-{chapter} D*' folder under {plan_root}, "
            f"found {len(matches)}: {matches}"
        )
    return matches[0]


def git_root_for(path):
    try:
        out = subprocess.run(
            ["git", "-C", os.path.dirname(path), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except Exception:
        return None


def rename_day_files(plan_root, plan):
    chapter_folder = find_chapter_folder(plan_root, plan["chapter"])
    repo_root = git_root_for(chapter_folder)

    for c in plan["changes"]:
        r = c["row"]
        candidates = glob.glob(os.path.join(chapter_folder, f"Day-{r['yday']}-Ch{plan['chapter']}-V*.md"))
        if len(candidates) != 1:
            print(
                f"  WARNING: expected exactly one existing file for day {r['yday']} in "
                f"{chapter_folder}, found {len(candidates)}: {candidates}. Skipping rename "
                f"for this day — rename it by hand.",
                file=sys.stderr,
            )
            continue
        old_path = candidates[0]
        new_name = f"Day-{r['yday']}-Ch{plan['chapter']}-V{c['new_vstart']}"
        if c["new_vend"] != c["new_vstart"]:
            new_name += f"-{c['new_vend']}"
        new_name += ".md"
        new_path = os.path.join(chapter_folder, new_name)

        if old_path == new_path:
            continue

        moved = False
        if repo_root:
            rel_old = os.path.relpath(old_path, repo_root)
            rel_new = os.path.relpath(new_path, repo_root)
            res = subprocess.run(
                ["git", "-C", repo_root, "mv", rel_old, rel_new],
                capture_output=True, text=True,
            )
            if res.returncode == 0:
                moved = True
            else:
                print(f"  git mv failed for {rel_old} -> {rel_new}: {res.stderr.strip()}", file=sys.stderr)
        if not moved:
            os.rename(old_path, new_path)
        print(f"  Renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")


def cmd_audit(args):
    _, rows, _ = load_schedule(args.schedule)
    chapters = sorted(set(r["chapter"] for r in rows))
    problems = 0
    for ch in chapters:
        crows = sorted([r for r in rows if r["chapter"] == ch], key=lambda r: r["yday"])
        offsets = {r["sstart"] - r["vstart"] for r in crows}
        expected_next = crows[0]["vstart"]
        gap_or_overlap = []
        for r in crows:
            if r["vstart"] != expected_next:
                gap_or_overlap.append(r["yday"])
            expected_next = r["vend"] + 1
        malformed = [r["yday"] for r in crows if not r["verse_well_formed"]]
        status = "OK"
        if len(offsets) != 1 or gap_or_overlap or malformed:
            status = "ISSUES"
            problems += 1
        print(
            f"Chapter {ch:>2}: days {crows[0]['yday']}-{crows[-1]['yday']}, "
            f"verses {crows[0]['vstart']}-{crows[-1]['vend']}, "
            f"studio-offset={sorted(offsets)}, status={status}"
        )
        if gap_or_overlap:
            print(f"    gap/overlap at day(s): {gap_or_overlap}")
        if malformed:
            print(f"    non-canonical Verses cell formatting at day(s): {malformed} "
                  f"(parsed via typo-tolerant fallback — verify by hand)")
    print(f"\n{len(chapters)} chapters checked, {problems} with issues.")


def cmd_plan_or_apply(args, do_apply):
    m = re.match(r"^\s*(\d+)[.\-](\d+)\s*$", args.verse)
    if not m:
        raise SystemExit(f"--verse must look like '3.22' or '3-22', got {args.verse!r}")
    chapter, verse = int(m.group(1)), int(m.group(2))

    lines, rows, col_widths = load_schedule(args.schedule)
    plan = compute_shift(rows, chapter, verse, args.to_day)
    if plan is None:
        return
    print_plan(plan)

    if do_apply:
        if not args.plan_root:
            raise SystemExit("--plan-root is required with 'apply' (needed to rename day files).")
        print()
        apply_schedule(args.schedule, lines, col_widths, plan)
        print("Renaming day files:")
        rename_day_files(args.plan_root, plan)
        print("\nDone. Day file *content* (verse text, headings) was NOT touched — "
              "only the schedule table and the file names. Review the renamed files "
              "if their content needs to follow the verses to their new day.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("audit", help="structural health check of the schedule file")
    pa.add_argument("--schedule", required=True)

    pp = sub.add_parser("plan", help="dry run: show what would change")
    pp.add_argument("--schedule", required=True)
    pp.add_argument("--verse", required=True, help="e.g. 3.22 or 3-22")
    pp.add_argument("--to-day", required=True, type=int)

    pap = sub.add_parser("apply", help="perform the edit")
    pap.add_argument("--schedule", required=True)
    pap.add_argument("--verse", required=True, help="e.g. 3.22 or 3-22")
    pap.add_argument("--to-day", required=True, type=int)
    pap.add_argument("--plan-root", required=True, help="path to the 'Dalai Lama' plan folder")

    args = p.parse_args()
    if args.cmd == "audit":
        cmd_audit(args)
    elif args.cmd == "plan":
        cmd_plan_or_apply(args, do_apply=False)
    elif args.cmd == "apply":
        cmd_plan_or_apply(args, do_apply=True)


if __name__ == "__main__":
    main()
