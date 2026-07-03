import json
import re
import sys
import time
import unicodedata
from pathlib import Path

import yake
from underthesea import word_tokenize

VI_STOP = {
    "và", "của", "là", "có", "không", "những", "các", "một", "này", "đó",
    "cho", "để", "với", "khi", "nếu", "thì", "mà", "cũng", "đã", "sẽ",
    "đang", "rất", "như", "vì", "nên", "hay", "hoặc", "ai", "gì", "sao",
    "làm", "được", "bị", "ra", "vào", "lên", "xuống", "lại", "nữa", "chỉ",
    "còn", "cả", "mọi", "mỗi", "từng", "dù", "tuy", "nhưng", "vậy", "thế",
    "nào", "đâu", "ở", "trong", "ngoài", "trên", "dưới", "giữa", "sau",
    "trước", "cùng", "theo", "tại", "bởi", "do", "con", "ta", "mình",
    "chính", "ngay", "cứ", "đến", "từ", "qua", "về", "cần", "phải",
    "thật", "sự", "việc", "điều", "người", "cái", "nó", "họ", "ấy", "kia",
    "vẫn", "hết", "lúc", "giờ", "ngày", "đêm", "biết",
    "thấy", "nói", "nghĩ", "muốn", "mong", "xin", "dạy", "kể", "gọi",
    "chưa", "mới", "đều", "nhiều", "ít", "hơn", "nhất", "quá",
    "thôi", "chăng", "chứ", "ạ", "nhé", "à", "ừ",
}

_VERSE_MARKER = re.compile(r"\^([\w][\w\-]*\d+)\s*$")
SCORE_THRESHOLD = 0.3


def extract_verses_from_text(text):
    verses = []
    pending = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("![[") or line.startswith("*Thus ends"):
            continue
        if re.match(r"^#{1,6}\s", line):   # skip markdown headings entirely
            continue
        m = _VERSE_MARKER.search(line)
        if m:
            last = line[: m.start()].strip()
            if last:
                pending.append(last)
            verse_text = " ".join(pending).strip()
            if verse_text:
                verses.append({"verse_id": m.group(1), "text": verse_text})
            pending = []
        else:
            if line:
                pending.append(line)
    return verses


def normalize(phrase):
    text = unicodedata.normalize("NFC", phrase.lower().strip())
    tokens = [t for t in text.split() if t]
    if not tokens:
        return None
    content_tokens = [t for t in tokens if t not in VI_STOP]
    if not content_tokens:
        return None
    while tokens and tokens[0] in VI_STOP:
        tokens.pop(0)
    while tokens and tokens[-1] in VI_STOP:
        tokens.pop()
    if not tokens:
        return None
    return " ".join(tokens)


def main():
    chapter_num = int(sys.argv[1])
    source_path = Path(sys.argv[2])
    out_dir = Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)

    full_text = source_path.read_text(encoding="utf-8")
    chapters = re.split(r"(?=^## Chương)", full_text, flags=re.M)
    chapter_chunks = [c for c in chapters if c.strip().startswith("## Chương")]

    if chapter_num < 1 or chapter_num > len(chapter_chunks):
        print(f"Chapter {chapter_num} out of range (1-{len(chapter_chunks)})")
        sys.exit(1)

    chunk = chapter_chunks[chapter_num - 1]
    title_line = chunk.strip().splitlines()[0]
    print(f"Processing chapter {chapter_num}: {title_line} ({len(chunk)} chars)")

    verses = extract_verses_from_text(chunk)
    # Build the YAKE corpus ONLY from cleaned verse text (no verse-id
    # markers, no markdown headings, no "*Thus ends ...*" trailer notes)
    # so those don't contaminate keyword candidates.
    corpus_text = ". ".join(v["text"] for v in verses)

    t0 = time.time()
    segmented_tokens = word_tokenize(corpus_text)
    joined_tokens = [t.replace(" ", "_") for t in segmented_tokens]
    joined_text = " ".join(joined_tokens)
    print(f"Segmented in {time.time()-t0:.2f}s, {len(segmented_tokens)} tokens")

    joined_stopwords = {w.replace(" ", "_") for w in VI_STOP}

    t1 = time.time()
    extractor = yake.KeywordExtractor(
        lan="vi", n=3, dedupLim=0.9, top=9999, stopwords=joined_stopwords
    )
    raw_keywords = extractor.extract_keywords(joined_text)
    print(f"YAKE done in {time.time()-t1:.2f}s, {len(raw_keywords)} raw candidates")

    kept = []
    seen = set()
    for phrase, score in raw_keywords:
        if score > SCORE_THRESHOLD:
            continue
        phrase = phrase.replace("_", " ")
        norm = normalize(phrase)
        if not norm or norm in seen:
            continue
        seen.add(norm)
        kept.append({"raw": phrase, "normalized": norm, "score": round(score, 6)})

    out_path = out_dir / f"partial_ch{chapter_num:02d}.json"
    out_path.write_text(
        json.dumps({"chapter": chapter_num, "title": title_line,
                    "keywords": kept, "verses": verses},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Saved {len(kept)} keywords, {len(verses)} verses -> {out_path}")


if __name__ == "__main__":
    main()
