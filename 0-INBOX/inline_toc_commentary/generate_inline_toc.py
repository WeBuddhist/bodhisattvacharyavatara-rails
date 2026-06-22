from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
SEGMENTATION_DIR = ROOT / "segmentation"
OUT_DIR = ROOT / "inline_toc_commentary"


def pick_input_file() -> Path:
    candidates = sorted(SEGMENTATION_DIR.glob("bo-*.segmented.md"))
    for candidate in candidates:
        try:
            lines = candidate.read_text(encoding="utf-8-sig").splitlines()
        except UnicodeDecodeError:
            continue
        if len(lines) == 6820:
            return candidate
    raise FileNotFoundError("Could not find the 6820-line target segmented commentary.")


COUNT_WORDS = {
    "གཉིས": 2,
    "གསུམ": 3,
    "བཞི": 4,
    "ལྔ": 5,
    "དྲུག": 6,
    "བདུན": 7,
    "བརྒྱད": 8,
    "དགུ": 9,
    "བཅུ": 10,
}

ORD_WORDS = [
    ("དང་པོ", 1),
    ("གཉིས་པ", 2),
    ("གསུམ་པ", 3),
    ("བཞི་པ", 4),
    ("ལྔ་པ", 5),
    ("དྲུག་པ", 6),
    ("བདུན་པ", 7),
    ("བརྒྱད་པ", 8),
    ("དགུ་པ", 9),
    ("བཅུ་པ", 10),
]

COUNT_RE = "|".join(map(re.escape, sorted(COUNT_WORDS, key=len, reverse=True)))
ANN_RE = re.compile(rf"(?P<prefix>.*?ལ(?:་ཡང)?་?)(?P<count>{COUNT_RE})།\s*(?P<topics>.+)")
FINAL_PARTICLE_RE = re.compile(r"(འོ|ནོ|སོ|ཏོ|ལོ|རོ)$")
LINK_RE = re.compile(r"\[\[#\^[^\]|]+\|([^\]]+)\]\]")
HEADING_RE = re.compile(r"^#{2,6} .+ \^[0-9][0-9-]*-0$")
MARKER_RE = re.compile(r"^\d+(?:\.\d+)+$")


def clean_topic(segment: str) -> str:
    topic = segment.strip()
    topic = re.sub(r"[།༎\s]+$", "", topic)
    topic = FINAL_PARTICLE_RE.sub("", topic)
    topic = re.sub(r"[།༎\s]+$", "", topic)
    return topic.strip()


def extract_topics(raw: str, expected: int) -> list[str]:
    text = re.sub(r"[།\s]*$", "", raw.strip())

    tmp = re.sub(r"\s*དང[་༌]?།\s*", "<<<SPLIT>>>", text)
    tmp = re.sub(r"\s*དང་།\s*", "<<<SPLIT>>>", tmp)
    tmp = re.sub(r"\s+དང༌།\s*", "<<<SPLIT>>>", tmp)
    parts = [clean_topic(part) for part in tmp.split("<<<SPLIT>>>")]
    parts = [part for part in parts if part]

    if len(parts) < expected:
        shad_parts = [clean_topic(part) for part in re.split(r"།\s*", text)]
        shad_parts = [part for part in shad_parts if part]
        if len(shad_parts) >= expected:
            parts = shad_parts

    if len(parts) < expected:
        simple_parts = [clean_topic(part) for part in re.split(r"\s*དང[་༌]\s*", text)]
        simple_parts = [part for part in simple_parts if part]
        if len(simple_parts) >= expected:
            parts = simple_parts

    return parts[:expected]


def parse_announcement(line: str) -> dict | None:
    match = ANN_RE.search(line)
    if not match:
        return None
    count = COUNT_WORDS[match.group("count")]
    topics = extract_topics(match.group("topics"), count)
    if len(topics) < 2:
        return None
    return {"count": count, "topics": topics, "start": match.start("topics")}


def parse_ordinal_start(line: str) -> dict | None:
    stripped = line.lstrip()
    leading = len(line) - len(stripped)
    for word, idx in ORD_WORDS:
        if stripped.startswith(word):
            end = leading + len(word)
            if len(line) > end and line[end] == "་":
                end += 1
            return {"word": word, "idx": idx, "start": leading, "end": end}
    return None


def path_id(path: list[int]) -> str:
    return "^" + "-".join(str(part) for part in path) + "-0"


def heading_level(path: list[int]) -> str:
    return "#" * min(len(path) + 1, 6)


def heading_title(topic: str) -> str:
    title = clean_topic(topic)
    if not title.endswith("།"):
        title += "།"
    return title


def wrap_span(line: str, start: int, end: int, block_id: str) -> str:
    return line[:start] + f"[[#{block_id}|{line[start:end]}]]" + line[end:]


def find_plain(line: str, term: str, start: int = 0) -> int:
    pos = line.find(term, start)
    while pos != -1:
        before = line[:pos]
        if before.rfind("[[") <= before.rfind("]]"):
            return pos
        pos = line.find(term, pos + 1)
    return -1


def tag_announcement_terms(line: str, announcement: dict, parent_path: list[int]) -> tuple[str, int]:
    tagged = line
    changed = 0
    search_start = announcement.get("start", 0)
    offset = 0

    for idx, topic in enumerate(announcement["topics"], start=1):
        block_id = path_id(parent_path + [idx])
        term = topic
        pos = find_plain(tagged, term, max(0, search_start + offset - 5))
        if pos == -1:
            alt = topic.rstrip("་")
            if alt and alt != topic:
                alt_pos = find_plain(tagged, alt, max(0, search_start + offset - 5))
                if alt_pos != -1:
                    pos = alt_pos
                    term = alt
        if pos == -1:
            continue

        replacement = f"[[#{block_id}|{term}]]"
        tagged = tagged[:pos] + replacement + tagged[pos + len(term):]
        offset += len(replacement) - len(term)
        changed += 1

    return tagged, changed


def output_path_for(input_path: Path) -> Path:
    out_path = OUT_DIR / ("tagged-" + input_path.name)
    if not out_path.exists():
        return out_path
    stem = out_path.stem
    suffix = out_path.suffix
    n = 2
    while True:
        candidate = OUT_DIR / f"{stem}-v{n}{suffix}"
        if not candidate.exists():
            return candidate
        n += 1


def main() -> None:
    input_path = pick_input_file()
    text = input_path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    out_path = output_path_for(input_path)

    contexts = []
    out = []
    current_chunk = "frontmatter"
    in_frontmatter = False
    frontmatter_marks = 0
    stats = {
        "headings_inserted": 0,
        "announcement_sentences_tagged": 0,
        "announcement_terms_tagged": 0,
        "section_body_restatements_tagged": 0,
        "todos": 0,
        "max_depth": 0,
        "chunks": {},
    }

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()
        if line_no == 1 and stripped == "---":
            in_frontmatter = True
            frontmatter_marks = 1
        elif in_frontmatter and stripped == "---":
            frontmatter_marks += 1
            if frontmatter_marks == 2:
                in_frontmatter = False

        if MARKER_RE.match(stripped):
            current_chunk = stripped.split(".")[0]
            stats["chunks"].setdefault(current_chunk, {"markers": 0, "headings": 0, "announcements": 0})
            stats["chunks"][current_chunk]["markers"] += 1

        if in_frontmatter or not stripped or MARKER_RE.match(stripped) or stripped.startswith("#"):
            out.append(line)
            continue
        if stripped.startswith("ལེའུ་"):
            out.append(line)
            continue

        announcement = parse_announcement(line)
        ordinal_start = parse_ordinal_start(line)
        opened_path = None
        working = line

        if ordinal_start:
            ord_idx = ordinal_start["idx"]
            opened_context = None
            for context in reversed(contexts):
                if ord_idx <= len(context["topics"]) and ord_idx not in context["opened"]:
                    opened_context = context
                    break

            if opened_context:
                opened_context["opened"].add(ord_idx)
                opened_path = opened_context["parent_path"] + [ord_idx]
                block_id = path_id(opened_path)
                title = heading_title(opened_context["topics"][ord_idx - 1])

                if out and out[-1] != "":
                    out.append("")
                out.append(f"{heading_level(opened_path)} {title} {block_id}")
                out.append("")

                working = wrap_span(working, ordinal_start["start"], ordinal_start["end"], block_id)
                stats["headings_inserted"] += 1
                stats["section_body_restatements_tagged"] += 1
                stats["max_depth"] = max(stats["max_depth"], len(opened_path))
                stats["chunks"].setdefault(current_chunk, {"markers": 0, "headings": 0, "announcements": 0})
                stats["chunks"][current_chunk]["headings"] += 1
            elif announcement:
                if out and out[-1] != "":
                    out.append("")
                out.append("<!-- TODO: unclear depth; ordinal opener had no active parent context -->")
                stats["todos"] += 1

        if announcement:
            parent_path = opened_path if opened_path is not None else []
            tagged, changed = tag_announcement_terms(working, announcement, parent_path)
            if changed:
                working = tagged
                stats["announcement_sentences_tagged"] += 1
                stats["announcement_terms_tagged"] += changed
                stats["chunks"].setdefault(current_chunk, {"markers": 0, "headings": 0, "announcements": 0})
                stats["chunks"][current_chunk]["announcements"] += 1
            contexts.append({"parent_path": parent_path, "topics": announcement["topics"], "opened": set(), "line": line_no})

        out.append(working)

    out_text = "\n".join(out) + ("\n" if text.endswith("\n") else "")
    out_path.write_text(out_text, encoding="utf-8")

    original_nonempty = [line for line in lines if line.strip()]
    output_unwrapped = []
    for line in out_text.splitlines():
        if not line.strip():
            continue
        if HEADING_RE.match(line.strip()):
            continue
        if line.strip().startswith("<!-- TODO:"):
            continue
        output_unwrapped.append(LINK_RE.sub(r"\1", line))

    stats["prose_nonempty_lines_match_after_unwrap"] = original_nonempty == output_unwrapped
    stats["output_path"] = str(out_path)
    stats["contexts_created"] = len(contexts)
    stats["unopened_declared_sections"] = sum(len(c["topics"]) - len(c["opened"]) for c in contexts)
    heading_ids = re.findall(r"\^([0-9][0-9-]*-0)\b", out_text)
    stats["duplicate_heading_ids"] = len(heading_ids) - len(set(heading_ids))
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
