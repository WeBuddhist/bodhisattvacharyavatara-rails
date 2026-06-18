from pymongo import MongoClient
from bson import Binary
from uuid import UUID
import argparse
import json
import csv

client = MongoClient("mongodb+srv://webuddhist_db_user:os9meNVni6FqC7if@webuddhist-prd.stty4w4.mongodb.net/")
db = client["webuddhist"]


def str_to_uuid_binary(uuid_str: str) -> Binary:
    return Binary.from_uuid(UUID(uuid_str))


def uuid_to_str(value) -> str:
    if value is None:
        return ""
    if hasattr(value, "as_uuid"):
        return str(value.as_uuid())
    if isinstance(value, Binary):
        return str(value.as_uuid())
    if isinstance(value, UUID):
        return str(value)
    return str(value)


def normalize_mapping(mapping) -> list:
    if not mapping:
        return []

    normalized = []
    for entry in mapping:
        normalized.append({
            "text_id": uuid_to_str(entry.get("text_id")),
            "segments": [uuid_to_str(seg) for seg in entry.get("segments", [])],
        })
    return normalized


def get_text_segments(text_id: str) -> dict:
    doc = db.TableOfContent.find_one({"text_id": text_id})
    if not doc:
        return None

    flat_segments = []
    for section in doc["sections"]:
        for seg in section["segments"]:
            flat_segments.append({
                "segment_id": seg["segment_id"],
                "segment_number": seg["segment_number"]
            })

    uuid_binaries = []
    for seg in flat_segments:
        b = str_to_uuid_binary(seg["segment_id"])
        uuid_binaries.append(b)

    segment_docs = db.Segment.find({"_id": {"$in": uuid_binaries}})

    segment_data_map = {}
    for seg_doc in segment_docs:
        uuid_str = str(seg_doc["_id"].as_uuid())
        segment_data_map[uuid_str] = {
            "content": seg_doc.get("content", ""),
            "mapping": normalize_mapping(seg_doc.get("mapping", [])),
        }

    segments = []
    for seg in flat_segments:
        data = segment_data_map.get(seg["segment_id"], {})
        segments.append({
            "segment_id": seg["segment_id"],
            "segment_number": seg["segment_number"],
            "content": data.get("content", "MISSING"),
            "mapping": data.get("mapping", []),
            "tags": "",
        })

    segments.sort(key=lambda x: x["segment_number"])

    return {
        "text_id": text_id,
        "segments": segments
    }


def save_csv(result: dict, output_path: str):
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["text_id", "segment_number", "segment_id", "content", "mapping", "tags"])
        for seg in result["segments"]:
            writer.writerow([
                result["text_id"],
                seg["segment_number"],
                seg["segment_id"],
                seg["content"],
                json.dumps(seg["mapping"], ensure_ascii=False),
                seg["tags"],
            ])
    print(f"Saved to {output_path}")


def save_json(result: dict, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_path}")


def save_md(result: dict, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Segments for text_id: `{result['text_id']}`\n\n")
        f.write(f"**Total segments:** {len(result['segments'])}\n\n")
        f.write("| segment_number | segment_id | content | mapping | tags |\n")
        f.write("|---|---|---|---|---|\n")
        for seg in result["segments"]:
            content = seg["content"].replace("|", "\\|").replace("\n", " ")
            mapping = json.dumps(seg["mapping"], ensure_ascii=False).replace("|", "\\|")
            f.write(
                f"| {seg['segment_number']} | `{seg['segment_id']}` | {content} | {mapping} | {seg['tags']} |\n"
            )
    print(f"Saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Fetch segments for a given text_id")
    parser.add_argument("text_id", type=str, help="The text_id UUID to query")
    parser.add_argument("--output", type=str, help="Output file path (.json, .csv, or .md)")
    args = parser.parse_args()

    result = get_text_segments(args.text_id)

    if not result:
        print(f"No result found for text_id: {args.text_id}")
        return

    print(f"text_id: {result['text_id']}")
    print(f"Total segments: {len(result['segments'])}")

    missing = [s for s in result["segments"] if s["content"] == "MISSING"]
    if missing:
        print(f"WARNING: {len(missing)} segments had no matching Segment doc")

    if args.output:
        ext = args.output.rsplit(".", 1)[-1].lower()
        if ext == "csv":
            save_csv(result, args.output)
        elif ext == "json":
            save_json(result, args.output)
        elif ext == "md":
            save_md(result, args.output)
        else:
            print("Unknown file extension, please use .csv, .json, or .md")
    else:
        print("\ntext_id,segment_number,segment_id,content,mapping,tags")
        for seg in result["segments"]:
            print(
                f"{result['text_id']},{seg['segment_number']},{seg['segment_id']},"
                f"{seg['content']},{json.dumps(seg['mapping'], ensure_ascii=False)},{seg['tags']}"
            )


if __name__ == "__main__":
    main()