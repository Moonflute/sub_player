from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shutil
import statistics
import time
from pathlib import Path

import main as engine
import requests


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input_script"
SOURCE_DIR = BASE_DIR / "site_src"
OUTPUT_DIR = BASE_DIR / "site"
SHOW_DB_DIR = BASE_DIR / "show_db"
JLPT_REFINED_DIR = BASE_DIR / "_jlpt source refined"
SYNC_OVERRIDES_FILE = BASE_DIR / "web_sync_offsets.json"
VERSION_FILE = BASE_DIR / "VERSION"

DIRECT_BATCH_MAX_CHARS = 3200
DIRECT_BATCH_SLEEP_SECONDS = 0.2
SYNC_MATCH_SAMPLE_SIZE = 140
SYNC_MATCH_SCAN_LIMIT = 320
SYNC_MATCH_MIN_RATIO = 0.55
SYNC_OFFSET_OUTLIER_SECONDS = 8.0
TRANSLATION_OVERLAP_PADDING = 0.45
TRANSLATION_NEARBY_THRESHOLD = 1.2
ASS_MATCH_WINDOW_SECONDS = 2.6
ASS_MATCH_MAX_SPAN = 3
ASS_MATCH_MIN_SCORE = 0.43
SHORT_SUBTITLE_MIN_SECONDS = 1.0
SHORT_SUBTITLE_MAX_CHARS = 8
SHORT_SUBTITLE_MERGE_GAP_SECONDS = 1.0
SHORT_SUBTITLE_MERGE_MAX_SPAN_SECONDS = 10.0

SPEAKER_PREFIX_RE = re.compile(
    r"^[\s\u3000]*(?:[\(\[「『【<＜][^)\]」』】>＞]{1,24}[\)\]」』】>＞][\s\u3000]*)+"
)
ASS_DIALOGUE_RE = re.compile(
    r"^Dialogue:\s*\d+,(?P<start>\d+:\d{2}:\d{2}\.\d{2}),(?P<end>\d+:\d{2}:\d{2}\.\d{2}),"
    r"(?P<style>[^,]*),(?P<name>[^,]*),(?P<margin_l>[^,]*),(?P<margin_r>[^,]*),"
    r"(?P<margin_v>[^,]*),(?P<effect>[^,]*),(?P<text>.*)$"
)
ASS_TAG_RE = re.compile(r"\{[^{}]*\}")
PAREN_CONTENT_RE = re.compile(r"\([^)]*\)|\[[^\]]*\]|【[^】]*】|＜[^＞]*＞|〈[^〉]*〉")
HANGUL_RE = re.compile(r"[가-힣]")
KOREAN_TOKEN_RE = re.compile(r"[가-힣A-Za-z0-9]+")


EPISODE_TOKEN_RE = re.compile(r"(?:S(?P<season>\d{1,2})E(?P<episode>\d{1,3})|(?P<episode_kr>\d{1,3})화)", re.IGNORECASE)
TITLE_CLEANUP_PATTERNS = [
    re.compile(r"^\[[^\]]+\]\s*"),
    re.compile(r"\s*\(BD [^)]+\)", re.IGNORECASE),
    re.compile(r"\s*\[[0-9A-F]{6,8}\]\s*$", re.IGNORECASE),
    re.compile(r"\s*\(번역\)\s*$"),
]


def strip_speaker_prefix(text: str) -> str:
    cleaned = SPEAKER_PREFIX_RE.sub("", text).strip()
    return cleaned or text.strip()


def strip_parenthetical_content(text: str) -> str:
    return PAREN_CONTENT_RE.sub("", text)


def clean_translation(text: str) -> str:
    value = str(text or "").strip()
    if not value:
        return ""
    blocked_markers = [
        "번역 비활성화",
        "자동 번역 실패",
        "ConnectionError",
    ]
    if any(marker in value for marker in blocked_markers):
        return ""
    return value


def direct_google_translate(text: str, source: str = "ja", target: str = "ko") -> str:
    response = requests.get(
        "https://translate.googleapis.com/translate_a/single",
        params={
            "client": "gtx",
            "sl": source,
            "tl": target,
            "dt": "t",
            "q": text,
        },
        timeout=20,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            )
        },
    )
    response.raise_for_status()
    payload = response.json()
    translated = clean_translation("".join(part[0] for part in payload[0] if part and part[0]))
    if not translated or translated == text.strip():
        return ""
    return translated


def segment_marker(index: int) -> str:
    return f"[[[SEG_{index:04d}]]]"


def pack_translation_batch(sentences: list[str]) -> str:
    return "\n".join(f"{segment_marker(index)}\n{sentence}" for index, sentence in enumerate(sentences))


def unpack_translation_batch(translated_text: str, size: int) -> list[str]:
    normalized = translated_text.replace("\r\n", "\n").replace("\r", "\n")
    positions: list[tuple[int, int]] = []
    for index in range(size):
        marker = segment_marker(index)
        pos = normalized.find(marker)
        if pos == -1:
            return []
        positions.append((index, pos))

    positions.sort(key=lambda item: item[1])
    results: list[str] = []
    for order, (index, start_pos) in enumerate(positions):
        marker = segment_marker(index)
        content_start = start_pos + len(marker)
        if content_start < len(normalized) and normalized[content_start] == "\n":
            content_start += 1
        content_end = positions[order + 1][1] if order + 1 < len(positions) else len(normalized)
        results.append(clean_translation(normalized[content_start:content_end].strip()))
    return results


def build_sentence_batches(sentences: list[str], max_chars: int = DIRECT_BATCH_MAX_CHARS) -> list[list[str]]:
    batches: list[list[str]] = []
    current_batch: list[str] = []
    current_size = 0

    for sentence in sentences:
        estimated_size = len(sentence) + 24
        if current_batch and current_size + estimated_size > max_chars:
            batches.append(current_batch)
            current_batch = []
            current_size = 0
        current_batch.append(sentence)
        current_size += estimated_size

    if current_batch:
        batches.append(current_batch)
    return batches


def direct_google_translate_batch(sentences: list[str], source: str = "ja", target: str = "ko") -> dict[str, str]:
    translation_map: dict[str, str] = {}
    batches = build_sentence_batches(sentences)
    print(f" -> direct Google batch translation: {len(sentences)} sentences / {len(batches)} batches")

    for batch_index, batch in enumerate(batches, start=1):
        try:
            packed = pack_translation_batch(batch)
            translated = direct_google_translate(packed, source=source, target=target)
            unpacked = unpack_translation_batch(translated, len(batch))
        except Exception as exc:
            print(f"    [warn] direct batch request failed {batch_index}/{len(batches)}: {exc.__class__.__name__}")
            unpacked = []

        if len(unpacked) == len(batch):
            for sentence, translated_sentence in zip(batch, unpacked):
                translation_map[sentence] = clean_translation(translated_sentence)
        else:
            print(f"    [warn] batch split failed {batch_index}/{len(batches)}; falling back to single requests")
            for sentence in batch:
                try:
                    translation_map[sentence] = direct_google_translate(sentence, source=source, target=target)
                    time.sleep(DIRECT_BATCH_SLEEP_SECONDS)
                except Exception as exc:
                    print(f"    [warn] direct single fallback failed: {exc.__class__.__name__}")
                    translation_map[sentence] = ""
            continue

        print(f"    - direct batch progress: {batch_index}/{len(batches)}")
        time.sleep(DIRECT_BATCH_SLEEP_SECONDS)

    return translation_map


def build_translation_map(sentences: list[str], translation_enabled: bool) -> dict[str, str]:
    if not translation_enabled:
        return {sentence: "" for sentence in sentences}
    translation_map = {sentence: "" for sentence in sentences}
    direct_map = direct_google_translate_batch(sentences)
    for sentence in sentences:
        translation_map[sentence] = clean_translation(direct_map.get(sentence, ""))
    return translation_map


def hhmmss_centiseconds_to_seconds(value: str) -> float:
    parts = value.split(":")
    if len(parts) != 3:
        return 0.0
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds, centiseconds = parts[2].split(".")
    return hours * 3600 + minutes * 60 + int(seconds) + int(centiseconds) / 100.0


def ass_text_to_plain(text: str) -> str:
    cleaned = text.lstrip("\ufeff")
    cleaned = ASS_TAG_RE.sub("", cleaned)
    cleaned = cleaned.replace("\\N", "\n").replace("\\n", "\n").replace("\\h", " ")
    cleaned = cleaned.replace("\u200b", " ")
    cleaned = strip_parenthetical_content(cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def normalize_korean_text(text: str) -> str:
    return "".join(KOREAN_TOKEN_RE.findall(text)).lower()


def compact_korean_length(text: str) -> int:
    return len(normalize_korean_text(text))


def parse_ass(path: Path) -> list[dict]:
    entries: list[dict] = []
    for raw_line in path.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
        match = ASS_DIALOGUE_RE.match(raw_line)
        if not match:
            continue
        text = ass_text_to_plain(match.group("text"))
        if not text or not HANGUL_RE.search(text):
            continue
        start_time = match.group("start")
        end_time = match.group("end")
        entries.append(
            {
                "text": text,
                "start_time": start_time,
                "end_time": end_time,
                "start_seconds": hhmmss_centiseconds_to_seconds(start_time),
                "end_seconds": hhmmss_centiseconds_to_seconds(end_time),
            }
        )
    return entries


def relative_input_path(path: Path) -> Path:
    try:
        return path.relative_to(INPUT_DIR)
    except ValueError:
        return path


def extract_episode_key(text: str) -> tuple[int | None, int | None]:
    match = EPISODE_TOKEN_RE.search(text or "")
    if not match:
        return None, None
    if match.group("episode_kr"):
        return 1, int(match.group("episode_kr"))
    season = int(match.group("season")) if match.group("season") else 1
    episode = int(match.group("episode")) if match.group("episode") else None
    return season, episode


def normalize_title_stem(stem: str) -> str:
    value = stem.strip()
    for pattern in TITLE_CLEANUP_PATTERNS:
        value = pattern.sub("", value).strip()
    return re.sub(r"\s+", " ", value).strip()


def canonical_show_title(path: Path) -> str:
    stem = normalize_title_stem(path.stem)
    season, episode = extract_episode_key(stem)
    if season is not None and episode is not None:
        prefix = re.sub(r"\s*-?\s*S\d{1,2}E\d{1,3}\b.*$", "", stem, flags=re.IGNORECASE).strip()
        if prefix:
            return f"{prefix} - S{season:02d}E{episode:02d}"
    return stem


def subtitle_sort_key(path: Path) -> tuple[str, int, int, str]:
    title = canonical_show_title(path)
    season, episode = extract_episode_key(title)
    series = re.sub(r"\s*-\s*S\d{2}E\d{2}$", "", title, flags=re.IGNORECASE)
    return (series.lower(), season or 999, episode or 999, title.lower())


def subtitle_candidate_priority(path: Path) -> tuple[int, int, int]:
    relative = relative_input_path(path)
    depth = len(relative.parts)
    has_local_ass = 1 if any(path.parent.glob("*.ass")) else 0
    return (depth, has_local_ass, -len(path.name))


def discover_subtitle_files(only_names: set[str] | None) -> list[Path]:
    subtitle_files = sorted(INPUT_DIR.rglob("*.srt"))
    if only_names:
        filtered: list[Path] = []
        for path in subtitle_files:
            relative = str(relative_input_path(path)).replace("\\", "/")
            candidates = {
                path.name,
                path.stem,
                relative,
                relative.rsplit(".", 1)[0],
            }
            parent_match = any(
                relative == name or relative.startswith(f"{name}/")
                for name in only_names
            )
            if candidates & only_names or parent_match:
                filtered.append(path)
        subtitle_files = filtered

    deduped: dict[str, Path] = {}
    for path in subtitle_files:
        key = canonical_show_title(path)
        current = deduped.get(key)
        if current is None or subtitle_candidate_priority(path) > subtitle_candidate_priority(current):
            deduped[key] = path

    return sorted(deduped.values(), key=subtitle_sort_key)


def find_translation_ass_file(source_path: Path) -> Path | None:
    candidates = sorted(source_path.parent.glob("*.ass"))
    if not candidates:
        candidates = sorted(INPUT_DIR.glob("*.ass"))
    if not candidates:
        return None

    source_stem = normalize_title_stem(source_path.stem).lower()
    source_tokens = set(re.findall(r"[0-9a-z가-힣]+", source_stem))
    source_episode = extract_episode_key(source_stem)
    source_parent = source_path.parent.name.lower()
    best_match: Path | None = None
    best_score = -1

    for candidate in candidates:
        candidate_stem = normalize_title_stem(candidate.stem).lower()
        candidate_tokens = set(re.findall(r"[0-9a-z가-힣]+", candidate_stem))
        candidate_episode = extract_episode_key(candidate_stem)
        score = len(source_tokens & candidate_tokens)
        if source_stem and source_stem in candidate_stem:
            score += 5
        if source_episode != (None, None) and source_episode == candidate_episode:
            score += 8
        if candidate.parent == source_path.parent:
            score += 4
        if source_parent and source_parent == candidate.parent.name.lower():
            score += 2
        if "번역" in candidate_stem:
            score += 2
        if score > best_score:
            best_score = score
            best_match = candidate

    return best_match if best_score >= 4 else None


def estimate_ass_sync_offset(
    subtitle_lines: list[engine.SubtitleLine],
    ass_entries: list[dict],
    google_translation_map: dict[str, str],
) -> float | None:
    sample_lines = subtitle_lines[:SYNC_MATCH_SAMPLE_SIZE]
    scan_entries = ass_entries[:SYNC_MATCH_SCAN_LIMIT]
    if not sample_lines or not scan_entries:
        return None

    offsets: list[float] = []

    for line in sample_lines:
        translated = clean_translation(google_translation_map.get(line.text, ""))
        normalized_translated = normalize_korean_text(translated)
        if len(normalized_translated) < 4:
            continue

        best_entry: dict | None = None
        best_ratio = 0.0
        for entry in scan_entries:
            normalized_ass = normalize_korean_text(str(entry["text"]))
            if len(normalized_ass) < 4:
                continue
            ratio = difflib.SequenceMatcher(None, normalized_translated, normalized_ass).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_entry = entry

        if best_entry is None or best_ratio < SYNC_MATCH_MIN_RATIO:
            continue

        source_seconds = engine.seconds_from_hhmmss(line.start_time)
        offsets.append(source_seconds - float(best_entry["start_seconds"]))

    if len(offsets) < 3:
        return None

    median_offset = statistics.median(offsets)
    filtered = [offset for offset in offsets if abs(offset - median_offset) <= SYNC_OFFSET_OUTLIER_SECONDS]
    if len(filtered) >= 3:
        median_offset = statistics.median(filtered)
    return float(median_offset)


def build_ass_candidate_spans(
    ass_entries: list[dict],
    line_start: float,
    line_end: float,
    offset_seconds: float,
    max_span: int = ASS_MATCH_MAX_SPAN,
) -> list[dict]:
    nearby_entries: list[tuple[int, dict, float, float]] = []
    window_start = line_start - ASS_MATCH_WINDOW_SECONDS
    window_end = line_end + ASS_MATCH_WINDOW_SECONDS

    for index, entry in enumerate(ass_entries):
        adjusted_start = float(entry["start_seconds"]) + offset_seconds
        adjusted_end = float(entry["end_seconds"]) + offset_seconds
        if adjusted_end < window_start or adjusted_start > window_end:
            continue
        nearby_entries.append((index, entry, adjusted_start, adjusted_end))

    spans: list[dict] = []
    seen: set[tuple[int, int]] = set()
    for start_pos in range(len(nearby_entries)):
        for span_size in range(1, max_span + 1):
            end_pos = start_pos + span_size - 1
            if end_pos >= len(nearby_entries):
                break
            start_index = nearby_entries[start_pos][0]
            end_index = nearby_entries[end_pos][0]
            if end_index - start_index != span_size - 1:
                break
            if (start_index, end_index) in seen:
                continue
            seen.add((start_index, end_index))
            chunk = nearby_entries[start_pos : end_pos + 1]
            texts = [str(item[1]["text"]).strip() for item in chunk if str(item[1]["text"]).strip()]
            if not texts:
                continue
            spans.append(
                {
                    "start_index": start_index,
                    "end_index": end_index,
                    "text": " ".join(dict.fromkeys(texts)),
                    "start_seconds": chunk[0][2],
                    "end_seconds": chunk[-1][3],
                }
            )
    return spans


def score_ass_span(
    line_start: float,
    line_end: float,
    line_translation: str,
    candidate_text: str,
    candidate_start: float,
    candidate_end: float,
) -> float:
    normalized_line = normalize_korean_text(line_translation)
    normalized_candidate = normalize_korean_text(candidate_text)
    if len(normalized_candidate) < 2 or len(normalized_line) < 2:
        return -1.0

    text_similarity = difflib.SequenceMatcher(None, normalized_line, normalized_candidate).ratio()
    overlap = max(0.0, min(line_end, candidate_end) - max(line_start, candidate_start))
    line_duration = max(0.1, line_end - line_start)
    candidate_duration = max(0.1, candidate_end - candidate_start)
    overlap_ratio = overlap / max(line_duration, min(candidate_duration, line_duration))
    center_gap = abs(((line_start + line_end) / 2.0) - ((candidate_start + candidate_end) / 2.0))

    line_len = len(normalized_line)
    candidate_len = len(normalized_candidate)
    if candidate_len > line_len:
        length_penalty = min(0.35, ((candidate_len - line_len) / max(1, line_len)) * 0.18)
    else:
        length_penalty = min(0.18, ((line_len - candidate_len) / max(1, line_len)) * 0.08)

    score = text_similarity + (overlap_ratio * 0.24) - (center_gap * 0.05) - length_penalty
    return score


def build_translation_map_from_ass(
    subtitle_lines: list[engine.SubtitleLine],
    ass_entries: list[dict],
    offset_seconds: float,
    google_translation_map: dict[str, str],
) -> dict[str, str]:
    translation_map: dict[str, str] = {}

    for line in subtitle_lines:
        line_start = engine.seconds_from_hhmmss(line.start_time)
        line_end = engine.seconds_from_hhmmss(line.end_time)
        line_translation = clean_translation(google_translation_map.get(line.text, ""))
        spans = build_ass_candidate_spans(ass_entries, line_start, line_end, offset_seconds)

        best_text = ""
        best_score = -1.0
        for span in spans:
            score = score_ass_span(
                line_start=line_start,
                line_end=line_end,
                line_translation=line_translation,
                candidate_text=str(span["text"]),
                candidate_start=float(span["start_seconds"]),
                candidate_end=float(span["end_seconds"]),
            )
            if score > best_score:
                best_score = score
                best_text = str(span["text"])

        if best_score >= ASS_MATCH_MIN_SCORE and best_text:
            translation_map[line.text] = clean_translation(best_text)
            continue

        nearest_text = ""
        nearest_gap: float | None = None
        for entry in ass_entries:
            adjusted_start = float(entry["start_seconds"]) + offset_seconds
            adjusted_end = float(entry["end_seconds"]) + offset_seconds
            gap = min(abs(adjusted_start - line_start), abs(adjusted_end - line_end))
            if nearest_gap is None or gap < nearest_gap:
                nearest_gap = gap
                nearest_text = str(entry["text"])

        if nearest_gap is not None and nearest_gap <= TRANSLATION_NEARBY_THRESHOLD:
            translation_map[line.text] = clean_translation(nearest_text)
        else:
            translation_map[line.text] = ""

    return translation_map


def resolve_translation_map(
    path: Path,
    subtitle_lines: list[engine.SubtitleLine],
    translation_enabled: bool,
) -> tuple[dict[str, str], dict]:
    metadata = {
        "source": "google" if translation_enabled else "disabled",
        "translation_file": "",
        "sync_offset_seconds": None,
    }

    if not translation_enabled:
        return {line.text: "" for line in subtitle_lines}, metadata

    ass_path = find_translation_ass_file(path)
    if ass_path is None:
        return build_translation_map([line.text for line in subtitle_lines], True), metadata

    ass_entries = parse_ass(ass_path)
    if not ass_entries:
        return build_translation_map([line.text for line in subtitle_lines], True), metadata

    print(f" -> translation ASS found: {ass_path.name}")
    google_translation_map = build_translation_map([line.text for line in subtitle_lines], True)
    offset_seconds = estimate_ass_sync_offset(subtitle_lines, ass_entries, google_translation_map)
    if offset_seconds is None:
        print("    [warn] ASS sync estimation failed; using Google translation only")
        return google_translation_map, metadata

    print(f"    - estimated ASS sync offset: {offset_seconds:+.2f}s")
    translation_map = build_translation_map_from_ass(
        subtitle_lines,
        ass_entries,
        offset_seconds,
        google_translation_map,
    )

    missing_sentences = [line.text for line in subtitle_lines if not translation_map.get(line.text)]
    if missing_sentences:
        print(f"    - filling missing translations with Google: {len(missing_sentences)} sentences")
        for sentence in missing_sentences:
            translation_map[sentence] = clean_translation(google_translation_map.get(sentence, ""))

    metadata = {
        "source": "ass+google-fallback",
        "translation_file": ass_path.name,
        "sync_offset_seconds": round(offset_seconds, 3),
    }
    return translation_map, metadata


def read_version() -> str:
    if not VERSION_FILE.exists():
        VERSION_FILE.write_text("0.0.1", encoding="utf-8")
        return "0.0.1"
    return VERSION_FILE.read_text(encoding="utf-8").strip() or "0.0.1"


def bump_version(version: str) -> str:
    parts = version.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise ValueError(f"Invalid version format: {version}")
    major, minor, patch = map(int, parts)
    return f"{major}.{minor}.{patch + 1}"


def resolve_version(keep_version: bool) -> str:
    current = read_version()
    if keep_version:
        return current
    updated = bump_version(current)
    VERSION_FILE.write_text(updated, encoding="utf-8")
    return updated


def load_sync_overrides() -> dict[str, int]:
    if not SYNC_OVERRIDES_FILE.exists():
        return {}
    try:
        raw = json.loads(SYNC_OVERRIDES_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}

    result: dict[str, int] = {}
    for key, value in raw.items():
        try:
            result[str(key)] = int(value)
        except Exception:
            continue
    return result


def show_id_for(path: Path) -> str:
    return hashlib.sha1(str(relative_input_path(path)).encode("utf-8")).hexdigest()[:12]


def serialize_vocab(match: engine.VocabMatch) -> dict:
    return {
        "surface": match.entry.surface,
        "reading": match.entry.reading,
        "meaning": match.entry.meaning,
        "level": match.entry.level,
        "surface_in_sentence": match.surface_in_sentence,
        "base_form": match.base_form,
        "pos": match.pos,
    }


def serialize_grammar(match: engine.GrammarMatch) -> dict:
    return {
        "label": match.entry.label,
        "meaning": match.entry.meaning,
        "level": match.entry.level,
        "category": match.category,
        "structure": match.structure,
        "note": match.note,
        "matched_texts": list(match.matched_texts),
        "is_pattern": match.is_pattern,
    }


def line_seconds(line: engine.SubtitleLine) -> tuple[float, float]:
    start = float(engine.seconds_from_hhmmss(line.start_time))
    end = float(engine.seconds_from_hhmmss(line.end_time))
    return start, end


def line_duration_seconds(line: engine.SubtitleLine) -> float:
    start, end = line_seconds(line)
    return max(0.0, end - start)


def compact_display_text(text: str) -> str:
    return engine.compact_japanese(strip_speaker_prefix(text))


def should_merge_short_line(line: engine.SubtitleLine) -> bool:
    compact = compact_display_text(line.text)
    duration = line_duration_seconds(line)
    return duration < SHORT_SUBTITLE_MIN_SECONDS or (
        duration <= SHORT_SUBTITLE_MIN_SECONDS and len(compact) <= SHORT_SUBTITLE_MAX_CHARS
    )


def can_merge_lines(left: engine.SubtitleLine, right: engine.SubtitleLine) -> bool:
    left_start, left_end = line_seconds(left)
    right_start, right_end = line_seconds(right)
    gap = right_start - left_end
    combined_span = right_end - left_start
    return gap <= SHORT_SUBTITLE_MERGE_GAP_SECONDS and combined_span <= SHORT_SUBTITLE_MERGE_MAX_SPAN_SECONDS


def merge_line_group(lines: list[engine.SubtitleLine]) -> engine.SubtitleLine:
    merged_text = " ".join(part.text.strip() for part in lines if part.text.strip())
    return engine.SubtitleLine(
        text=merged_text.strip(),
        start_time=lines[0].start_time,
        end_time=lines[-1].end_time,
    )


def merge_short_subtitle_lines(lines: list[engine.SubtitleLine]) -> list[engine.SubtitleLine]:
    if not lines:
        return []

    merged: list[engine.SubtitleLine] = []
    index = 0

    while index < len(lines):
        current = lines[index]
        if should_merge_short_line(current):
            next_line = lines[index + 1] if index + 1 < len(lines) else None
            prev_line = merged[-1] if merged else None

            if next_line and can_merge_lines(current, next_line):
                combined = merge_line_group([current, next_line])
                index += 2
                while index < len(lines) and should_merge_short_line(combined) and can_merge_lines(combined, lines[index]):
                    combined = merge_line_group([combined, lines[index]])
                    index += 1
                merged.append(combined)
                continue

            if prev_line and can_merge_lines(prev_line, current):
                merged[-1] = merge_line_group([prev_line, current])
                index += 1
                continue

        merged.append(current)
        index += 1

    return merged


def build_show_payload(
    path: Path,
    tokenizer,
    vocab_index,
    grammar_entries,
    hackers_reference,
    translation_enabled: bool,
    sync_overrides: dict[str, int],
) -> dict:
    raw_lines = engine.parse_srt(path)
    split_lines = engine.split_sentences(raw_lines)
    cleaned_lines = [
        engine.SubtitleLine(strip_speaker_prefix(line.text), line.start_time, line.end_time)
        for line in split_lines
        if strip_speaker_prefix(line.text)
    ]
    merged_lines = merge_short_subtitle_lines(cleaned_lines)
    unique_lines = list(dict.fromkeys((line.text, line.start_time, line.end_time) for line in merged_lines))
    subtitle_lines = [engine.SubtitleLine(text, start, end) for text, start, end in unique_lines]

    translation_map, translation_info = resolve_translation_map(path, subtitle_lines, translation_enabled)
    manual_sync_offset = int(sync_overrides.get(path.name, sync_overrides.get(path.stem, 0)))

    sentences = []
    relevant_sentence_count = 0
    for index, line in enumerate(subtitle_lines, start=1):
        analysis = engine.analyze_sentence(
            line.text,
            translation_map,
            tokenizer,
            vocab_index,
            grammar_entries,
            hackers_reference,
        )

        vocab_matches = []
        grammar_matches = []
        has_jlpt = False
        if analysis:
            vocab_matches = [serialize_vocab(item) for item in analysis.vocab_matches]
            grammar_matches = [serialize_grammar(item) for item in analysis.grammar_matches]
            has_jlpt = bool(vocab_matches or grammar_matches)
            if has_jlpt:
                relevant_sentence_count += 1

        start_seconds = engine.seconds_from_hhmmss(line.start_time) + manual_sync_offset
        end_seconds = engine.seconds_from_hhmmss(line.end_time) + manual_sync_offset
        sentences.append(
            {
                "index": index,
                "text": line.text,
                "translation": clean_translation(translation_map.get(line.text, "")),
                "start_time": line.start_time,
                "end_time": line.end_time,
                "start_seconds": max(0, start_seconds),
                "end_seconds": max(0, end_seconds),
                "has_jlpt": has_jlpt,
                "vocab_matches": vocab_matches,
                "grammar_matches": grammar_matches,
            }
        )

    show_id = show_id_for(path)
    return {
        "id": show_id,
        "title": canonical_show_title(path),
        "file_name": str(relative_input_path(path)).replace("\\", "/"),
        "duration_seconds": max((item["end_seconds"] for item in sentences), default=0),
        "sentence_count": len(sentences),
        "relevant_sentence_count": relevant_sentence_count,
        "translation_info": translation_info,
        "manual_sync_offset_seconds": manual_sync_offset,
        "sentences": sentences,
    }


def copy_site_source(output_dir: Path, version: str) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    shutil.copytree(SOURCE_DIR, output_dir)
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")
    for path in output_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".css", ".js", ".json", ".webmanifest", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        if "__APP_VERSION__" in text:
            path.write_text(text.replace("__APP_VERSION__", version), encoding="utf-8")


def write_show_database(
    db_dir: Path,
    disable_translation: bool,
    rebuild_db: bool,
    only_names: set[str] | None,
) -> Path:
    shows_dir = db_dir / "shows"
    if db_dir.exists():
        shutil.rmtree(db_dir)
    shows_dir.mkdir(parents=True, exist_ok=True)

    engine.ensure_reference_database(BASE_DIR, force_rebuild=rebuild_db)
    vocab_index, grammar_entries, hackers_reference = engine.load_reference_data_from_database(BASE_DIR)

    from janome.tokenizer import Tokenizer

    tokenizer = Tokenizer()
    sync_overrides = load_sync_overrides()

    library_items: list[dict] = []
    subtitle_files = discover_subtitle_files(only_names)

    for path in subtitle_files:
        print(f"[build-db] {path.name}")
        payload = build_show_payload(
            path=path,
            tokenizer=tokenizer,
            vocab_index=vocab_index,
            grammar_entries=grammar_entries,
            hackers_reference=hackers_reference,
            translation_enabled=not disable_translation,
            sync_overrides=sync_overrides,
        )
        show_path = shows_dir / f"{payload['id']}.json"
        show_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        library_items.append(
            {
                "id": payload["id"],
                "title": payload["title"],
                "file_name": payload["file_name"],
                "duration_seconds": payload["duration_seconds"],
                "sentence_count": payload["sentence_count"],
                "relevant_sentence_count": payload["relevant_sentence_count"],
            }
        )

    (db_dir / "library.json").write_text(
        json.dumps({"items": library_items}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[done] show db written to {db_dir}")
    return db_dir


def build_site(
    output_dir: Path,
    db_dir: Path,
    version: str,
) -> None:
    copy_site_source(output_dir, version)
    data_dir = output_dir / "data" / "shows"
    data_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(db_dir / "library.json", output_dir / "data" / "library.json")
    for show_json in (db_dir / "shows").glob("*.json"):
        shutil.copy2(show_json, data_dir / show_json.name)
    if JLPT_REFINED_DIR.exists():
        jlpt_data_dir = output_dir / "data" / "jlpt"
        if jlpt_data_dir.exists():
            shutil.rmtree(jlpt_data_dir)
        shutil.copytree(
            JLPT_REFINED_DIR,
            jlpt_data_dir,
            ignore=shutil.ignore_patterns("transcripts", "gemini_translation_polish_cache.json"),
        )
    print(f"[done] static site written to {output_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a static JLPT subtitle web app.")
    parser.add_argument("--output-dir", default="site")
    parser.add_argument("--db-dir", default="show_db")
    parser.add_argument("--disable-translation", action="store_true")
    parser.add_argument("--rebuild-db", action="store_true")
    parser.add_argument("--keep-version", action="store_true")
    parser.add_argument("--skip-show-db", action="store_true")
    parser.add_argument("--only", nargs="*", help="Build only selected subtitle filenames or stems")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = (BASE_DIR / args.output_dir).resolve()
    db_dir = (BASE_DIR / args.db_dir).resolve()
    only_names = set(args.only or []) or None
    version = resolve_version(args.keep_version)
    print(f"[version] {version}")
    if not args.skip_show_db:
        write_show_database(
            db_dir=db_dir,
            disable_translation=args.disable_translation,
            rebuild_db=args.rebuild_db,
            only_names=only_names,
        )
    build_site(
        output_dir=output_dir,
        db_dir=db_dir,
        version=version,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
