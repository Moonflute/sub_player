from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import main as engine
from build_webapp import build_translation_map, clean_translation, serialize_grammar, serialize_vocab


BASE_DIR = Path(__file__).resolve().parent
SOURCE_DIR = BASE_DIR / "_jlpt source"
REFINED_DIR = BASE_DIR / "_jlpt source refined"
READING_SOURCE = SOURCE_DIR / "N3 reading official workbook.pdf"
LISTENING_SOURCE_DIR = SOURCE_DIR / "jlpt_n3_listening_review"

JAPANESE_SENTENCE_RE = re.compile(r"[^。！？\n]*(?:[。！？]|$)")
CID_RE = re.compile(r"\(cid:\d+\)")
PAGE_MARK_RE = re.compile(r"―\s*\d+\s*―")
HEADER_RE = re.compile(r"言語知識（文法）・読解[−-]\d+")
RUBY_NOISE_RE = re.compile(r"^[ぁ-んァ-ンー]{1,4}$")


def ensure_dirs() -> None:
    (REFINED_DIR / "reading").mkdir(parents=True, exist_ok=True)
    (REFINED_DIR / "listening").mkdir(parents=True, exist_ok=True)


def extract_pdf_text(path: Path) -> tuple[str, list[dict]]:
    import pdfplumber

    pages: list[dict] = []
    with pdfplumber.open(path) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            pages.append({"page": index, "text": clean_pdf_text(text)})
    return "\n".join(page["text"] for page in pages), pages


def clean_pdf_text(text: str) -> str:
    value = CID_RE.sub("", text)
    value = HEADER_RE.sub("", value)
    value = PAGE_MARK_RE.sub("", value)
    value = value.replace("\u3000", " ")
    lines = []
    for raw_line in value.splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line:
            continue
        if RUBY_NOISE_RE.match(line):
            continue
        if line in {"読ど", "解か", "い"}:
            continue
        lines.append(line)
    return "\n".join(lines)


def normalize_sentence(text: str) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    value = value.strip(" 　-–—")
    return value


def split_reading_sentences(text: str) -> list[str]:
    sentences: list[str] = []
    seen: set[str] = set()
    for match in JAPANESE_SENTENCE_RE.finditer(text):
        sentence = normalize_sentence(match.group(0))
        if len(sentence) < 8:
            continue
        if not engine.has_japanese(sentence):
            continue
        if sentence in seen:
            continue
        seen.add(sentence)
        sentences.append(sentence)
    return sentences


def analyze_reading_sentences(sentences: list[str], translate: bool) -> list[dict]:
    engine.ensure_reference_database(BASE_DIR)
    vocab_index, grammar_entries, hackers_reference = engine.load_reference_data_from_database(BASE_DIR)

    from janome.tokenizer import Tokenizer

    tokenizer = Tokenizer()
    translation_map = build_translation_map(sentences, translate) if translate else {sentence: "" for sentence in sentences}

    items: list[dict] = []
    for index, sentence in enumerate(sentences, start=1):
        analysis = engine.analyze_sentence(
            sentence,
            translation_map,
            tokenizer,
            vocab_index,
            grammar_entries,
            hackers_reference,
        )
        items.append(
            {
                "index": index,
                "text": sentence,
                "translation": clean_translation(translation_map.get(sentence, "")),
                "vocab_matches": [serialize_vocab(item) for item in analysis.vocab_matches] if analysis else [],
                "grammar_matches": [serialize_grammar(item) for item in analysis.grammar_matches] if analysis else [],
            }
        )
    return items


def build_reading_refined(translate: bool) -> dict:
    raw_text, pages = extract_pdf_text(READING_SOURCE)
    sentences = split_reading_sentences(raw_text)
    items = analyze_reading_sentences(sentences, translate)
    payload = {
        "id": "n3_official_workbook_reading",
        "mode": "reading",
        "level": "N3",
        "title": "N3 Reading Official Workbook",
        "source_file": str(READING_SOURCE.relative_to(BASE_DIR)).replace("\\", "/"),
        "sentence_count": len(items),
        "items": items,
    }

    reading_dir = REFINED_DIR / "reading"
    (reading_dir / "n3_official_workbook_raw_pages.json").write_text(
        json.dumps({"pages": pages}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (reading_dir / "n3_official_workbook_reading.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return payload


def section_sort_key(path: Path) -> tuple[int, str]:
    match = re.match(r"(\d+)", path.name)
    return (int(match.group(1)) if match else 999, path.name)


def build_listening_index() -> dict:
    sections: list[dict] = []
    all_tracks: list[dict] = []
    for section_dir in sorted((p for p in LISTENING_SOURCE_DIR.iterdir() if p.is_dir()), key=section_sort_key):
        section_tracks: list[dict] = []
        section_match = re.match(r"(?P<order>\d+)\.(?P<title>.+)", section_dir.name)
        section_order = int(section_match.group("order")) if section_match else len(sections) + 1
        section_title = section_match.group("title") if section_match else section_dir.name
        section_title = section_title.replace("_복습용분할(1.0배속)", "").replace("_", " ").strip()

        for index, audio_path in enumerate(sorted(section_dir.glob("*.mp3")), start=1):
            track_id = f"listening_{section_order:02d}_{index:03d}"
            rel_path = audio_path.relative_to(BASE_DIR)
            track = {
                "id": track_id,
                "mode": "listening",
                "level": "N3",
                "section_order": section_order,
                "section_title": section_title,
                "title": audio_path.stem,
                "source_audio": str(rel_path).replace("\\", "/"),
                "file_size": audio_path.stat().st_size,
                "transcript_status": "pending",
                "transcript_file": "",
                "segments": [],
            }
            section_tracks.append(track)
            all_tracks.append(track)

        sections.append(
            {
                "order": section_order,
                "title": section_title,
                "track_count": len(section_tracks),
                "tracks": section_tracks,
            }
        )

    payload = {
        "id": "n3_listening_review",
        "mode": "listening",
        "level": "N3",
        "title": "N3 Listening Review",
        "track_count": len(all_tracks),
        "sections": sections,
    }
    (REFINED_DIR / "listening" / "n3_listening_review_index.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Refine local JLPT reading/listening sources into JSON DB inputs.")
    parser.add_argument("--no-translate", action="store_true", help="Skip Google translation for reading sentences.")
    args = parser.parse_args()

    ensure_dirs()
    reading = build_reading_refined(translate=not args.no_translate)
    listening = build_listening_index()

    summary = {
        "reading_sentence_count": reading["sentence_count"],
        "listening_track_count": listening["track_count"],
        "outputs": [
            "reading/n3_official_workbook_reading.json",
            "reading/n3_official_workbook_raw_pages.json",
            "listening/n3_listening_review_index.json",
        ],
    }
    (REFINED_DIR / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
