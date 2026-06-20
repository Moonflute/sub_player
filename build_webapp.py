from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

import main as engine


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input_script"
SOURCE_DIR = BASE_DIR / "site_src"
OUTPUT_DIR = BASE_DIR / "site"
SYNC_OVERRIDES_FILE = BASE_DIR / "web_sync_offsets.json"
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
    translator,
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

    if translator is None:
        translation_map = {line.text: "" for line in subtitle_lines}
    else:
        raw_translation_map = engine.translate_sentences(
            [line.text for line in subtitle_lines],
            translator,
        )
        translation_map = {
            sentence: clean_translation(translated)
            for sentence, translated in raw_translation_map.items()
        }

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


def copy_site_source(output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    shutil.copytree(SOURCE_DIR, output_dir)
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")


def build_site(
    output_dir: Path,
    disable_translation: bool,
    rebuild_db: bool,
    only_names: set[str] | None,
) -> None:
    copy_site_source(output_dir)
    data_dir = output_dir / "data" / "shows"
    data_dir.mkdir(parents=True, exist_ok=True)

    engine.ensure_reference_database(BASE_DIR, force_rebuild=rebuild_db)
    vocab_index, grammar_entries, hackers_reference = engine.load_reference_data_from_database(BASE_DIR)

    from janome.tokenizer import Tokenizer
    from deep_translator import GoogleTranslator

    tokenizer = Tokenizer()
    translator = None if disable_translation else GoogleTranslator(source="ja", target="ko")
    sync_overrides = load_sync_overrides()

    library_items: list[dict] = []
    subtitle_files = sorted(INPUT_DIR.glob("*.srt"))
    if only_names:
        subtitle_files = [path for path in subtitle_files if path.name in only_names or path.stem in only_names]

    for path in subtitle_files:
        print(f"[build] {path.name}")
        payload = build_show_payload(
            path=path,
            tokenizer=tokenizer,
            vocab_index=vocab_index,
            grammar_entries=grammar_entries,
            hackers_reference=hackers_reference,
            translator=translator,
            sync_overrides=sync_overrides,
        )
        show_path = data_dir / f"{payload['id']}.json"
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
    (output_dir / "data" / "library.json").write_text(
        json.dumps(library_payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[done] static site written to {output_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a static JLPT subtitle web app.")
    parser.add_argument("--output-dir", default="site")
    parser.add_argument("--disable-translation", action="store_true")
    parser.add_argument("--rebuild-db", action="store_true")
    parser.add_argument("--only", nargs="*", help="Build only selected subtitle filenames or stems")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = (BASE_DIR / args.output_dir).resolve()
    only_names = set(args.only or []) or None
    build_site(
        output_dir=output_dir,
        disable_translation=args.disable_translation,
        rebuild_db=args.rebuild_db,
        only_names=only_names,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
