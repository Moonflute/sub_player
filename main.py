from __future__ import annotations

import argparse
import csv
import html
import re
import sqlite3
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pandas as pd
    from deep_translator import GoogleTranslator
    from janome.tokenizer import Tokenizer


JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[。！？!?])\s+|\n+")
TAG_RE = re.compile(r"<[^>]+>")
BRACKET_ONLY_RE = re.compile(r"^[\(\[（【].*[\)\]）】]$")
JAPANESE_CHUNK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fffー]+")
MULTISPACE_RE = re.compile(r"\s+")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b-\x1f\x7f]")
HIRAGANA_KATAKANA_RE = re.compile(r"^[\u3040-\u30ffー]+$")
TIME_RE = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2}),\d{3}\s*-->\s*(?P<end>\d{2}:\d{2}:\d{2}),\d{3}"
)

FORM_PRIORITY = {"N3": 3, "N4": 2, "N5": 1}
POS_LABELS = {
    "名詞": "명사",
    "動詞": "동사",
    "形容詞": "형용사",
    "副詞": "부사",
    "連体詞": "연체사",
}


def configure_console_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


@dataclass(frozen=True)
class SubtitleLine:
    text: str
    start_time: str
    end_time: str


@dataclass(frozen=True)
class VocabEntry:
    surface: str
    reading: str
    meaning: str
    level: str
    source: str


@dataclass(frozen=True)
class GrammarEntry:
    label: str
    meaning: str
    level: str
    source: str
    keys: tuple[str, ...] = field(default_factory=tuple)
    regex: str | None = None


@dataclass(frozen=True)
class GrammarReference:
    label: str
    meaning: str
    example_jp: str
    example_ko: str
    category: str
    memo: str
    source: str


@dataclass(frozen=True)
class VocabMatch:
    entry: VocabEntry
    surface_in_sentence: str
    base_form: str
    pos: str


@dataclass(frozen=True)
class GrammarMatch:
    entry: GrammarEntry
    matched_texts: tuple[str, ...]
    category: str
    structure: str
    note: str
    example_jp: str = ""
    example_ko: str = ""

    @property
    def is_pattern(self) -> bool:
        return "문형" in self.category


@dataclass
class SentenceAnalysis:
    sentence: str
    translation: str
    vocab_matches: list[VocabMatch]
    grammar_matches: list[GrammarMatch]
    start_time: str = ""
    end_time: str = ""

    @property
    def n3_vocab(self) -> int:
        return sum(1 for item in self.vocab_matches if item.entry.level == "N3")

    @property
    def n3_grammar(self) -> int:
        return sum(1 for item in self.grammar_matches if item.entry.level == "N3")

    @property
    def grammar_weight(self) -> float:
        return sum(grammar_weight(item) for item in self.grammar_matches)

    @property
    def vocab_weight(self) -> float:
        return float(len(self.vocab_matches))

    @property
    def total_weight(self) -> float:
        return self.grammar_weight + self.vocab_weight


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = TAG_RE.sub("", text)
    text = text.replace("\ufeff", "")
    text = CONTROL_RE.sub("", text)
    text = MULTISPACE_RE.sub(" ", text)
    return text.strip()


def compact_japanese(text: str) -> str:
    return re.sub(r"\s+", "", normalize_text(text))


def has_japanese(text: str) -> bool:
    return bool(JAPANESE_RE.search(text))


def sanitize_filename(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|]+", "_", name)
    return name.strip(" ._") or "output"


def register_fonts() -> tuple[str, str]:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    font_candidates = [
        ("MalgunGothic", r"C:\Windows\Fonts\malgun.ttf"),
        ("YuGothic", r"C:\Windows\Fonts\YuGothM.ttc"),
        ("MSGothic", r"C:\Windows\Fonts\msgothic.ttc"),
    ]
    bold_candidates = [
        ("MalgunGothicBold", r"C:\Windows\Fonts\malgunbd.ttf"),
        ("YuGothic", r"C:\Windows\Fonts\YuGothM.ttc"),
        ("MSGothic", r"C:\Windows\Fonts\msgothic.ttc"),
    ]

    body_font = "Helvetica"
    bold_font = "Helvetica-Bold"

    for font_name, font_path in font_candidates:
        if Path(font_path).exists():
            try:
                pdfmetrics.registerFont(TTFont(font_name, font_path))
                body_font = font_name
                break
            except Exception:
                continue

    for font_name, font_path in bold_candidates:
        if Path(font_path).exists():
            try:
                pdfmetrics.registerFont(TTFont(font_name, font_path))
                bold_font = font_name
                break
            except Exception:
                continue

    return body_font, bold_font


def get_styles(body_font: str, bold_font: str):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleJP",
            parent=styles["Title"],
            fontName=bold_font,
            fontSize=18,
            leading=24,
            textColor=colors.HexColor("#17324d"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyJP",
            parent=styles["BodyText"],
            fontName=body_font,
            fontSize=10.5,
            leading=15,
            alignment=TA_LEFT,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SentenceJP",
            parent=styles["BodyText"],
            fontName=bold_font,
            fontSize=12,
            leading=18,
            alignment=TA_LEFT,
            spaceBefore=5,
            spaceAfter=4,
            textColor=colors.HexColor("#14213d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionJP",
            parent=styles["BodyText"],
            fontName=bold_font,
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#7a2e0b"),
            spaceBefore=2,
            spaceAfter=2,
        )
    )
    return styles


def load_csv(path: Path) -> pd.DataFrame:
    import pandas as pd
    return pd.read_csv(path, encoding="utf-8-sig").fillna("")


def extract_grammar_keys(expression: str) -> list[str]:
    text = compact_japanese(expression)
    text = (
        text.replace("〜", "")
        .replace("～", "")
        .replace("~", "")
        .replace("・", "")
        .replace("＋", "")
        .replace("+", "")
        .replace("…", "")
    )
    text = re.sub(r"[A-Za-z0-9\-_/\(\)\[\]\{\},.:]", "", text)
    text = re.sub(r"[「」『』]", "", text)
    chunks = JAPANESE_CHUNK_RE.findall(text)

    stop_words = {"ます", "です", "だ", "な", "の", "こと", "もの", "ひと"}
    results = []
    for chunk in chunks:
        if len(chunk) < 2:
            continue
        if chunk in stop_words:
            continue
        if len(chunk) < 3 and HIRAGANA_KATAKANA_RE.fullmatch(chunk):
            continue
        results.append(chunk)
    return list(dict.fromkeys(results))


def normalize_grammar_label(text: str) -> str:
    text = compact_japanese(text)
    text = text.replace("〜", "~").replace("～", "~")
    return text


def builtin_grammar() -> list[GrammarEntry]:
    raw = [
        ("〜たい", "~하고 싶다", "N5", r"[ぁ-んァ-ン一-龯]+たい"),
        ("〜ている", "~하고 있다 / ~해 있다", "N5", r"てい(?:る|た|ます|ました|ない|ません)"),
        ("〜てもいい", "~해도 된다", "N5", r"てもいい|てもかまわない"),
        ("〜てはいけない", "~하면 안 된다", "N5", r"てはいけない|ちゃいけない|ではいけない|じゃいけない"),
        ("〜つもり", "~할 생각이다", "N4", r"つもり(?:だ|です|で|だった)"),
        ("〜ことがある", "~한 적이 있다 / ~하는 경우가 있다", "N4", r"ことがある"),
        ("〜なければならない", "~해야 한다", "N4", r"なければならない|なくてはならない|なきゃ"),
        ("〜てみる", "~해 보다", "N4", r"てみ(?:る|た|ます|ました)"),
        ("〜ておく", "~해 두다", "N4", r"てお(?:く|いた|きます|きました)"),
        ("〜ように", "~하도록 / ~처럼", "N4", r"ように"),
        ("〜ために", "~하기 위해 / ~때문에", "N4", r"ために"),
        ("〜たり〜たりする", "~했다가 ~했다가 하다", "N4", r"たり.+たり"),
        ("〜ば", "~하면", "N4", r"[ぁ-んァ-ン一-龯]+(?:えば|けば|げば|せば|てば|ねば|べば|めば|れば)"),
        ("〜たら", "~하면", "N4", r"たら"),
        ("〜そうだ", "~일 것 같다 / ~라고 한다", "N4", r"そうだ"),
        ("〜らしい", "~인 것 같다 / ~답다", "N3", r"らしい"),
        ("〜ようだ", "~인 것 같다", "N3", r"ようだ"),
        ("〜ことになる", "~하게 되다", "N3", r"ことにな(?:る|った|ります|りました)"),
        ("〜ことにする", "~하기로 하다", "N3", r"ことにす(?:る|るよ|るね|るんだ|ること)"),
        ("〜わけだ", "~인 것이다 / 즉", "N3", r"わけだ|わけです"),
        ("〜はずだ", "~할 것이다 / 틀림없다", "N3", r"はずだ|はずです"),
        ("〜かもしれない", "~일지도 모른다", "N3", r"かもしれない|かもしれません"),
        ("〜てしまう", "~해 버리다", "N3", r"てしま(?:う|った|います|いました|うと)"),
        ("〜ながら", "~하면서", "N3", r"ながら"),
        ("〜ばかり", "~뿐 / 방금 ~했다", "N3", r"ばかり"),
        ("사역형", "시키다 / 하게 하다", "N3", r"[ぁ-んァ-ン一-龯]+(?:せる|させる)"),
        ("사역수동형", "억지로 ~하게 되다", "N3", r"[ぁ-んァ-ン一-龯]+(?:せられる|させられる)"),
        ("수동형", "~당하다 / ~되다", "N3", r"[ぁ-んァ-ン一-龯]+(?:れる|られる)"),
    ]
    return [GrammarEntry(label, meaning, level, "builtin", regex=regex) for label, meaning, level, regex in raw]


def grammar_meta(label: str, meaning: str) -> tuple[str, str, str]:
    checks = [
        (("させられる", "사역수동"), "사역수동형", "동사 사역형 + 수동형", "상대에게 강제로 어떤 행동을 하게 되는 형태다."),
        (("させる", "사역형"), "사역형", "동사 사역형", "누군가에게 어떤 행동을 시키거나 허락하는 의미로 쓴다."),
        (("られる", "受け身", "수동형"), "수동형", "동사 수동형", "행동을 당하거나 영향을 받는 흐름을 만든다."),
        (("たい",), "희망 표현", "동사 ます형 어간 + たい", "말하는 사람의 바람이나 의지를 나타낸다."),
        (("ている",), "진행/상태", "동사 て형 + いる", "현재 진행 중인 행동이나 결과 상태를 나타낸다."),
        (("たら",), "조건 표현", "동사/형용사 た형 + ら", "가정이나 계기를 나타내는 대표 조건형이다."),
        (("ば",), "조건 표현", "동사/형용사 ば형", "조건이 성립하면 뒤 문장이 이어지는 구조다."),
        (("そうだ",), "추측/전언", "기본형 또는 어간 + そうだ", "겉으로 보이는 추측이나 들은 내용을 전하는 데 쓴다."),
        (("らしい",), "추측/전형성", "보통형 + らしい", "근거 있는 추측 또는 그 대상다운 성질을 나타낸다."),
        (("ようだ",), "비유/추측", "보통형 + ようだ", "단정은 피하면서 비슷함이나 추측을 나타낸다."),
        (("ことになる",), "결정/귀결", "동사 사전형 + ことになる", "외부 결정이나 흐름으로 그렇게 정해졌음을 나타낸다."),
        (("ことにする",), "결정", "동사 사전형 + ことにする", "주체가 스스로 그렇게 하기로 정하는 표현이다."),
        (("わけだ",), "논리적 귀결", "보통형 + わけだ", "앞 내용에서 자연스럽게 도출되는 결론을 정리한다."),
        (("はずだ",), "예상/확신", "보통형 + はずだ", "상황상 그렇게 되는 것이 당연하다는 강한 예상을 보인다."),
        (("かもしれない",), "불확실 추측", "보통형 + かもしれない", "가능성을 조심스럽게 말할 때 쓴다."),
        (("てしまう",), "완료/유감", "동사 て형 + しまう", "끝내 버림, 아쉬움, 후회를 함께 담는 경우가 많다."),
        (("ながら",), "동시 진행", "동사 ます형 어간 + ながら", "두 행동이 동시에 진행됨을 보인다."),
        (("ばかり",), "한정/직후", "명사/동사 형태 + ばかり", "대상을 한정하거나 막 어떤 일이 끝났음을 말한다."),
    ]
    for keywords, category, structure, note in checks:
        if any(keyword in label for keyword in keywords):
            return category, structure, note
    return "문법 표현", label, meaning


def grammar_weight(match: GrammarMatch) -> float:
    label = match.entry.label
    category = match.category

    strong_keywords = (
        "사역수동",
        "사역형",
        "수동형",
        "ことになる",
        "ことにする",
        "わけだ",
        "はずだ",
        "かもしれない",
        "てしまう",
        "ようだ",
        "らしい",
        "ながら",
        "ばかり",
        "ために",
    )
    medium_keywords = (
        "たら",
        "ば",
        "ている",
        "そうだ",
        "つもり",
        "ことがある",
        "なければならない",
        "てみる",
        "ておく",
        "ように",
        "たり",
        "たい",
    )
    weak_keywords = ("なんか", "どうぞ", "だから", "いつも", "しか", "って", "でも", "とか")

    if any(keyword in label for keyword in strong_keywords):
        return 1.6
    if any(keyword in label for keyword in medium_keywords):
        return 1.0
    if any(keyword in label for keyword in weak_keywords):
        return 0.35
    if category in {"사역수동형", "사역형", "수동형"}:
        return 1.6
    if "문형" in category:
        return 0.7
    return 0.7


def load_reference_data(base_dir: Path) -> tuple[dict[str, list[VocabEntry]], list[GrammarEntry]]:
    ref_dir = base_dir / "_N3"
    vocab_index: dict[str, list[VocabEntry]] = {}
    grammar_entries: list[GrammarEntry] = []

    vocab_sources = [
        (ref_dir / "JLPT N3 단어.csv", "일본어 단어", "요미가나", "단어 뜻", "N3"),
        (ref_dir / "다락원 N3 기출단어.csv", "한자형태", "요미가나", "한글뜻", "N3"),
    ]

    seen_vocab: set[tuple[str, str]] = set()
    for path, surface_col, reading_col, meaning_col, level in vocab_sources:
        if not path.exists():
            continue
        df = load_csv(path)
        for row in df.to_dict(orient="records"):
            surface = normalize_text(str(row.get(surface_col, "")))
            reading = normalize_text(str(row.get(reading_col, "")))
            meaning = normalize_text(str(row.get(meaning_col, "")))
            if not surface or not meaning:
                continue
            if len(compact_japanese(surface)) < 2 and HIRAGANA_KATAKANA_RE.fullmatch(surface):
                continue
            dedupe_key = (surface, meaning)
            if dedupe_key in seen_vocab:
                continue
            seen_vocab.add(dedupe_key)
            entry = VocabEntry(surface, reading, meaning, level, path.name)
            for key in {surface, compact_japanese(surface), reading, compact_japanese(reading)}:
                if key:
                    vocab_index.setdefault(key, []).append(entry)

    grammar_files = [
        (ref_dir / "JLPT N3 문법.csv", "표현", "뜻"),
        (ref_dir / "JLPT N3 문형.csv", "문형", "문형 뜻"),
        (ref_dir / "JLPT N3 표현.csv", "표현", "뜻"),
    ]

    seen_grammar: set[tuple[str, str]] = set()
    for path, expr_col, meaning_col in grammar_files:
        if not path.exists():
            continue
        df = load_csv(path)
        for row in df.to_dict(orient="records"):
            label = normalize_text(str(row.get(expr_col, "")))
            meaning = normalize_text(str(row.get(meaning_col, "")))
            keys = tuple(extract_grammar_keys(label))
            if not label or not meaning or not keys:
                continue
            dedupe_key = (label, meaning)
            if dedupe_key in seen_grammar:
                continue
            seen_grammar.add(dedupe_key)
            grammar_entries.append(GrammarEntry(label, meaning, "N3", path.name, keys=keys))

    grammar_entries.extend(builtin_grammar())
    return vocab_index, grammar_entries


def load_hackers_grammar_reference(base_dir: Path) -> dict[str, GrammarReference]:
    ref_dir = base_dir / "_N3"
    txt_files = [path for path in ref_dir.iterdir() if path.suffix.lower() == ".txt"]
    references: dict[str, GrammarReference] = {}
    if not txt_files:
        return references

    lines = txt_files[0].read_text(encoding="utf-8-sig").splitlines()[3:]
    for row in csv.reader(lines, delimiter="\t"):
        if len(row) != 13:
            continue
        label = normalize_text(row[0] or row[2])
        meaning = normalize_text(row[3])
        example_jp = normalize_text(row[4])
        example_ko = normalize_text(row[6])
        category = normalize_text(row[9]).strip("[]")
        memo = normalize_text(row[10])
        source = normalize_text(row[12])
        if not label or not meaning:
            continue
        references[normalize_grammar_label(label)] = GrammarReference(
            label=label,
            meaning=meaning,
            example_jp=example_jp,
            example_ko=example_ko,
            category=category,
            memo=memo,
            source=source,
        )
    return references


def get_database_path(base_dir: Path) -> Path:
    return base_dir / "_N3" / "jlpt_n3_cache.sqlite3"


def get_reference_source_paths(base_dir: Path) -> list[Path]:
    ref_dir = base_dir / "_N3"
    paths = [
        ref_dir / "JLPT N3 단어.csv",
        ref_dir / "다락원 N3 기출단어.csv",
        ref_dir / "JLPT N3 문법.csv",
        ref_dir / "JLPT N3 문형.csv",
        ref_dir / "JLPT N3 표현.csv",
    ]
    paths.extend(path for path in ref_dir.iterdir() if path.suffix.lower() == ".txt")
    return [path for path in paths if path.exists()]


def build_reference_database(base_dir: Path) -> Path:
    db_path = get_database_path(base_dir)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    vocab_index, grammar_entries = load_reference_data(base_dir)
    hackers_reference = load_hackers_grammar_reference(base_dir)

    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.executescript(
            """
            CREATE TABLE meta (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            CREATE TABLE vocab_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                surface TEXT NOT NULL,
                reading TEXT NOT NULL,
                meaning TEXT NOT NULL,
                level TEXT NOT NULL,
                source TEXT NOT NULL
            );
            CREATE TABLE vocab_keys (
                key_text TEXT NOT NULL,
                vocab_id INTEGER NOT NULL
            );
            CREATE INDEX idx_vocab_keys_key_text ON vocab_keys(key_text);
            CREATE TABLE grammar_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                label TEXT NOT NULL,
                meaning TEXT NOT NULL,
                level TEXT NOT NULL,
                source TEXT NOT NULL,
                regex TEXT,
                keys_text TEXT NOT NULL
            );
            CREATE TABLE grammar_references (
                normalized_label TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                meaning TEXT NOT NULL,
                example_jp TEXT NOT NULL,
                example_ko TEXT NOT NULL,
                category TEXT NOT NULL,
                memo TEXT NOT NULL,
                source TEXT NOT NULL
            );
            """
        )

        source_paths = get_reference_source_paths(base_dir)
        newest_mtime = max((path.stat().st_mtime for path in source_paths), default=0.0)
        cur.executemany(
            "INSERT INTO meta(key, value) VALUES (?, ?)",
            [
                ("built_at", datetime.now().isoformat(timespec="seconds")),
                ("source_mtime", str(newest_mtime)),
            ],
        )

        vocab_id_map: dict[tuple[str, str, str, str, str], int] = {}
        for entries in vocab_index.values():
            for entry in entries:
                row = (entry.surface, entry.reading, entry.meaning, entry.level, entry.source)
                if row in vocab_id_map:
                    continue
                cur.execute(
                    """
                    INSERT INTO vocab_entries(surface, reading, meaning, level, source)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    row,
                )
                vocab_id_map[row] = int(cur.lastrowid)

        seen_links: set[tuple[str, int]] = set()
        for key_text, entries in vocab_index.items():
            for entry in entries:
                vocab_id = vocab_id_map[(entry.surface, entry.reading, entry.meaning, entry.level, entry.source)]
                link = (key_text, vocab_id)
                if link in seen_links:
                    continue
                seen_links.add(link)
                cur.execute("INSERT INTO vocab_keys(key_text, vocab_id) VALUES (?, ?)", link)

        seen_grammar_rows: set[tuple[str, str, str, str, str | None, str]] = set()
        for entry in grammar_entries:
            row = (entry.label, entry.meaning, entry.level, entry.source, entry.regex, "\u241f".join(entry.keys))
            if row in seen_grammar_rows:
                continue
            seen_grammar_rows.add(row)
            cur.execute(
                """
                INSERT INTO grammar_entries(label, meaning, level, source, regex, keys_text)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                row,
            )

        for normalized_label, ref in hackers_reference.items():
            cur.execute(
                """
                INSERT INTO grammar_references(
                    normalized_label, label, meaning, example_jp, example_ko, category, memo, source
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    normalized_label,
                    ref.label,
                    ref.meaning,
                    ref.example_jp,
                    ref.example_ko,
                    ref.category,
                    ref.memo,
                    ref.source,
                ),
            )

        conn.commit()
    finally:
        conn.close()

    return db_path


def ensure_reference_database(base_dir: Path, force_rebuild: bool = False) -> Path:
    db_path = get_database_path(base_dir)
    newest_mtime = max((path.stat().st_mtime for path in get_reference_source_paths(base_dir)), default=0.0)
    rebuild = force_rebuild or not db_path.exists()
    if not rebuild and db_path.stat().st_mtime < newest_mtime:
        rebuild = True
    if rebuild:
        build_reference_database(base_dir)
    return db_path


def load_reference_data_from_database(
    base_dir: Path,
) -> tuple[dict[str, list[VocabEntry]], list[GrammarEntry], dict[str, GrammarReference]]:
    db_path = ensure_reference_database(base_dir)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        vocab_index: dict[str, list[VocabEntry]] = {}
        for row in conn.execute(
            """
            SELECT vk.key_text, ve.surface, ve.reading, ve.meaning, ve.level, ve.source
            FROM vocab_keys vk
            JOIN vocab_entries ve ON ve.id = vk.vocab_id
            ORDER BY vk.key_text, ve.level DESC, ve.surface
            """
        ):
            entry = VocabEntry(row["surface"], row["reading"], row["meaning"], row["level"], row["source"])
            vocab_index.setdefault(row["key_text"], []).append(entry)

        grammar_entries: list[GrammarEntry] = []
        for row in conn.execute(
            """
            SELECT label, meaning, level, source, regex, keys_text
            FROM grammar_entries
            ORDER BY level DESC, label
            """
        ):
            keys = tuple(part for part in str(row["keys_text"]).split("\u241f") if part)
            grammar_entries.append(
                GrammarEntry(
                    label=row["label"],
                    meaning=row["meaning"],
                    level=row["level"],
                    source=row["source"],
                    regex=row["regex"],
                    keys=keys,
                )
            )

        hackers_reference: dict[str, GrammarReference] = {}
        for row in conn.execute(
            """
            SELECT normalized_label, label, meaning, example_jp, example_ko, category, memo, source
            FROM grammar_references
            """
        ):
            hackers_reference[row["normalized_label"]] = GrammarReference(
                label=row["label"],
                meaning=row["meaning"],
                example_jp=row["example_jp"],
                example_ko=row["example_ko"],
                category=row["category"],
                memo=row["memo"],
                source=row["source"],
            )
    finally:
        conn.close()
    return vocab_index, grammar_entries, hackers_reference


def parse_srt(path: Path) -> list[SubtitleLine]:
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    blocks = re.split(r"\r?\n\r?\n+", text.strip())
    entries: list[SubtitleLine] = []
    for block in blocks:
        lines = [normalize_text(line) for line in block.splitlines() if normalize_text(line)]
        if len(lines) < 3:
            continue
        match = TIME_RE.match(lines[1])
        if not match:
            continue
        content = normalize_text(html.unescape(" ".join(lines[2:])))
        if not content or not has_japanese(content):
            continue
        if BRACKET_ONLY_RE.match(content) and len(content) <= 30:
            continue
        entries.append(SubtitleLine(content, match.group("start"), match.group("end")))
    return entries


def split_sentences(lines: list[SubtitleLine]) -> list[SubtitleLine]:
    results: list[SubtitleLine] = []
    for line in lines:
        parts = [normalize_text(part) for part in SENTENCE_SPLIT_RE.split(line.text) if normalize_text(part)]
        for part in parts:
            if has_japanese(part):
                results.append(SubtitleLine(part, line.start_time, line.end_time))
    return results


def translate_sentences(sentences: list[str], translator: GoogleTranslator | None) -> dict[str, str]:
    if translator is None:
        return {sentence: "(자동 번역 비활성화)" for sentence in sentences}

    import time
    translations: dict[str, str] = {}
    chunk_size = 40
    total_sentences = len(sentences)
    if total_sentences == 0:
        return translations

    print(f" -> 구글 번역 시작: 총 {total_sentences}개 문장 번역 요청 중...")

    for start in range(0, total_sentences, chunk_size):
        end = min(start + chunk_size, total_sentences)
        chunk = sentences[start:end]
        print(f"    - 번역 진행 상황: {end}/{total_sentences} 문장 완료...")
        try:
            results = translator.translate_batch(chunk)
            for sentence, translated in zip(chunk, results):
                translations[sentence] = normalize_text(str(translated))
            time.sleep(3)  # 배치 요청 간 3초 대기
        except Exception:
            print("    [경고] 배치 번역 실패. 개별 문장 번역으로 대체합니다...")
            for sentence in chunk:
                try:
                    translations[sentence] = normalize_text(translator.translate(sentence))
                    time.sleep(1)  # 개별 번역 건당 1초 대기
                except Exception as exc:
                    translations[sentence] = f"(자동 번역 실패: {exc.__class__.__name__})"
    print(" -> 번역 완료!")
    return translations


def analyze_sentence(
    sentence: str,
    translation_map: dict[str, str],
    tokenizer: Tokenizer,
    vocab_index: dict[str, list[VocabEntry]],
    grammar_entries: list[GrammarEntry],
    hackers_reference: dict[str, GrammarReference],
) -> SentenceAnalysis | None:
    compact_sentence = compact_japanese(sentence)
    tokens = list(tokenizer.tokenize(sentence))

    vocab_matches: list[VocabMatch] = []
    seen_vocab: set[tuple[str, str]] = set()
    for token in tokens:
        pos = token.part_of_speech.split(",")[0]
        if pos not in {"名詞", "動詞", "形容詞", "副詞", "連体詞"}:
            continue

        token_surface = normalize_text(token.surface)
        base_form = normalize_text(token.base_form if token.base_form != "*" else token.surface)
        reading = normalize_text(token.reading if token.reading != "*" else "")
        keys = [
            token_surface,
            compact_japanese(token_surface),
            base_form,
            compact_japanese(base_form),
            reading,
            compact_japanese(reading),
        ]
        for key in keys:
            if not key:
                continue
            for entry in vocab_index.get(key, []):
                dedupe_key = (entry.surface, entry.meaning)
                if dedupe_key in seen_vocab:
                    continue
                seen_vocab.add(dedupe_key)
                vocab_matches.append(
                    VocabMatch(
                        entry=entry,
                        surface_in_sentence=token_surface,
                        base_form=base_form,
                        pos=POS_LABELS.get(pos, pos),
                    )
                )

    grammar_matches: list[GrammarMatch] = []
    seen_grammar: set[str] = set()
    for entry in grammar_entries:
        matched_texts: list[str] = []
        if entry.regex:
            matched_texts = list(dict.fromkeys(re.findall(entry.regex, compact_sentence)))
        elif entry.keys and all(key in compact_sentence for key in entry.keys):
            matched_texts = list(entry.keys)

        if matched_texts and entry.label not in seen_grammar:
            seen_grammar.add(entry.label)
            ref = hackers_reference.get(normalize_grammar_label(entry.label))
            category, structure, note = grammar_meta(entry.label, entry.meaning)
            if ref:
                category = ref.category or category
                note = ref.memo or note
            grammar_matches.append(
                GrammarMatch(
                    entry=entry,
                    matched_texts=tuple(matched_texts[:3]),
                    category=category,
                    structure=structure,
                    note=note,
                    example_jp=ref.example_jp if ref else "",
                    example_ko=ref.example_ko if ref else "",
                )
            )

    if not vocab_matches and not grammar_matches:
        return None

    vocab_matches.sort(key=lambda item: (-FORM_PRIORITY.get(item.entry.level, 0), item.entry.surface))
    grammar_matches.sort(key=lambda item: (-FORM_PRIORITY.get(item.entry.level, 0), item.entry.label))
    return SentenceAnalysis(
        sentence=sentence,
        translation=translation_map.get(sentence, "(번역 없음)"),
        vocab_matches=vocab_matches[:10],
        grammar_matches=grammar_matches[:8],
    )


def should_include(analysis: SentenceAnalysis) -> bool:
    return (
        (analysis.n3_grammar >= 1 and analysis.n3_vocab >= 1)
        or (analysis.grammar_weight >= 1.5 and analysis.vocab_weight >= 2)
        or (analysis.total_weight >= 3.0)
    )


def escape_pdf_text(text: str) -> str:
    return html.escape(text).replace("\n", "<br/>")


def seconds_from_hhmmss(value: str) -> int:
    hours, minutes, seconds = map(int, value.split(":"))
    return hours * 3600 + minutes * 60 + seconds


def hhmmss_from_seconds(value: int) -> str:
    value = max(0, value)
    hours = value // 3600
    minutes = (value % 3600) // 60
    seconds = value % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def apply_sync_offset(timestamp: str, offset_seconds: int) -> str:
    return hhmmss_from_seconds(seconds_from_hhmmss(timestamp) + offset_seconds)


def highlight_sentence(sentence: str, analysis: SentenceAnalysis) -> str:
    marks: list[tuple[str, str]] = []
    for item in analysis.grammar_matches:
        for text in item.matched_texts:
            if text and len(text) >= 2:
                marks.append((text, "#b54708"))
    for item in analysis.vocab_matches:
        text = item.surface_in_sentence or item.entry.surface
        if text:
            marks.append((text, "#1d4ed8"))

    escaped = escape_pdf_text(sentence)
    for text, color in sorted(set(marks), key=lambda pair: (len(pair[0]), pair[0]), reverse=True):
        escaped_text = html.escape(text)
        escaped = re.sub(
            re.escape(escaped_text),
            f'<font color="{color}"><b>{escaped_text}</b></font>',
            escaped,
            count=0,
        )
    return escaped


def build_vocab_lines(analysis: SentenceAnalysis) -> str:
    grouped: dict[tuple[str, str], list[str]] = {}
    order: list[tuple[str, str]] = []

    for item in analysis.vocab_matches:
        key = (item.entry.surface, item.entry.reading)
        if key not in grouped:
            grouped[key] = []
            order.append(key)

        meanings = [part.strip() for part in re.split(r"[,/;]\s*|,\s*| · ", item.entry.meaning) if part.strip()]
        if not meanings:
            meanings = [item.entry.meaning.strip()]
        for meaning in meanings:
            if meaning and meaning not in grouped[key]:
                grouped[key].append(meaning)

    lines = []
    for surface, reading in order:
        lines.append(
            f'- <font color="#1d4ed8"><b>{escape_pdf_text(surface)}</b></font> '
            f'({escape_pdf_text(reading)}) - {escape_pdf_text(", ".join(grouped[(surface, reading)]))}'
        )
    return "<br/>".join(lines)


def build_grammar_lines(analysis: SentenceAnalysis) -> str:
    grammar_items = [item for item in analysis.grammar_matches if not item.is_pattern]
    lines = []
    for item in grammar_items:
        lines.append(
            f'- <font color="#b54708"><b>{escape_pdf_text(item.entry.label)}</b></font> - '
            f'{escape_pdf_text(item.entry.meaning)} | {escape_pdf_text(item.category)}'
        )
    return "<br/>".join(lines)


def build_pattern_lines(analysis: SentenceAnalysis) -> str:
    pattern_items = [item for item in analysis.grammar_matches if item.is_pattern]
    lines = []
    for item in pattern_items:
        lines.append(
            f'- <font color="#b54708"><b>{escape_pdf_text(item.entry.label)}</b></font> - '
            f'{escape_pdf_text(item.entry.meaning)} | {escape_pdf_text(item.category)}'
        )
    return "<br/>".join(lines)


def render_sentence_line(index: int, analysis: SentenceAnalysis, with_timestamp: bool, sync_seconds: int) -> str:
    sentence_html = highlight_sentence(analysis.sentence, analysis)
    if with_timestamp and analysis.start_time:
        adjusted = apply_sync_offset(analysis.start_time, sync_seconds)
        sentence_html += f' <font size="8" color="#6b7280">[{escape_pdf_text(adjusted)}]</font>'
    return f"{index}. {sentence_html}"


def build_story(source_file: Path, analyses: list[SentenceAnalysis], styles, with_timestamp: bool, sync_seconds: int) -> list:
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, Spacer
    story = []
    title = f"{source_file.stem} JLPT N3 학습 노트"
    story.append(Paragraph(escape_pdf_text(title), styles["TitleJP"]))
    story.append(Spacer(1, 3 * mm))

    for index, analysis in enumerate(analyses, start=1):
        story.append(Paragraph(render_sentence_line(index, analysis, with_timestamp, sync_seconds), styles["SentenceJP"]))
        translation_html = f'<font color="#7a2e0b"><b>해석:</b></font> {escape_pdf_text(analysis.translation)}'
        story.append(Paragraph(translation_html, styles["BodyJP"]))

        vocab_lines = build_vocab_lines(analysis)
        grammar_lines = build_grammar_lines(analysis)
        pattern_lines = build_pattern_lines(analysis)

        if vocab_lines:
            story.append(Paragraph("단어", styles["SectionJP"]))
            story.append(Paragraph(vocab_lines, styles["BodyJP"]))
        if grammar_lines:
            story.append(Paragraph("문법", styles["SectionJP"]))
            story.append(Paragraph(grammar_lines, styles["BodyJP"]))
        if pattern_lines:
            story.append(Paragraph("문형", styles["SectionJP"]))
            story.append(Paragraph(pattern_lines, styles["BodyJP"]))

        story.append(Spacer(1, 4 * mm))
    return story


def build_sync_check_story(source_file: Path, lines: list[SubtitleLine], translations: dict[str, str], styles) -> list:
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, Spacer
    story = []
    title = f"{source_file.stem} Sync Check"
    story.append(Paragraph(escape_pdf_text(title), styles["TitleJP"]))
    story.append(Spacer(1, 3 * mm))

    for index, line in enumerate(lines, start=1):
        sentence = escape_pdf_text(line.text)
        stamp = f'<font size="8" color="#6b7280">[{escape_pdf_text(line.start_time)}]</font>'
        story.append(Paragraph(f"{index}. {sentence} {stamp}", styles["SentenceJP"]))
        translation_html = f'<font color="#7a2e0b"><b>해석:</b></font> {escape_pdf_text(translations.get(line.text, "(번역 없음)"))}'
        story.append(Paragraph(translation_html, styles["BodyJP"]))
        story.append(Spacer(1, 3 * mm))
    return story


def save_pdf(output_path: Path, story: list) -> Path:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.platypus import SimpleDocTemplate
    output_path.parent.mkdir(parents=True, exist_ok=True)

    target_path = output_path
    if target_path.exists():
        try:
            with target_path.open("ab"):
                pass
        except PermissionError:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            target_path = target_path.with_name(f"{target_path.stem}_updated_{timestamp}{target_path.suffix}")

    doc = SimpleDocTemplate(
        str(target_path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title=target_path.stem,
        author="Codex",
    )
    doc.build(story)
    return target_path


def analyze_file(
    source_file: Path,
    output_dir: Path,
    tokenizer: Tokenizer,
    vocab_index: dict[str, list[VocabEntry]],
    grammar_entries: list[GrammarEntry],
    hackers_reference: dict[str, GrammarReference],
    translator: GoogleTranslator | None,
    styles,
    max_sentences: int,
    sync_seconds: int,
) -> tuple[list[Path], int]:
    print(f"\n[{source_file.name}] 파일 분석 시작...")
    raw_lines = parse_srt(source_file)
    split_lines = split_sentences(raw_lines)
    unique_lines = list(dict.fromkeys((line.text, line.start_time, line.end_time) for line in split_lines))
    subtitle_lines = [SubtitleLine(text, start, end) for text, start, end in unique_lines]
    print(f" -> 자막 파싱 완료: 총 {len(subtitle_lines)}개 일본어 문장 추출")

    # 번역을 수행하기 전에 N3 필터링 조건에 부합하는 대상 문장들만 먼저 추출합니다.
    analyses: list[SentenceAnalysis] = []
    for line in subtitle_lines:
        analysis = analyze_sentence(line.text, {}, tokenizer, vocab_index, grammar_entries, hackers_reference)
        if analysis and should_include(analysis):
            analysis.start_time = line.start_time
            analysis.end_time = line.end_time
            analyses.append(analysis)

    print(f" -> N3 기준 매칭 완료: 총 {len(analyses)}개 문장 최종 매칭됨")

    if max_sentences > 0:
        analyses = analyses[:max_sentences]
        print(f" -> 최대 출력 개수 제한 적용: 상위 {len(analyses)}개 문장 선택")

    # 필터링 및 개수 제한이 완료된 문장들에 대해서만 번역 요청을 전송합니다.
    sentences_to_translate = [analysis.sentence for analysis in analyses]
    translation_map = translate_sentences(sentences_to_translate, translator)

    # 번역 결과를 분석 객체에 다시 할당합니다.
    for analysis in analyses:
        analysis.translation = translation_map.get(analysis.sentence, "(번역 없음)")

    suffix = "_N3"
    if max_sentences > 0:
        suffix += f"_top{max_sentences}"

    print(" -> PDF 파일 저장 중...")
    base_output = output_dir / sanitize_filename(f"{source_file.stem}{suffix}.pdf")
    time_output = output_dir / sanitize_filename(f"{source_file.stem}{suffix}_timestamp.pdf")
    saved_plain = save_pdf(base_output, build_story(source_file, analyses, styles, with_timestamp=False, sync_seconds=sync_seconds))
    saved_time = save_pdf(time_output, build_story(source_file, analyses, styles, with_timestamp=True, sync_seconds=sync_seconds))
    return [saved_plain, saved_time], len(analyses)


def build_sync_check_pdf(
    source_file: Path,
    output_dir: Path,
    translator: GoogleTranslator | None,
    styles,
    minutes: int = 3,
) -> Path:
    raw_lines = parse_srt(source_file)
    if not raw_lines:
        raise ValueError(f"No subtitle lines found in {source_file.name}")

    limit_seconds = minutes * 60
    selected_lines = [line for line in raw_lines if seconds_from_hhmmss(line.start_time) < limit_seconds]
    unique_lines = list(dict.fromkeys((line.text, line.start_time, line.end_time) for line in selected_lines))
    subtitle_lines = [SubtitleLine(text, start, end) for text, start, end in unique_lines]
    translations = translate_sentences([line.text for line in subtitle_lines], translator)

    output_path = output_dir / sanitize_filename(f"{source_file.stem}_sync_check.pdf")
    return save_pdf(output_path, build_sync_check_story(source_file, subtitle_lines, translations, styles))


def list_subtitle_files(input_dir: Path) -> list[Path]:
    return sorted(input_dir.glob("*.srt"))


def print_file_menu(files: list[Path]) -> None:
    print("처리할 파일을 선택하세요.")
    print("0. 전부 처리")
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path.name}")


def parse_file_selection(raw: str, files: list[Path]) -> list[Path]:
    raw = raw.strip()
    if not raw:
        raise ValueError("번호를 입력해야 합니다.")
    if raw == "0":
        return files

    selected_indexes: list[int] = []
    for part in raw.split(","):
        token = part.strip()
        if not token:
            continue
        value = int(token)
        if value < 1 or value > len(files):
            raise ValueError(f"잘못된 번호: {value}")
        if value not in selected_indexes:
            selected_indexes.append(value)
    return [files[index - 1] for index in selected_indexes]


def prompt_file_selection(files: list[Path]) -> list[Path]:
    print_file_menu(files)
    while True:
        try:
            raw = input("번호 입력: ")
            return parse_file_selection(raw, files)
        except Exception as exc:
            print(f"다시 입력해 주세요: {exc}")


def parse_sync_value(raw: str) -> int:
    text = raw.strip()
    if not text:
        return 0
    return int(text)


def find_sync_offset_from_input(srt_path: Path, raw_input: str) -> int | False | None:
    import re
    import difflib
    
    # "2:34 이거 보는 거야?" -> time="2:34", text="이거 보는 거야?"
    time_prefix_re = re.compile(r"^(?P<time>(?:\d{1,2}:)?\d{1,2}:\d{2})\s+(?P<text>.+)$")
    match = time_prefix_re.match(raw_input.strip())
    if not match:
        return None

    time_str = match.group("time")
    target_text = match.group("text").strip()

    # Parse HH:MM:SS or MM:SS
    parts = list(map(int, time_str.split(":")))
    if len(parts) == 2:
        video_seconds = parts[0] * 60 + parts[1]
    elif len(parts) == 3:
        video_seconds = parts[0] * 3600 + parts[1] * 60 + parts[2]
    else:
        return None

    try:
        raw_lines = parse_srt(srt_path)
        split_lines = split_sentences(raw_lines)
        unique_lines = list(dict.fromkeys((line.text, line.start_time, line.end_time) for line in split_lines))
        subtitle_lines = [SubtitleLine(text, start, end) for text, start, end in unique_lines]
    except Exception as e:
        print(f"[오류] 자막 파일을 읽을 수 없습니다: {e}")
        return False

    if not subtitle_lines:
        print("[경고] 자막 파일에 문장이 없습니다.")
        return False

    search_key = target_text
    if not has_japanese(target_text):
        print(f" -> 입력 대사 번역 중 ('{target_text}' -> 일본어)...")
        try:
            from deep_translator import GoogleTranslator
            search_key = GoogleTranslator(source="ko", target="ja").translate(target_text)
            print(f" -> 번역 결과: '{search_key}'")
        except Exception as e:
            print(f" -> [경고] 번역에 실패하여 입력한 텍스트 그대로 매칭을 시도합니다. ({e})")

    def clean_text(t: str) -> str:
        # 1. 괄호 내용(화자 태그, 지문 등)을 통째로 제거: (반자와), （面接官）, [비명] 등
        t = re.sub(r"\([^)]*\)", "", t)
        t = re.sub(r"（[^）]*）", "", t)
        t = re.sub(r"\[[^\]]*\]", "", t)
        t = re.sub(r"【[^】]*】", "", t)
        # 2. ≪ ≫ ➡ → ← 같은 닫힌 자막 특수 문자 제거
        t = re.sub(r"[≪≫➡→←]", "", t)
        # 3. 띄어쓰기 제거
        t = compact_japanese(t)
        # 4. 문장 부호 제거
        t = re.sub(r"[?？!！.。,、・~〜()（）\[\]【】_\"'`+\-*]", "", t)
        return t

    clean_search_key = clean_text(search_key)
    best_match = None
    best_ratio = 0.0

    for line in subtitle_lines:
        clean_line = clean_text(line.text)
        ratio = difflib.SequenceMatcher(None, clean_search_key, clean_line).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = line

    if best_match and best_ratio >= 0.4:
        sub_seconds = seconds_from_hhmmss(best_match.start_time)
        offset = video_seconds - sub_seconds
        print(f"\n[유사도 {best_ratio:.1%}] 가장 일치하는 자막을 찾았습니다:")
        print(f"  - 원본 자막: {best_match.text}")
        print(f"  - 원래 시간: {best_match.start_time} ({sub_seconds}초)")
        print(f"  - 영상 시간: {time_str} ({video_seconds}초)")
        print(f"  - 계산된 싱크 편차: {offset:+d}초")
        
        confirm = input(f"  이 싱크 값({offset:+d}초)을 적용하시겠습니까? (Y/n, 엔터=Y): ").strip().lower()
        if confirm in ("", "y", "yes"):
            return offset
        else:
            return False
    else:
        print(f"\n[실패] 유사한 자막을 찾지 못했습니다. (최대 유사도: {best_ratio:.1%})")
        print("  대사 내용에 화자 이름이나 특수 문자가 들어있다면 이를 빼고 다시 입력해 보세요.")
        print("  또는 다른 명확하고 긴 대사로 다시 입력해 주시기 바랍니다.")
        return False


def prompt_sync_for_files(selected_files: list[Path], all_selected: bool) -> dict[Path, int]:
    sync_map: dict[Path, int] = {}
    if all_selected:
        while True:
            raw = input("적용할 sync 값은? (초 단위 예: +120, 또는 '시간 대사' 입력으로 자동 계산, 엔터=0): ")
            res = find_sync_offset_from_input(selected_files[0], raw)
            if res is False:
                continue
            if res is not None:
                sync_value = res
                break
            try:
                sync_value = parse_sync_value(raw)
                break
            except Exception as e:
                print(f"올바른 숫자를 입력하거나 '분:초 대사' 형식으로 입력하세요.")
        
        for path in selected_files:
            sync_map[path] = sync_value
        return sync_map

    if len(selected_files) == 1:
        while True:
            raw = input("적용할 sync 값은? (초 단위 예: +120, 또는 '시간 대사' 입력으로 자동 계산, 엔터=0): ")
            res = find_sync_offset_from_input(selected_files[0], raw)
            if res is False:
                continue
            if res is not None:
                sync_value = res
                break
            try:
                sync_value = parse_sync_value(raw)
                break
            except Exception as e:
                print(f"올바른 숫자를 입력하거나 '분:초 대사' 형식으로 입력하세요.")
        sync_map[selected_files[0]] = sync_value
        return sync_map

    print("여러 파일이 선택되어 파일별 sync 값을 입력합니다. 엔터는 0초입니다.")
    for path in selected_files:
        while True:
            raw = input(f"{path.name} sync 값 (또는 '시간 대사' 입력): ")
            res = find_sync_offset_from_input(path, raw)
            if res is False:
                continue
            if res is not None:
                sync_value = res
                break
            try:
                sync_value = parse_sync_value(raw)
                break
            except Exception as e:
                print(f"올바른 숫자를 입력하거나 '분:초 대사' 형식으로 입력하세요.")
        sync_map[path] = sync_value
    return sync_map


def process_selected_files(
    files: list[Path],
    input_dir: Path,
    output_dir: Path,
    disable_translation: bool,
    rebuild_db: bool,
    max_sentences: int,
    sync_map: dict[Path, int],
) -> list[tuple[str, str, int]]:
    print("\n[작업 중] 데이터를 로드하고 PDF 생성을 시작합니다. 잠시만 기다려 주세요...")
    base_dir = input_dir.parent
    ensure_reference_database(base_dir, force_rebuild=rebuild_db)
    vocab_index, grammar_entries, hackers_reference = load_reference_data_from_database(base_dir)
    print(" -> N3 기준 사전 데이터베이스 로드 완료.")
    from janome.tokenizer import Tokenizer
    from deep_translator import GoogleTranslator
    tokenizer = Tokenizer()
    translator = None if disable_translation else GoogleTranslator(source="ja", target="ko")
    body_font, bold_font = register_fonts()
    styles = get_styles(body_font, bold_font)
    print(" -> 형태소 분석기 및 번역기 초기화 완료.")

    summary_rows: list[tuple[str, str, int]] = []
    for path in files:
        output_paths, count = analyze_file(
            source_file=path,
            output_dir=output_dir,
            tokenizer=tokenizer,
            vocab_index=vocab_index,
            grammar_entries=grammar_entries,
            hackers_reference=hackers_reference,
            translator=translator,
            styles=styles,
            max_sentences=max_sentences,
            sync_seconds=sync_map.get(path, 0),
        )
        print(
            f"[done] {path.name} -> "
            + ", ".join(output_path.name for output_path in output_paths)
            + f" ({count} sentences)"
        )
        for output_path in output_paths:
            summary_rows.append((path.name, output_path.name, count))
    return summary_rows



def interactive_main(args: argparse.Namespace) -> int:
    base_dir = Path(__file__).resolve().parent
    input_dir = (base_dir / args.input_dir).resolve()
    output_dir = (base_dir / args.output_dir).resolve()

    if not input_dir.exists():
        print(f"Input directory does not exist: {input_dir}", file=sys.stderr)
        return 1

    files = list_subtitle_files(input_dir)
    if not files:
        print(f"No .srt files found in: {input_dir}", file=sys.stderr)
        return 1

    selected_files = prompt_file_selection(files)
    sync_map = prompt_sync_for_files(selected_files, len(selected_files) == len(files))

    process_selected_files(
        files=selected_files,
        input_dir=input_dir,
        output_dir=output_dir,
        disable_translation=args.disable_translation,
        rebuild_db=args.rebuild_db,
        max_sentences=args.max_sentences,
        sync_map=sync_map,
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate JLPT N3 study PDFs from Japanese subtitle files.")
    parser.add_argument("--input-dir", default="input_script")
    parser.add_argument("--output-dir", default="output_pdf")
    parser.add_argument("--max-sentences", type=int, default=0)
    parser.add_argument("--disable-translation", action="store_true")
    parser.add_argument("--rebuild-db", action="store_true")
    parser.add_argument("--selection", help="0 for all, or comma-separated file numbers")
    parser.add_argument("--sync", help="Common sync offset in seconds for non-interactive mode")
    parser.add_argument("--non-interactive", action="store_true")
    return parser.parse_args()


def non_interactive_main(args: argparse.Namespace) -> int:
    base_dir = Path(__file__).resolve().parent
    input_dir = (base_dir / args.input_dir).resolve()
    output_dir = (base_dir / args.output_dir).resolve()

    if not input_dir.exists():
        print(f"Input directory does not exist: {input_dir}", file=sys.stderr)
        return 1

    files = list_subtitle_files(input_dir)
    if not files:
        print(f"No .srt files found in: {input_dir}", file=sys.stderr)
        return 1

    selection = args.selection or "0"
    selected_files = parse_file_selection(selection, files)
    common_sync = parse_sync_value(args.sync or "")
    sync_map = {path: common_sync for path in selected_files}

    process_selected_files(
        files=selected_files,
        input_dir=input_dir,
        output_dir=output_dir,
        disable_translation=args.disable_translation,
        rebuild_db=args.rebuild_db,
        max_sentences=args.max_sentences,
        sync_map=sync_map,
    )
    return 0


def main() -> int:
    configure_console_output()
    args = parse_args()
    
    is_interactive = not (args.non_interactive or args.selection is not None or args.sync is not None)
    exit_code = 0
    try:
        if not is_interactive:
            exit_code = non_interactive_main(args)
        else:
            exit_code = interactive_main(args)
            
        if exit_code == 0:
            print("\n[완료] 모든 작업이 완료되었습니다.")
        else:
            print("\n[실패] 작업 중 오류가 발생했습니다.")
    except Exception as e:
        print(f"\n[오류] 예외가 발생했습니다: {e}")
        exit_code = 1
    finally:
        if is_interactive:
            input("\n엔터를 누르면 창이 닫힙니다...")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
