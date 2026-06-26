from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT = BASE_DIR / "_jlpt source refined" / "grammar" / "n3_grammar_quiz.json"
DATA = json.loads(r'''{
  "id": "n3_grammar_quiz",
  "mode": "grammar",
  "level": "N3",
  "title": "N3 \ubb38\ubc95 \ube48\uce78 \uc120\ud0dd",
  "description": "JLPT N3 \ubb38\ubc95/\ubb38\ud615 \uc120\ud0dd \ubb38\uc81c\ub97c \uc6d0\ubb38 \uc0dd\uc131 \ubb38\uc7a5\uc73c\ub85c \uc5f0\uc2b5\ud569\ub2c8\ub2e4.",
  "sections": [
    {
      "id": "connectors",
      "title": "\uc811\uc18d \ud45c\ud604",
      "questions": [
        {
          "id": "gq_001",
          "question": "\u96e8\u304c\u964d\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u8a66\u5408\u306f\u4e88\u5b9a\u901a\u308a\u884c\u308f\u308c\u307e\u3059\u3002",
          "translation": "\ube44\uac00 \uc624\uace0 \uc788\uc9c0\ub9cc \uc2dc\ud569\uc740 \uc608\uc815\ub300\ub85c \uc9c4\ud589\ub429\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u306e\u306b",
            "\u3088\u3046\u306b",
            "\u3070\u304b\u308a\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u306e\u306b",
          "explanation": "\uc55e \ub0b4\uc6a9\uacfc \uc608\uc0c1\uc774 \ub2e4\ub978 \ub4a4 \ub0b4\uc6a9\uc744 \uc5f0\uacb0\ud558\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_002",
          "question": "\u71b1\u304c\u3042\u308b\uff08\u3000\uff09\u3001\u5b66\u6821\u3092\u4f11\u3080\u3053\u3068\u306b\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc5f4\uc774 \uc788\uc5b4\uc11c \ud559\uad50\ub97c \uc26c\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305b\u3044\u3067",
            "\u305f\u3081\u306b",
            "\u304b\u308f\u308a\u306b",
            "\u3068\u3057\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u305f\u3081\u306b",
          "explanation": "\uc6d0\uc778\uc774\ub098 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4. \ubd80\uc815\uc801\uc778 \ud0d3\uc744 \uac15\ud558\uac8c \ub9d0\ud560 \ub54c\ub294 \u305b\u3044\u3067\uac00 \uc790\uc5f0\uc2a4\ub7fd\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_003",
          "question": "\u96fb\u8eca\u304c\u9045\u308c\u305f\uff08\u3000\uff09\u3001\u4f1a\u8b70\u306b\u9593\u306b\u5408\u3044\u307e\u305b\u3093\u3067\u3057\u305f\u3002",
          "translation": "\uc804\ucca0\uc774 \ub2a6\uc740 \ud0d3\uc5d0 \ud68c\uc758\uc5d0 \ub9de\ucd94\uc9c0 \ubabb\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067",
            "\u304b\u308f\u308a\u306b",
            "\u3064\u3044\u3067\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305b\u3044\u3067",
          "explanation": "\uc88b\uc9c0 \uc54a\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ucc45\uc784\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_004",
          "question": "\u53cb\u3060\u3061\u304c\u624b\u4f1d\u3063\u3066\u304f\u308c\u305f\uff08\u3000\uff09\u3001\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\uac00 \ub3c4\uc640\uc900 \ub355\ubd84\uc5d0 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305b\u3044\u3067",
            "\u3070\u304b\u308a\u306b",
            "\u304a\u304b\u3052\u3067",
            "\u3068\u3053\u308d\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "explanation": "\uc88b\uc740 \uacb0\uacfc\uac00 \ub098\uc628 \uc774\uc720\ub97c \ub9d0\ud560 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_005",
          "question": "\u6642\u9593\u304c\u306a\u3044\uff08\u3000\uff09\u3001\u8aac\u660e\u3060\u3051\u805e\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc2dc\uac04\uc774 \uc5c6\uc73c\ub2c8 \uc124\uba85\ub9cc \ub4e4\uc5b4 \uc8fc\uc138\uc694.",
          "options": [
            "\u304b\u3089",
            "\u306e\u306b",
            "\u307b\u3069",
            "\u3070\u304b\u308a"
          ],
          "answer": 0,
          "point": "\u301c\u304b\u3089",
          "explanation": "\uc774\uc720\ub97c \ub9d0\ud558\uace0 \ub4a4\uc5d0 \ubd80\ud0c1\uc774\ub098 \ud310\ub2e8\uc744 \uc774\uc5b4 \ubd99\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_006",
          "question": "\u7d04\u675f\u3057\u305f\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u3084\u308b\u3079\u304d\u3067\u3059\u3002",
          "translation": "\uc57d\uc18d\ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3089\u306b\u306f",
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b",
            "\u307b\u3069"
          ],
          "answer": 0,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "explanation": "\uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \uc758\ubb34\ub098 \uac01\uc624\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_007",
          "question": "\u3053\u306e\u85ac\u306f\u5b50\u3069\u3082\uff08\u3000\uff09\u3001\u5927\u4eba\u3082\u98f2\u3081\u307e\u3059\u3002",
          "translation": "\uc774 \uc57d\uc740 \uc544\uc774\ubfd0\ub9cc \uc544\ub2c8\ub77c \uc5b4\ub978\ub3c4 \uba39\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3060\u3051\u3067\u306a\u304f",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u3060\u3051\u3067\u306a\u304f",
          "explanation": "\ud558\ub098\uc5d0 \ub354\ud574 \ub2e4\ub978 \uac83\ub3c4 \ud3ec\ud568\ub41c\ub2e4\ub294 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_008",
          "question": "\u8aac\u660e\u3092\u805e\u3044\u305f\uff08\u3000\uff09\u3001\u307e\u3060\u3088\u304f\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uc124\uba85\uc744 \ub4e4\uc5c8\ub294\ub370\ub3c4 \uc544\uc9c1 \uc798 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3066\u3082",
            "\u306a\u3089",
            "\u3070",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3082",
          "explanation": "\uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ub2ec\ub77c\uc9c0\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "sentence_patterns",
      "title": "\ubb38\ud615 \uc120\ud0dd",
      "questions": [
        {
          "id": "gq_009",
          "question": "\u6bce\u671d\u30b8\u30e7\u30ae\u30f3\u30b0\u3059\u308b\uff08\u3000\uff09\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc544\uce68 \uc870\uae45\ud558\uae30\ub85c \ud558\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b",
            "\u3053\u3068\u3092",
            "\u3053\u3068\u304c",
            "\u3053\u3068\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u3057\u3066\u3044\u308b",
          "explanation": "\uc2a4\uc2a4\ub85c \uc815\ud55c \uc2b5\uad00\uc774\ub098 \uaddc\uce59\uc744 \ub9d0\ud560 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_010",
          "question": "\u3053\u306e\u90e8\u5c4b\u3067\u306f\u98df\u3079\u7269\u3092\u6301\u3061\u8fbc\u307e\u306a\u3044\uff08\u3000\uff09\u306a\u3063\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ubc29\uc5d0\uc11c\ub294 \uc74c\uc2dd\uc744 \ubc18\uc785\ud558\uc9c0 \uc54a\ub3c4\ub85d \ub418\uc5b4 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b",
            "\u3053\u3068\u304c",
            "\u3053\u3068\u3092",
            "\u3053\u3068\u3082"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u306a\u3063\u3066\u3044\u308b",
          "explanation": "\uaddc\uce59\uc774\ub098 \uc608\uc815\uc73c\ub85c \uc815\ud574\uc838 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_011",
          "question": "\u65e5\u672c\u3078\u884c\u3063\u305f\uff08\u3000\uff09\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc77c\ubcf8\uc5d0 \uac04 \uc801\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3082\u306e",
            "\u3053\u3068",
            "\u3068\u3053\u308d",
            "\u306f\u305a"
          ],
          "answer": 1,
          "point": "\u301c\u305f\u3053\u3068\u304c\u3042\u308b",
          "explanation": "\uacbd\ud5d8\uc744 \ub9d0\ud558\ub294 \ubb38\ud615\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_012",
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3059\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub3c4\ub85d \uba54\ubaa8\ud574 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u3088\u3046\u306b",
            "\u306e\u306b",
            "\u3070\u304b\u308a\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u3088\u3046\u306b",
          "explanation": "\uc5b4\ub5a4 \uc0c1\ud0dc\uac00 \ub418\uac8c \ud558\uac70\ub098 \ubaa9\uc801\uc744 \ub098\ud0c0\ub0bc \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_013",
          "question": "\u6f22\u5b57\u304c\u5c11\u3057\u305a\u3064\u8aad\u3081\u308b\uff08\u3000\uff09\u306a\u308a\u307e\u3057\u305f\u3002",
          "translation": "\ud55c\uc790\ub97c \uc870\uae08\uc529 \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b",
            "\u3088\u3046\u306b",
            "\u305f\u3081\u306b",
            "\u3068\u3053\u308d\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "explanation": "\ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc \ubcc0\ud654\uac00 \uc0dd\uacbc\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_014",
          "question": "\u6765\u6708\u304b\u3089\u5927\u962a\u306b\u8ee2\u52e4\u3059\u308b\uff08\u3000\uff09\u306a\u308a\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \uc624\uc0ac\uce74\ub85c \uc804\uadfc \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b",
            "\u3088\u3046\u306b",
            "\u3068\u3053\u308d\u306b",
            "\u3060\u3051\u306b"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "explanation": "\uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uacb0\uc815\ub41c \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_015",
          "question": "\u4eca\u3001\u51fa\u304b\u3051\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\uae08 \ub9c9 \ub098\uac00\ub824\ub294 \ucc38\uc785\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3053\u308d",
            "\u3070\u304b\u308a",
            "\u306f\u305a",
            "\u3064\u3082\u308a"
          ],
          "answer": 0,
          "point": "\u301c\u3068\u3053\u308d\u3060",
          "explanation": "\ub3d9\uc791\uc774 \ub9c9 \uc2dc\uc791\ub418\ub824\ub294 \uc2dc\uc810\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_016",
          "question": "\u3053\u306e\u4ed5\u4e8b\u306f\u4e00\u4eba\u3067\u3067\u304d\u306a\u3044\uff08\u3000\uff09\u306f\u3042\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uc774 \uc77c\uc740 \ud63c\uc790\uc11c \ubabb \ud560 \uac83\uc740 \uc5c6\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068",
            "\u3082\u306e",
            "\u3068\u3053\u308d",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u306a\u3044\u3053\u3068\u306f\u306a\u3044",
          "explanation": "\ubd88\uac00\ub2a5\ud558\uc9c0\ub294 \uc54a\uc9c0\ub9cc \uc801\uadf9\uc801\uc73c\ub85c \uae0d\uc815\ud558\uc9c0\ub294 \uc54a\ub294 \ud45c\ud604\uc785\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "auxiliary_forms",
      "title": "\ubcf4\uc870\ud45c\ud604\uacfc \ud615\ud0dc",
      "questions": [
        {
          "id": "gq_017",
          "question": "\u5bbf\u984c\u3092\u5168\u90e8\u3084\u3063\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc219\uc81c\ub97c \uc804\ubd80 \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u3057\u307e\u3044",
            "\u3042\u308a",
            "\u304a\u304d"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "explanation": "\uc644\ub8cc\ub098 \uc544\uc26c\uc6c0, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_018",
          "question": "\u65c5\u884c\u306e\u524d\u306b\u30db\u30c6\u30eb\u3092\u4e88\u7d04\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\uc5ec\ud589 \uc804\uc5d0 \ud638\ud154\uc744 \uc608\uc57d\ud574 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304d",
            "\u307f",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u304a\u304f",
          "explanation": "\ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub454\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_019",
          "question": "\u30c9\u30a2\u304c\u958b\u3051\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ubb38\uc774 \uc5f4\ub824 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304d",
            "\u307f",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3042\u308b",
          "explanation": "\ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_020",
          "question": "\u5206\u304b\u3089\u306a\u3044\u8a00\u8449\u3092\u8f9e\u66f8\u3067\u8abf\u3079\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ubaa8\ub974\ub294 \ub9d0\uc744 \uc0ac\uc804\uc5d0\uc11c \ucc3e\uc544 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u307f\u308b",
          "explanation": "\uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_021",
          "question": "\u5916\u306f\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc740 \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305d\u3046",
            "\u3088\u3046",
            "\u3089\u3057\u3044",
            "\u307f\u305f\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u305d\u3046\u3060",
          "explanation": "\ub208\uc73c\ub85c \ubcf8 \ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \uadfc\uac70\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_022",
          "question": "\u3053\u306e\u8a71\u306f\u672c\u5f53\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc774\uc57c\uae30\ub294 \uc0ac\uc2e4\uc778 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305d\u3046",
            "\u3088\u3046",
            "\u305f\u304c\u308b",
            "\u3059\u304e\u308b"
          ],
          "answer": 1,
          "point": "\u301c\u3088\u3046\u3060",
          "explanation": "\uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ud310\ub2e8, \ube44\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_023",
          "question": "\u5f7c\u306f\u65b0\u3057\u3044\u4ed5\u4e8b\u3092\u59cb\u3081\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uadf8\ub294 \uc0c8 \uc77c\uc744 \uc2dc\uc791\ud588\ub2e4\ub294 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u305d\u3046\u306b",
            "\u3059\u304e\u308b",
            "\u305f\u304c\u308b"
          ],
          "answer": 0,
          "point": "\u301c\u3089\u3057\u3044",
          "explanation": "\ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_024",
          "question": "\u3053\u306e\u304b\u3070\u3093\u306f\u91cd\uff08\u3000\uff09\u3059\u304e\u307e\u3059\u3002",
          "translation": "\uc774 \uac00\ubc29\uc740 \ub108\ubb34 \ubb34\uac81\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044",
            "\u304f",
            "\u3055",
            "\u306a"
          ],
          "answer": 0,
          "point": "\u3044\ud615\uc6a9\uc0ac \uc5b4\uac04 + \u3059\u304e\u308b",
          "explanation": "\uc815\ub3c4\uac00 \uc9c0\ub098\uce58\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4. \u3044\ud615\uc6a9\uc0ac\ub294 \u3044\ub97c \ube80 \uc5b4\uac04\uc5d0 \u3059\u304e\u308b\uac00 \ubd99\uc2b5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "particles_context",
      "title": "\uc870\uc0ac\uc640 \ubb38\ub9e5",
      "questions": [
        {
          "id": "gq_025",
          "question": "\u65e5\u672c\u306e\u6587\u5316\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc77c\ubcf8 \ubb38\ud654\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3067",
            "\u3092",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "explanation": "\uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_026",
          "question": "\u5148\u751f\uff08\u3000\uff09\u76f8\u8ac7\u3057\u3066\u304b\u3089\u6c7a\u3081\u307e\u3059\u3002",
          "translation": "\uc120\uc0dd\ub2d8\uacfc \uc0c1\ub2f4\ud55c \ub4a4 \uacb0\uc815\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3067",
            "\u3092",
            "\u3068"
          ],
          "answer": 3,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "explanation": "\uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_027",
          "question": "\u3053\u306e\u554f\u984c\uff08\u3000\uff09\u3064\u3044\u3066\u3001\u3069\u3046\u601d\u3044\u307e\u3059\u304b\u3002",
          "translation": "\uc774 \ubb38\uc81c\uc5d0 \ub300\ud574 \uc5b4\ub5bb\uac8c \uc0dd\uac01\ud569\ub2c8\uae4c?",
          "options": [
            "\u306b",
            "\u3067",
            "\u3092",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "explanation": "\ud654\uc81c\ub098 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0b4\ub294 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_028",
          "question": "\u99c5\uff08\u3000\uff09\u8fd1\u3044\u90e8\u5c4b\u3092\u63a2\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b4 \ubc29\uc744 \ucc3e\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u304b\u3089",
            "\u3067",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "explanation": "\uac70\ub9ac\uc758 \uae30\uc900\uc810\uc744 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_029",
          "question": "\u3053\u306e\u8cc7\u6599\u306f\u76ee\u7684\uff08\u3000\uff09\u5206\u3051\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc774 \uc790\ub8cc\ub294 \ubaa9\uc801\uc5d0 \ub530\ub77c \ub098\ub204\uc5b4 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "explanation": "\uae30\uc900\uc774\ub098 \ubc29\ubc95, \uacbd\uc6b0\uc758 \ucc28\uc774\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_030",
          "question": "\u5b50\u3069\u3082\uff08\u3000\uff09\u5206\u304b\u308a\u3084\u3059\u3044\u8aac\u660e\u304c\u5fc5\u8981\u3067\u3059\u3002",
          "translation": "\uc544\uc774\uc5d0\uac8c\ub294 \uc774\ud574\ud558\uae30 \uc26c\uc6b4 \uc124\uba85\uc774 \ud544\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "explanation": "\ub300\uc0c1\uc774\ub098 \uc0c1\ub300\ub97c \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_031",
          "question": "\u5f7c\u306f\u5b66\u751f\uff08\u3000\uff09\u3068\u3066\u3082\u307e\u3058\u3081\u3067\u3059\u3002",
          "translation": "\uadf8\ub294 \ud559\uc0dd\uc73c\ub85c\uc11c \ub9e4\uc6b0 \uc131\uc2e4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u3068\u3057\u3066",
          "explanation": "\uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_032",
          "question": "\u6642\u9593\uff08\u3000\uff09\u3042\u308c\u3070\u3001\u3082\u3046\u4e00\u5ea6\u8aac\u660e\u3057\u307e\u3059\u3002",
          "translation": "\uc2dc\uac04\ub9cc \uc788\ub2e4\uba74 \ud55c \ubc88 \ub354 \uc124\uba85\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3055\u3048",
            "\u307b\u3069",
            "\u3070\u304b\u308a",
            "\u3057\u304b"
          ],
          "answer": 0,
          "point": "\u301c\u3055\u3048\u301c\u3070",
          "explanation": "\ucd5c\uc18c \uc870\uac74\ub9cc \ucda9\uc871\ub418\uba74 \ub41c\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        }
      ]
    }
  ]
}''')


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = sum(len(section.get("questions", [])) for section in DATA.get("sections", []))
    print(f"wrote {OUTPUT} ({total} questions)")


if __name__ == "__main__":
    main()
