from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import time
from pathlib import Path
from urllib.parse import urlencode

import main as engine
import requests


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input_script"
SOURCE_DIR = BASE_DIR / "site_src"
OUTPUT_DIR = BASE_DIR / "site"
SHOW_DB_DIR = BASE_DIR / "show_db"
SYNC_OVERRIDES_FILE = BASE_DIR / "web_sync_offsets.json"
VERSION_FILE = BASE_DIR / "VERSION"
DIRECT_BATCH_MAX_CHARS = 3200
DIRECT_BATCH_SLEEP_SECONDS = 0.2
SPEAKER_PREFIX_RE = re.compile(
    r"^[\s\u3000]*(?:[\(\[（【《〈≪][^)\]）】》〉≫]{1,24}[\)\]）】》〉≫][\s\u3000]*)+"
)


def strip_speaker_prefix(text: str) -> str:
    cleaned = SPEAKER_PREFIX_RE.sub("", text).strip()
    return cleaned or text.strip()


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
    print(f" -> direct Google batch fallback: {len(sentences)} sentences / {len(batches)} batches")

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
    return hashlib.sha1(path.name.encode("utf-8")).hexdigest()[:12]


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
    unique_lines = list(dict.fromkeys((line.text, line.start_time, line.end_time) for line in cleaned_lines))
    subtitle_lines = [engine.SubtitleLine(text, start, end) for text, start, end in unique_lines]

    translation_map = build_translation_map([line.text for line in subtitle_lines], translation_enabled)

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

        sentences.append(
            {
                "index": index,
                "text": line.text,
                "translation": clean_translation(translation_map.get(line.text, "")),
                "start_time": line.start_time,
                "end_time": line.end_time,
                "start_seconds": engine.seconds_from_hhmmss(line.start_time),
                "end_seconds": engine.seconds_from_hhmmss(line.end_time),
                "has_jlpt": has_jlpt,
                "vocab_matches": vocab_matches,
                "grammar_matches": grammar_matches,
            }
        )

    show_id = show_id_for(path)
    return {
        "id": show_id,
        "title": path.stem,
        "file_name": path.name,
        "duration_seconds": max((item["end_seconds"] for item in sentences), default=0),
        "sentence_count": len(sentences),
        "relevant_sentence_count": relevant_sentence_count,
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
    subtitle_files = sorted(INPUT_DIR.glob("*.srt"))
    if only_names:
        subtitle_files = [path for path in subtitle_files if path.name in only_names or path.stem in only_names]

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

    library_payload = {"items": library_items}
    (db_dir / "library.json").write_text(
        json.dumps(library_payload, ensure_ascii=False, indent=2),
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
