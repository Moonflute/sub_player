from __future__ import annotations

import json
import random
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SOURCE_DIR = BASE_DIR / "_N3"
OUTPUT = BASE_DIR / "_jlpt source refined" / "grammar" / "n3_grammar_quiz.json"
BLANK = "（　）"
VARIANTS_PER_POINT = 4

SECTION_ORDER = [
    ("noun_patterns", "명사 접속 문형"),
    ("verb_patterns", "동사 접속 문형"),
    ("mixed_patterns", "복합 문형"),
    ("particles", "조사·짧은 표현"),
    ("adverbs", "부사 표현"),
    ("conjunctions", "접속사"),
    ("guess_hearsay", "추량·전문·양태"),
    ("giving_receiving", "수수표현"),
    ("conjugation", "활용형"),
    ("honorifics", "경어·겸양어"),
]

SECTION_HINTS = {
    "noun_patterns": "명사 뒤에 붙는 문형입니다.",
    "verb_patterns": "동사 활용 뒤에 붙는 문형입니다.",
    "mixed_patterns": "여러 품사나 절 뒤에 붙는 복합 문형입니다.",
    "particles": "조사나 짧은 표현의 문맥 차이를 고르는 문제입니다.",
    "adverbs": "부사 표현의 뉘앙스와 함께 쓰이는 말에 주의합니다.",
    "conjunctions": "앞뒤 문장의 논리 관계를 고르는 문제입니다.",
    "guess_hearsay": "추측, 전언, 양태 표현의 차이를 고르는 문제입니다.",
    "giving_receiving": "누가 누구에게 주고받는지 방향을 보는 수수표현입니다.",
    "conjugation": "수동, 사역, 사역수동, 가능, 존경 활용을 고르는 문제입니다.",
    "honorifics": "상대의 동작을 높이는 존경어와 내 쪽 동작을 낮추는 겸양어를 구별합니다.",
}

REPLACEMENT_VARIANTS = [
    {},
    {"田中": "山田", "彼": "友人", "先生": "部長", "今日": "明日", "日本": "韓国", "会社": "学校"},
    {"田中": "佐藤", "彼女": "先輩", "先生": "社長", "昨日": "先週", "友だち": "同僚", "東京": "大阪"},
    {"子供": "学生", "私": "妹", "母": "父", "明日": "来週", "学校": "会社", "部長": "先生"},
]


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip())


def source_file() -> Path:
    matches = list(SOURCE_DIR.glob("*문법*.txt"))
    if not matches:
        raise FileNotFoundError("_N3 문법 txt 파일을 찾지 못했습니다.")
    return matches[0]


def parse_rows() -> list[dict]:
    rows: list[dict] = []
    for line_no, line in enumerate(source_file().read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        expr = clean_text(parts[0])
        if not expr:
            continue
        rows.append({
            "line": line_no,
            "expr": expr,
            "display": clean_text(parts[2] if len(parts) > 2 and parts[2].strip() else expr),
            "meaning": clean_text(parts[3] if len(parts) > 3 else ""),
            "jp_example": clean_text(parts[4] if len(parts) > 4 else ""),
            "ko_example": clean_text(parts[6] if len(parts) > 6 else ""),
            "tag": clean_text(parts[-1] if parts else ""),
        })
    return rows


def classify(row: dict) -> str:
    expr = row["expr"]
    tag = row["tag"]
    line = row["line"]
    if line >= 303 or "敬" in row["display"] or any(key in expr for key in ["お目", "いらっしゃ", "参る", "おる", "存じ", "なさる", "おっしゃ", "申", "伺", "ご覧", "拝見", "召し", "お休み", "お越", "お見え"]):
        return "honorifics"
    if 286 <= line <= 302:
        return "conjugation"
    if 276 <= line <= 285:
        return "giving_receiving"
    if 271 <= line <= 275 or any(key in expr for key in ["そうだ", "らしい", "ようだ", "かもしれない", "はず", "だろう", "に違いない", "に決まっている"]):
        return "guess_hearsay"
    if 240 <= line <= 270:
        return "conjunctions"
    if 185 <= line <= 239:
        return "adverbs"
    if 156 <= line <= 184:
        return "particles"
    if "名사뒤" in tag or "명사뒤" in tag:
        return "noun_patterns"
    if "동사뒤" in tag:
        return "verb_patterns"
    if "여러뒤" in tag:
        return "mixed_patterns"
    if expr.startswith("～に") or expr.startswith("～を") or expr.startswith("A,") or "名사" in tag:
        return "noun_patterns"
    if expr.startswith("～て") or expr.startswith("～た") or expr.startswith("～ない") or "動" in tag:
        return "verb_patterns"
    return "mixed_patterns"


def option_surface(expr: str) -> str:
    raw = expr.strip()
    raw_no_paren = re.sub(r"\s*（.*?）", "", raw)
    raw_no_paren = re.sub(r"\s*\(.*?\)", "", raw_no_paren)
    special_raw = {
        "お / ご + ます형 + になる": "お/ご〜になる",
        "お / ご + ます형 + ください": "お/ご〜ください",
        "お / ご + ます형 + する": "お/ご〜する",
        "お / ご + ます형 + する (いたす)": "お/ご〜する/いたす",
        "お / ご + ます형 + いたす": "お/ご〜いたす",
        "(마스형/어간) + そうだ": "そう",
        "(기본형/보통형) + そうだ": "そうだ",
        "(보통형) + らしい": "らしい",
        "(명사+の/보통형) + ようだ": "ようだ",
        "いまにも～そうだ": "そう",
    }
    if raw in special_raw:
        return special_raw[raw]
    if raw_no_paren in special_raw:
        return special_raw[raw_no_paren]
    value = raw_no_paren.replace("～", "")
    value = value.replace("A, B", "").replace("A", "").replace("B", "").replace("C", "")
    value = value.replace("お / ご", "お/ご")
    if "+" in value:
        value = value.split("+")[-1].strip()
    value = value.strip(" ・/、")
    if "そうだ" in value and "いまにも" in raw:
        return "そう"
    return value or expr

def candidate_surfaces(row: dict) -> list[str]:
    expr = row["expr"]
    display = row["display"]
    candidates = []
    for value in [expr, display, option_surface(expr), option_surface(display)]:
        value = clean_text(value)
        value = re.sub(r"\s*（.*?）", "", value)
        value = re.sub(r"\s*\(.*?\)", "", value)
        for token in [value, value.replace("～", "")]:
            token = token.strip()
            if token and token not in candidates:
                candidates.append(token)
    more = []
    for token in candidates:
        if token.startswith("て") and len(token) > 2:
            more.append(token[1:])
        if token.startswith("た") and len(token) > 2:
            more.append(token[1:])
        if "そうだ" in token:
            more.extend(["そう", "そうだ"])
        if "らしい" in token:
            more.append("らしい")
        if "ようだ" in token:
            more.append("よう")
        if "みたい" in token:
            more.append("みたい")
    for token in more:
        if token and token not in candidates:
            candidates.append(token)
    return sorted(candidates, key=len, reverse=True)


def blank_example(row: dict) -> tuple[str, str]:
    jp = row["jp_example"]
    if not jp:
        return "", option_surface(row["expr"])
    for candidate in candidate_surfaces(row):
        if candidate and candidate in jp:
            return jp.replace(candidate, BLANK, 1), candidate
    return "", option_surface(row["expr"])


def apply_variant(text: str, variant_index: int) -> str:
    result = text
    for before, after in REPLACEMENT_VARIANTS[variant_index % len(REPLACEMENT_VARIANTS)].items():
        result = result.replace(before, after)
    return result


def build_fallback_sentence(row: dict, section_id: str, variant_index: int) -> str:
    surface = option_surface(row["expr"])
    meaning = row["meaning"] or surface
    templates = {
        "conjunctions": [
            f"前の文と後の文をつなぐ表現として、{BLANK}が最も自然です。",
            f"文の流れに合う接続表現として、{BLANK}を選びます。",
        ],
        "adverbs": [
            f"後ろの表現と合う副詞として、{BLANK}が自然です。",
            f"この文の空欄に入る副詞として、{BLANK}を選びます。",
        ],
        "particles": [
            f"この文の助詞・短い表現として、{BLANK}が最も自然です。",
            f"文の流れに合う表現として、{BLANK}を選びます。",
        ],
    }
    choices = templates.get(section_id, [
        f"文脈に合うN3文法表現として、{BLANK}が最も自然です。",
        f"この文の空欄に入る表現として、{BLANK}を選びます。",
    ])
    return choices[variant_index % len(choices)]


def rotate_options(options: list[dict], seed: int) -> tuple[list[str], int, list[dict]]:
    rng = random.Random(seed)
    copied = [dict(item) for item in options]
    rng.shuffle(copied)
    return [item["surface"] for item in copied], next(i for i, item in enumerate(copied) if item["correct"]), [
        {"option": item["surface"], "meaning": item["meaning"], "point": item["expr"]} for item in copied
    ]


def make_option_pool(rows: list[dict], section_id: str) -> list[dict]:
    pool = []
    seen = set()
    for row in rows:
        if row["section"] != section_id:
            continue
        surface = option_surface(row["expr"])
        key = (surface, row["meaning"])
        if not surface or key in seen:
            continue
        seen.add(key)
        pool.append({"surface": surface, "meaning": row["meaning"], "expr": row["expr"]})
    return pool


def build_question(row: dict, section_rows: list[dict], variant_index: int, number: int) -> dict:
    section_id = row["section"]
    base, preferred_surface = blank_example(row)
    answer_surface = preferred_surface or option_surface(row["expr"])
    answer_item = {"surface": answer_surface, "meaning": row["meaning"], "expr": row["expr"], "correct": True}
    pool = [item for item in make_option_pool(section_rows, section_id) if item["surface"] != answer_surface]
    if len(pool) < 3:
        all_pool = [item for item in make_option_pool(section_rows, "mixed_patterns") if item["surface"] != answer_surface]
        pool.extend(all_pool)
    rng = random.Random(number * 97 + variant_index)
    distractors = rng.sample(pool, k=min(3, len(pool)))
    while len(distractors) < 3:
        distractors.append({"surface": f"選択肢{len(distractors)+1}", "meaning": "오답 보기", "expr": "오답"})
    options, answer, option_explanations = rotate_options([answer_item] + [{**item, "correct": False} for item in distractors], number)
    if not base:
        base = build_fallback_sentence(row, section_id, variant_index)
    question = apply_variant(base, variant_index)
    translation = row["ko_example"] or f"문맥상 '{row['meaning']}'에 해당하는 표현을 고르는 문제입니다."
    section_hint = SECTION_HINTS.get(section_id, "N3 문법 표현의 문맥 차이를 확인합니다.")
    option_lines = "\n".join(
        f"{idx + 1}. {item['option']} - {item['meaning']} ({item['point']})"
        for idx, item in enumerate(option_explanations)
    )
    explanation = f"{row['expr']} - {row['meaning']}\n{section_hint}\n보기 설명\n{option_lines}"
    return {
        "id": f"gq_{number:04d}",
        "number": number,
        "question": question,
        "translation": translation,
        "options": options,
        "answer": answer,
        "point": row["expr"],
        "meaning": row["meaning"],
        "explanation": explanation,
        "option_explanations": option_explanations,
        "source_line": row["line"],
    }


def build() -> dict:
    rows = parse_rows()
    unique_rows = []
    seen = set()
    for row in rows:
        key = (row["expr"], row["meaning"])
        if key in seen:
            continue
        seen.add(key)
        row["section"] = classify(row)
        unique_rows.append(row)
    sections = []
    number = 1
    for section_id, title in SECTION_ORDER:
        section_rows = [row for row in unique_rows if row["section"] == section_id]
        questions = []
        for row in section_rows:
            for variant_index in range(VARIANTS_PER_POINT):
                questions.append(build_question(row, unique_rows, variant_index, number))
                number += 1
        if questions:
            sections.append({"id": section_id, "title": title, "questions": questions})
    return {
        "id": "n3_grammar_quiz",
        "mode": "grammar",
        "level": "N3",
        "title": "N3 문법 빈칸 선택",
        "description": "_N3 문법 자료의 전체 항목을 기준으로 JLPT N3 문법 형식 선택 문제를 생성합니다.",
        "sources_note": "사용자가 제공한 로컬 N3 문법 DB를 기준 목록으로 삼고, 각 보기의 뜻과 용도를 해설에 포함합니다.",
        "source_item_count": len(unique_rows),
        "variants_per_point": VARIANTS_PER_POINT,
        "sections": sections,
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = build()
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = sum(len(section.get("questions", [])) for section in payload.get("sections", []))
    print(f"wrote {OUTPUT} ({payload['source_item_count']} points, {total} questions)")


if __name__ == "__main__":
    main()
