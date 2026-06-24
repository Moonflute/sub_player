from __future__ import annotations

import json
from pathlib import Path

import main as engine
from build_webapp import clean_translation, serialize_grammar, serialize_vocab


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "_jlpt source refined" / "reading" / "n3_custom_reading.json"


PASSAGES = [
    {
        "id": "short_01",
        "section": "단문 독해",
        "title": "図書館の利用時間",
        "question": "このお知らせで一番大切なことは何ですか。",
        "sentences": [
            ("来週の月曜日から、図書館の開く時間が一時間早くなります。", "다음 주 월요일부터 도서관 여는 시간이 한 시간 빨라집니다."),
            ("試験の準備をする学生が多いためです。", "시험 준비를 하는 학생이 많기 때문입니다."),
            ("ただし、閉まる時間は今までと同じ午後八時です。", "다만 닫는 시간은 지금까지와 같은 오후 8시입니다."),
            ("朝早く利用したい人は、学生証を忘れないようにしてください。", "아침 일찍 이용하고 싶은 사람은 학생증을 잊지 않도록 해 주세요."),
        ],
    },
    {
        "id": "short_02",
        "section": "단문 독해",
        "title": "アルバイトの連絡",
        "question": "店長は何を頼んでいますか。",
        "sentences": [
            ("田中さん、明日のアルバイトについて連絡します。", "다나카 씨, 내일 아르바이트에 대해 연락드립니다."),
            ("午後三時からの予定でしたが、店が混みそうなので二時に来てください。", "오후 3시부터 예정이었지만, 가게가 붐빌 것 같으니 2시에 와 주세요."),
            ("もし都合が悪ければ、今日の夜九時までに電話してください。", "만약 사정이 좋지 않으면 오늘 밤 9시까지 전화해 주세요."),
        ],
    },
    {
        "id": "short_03",
        "section": "단문 독해",
        "title": "忘れ物",
        "question": "この人はこれからどうしますか。",
        "sentences": [
            ("駅に着いてから、財布を家に忘れたことに気がつきました。", "역에 도착하고 나서 지갑을 집에 두고 온 것을 깨달았습니다."),
            ("電車に乗れないので、友だちに電話して少し待ってもらうことにしました。", "전철을 탈 수 없어서 친구에게 전화해 조금 기다려 달라고 하기로 했습니다."),
            ("急いで家に戻れば、約束の時間には少し遅れるだけですみそうです。", "서둘러 집에 돌아가면 약속 시간에는 조금 늦는 정도로 끝날 것 같습니다."),
        ],
    },
    {
        "id": "mid_01",
        "section": "중문 독해",
        "title": "自転車通学",
        "question": "筆者が自転車通学を続けたい理由は何ですか。",
        "sentences": [
            ("私は先月から自転車で学校へ通っています。", "저는 지난달부터 자전거로 학교에 다니고 있습니다."),
            ("最初は電車代を節約するためでしたが、今は別の理由で続けたいと思っています。", "처음에는 전철비를 아끼기 위해서였지만, 지금은 다른 이유로 계속하고 싶다고 생각합니다."),
            ("朝の空気を感じながら走ると、授業が始まる前に頭がすっきりします。", "아침 공기를 느끼며 달리면 수업이 시작되기 전에 머리가 맑아집니다."),
            ("雨の日は少し大変ですが、駅まで歩いて電車を待つより気分が楽です。", "비 오는 날은 조금 힘들지만, 역까지 걸어가 전철을 기다리는 것보다 기분이 편합니다."),
            ("安全に気をつけながら、これからもできるだけ自転車で通うつもりです。", "안전에 주의하면서 앞으로도 가능한 한 자전거로 다닐 생각입니다."),
        ],
    },
    {
        "id": "mid_02",
        "section": "중문 독해",
        "title": "メールの返事",
        "question": "筆者はメールについてどう考えていますか。",
        "sentences": [
            ("メールは便利ですが、返事を急ぎすぎる必要はないと思います。", "메일은 편리하지만 답장을 너무 서두를 필요는 없다고 생각합니다."),
            ("仕事の連絡なら早く返したほうがいいですが、友人との会話では少し時間を置いても失礼ではありません。", "일 연락이라면 빨리 답하는 편이 좋지만, 친구와의 대화에서는 조금 시간을 두어도 실례가 아닙니다."),
            ("すぐに返事をしようとして、内容をよく読まずに送ってしまうことがあります。", "바로 답장을 하려고 하다가 내용을 잘 읽지 않고 보내 버리는 일이 있습니다."),
            ("そのため、私は大切なメールほど、一度読み返してから送るようにしています。", "그래서 저는 중요한 메일일수록 한 번 다시 읽고 나서 보내도록 하고 있습니다."),
        ],
    },
    {
        "id": "mid_03",
        "section": "중문 독해",
        "title": "小さな店のよさ",
        "question": "この文章で筆者が言いたいことは何ですか。",
        "sentences": [
            ("最近、大きな店で何でも安く買えるようになりました。", "최근에는 큰 가게에서 무엇이든 싸게 살 수 있게 되었습니다."),
            ("しかし、私は家の近くの小さな店も大切にしたいと思っています。", "하지만 저는 집 근처의 작은 가게도 소중히 하고 싶다고 생각합니다."),
            ("店の人が客の好みを覚えていて、必要なものをすすめてくれるからです。", "가게 사람이 손님의 취향을 기억하고 필요한 것을 추천해 주기 때문입니다."),
            ("値段だけを比べると大きな店のほうが便利かもしれません。", "가격만 비교하면 큰 가게 쪽이 편리할지도 모릅니다."),
            ("でも、安心して相談できる場所が近くにあることも、生活には必要だと思います。", "그래도 안심하고 상담할 수 있는 장소가 가까이에 있는 것도 생활에는 필요하다고 생각합니다."),
        ],
    },
    {
        "id": "long_01",
        "section": "장문 독해",
        "title": "失敗から学ぶこと",
        "question": "筆者は失敗をどう考えていますか。",
        "sentences": [
            ("新しいことを始めるとき、失敗しない方法ばかり探してしまう人がいます。", "새로운 일을 시작할 때 실패하지 않는 방법만 찾게 되는 사람이 있습니다."),
            ("もちろん準備は大切ですが、どれだけ準備しても思った通りにならないことはあります。", "물론 준비는 중요하지만, 아무리 준비해도 생각한 대로 되지 않는 일은 있습니다."),
            ("私が料理を習い始めたときも、最初は何度も味付けに失敗しました。", "제가 요리를 배우기 시작했을 때도 처음에는 몇 번이나 간 맞추기에 실패했습니다."),
            ("しかし、なぜおいしくならなかったのかを考えるうちに、材料の量や火の強さに気をつけるようになりました。", "하지만 왜 맛있어지지 않았는지 생각하는 동안 재료의 양이나 불 세기에 주의하게 되었습니다."),
            ("失敗はできれば避けたいものですが、次に何を直せばいいかを教えてくれます。", "실패는 가능하면 피하고 싶은 것이지만, 다음에 무엇을 고치면 좋을지 알려 줍니다."),
            ("だから私は、失敗したときこそ、すぐにやめずに理由を探すことが大切だと思います。", "그래서 저는 실패했을 때야말로 바로 그만두지 않고 이유를 찾는 것이 중요하다고 생각합니다."),
        ],
    },
    {
        "id": "long_02",
        "section": "장문 독해",
        "title": "町の祭り",
        "question": "筆者が祭りに参加して感じたことは何ですか。",
        "sentences": [
            ("私の町では、毎年秋に小さな祭りが行われます。", "우리 동네에서는 매년 가을에 작은 축제가 열립니다."),
            ("以前の私は、人が多い場所が苦手だったので、祭りにはあまり行きませんでした。", "예전의 저는 사람이 많은 장소를 어려워해서 축제에는 별로 가지 않았습니다."),
            ("ところが今年、友人に頼まれて、会場の案内を手伝うことになりました。", "그런데 올해 친구의 부탁으로 행사장 안내를 돕게 되었습니다."),
            ("道を聞かれたり、落とし物を探したりして一日中忙しかったです。", "길을 묻는 사람을 상대하거나 분실물을 찾거나 하며 하루 종일 바빴습니다."),
            ("それでも、帰るときに何人もの人からありがとうと言われて、とてもうれしくなりました。", "그래도 돌아갈 때 여러 사람에게서 고맙다는 말을 듣고 매우 기뻤습니다."),
            ("祭りは見るだけのものだと思っていましたが、作る側に立つと町の人とのつながりを感じられるのだと分かりました。", "축제는 보기만 하는 것이라고 생각했지만, 만드는 쪽에 서면 동네 사람들과의 연결을 느낄 수 있다는 것을 알았습니다."),
        ],
    },
    {
        "id": "long_03",
        "section": "장문 독해",
        "title": "本を選ぶ楽しさ",
        "question": "筆者は本屋で本を選ぶことについてどう思っていますか。",
        "sentences": [
            ("インターネットで本を買うと、家にいながらすぐに注文できて便利です。", "인터넷으로 책을 사면 집에 있으면서 바로 주문할 수 있어 편리합니다."),
            ("私もよく利用していますが、時間があるときはできるだけ本屋へ行くようにしています。", "저도 자주 이용하지만 시간이 있을 때는 가능한 한 서점에 가도록 하고 있습니다."),
            ("本屋では、探していた本だけでなく、偶然目に入った本にも出会えます。", "서점에서는 찾고 있던 책뿐 아니라 우연히 눈에 들어온 책도 만날 수 있습니다."),
            ("表紙を見たり、少し読んだりしているうちに、今まで興味がなかった分野にも関心がわくことがあります。", "표지를 보거나 조금 읽거나 하는 동안 지금까지 관심이 없던 분야에도 흥미가 생기는 일이 있습니다."),
            ("目的の本を早く手に入れるだけなら、ネットのほうが便利でしょう。", "목적한 책을 빨리 손에 넣는 것만이라면 인터넷 쪽이 편리할 것입니다."),
            ("しかし、思いがけない本との出会いを楽しめることが、本屋に行く一番のよさだと思います。", "하지만 예상치 못한 책과의 만남을 즐길 수 있는 것이 서점에 가는 가장 큰 장점이라고 생각합니다."),
        ],
    },
    {
        "id": "info_01",
        "section": "정보 검색",
        "title": "料理教室のお知らせ",
        "question": "土曜日に参加したい人は何時までに申し込めばいいですか。",
        "sentences": [
            ("市民センターでは、来月から初心者向けの料理教室を開きます。", "시민센터에서는 다음 달부터 초보자 대상 요리 교실을 엽니다."),
            ("教室は火曜日の夜と土曜日の午前に行われ、どちらも内容は同じです。", "교실은 화요일 밤과 토요일 오전에 열리며 둘 다 내용은 같습니다."),
            ("参加費は一回千円で、材料費も含まれています。", "참가비는 1회 1,000엔이며 재료비도 포함되어 있습니다."),
            ("火曜日の教室は前日の午後五時まで、土曜日の教室は木曜日の午後五時までに申し込んでください。", "화요일 교실은 전날 오후 5시까지, 토요일 교실은 목요일 오후 5시까지 신청해 주세요."),
            ("申し込みは電話かセンターの受付でできます。", "신청은 전화나 센터 접수처에서 할 수 있습니다."),
        ],
    },
    {
        "id": "info_02",
        "section": "정보 검색",
        "title": "バスの一日券",
        "question": "一日券を買うときに注意することは何ですか。",
        "sentences": [
            ("観光地を回る人には、町のバス一日券が便利です。", "관광지를 둘러보는 사람에게는 마을 버스 1일권이 편리합니다."),
            ("一日券を使うと、決められた地域のバスに何度でも乗ることができます。", "1일권을 사용하면 정해진 지역의 버스를 몇 번이든 탈 수 있습니다."),
            ("大人は八百円、子どもは四百円で、駅前の案内所と一部のホテルで販売しています。", "어른은 800엔, 어린이는 400엔이며 역 앞 안내소와 일부 호텔에서 판매합니다."),
            ("ただし、バスの中では買えないので、乗る前に準備しておく必要があります。", "다만 버스 안에서는 살 수 없으므로 타기 전에 준비해 둘 필요가 있습니다."),
            ("使い始めた日の夜十二時を過ぎると、券は使えなくなります。", "사용하기 시작한 날 밤 12시가 지나면 표는 사용할 수 없게 됩니다."),
        ],
    },
    {
        "id": "info_03",
        "section": "정보 검색",
        "title": "交流イベント",
        "question": "日本語で発表したい人はどうしなければなりませんか。",
        "sentences": [
            ("国際交流イベントでは、外国人と日本人が自分の国の文化を紹介します。", "국제 교류 이벤트에서는 외국인과 일본인이 자기 나라의 문화를 소개합니다."),
            ("参加するだけなら予約はいりませんが、発表したい人は事前の申し込みが必要です。", "참가만 할 경우 예약은 필요 없지만, 발표하고 싶은 사람은 사전 신청이 필요합니다."),
            ("発表は一人五分以内で、日本語で行ってください。", "발표는 1인 5분 이내이며 일본어로 해 주세요."),
            ("申し込み用紙にテーマを書いて、来週金曜日までに交流課へ出してください。", "신청서에 주제를 적어서 다음 주 금요일까지 교류과에 제출해 주세요."),
            ("発表者には、イベント当日に飲み物の券を一枚配ります。", "발표자에게는 이벤트 당일 음료권 한 장을 배부합니다."),
        ],
    },
]


def ensure_output_dir() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


def analyze_items(items: list[dict]) -> list[dict]:
    engine.ensure_reference_database(BASE_DIR)
    vocab_index, grammar_entries, hackers_reference = engine.load_reference_data_from_database(BASE_DIR)

    from janome.tokenizer import Tokenizer

    tokenizer = Tokenizer()
    translation_map = {item["text"]: item["translation"] for item in items}
    analyzed: list[dict] = []
    for item in items:
        analysis = engine.analyze_sentence(
            item["text"],
            translation_map,
            tokenizer,
            vocab_index,
            grammar_entries,
            hackers_reference,
        )
        analyzed.append(
            {
                **item,
                "translation": clean_translation(item["translation"]),
                "vocab_matches": [serialize_vocab(match) for match in analysis.vocab_matches] if analysis else [],
                "grammar_matches": [serialize_grammar(match) for match in analysis.grammar_matches] if analysis else [],
            }
        )
    return analyzed


def build_payload() -> dict:
    flat_items: list[dict] = []
    passages: list[dict] = []
    sentence_index = 1

    for order, passage in enumerate(PASSAGES, start=1):
        passage_items: list[dict] = []
        for local_index, (text, translation) in enumerate(passage["sentences"], start=1):
            item = {
                "index": sentence_index,
                "passage_sentence_index": local_index,
                "passage_id": passage["id"],
                "passage_title": passage["title"],
                "section_title": passage["section"],
                "text": text,
                "translation": translation,
            }
            flat_items.append(item)
            passage_items.append(item)
            sentence_index += 1

        passages.append(
            {
                "id": passage["id"],
                "order": order,
                "section_title": passage["section"],
                "title": passage["title"],
                "question": passage["question"],
                "start_index": passage_items[0]["index"] - 1,
                "sentence_count": len(passage_items),
                "text": "".join(item["text"] for item in passage_items),
                "translation": "\n".join(item["translation"] for item in passage_items),
            }
        )

    analyzed_items = analyze_items(flat_items)
    items_by_passage = {}
    for item in analyzed_items:
        items_by_passage.setdefault(item["passage_id"], []).append(item)

    for passage in passages:
        passage["items"] = items_by_passage.get(passage["id"], [])

    return {
        "id": "n3_custom_reading",
        "mode": "reading",
        "level": "N3",
        "title": "N3 독해 자체 제작",
        "source": "original",
        "sentence_count": len(analyzed_items),
        "passage_count": len(passages),
        "sections": [
            {
                "title": section,
                "passages": [passage for passage in passages if passage["section_title"] == section],
            }
            for section in ["단문 독해", "중문 독해", "장문 독해", "정보 검색"]
        ],
        "passages": passages,
        "items": analyzed_items,
    }


def main() -> int:
    ensure_output_dir()
    payload = build_payload()
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT_PATH), "passages": payload["passage_count"], "sentences": payload["sentence_count"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
