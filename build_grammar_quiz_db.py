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
  "description": "JLPT N3\uc758 \ubb38\ubc95 \ud615\uc2dd \uc120\ud0dd \uc720\ud615\uc744 \uc6d0\ubb38 \uc0dd\uc131 \ubb38\uc81c\ub85c \uc5f0\uc2b5\ud569\ub2c8\ub2e4.",
  "sources_note": "\uacf5\uc2dd JLPT \ubb38\ud56d \uc720\ud615\uacfc \ub85c\uceec N3 \ubb38\ubc95 DB\uc758 \uc811\uc18d \ubd84\ub958\ub97c \ucc38\uace0\ud588\uc73c\uba70, \ubb38\ud56d \ubb38\uc7a5\uc740 \uc0c8\ub85c \uc0dd\uc131\ud588\uc2b5\ub2c8\ub2e4.",
  "sections": [
    {
      "id": "noun_connection",
      "title": "\uba85\uc0ac \uc811\uc18d \ubb38\ud615",
      "questions": [
        {
          "id": "gq_001",
          "number": 1,
          "question": "\u533b\u8005\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uc758\uc0ac\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_002",
          "number": 2,
          "question": "\u4ee3\u8868\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\ub300\ud45c\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_003",
          "number": 3,
          "question": "\u6559\u5e2b\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uad50\uc0ac\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_004",
          "number": 4,
          "question": "\u7559\u5b66\u751f\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uc720\ud559\uc0dd\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_005",
          "number": 5,
          "question": "\u5e97\u9577\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uc810\uc7a5\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_006",
          "number": 6,
          "question": "\u7814\u7a76\u8005\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uc5f0\uad6c\uc790\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_007",
          "number": 7,
          "question": "\u89aa\uff08\u3000\uff09\u3001\u6b63\u3057\u3044\u5224\u65ad\u3092\u3057\u306a\u3051\u308c\u3070\u306a\u308a\u307e\u305b\u3093\u3002",
          "translation": "\ubd80\ubaa8\ub85c\uc11c \uc62c\ubc14\ub978 \ud310\ub2e8\uc744 \ud574\uc57c \ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u3068\u3057\u3066",
          "meaning": "\u3068\u3057\u3066",
          "explanation": "\u301c\u3068\u3057\u3066 - \uc790\uaca9, \uc785\uc7a5, \uc5ed\ud560\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_008",
          "number": 8,
          "question": "\u3053\u306e\u554f\u984c\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc774 \ubb38\uc81c\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_009",
          "number": 9,
          "question": "\u65e5\u672c\u306e\u6587\u5316\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc77c\ubcf8 \ubb38\ud654\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_010",
          "number": 10,
          "question": "\u5c06\u6765\u306e\u4ed5\u4e8b\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc7a5\ub798\uc758 \uc77c\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_011",
          "number": 11,
          "question": "\u74b0\u5883\u4fdd\u8b77\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ud658\uacbd \ubcf4\ud638\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_012",
          "number": 12,
          "question": "\u99c5\u524d\u306e\u5de5\u4e8b\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc5ed \uc55e \uacf5\uc0ac\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_013",
          "number": 13,
          "question": "\u65b0\u3057\u3044\u5236\u5ea6\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc0c8 \uc81c\ub3c4\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_014",
          "number": 14,
          "question": "\u7559\u5b66\u751f\u6d3b\uff08\u3000\uff09\u3001\u77ed\u3044\u610f\u898b\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uc720\ud559 \uc0dd\ud65c\uc5d0 \ub300\ud574 \uc9e7\uc740 \uc758\uacac\uc744 \uc368 \uc8fc\uc138\uc694.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3064\u3044\u3066",
          "meaning": "\u306b\u3064\u3044\u3066",
          "explanation": "\u301c\u306b\u3064\u3044\u3066 - \ud654\uc81c\ub098 \uc870\uc0ac\u00b7\uc124\uba85\uc758 \ub300\uc0c1\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_015",
          "number": 15,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u5b66\u751f\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \ud559\uc0dd\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_016",
          "number": 16,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u5b50\u3069\u3082\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \uc544\uc774\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_017",
          "number": 17,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u5229\u7528\u8005\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \uc774\uc6a9\uc790\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_018",
          "number": 18,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u5916\u56fd\u4eba\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \uc678\uad6d\uc778\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_019",
          "number": 19,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u4f4f\u6c11\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \uc8fc\ubbfc\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_020",
          "number": 20,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u65b0\u5165\u793e\u54e1\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \uc2e0\uc785\uc0ac\uc6d0\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_021",
          "number": 21,
          "question": "\u3053\u306e\u5b66\u6821\u306f\u9ad8\u9f62\u8005\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u8aac\u660e\u3092\u5897\u3084\u3057\u3066\u3044\u307e\u3059\u3002",
          "translation": "\uc774 \ud559\uad50\ub294 \uace0\ub839\uc790\uc5d0 \ub300\ud574 \uc77c\ubcf8\uc5b4 \uc124\uba85\uc744 \ub298\ub9ac\uace0 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3057\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u5bfe\u3057\u3066",
          "meaning": "\u306b\u5bfe\u3057\u3066",
          "explanation": "\u301c\u306b\u5bfe\u3057\u3066 - \uc0c1\ub300\ub098 \ub300\uc0c1\uc744 \ud5a5\ud55c \ud0dc\ub3c4, \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_022",
          "number": 22,
          "question": "\u7b54\u3048\u306f\u3053\u306e\u554f\u984c\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \uc774 \ubb38\uc81c\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_023",
          "number": 23,
          "question": "\u7b54\u3048\u306f\u65e5\u672c\u306e\u6587\u5316\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \uc77c\ubcf8 \ubb38\ud654\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_024",
          "number": 24,
          "question": "\u7b54\u3048\u306f\u5c06\u6765\u306e\u4ed5\u4e8b\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \uc7a5\ub798\uc758 \uc77c\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_025",
          "number": 25,
          "question": "\u7b54\u3048\u306f\u74b0\u5883\u4fdd\u8b77\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \ud658\uacbd \ubcf4\ud638\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_026",
          "number": 26,
          "question": "\u7b54\u3048\u306f\u99c5\u524d\u306e\u5de5\u4e8b\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \uc5ed \uc55e \uacf5\uc0ac\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_027",
          "number": 27,
          "question": "\u7b54\u3048\u306f\u65b0\u3057\u3044\u5236\u5ea6\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \uc0c8 \uc81c\ub3c4\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_028",
          "number": 28,
          "question": "\u7b54\u3048\u306f\u7559\u5b66\u751f\u6d3b\uff08\u3000\uff09\u3001\u5c11\u3057\u305a\u3064\u9055\u3044\u307e\u3059\u3002",
          "translation": "\ub2f5\uc740 \uc720\ud559 \uc0dd\ud65c\uc5d0 \ub530\ub77c \uc870\uae08\uc529 \ub2e4\ub985\ub2c8\ub2e4.",
          "options": [
            "\u306b\u5bfe\u3057\u3066",
            "\u3068\u3057\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3088\u3063\u3066",
          "meaning": "\u306b\u3088\u3063\u3066",
          "explanation": "\u301c\u306b\u3088\u3063\u3066 - \uacbd\uc6b0\u00b7\ubc29\ubc95\u00b7\uc6d0\uc778\u00b7\uc218\ub2e8\uc774 \ub2ec\ub77c\uc9d0\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_029",
          "number": 29,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u65e5\u672c\u8a9e\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \uc77c\ubcf8\uc5b4\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_030",
          "number": 30,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u6f22\u5b57\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \ud55c\uc790\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066",
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_031",
          "number": 31,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u3053\u306e\u8aac\u660e\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \uc774 \uc124\uba85\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_032",
          "number": 32,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u99c5\u306e\u6848\u5185\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \uc5ed \uc548\ub0b4\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066",
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_033",
          "number": 33,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u3053\u306e\u85ac\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \uc774 \uc57d\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_034",
          "number": 34,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u30b9\u30de\u30db\u306e\u753b\u9762\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \uc2a4\ub9c8\ud2b8\ud3f0 \ud654\uba74\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066",
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_035",
          "number": 35,
          "question": "\u524d\u306e\u65b9\u6cd5\uff08\u3000\uff09\u3001\u3053\u306e\u65b9\u6cd5\u306f\u65b0\u3057\u3044\u9053\u5177\u304c\u5206\u304b\u308a\u3084\u3059\u3044\u3067\u3059\u3002",
          "translation": "\uc774\uc804 \ubc29\ubc95\uc5d0 \ube44\ud574 \uc774 \ubc29\ubc95\uc740 \uc0c8 \ub3c4\uad6c\uac00 \uc774\ud574\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u52a0\u3048\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u304a\u3044\u3066",
            "\u306b\u6bd4\u3079\u3066"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u6bd4\u3079\u3066",
          "meaning": "\u306b\u6bd4\u3079\u3066",
          "explanation": "\u301c\u306b\u6bd4\u3079\u3066 - \ube44\uad50 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_036",
          "number": 36,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u5b66\u751f\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \ud559\uc0dd\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_037",
          "number": 37,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u5b50\u3069\u3082\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \uc544\uc774\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_038",
          "number": 38,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u5229\u7528\u8005\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \uc774\uc6a9\uc790\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_039",
          "number": 39,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u5916\u56fd\u4eba\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \uc678\uad6d\uc778\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_040",
          "number": 40,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u4f4f\u6c11\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \uc8fc\ubbfc\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_041",
          "number": 41,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u65b0\u5165\u793e\u54e1\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \uc2e0\uc785\uc0ac\uc6d0\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066",
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_042",
          "number": 42,
          "question": "\u6bce\u65e5\u306e\u7df4\u7fd2\u306f\u9ad8\u9f62\u8005\uff08\u3000\uff09\u3001\u3068\u3066\u3082\u5927\u5207\u3067\u3059\u3002",
          "translation": "\ub9e4\uc77c \uc5f0\uc2b5\uc740 \uace0\ub839\uc790\uc5d0\uac8c \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b\u3068\u3063\u3066",
            "\u306b\u3064\u3044\u3066",
            "\u306b\u3088\u3063\u3066",
            "\u306b\u5bfe\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u306b\u3068\u3063\u3066",
          "meaning": "\u306b\u3068\u3063\u3066",
          "explanation": "\u301c\u306b\u3068\u3063\u3066 - \uadf8 \uc0ac\ub78c\uc774\ub098 \uc785\uc7a5\uc5d0\uc11c\uc758 \ud3c9\uac00 \uae30\uc900\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "verb_connection",
      "title": "\ub3d9\uc0ac \uc811\uc18d \ubb38\ud615",
      "questions": [
        {
          "id": "gq_043",
          "number": 43,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u8cc7\u6599\u3092\u30b3\u30d4\u30fc\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \uc790\ub8cc\ub97c \ubcf5\uc0ac\ud574 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3057\u307e\u3044",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u307f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_044",
          "number": 44,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u90e8\u5c4b\u3092\u4e88\u7d04\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \ubc29\uc744 \uc608\uc57d\ud574 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u307f",
            "\u3057\u307e\u3044",
            "\u304a\u304d"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_045",
          "number": 45,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u7a93\u3092\u958b\u3051\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \ucc3d\ubb38\uc744 \uc5f4\uc5b4 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3057\u307e\u3044",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u307f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_046",
          "number": 46,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u4e88\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \uc608\uc815\uc744 \ud655\uc778\ud574 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u307f",
            "\u3057\u307e\u3044",
            "\u304a\u304d"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_047",
          "number": 47,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u5bbf\u984c\u3092\u7d42\u308f\u3089\u305b\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \uc219\uc81c\ub97c \ub05d\ub0b4 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3057\u307e\u3044",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u307f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_048",
          "number": 48,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u540d\u524d\u3092\u66f8\u3044\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \uc774\ub984\uc744 \uc368 \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u307f",
            "\u3057\u307e\u3044",
            "\u304a\u304d"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_049",
          "number": 49,
          "question": "\u4f1a\u8b70\u306e\u524d\u306b\u5f01\u5f53\u3092\u8cb7\u3063\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ud68c\uc758 \uc804\uc5d0 \ub3c4\uc2dc\ub77d\uc744 \uc0ac \ub461\ub2c8\ub2e4.",
          "options": [
            "\u3057\u307e\u3044",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u307f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u304a\u304f",
          "meaning": "\u304a\u304d",
          "explanation": "\u301c\u3066\u304a\u304f - \ub098\uc911\uc744 \uc704\ud574 \ubbf8\ub9ac \ud574 \ub460\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_050",
          "number": 50,
          "question": "\u673a\u306e\u4e0a\u306b\u8cc7\u6599\u3092\u30b3\u30d4\u30fc\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \uc790\ub8cc\ub97c \ubcf5\uc0ac\ud574\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u3057\u307e\u3044",
            "\u3042\u308a",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_051",
          "number": 51,
          "question": "\u673a\u306e\u4e0a\u306b\u90e8\u5c4b\u3092\u4e88\u7d04\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \ubc29\uc744 \uc608\uc57d\ud574\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u304a\u304d",
            "\u307f",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_052",
          "number": 52,
          "question": "\u673a\u306e\u4e0a\u306b\u7a93\u3092\u958b\u3051\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \ucc3d\ubb38\uc744 \uc5f4\uc5b4\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u3057\u307e\u3044",
            "\u3042\u308a",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_053",
          "number": 53,
          "question": "\u673a\u306e\u4e0a\u306b\u4e88\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \uc608\uc815\uc744 \ud655\uc778\ud574\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u304a\u304d",
            "\u307f",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_054",
          "number": 54,
          "question": "\u673a\u306e\u4e0a\u306b\u5bbf\u984c\u3092\u7d42\u308f\u3089\u305b\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \uc219\uc81c\ub97c \ub05d\ub0b4\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u3057\u307e\u3044",
            "\u3042\u308a",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_055",
          "number": 55,
          "question": "\u673a\u306e\u4e0a\u306b\u540d\u524d\u3092\u66f8\u3044\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \uc774\ub984\uc744 \uc368\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u304a\u304d",
            "\u307f",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_056",
          "number": 56,
          "question": "\u673a\u306e\u4e0a\u306b\u5f01\u5f53\u3092\u8cb7\u3063\u3066\uff08\u3000\uff09\u307e\u3059\u3002",
          "translation": "\ucc45\uc0c1 \uc704\uc5d0 \ub3c4\uc2dc\ub77d\uc744 \uc0ac\uc838 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u3057\u307e\u3044",
            "\u3042\u308a",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3042\u308b",
          "meaning": "\u3042\u308a",
          "explanation": "\u301c\u3066\u3042\u308b - \ub204\uad70\uac00\uc758 \ud589\uc704 \uacb0\uacfc\uac00 \ub0a8\uc544 \uc788\ub294 \uc0c1\ud0dc\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_057",
          "number": 57,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u8cc7\u6599\u3092\u30b3\u30d4\u30fc\u3057\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \uc790\ub8cc\ub97c \ubcf5\uc0ac\ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_058",
          "number": 58,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u90e8\u5c4b\u3092\u4e88\u7d04\u3057\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \ubc29\uc744 \uc608\uc57d\ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u3057\u307e\u3044",
            "\u307f",
            "\u304a\u304d"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_059",
          "number": 59,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u7a93\u3092\u958b\u3051\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \ucc3d\ubb38\uc744 \uc5f4\uc5b4 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_060",
          "number": 60,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u4e88\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \uc608\uc815\uc744 \ud655\uc778\ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u3057\u307e\u3044",
            "\u307f",
            "\u304a\u304d"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_061",
          "number": 61,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u5bbf\u984c\u3092\u7d42\u308f\u3089\u305b\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \uc219\uc81c\ub97c \ub05d\ub0b4 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_062",
          "number": 62,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u540d\u524d\u3092\u66f8\u3044\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \uc774\ub984\uc744 \uc368 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u3057\u307e\u3044",
            "\u307f",
            "\u304a\u304d"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_063",
          "number": 63,
          "question": "\u6025\u3044\u3067\u3044\u305f\u306e\u3067\u3001\u9593\u9055\u3048\u3066\u5f01\u5f53\u3092\u8cb7\u3063\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc11c\ub450\ub974\uace0 \uc788\uc5b4\uc11c \uc2e4\uc218\ub85c \ub3c4\uc2dc\ub77d\uc744 \uc0ac \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3057\u307e\u3046",
          "meaning": "\u3057\u307e\u3044",
          "explanation": "\u301c\u3066\u3057\u307e\u3046 - \uc644\ub8cc, \uc720\uac10, \uc2e4\uc218\uc758 \ub290\ub08c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_064",
          "number": 64,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u8cc7\u6599\u3092\u30b3\u30d4\u30fc\u3057\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \uc790\ub8cc\ub97c \ubcf5\uc0ac\ud574 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_065",
          "number": 65,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u90e8\u5c4b\u3092\u4e88\u7d04\u3057\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \ubc29\uc744 \uc608\uc57d\ud574 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u3057\u307e\u3044",
            "\u307f",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_066",
          "number": 66,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u7a93\u3092\u958b\u3051\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \ucc3d\ubb38\uc744 \uc5f4\uc5b4 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_067",
          "number": 67,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u4e88\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \uc608\uc815\uc744 \ud655\uc778\ud574 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u3057\u307e\u3044",
            "\u307f",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_068",
          "number": 68,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u5bbf\u984c\u3092\u7d42\u308f\u3089\u305b\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \uc219\uc81c\ub97c \ub05d\ub0b4 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_069",
          "number": 69,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u540d\u524d\u3092\u66f8\u3044\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \uc774\ub984\uc744 \uc368 \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3042\u308a",
            "\u3057\u307e\u3044",
            "\u307f",
            "\u304a\u304d"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_070",
          "number": 70,
          "question": "\u5206\u304b\u3089\u306a\u304b\u3063\u305f\u306e\u3067\u3001\u4e00\u5ea6\u5f01\u5f53\u3092\u8cb7\u3063\u3066\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc798 \ubab0\ub77c\uc11c \ud55c \ubc88 \ub3c4\uc2dc\ub77d\uc744 \uc0ac \ubcf4\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u307f",
            "\u304a\u304d",
            "\u3042\u308a",
            "\u3057\u307e\u3044"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u307f\u308b",
          "meaning": "\u307f",
          "explanation": "\u301c\u3066\u307f\u308b - \uc2dc\ud5d8 \uc0bc\uc544 \ud574 \ubcf4\ub294 \ud589\ub3d9\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_071",
          "number": 71,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u8aad\u307f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \uc77d\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044",
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_072",
          "number": 72,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u4f7f\u3044\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \uc0ac\uc6a9\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060",
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_073",
          "number": 73,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u899a\u3048\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \uc678\uc6b0\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044",
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_074",
          "number": 74,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u8aac\u660e\u3057\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \uc124\uba85\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060",
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_075",
          "number": 75,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u8a71\u3057\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \ub9d0\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044",
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_076",
          "number": 76,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u63a2\u3057\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \ucc3e\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060",
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_077",
          "number": 77,
          "question": "\u3053\u306e\u30a2\u30d7\u30ea\u306f\u521d\u3081\u3066\u3067\u3082\u904b\u3073\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uc571\uc740 \ucc98\uc74c\uc774\uc5b4\ub3c4 \ub098\ub974\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3059\u304e\u308b",
            "\u3084\u3059\u3044",
            "\u306b\u304f\u3044",
            "\u304c\u3061\u3060"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u3084\u3059\u3044",
          "meaning": "\u3084\u3059\u3044",
          "explanation": "\u307e\u3059\ud615 + \u3084\u3059\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc27d\uac70\ub098 \uadf8\ub7f0 \uc131\uc9c8\uc774 \uc788\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_078",
          "number": 78,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u8aad\u307f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \uc77d\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060",
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044"
          ],
          "answer": 2,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_079",
          "number": 79,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u4f7f\u3044\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \uc0ac\uc6a9\ud558\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044",
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_080",
          "number": 80,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u899a\u3048\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \uc678\uc6b0\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060",
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044"
          ],
          "answer": 2,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_081",
          "number": 81,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u8aac\u660e\u3057\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \uc124\uba85\ud558\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044",
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_082",
          "number": 82,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u8a71\u3057\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \ub9d0\ud558\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060",
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044"
          ],
          "answer": 2,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_083",
          "number": 83,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u63a2\u3057\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \ucc3e\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044",
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_084",
          "number": 84,
          "question": "\u3053\u306e\u5b57\u306f\u5c0f\u3055\u304f\u3066\u904b\u3073\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc774 \uae00\uc790\ub294 \uc791\uc544\uc11c \ub098\ub974\uae30 \uc5b4\ub835\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304c\u3061\u3060",
            "\u305d\u3046\u3060",
            "\u306b\u304f\u3044",
            "\u3084\u3059\u3044"
          ],
          "answer": 2,
          "point": "\u307e\u3059\ud615 + \u306b\u304f\u3044",
          "meaning": "\u306b\u304f\u3044",
          "explanation": "\u307e\u3059\ud615 + \u306b\u304f\u3044 - \uc5b4\ub5a4 \ud589\ub3d9\uc744 \ud558\uae30 \uc5b4\ub835\ub2e4\ub294 \ub73b\uc785\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "reason_condition",
      "title": "\uc870\uac74\u00b7\uc5ed\uc811\u00b7\uc774\uc720",
      "questions": [
        {
          "id": "gq_085",
          "number": 85,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_086",
          "number": 86,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b",
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f"
          ],
          "answer": 1,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_087",
          "number": 87,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_088",
          "number": 88,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b",
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f"
          ],
          "answer": 1,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_089",
          "number": 89,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_090",
          "number": 90,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b",
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f"
          ],
          "answer": 1,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_091",
          "number": 91,
          "question": "\u5341\u5206\u306b\u6ce8\u610f\u3057\u305f\uff08\u3000\uff09\u3001\u5c0f\u3055\u306a\u30df\u30b9\u3092\u3057\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
          "translation": "\ucda9\ubd84\ud788 \uc8fc\uc758\ud588\ub294\ub370\ub3c4 \uc791\uc740 \uc2e4\uc218\ub97c \ud574 \ubc84\ub838\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u304a\u304b\u3052\u3067",
            "\u306e\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306e\u306b",
          "meaning": "\u306e\u306b",
          "explanation": "\u301c\u306e\u306b - \uc608\uc0c1\uacfc \ubc18\ub300\ub418\ub294 \uacb0\uacfc\ub97c \uc774\uc5b4 \uc8fc\ub294 \uc5ed\uc811 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_092",
          "number": 92,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u65e5\u672c\u8a9e\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \uc77c\ubcf8\uc5b4\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3066\u3082",
            "\u306a\u3089",
            "\u3070",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_093",
          "number": 93,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u6f22\u5b57\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \ud55c\uc790\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3070",
            "\u3068",
            "\u3066\u3082",
            "\u306a\u3089"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_094",
          "number": 94,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u3053\u306e\u8aac\u660e\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \uc774 \uc124\uba85\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3066\u3082",
            "\u306a\u3089",
            "\u3070",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_095",
          "number": 95,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u99c5\u306e\u6848\u5185\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \uc5ed \uc548\ub0b4\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3070",
            "\u3068",
            "\u3066\u3082",
            "\u306a\u3089"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_096",
          "number": 96,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u3053\u306e\u85ac\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \uc774 \uc57d\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3066\u3082",
            "\u306a\u3089",
            "\u3070",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_097",
          "number": 97,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u30b9\u30de\u30db\u306e\u753b\u9762\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \uc2a4\ub9c8\ud2b8\ud3f0 \ud654\uba74\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3070",
            "\u3068",
            "\u3066\u3082",
            "\u306a\u3089"
          ],
          "answer": 2,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_098",
          "number": 98,
          "question": "\u4f55\u5ea6\u805e\u3044\uff08\u3000\uff09\u3001\u65b0\u3057\u3044\u9053\u5177\u306e\u610f\u5473\u304c\u5206\u304b\u308a\u307e\u305b\u3093\u3002",
          "translation": "\uba87 \ubc88\uc744 \ub4e4\uc5b4\ub3c4 \uc0c8 \ub3c4\uad6c\uc758 \ub73b\uc744 \ubaa8\ub974\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3066\u3082",
            "\u306a\u3089",
            "\u3070",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3066\u3082",
          "meaning": "\u3066\u3082",
          "explanation": "\u301c\u3066\u3082 - \uadf8 \uc870\uac74\uc774 \uc788\uc5b4\ub3c4 \uacb0\uacfc\uac00 \ubc14\ub00c\uc9c0 \uc54a\uc74c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_099",
          "number": 99,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_100",
          "number": 100,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f"
          ],
          "answer": 3,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_101",
          "number": 101,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_102",
          "number": 102,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f"
          ],
          "answer": 3,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_103",
          "number": 103,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_104",
          "number": 104,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f"
          ],
          "answer": 3,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_105",
          "number": 105,
          "question": "\u8a66\u9a13\u3092\u53d7\u3051\u308b\uff08\u3000\uff09\u3001\u6700\u5f8c\u307e\u3067\u6e96\u5099\u3057\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc2dc\ud5d8\uc744 \ubcf4\uae30\ub85c \ud55c \uc774\uc0c1 \ub05d\uae4c\uc9c0 \uc900\ube44\ud569\uc2dc\ub2e4.",
          "options": [
            "\u3070\u304b\u308a\u306b",
            "\u304b\u3089\u306b\u306f",
            "\u3068\u3053\u308d\u3067",
            "\u304b\u308f\u308a\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u306b\u306f",
          "meaning": "\u304b\u3089\u306b\u306f",
          "explanation": "\u301c\u304b\u3089\u306b\u306f - \uc774\ubbf8 \uadf8\ub807\uac8c \ud55c \uc774\uc0c1 \ub2f9\uc5f0\ud788 \ud574\uc57c \ud55c\ub2e4\ub294 \ud310\ub2e8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_106",
          "number": 106,
          "question": "\u53cb\u3060\u3061\u304c\u624b\u4f1d\u3063\u3066\u304f\u308c\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\uac00 \ub3c4\uc640\uc900 \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_107",
          "number": 107,
          "question": "\u5148\u751f\u304c\u8a73\u3057\u304f\u8aac\u660e\u3057\u3066\u304f\u308c\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uc120\uc0dd\ub2d8\uc774 \uc790\uc138\ud788 \uc124\uba85\ud574 \uc900 \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067",
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b"
          ],
          "answer": 0,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_108",
          "number": 108,
          "question": "\u99c5\u304c\u8fd1\u304f\u306a\u3063\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uc5ed\uc774 \uac00\uae4c\uc6cc\uc9c4 \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_109",
          "number": 109,
          "question": "\u7df4\u7fd2\u3092\u7d9a\u3051\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\uc744 \uacc4\uc18d\ud55c \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067",
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b"
          ],
          "answer": 0,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_110",
          "number": 110,
          "question": "\u8cc7\u6599\u3092\u65e9\u304f\u9001\u3063\u3066\u304f\u308c\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ube68\ub9ac \ubcf4\ub0b4 \uc900 \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_111",
          "number": 111,
          "question": "\u5bb6\u65cf\u304c\u5fdc\u63f4\u3057\u3066\u304f\u308c\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\uac00\uc871\uc774 \uc751\uc6d0\ud574 \uc900 \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067",
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b"
          ],
          "answer": 0,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_112",
          "number": 112,
          "question": "\u5929\u6c17\u304c\u3088\u304b\u3063\u305f\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3088\u308a\u65e9\u304f\u7d42\u308f\u308a\u307e\u3057\u305f\u3002",
          "translation": "\ub0a0\uc528\uac00 \uc88b\uc558\ub358 \ub355\ubd84\uc5d0 \uc608\uc815\ubcf4\ub2e4 \ube68\ub9ac \ub05d\ub0ac\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u3070\u304b\u308a\u306b",
            "\u304a\u304b\u3052\u3067",
            "\u305b\u3044\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u304a\u304b\u3052\u3067",
          "meaning": "\u304a\u304b\u3052\u3067",
          "explanation": "\u301c\u304a\u304b\u3052\u3067 - \uc88b\uc740 \uacb0\uacfc\uc758 \uc6d0\uc778\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_113",
          "number": 113,
          "question": "\u96fb\u8eca\u304c\u9045\u308c\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\uc804\ucca0\uc774 \ub2a6\uc740 \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b",
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067"
          ],
          "answer": 3,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_114",
          "number": 114,
          "question": "\u6e96\u5099\u304c\u8db3\u308a\u306a\u304b\u3063\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\uc900\ube44\uac00 \ubd80\uc871\ud588\ub358 \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067",
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_115",
          "number": 115,
          "question": "\u96e8\u304c\u5f37\u304f\u306a\u3063\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\ube44\uac00 \uac15\ud574\uc9c4 \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b",
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067"
          ],
          "answer": 3,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_116",
          "number": 116,
          "question": "\u4f4f\u6240\u3092\u9593\u9055\u3048\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\uc8fc\uc18c\ub97c \ud2c0\ub9b0 \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067",
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_117",
          "number": 117,
          "question": "\u5bdd\u574a\u3057\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\ub2a6\uc7a0 \uc794 \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b",
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067"
          ],
          "answer": 3,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_118",
          "number": 118,
          "question": "\u30d1\u30bd\u30b3\u30f3\u304c\u58ca\u308c\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\ucef4\ud4e8\ud130\uac00 \uace0\uc7a5 \ub09c \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067",
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_119",
          "number": 119,
          "question": "\u9023\u7d61\u3092\u5fd8\u308c\u305f\uff08\u3000\uff09\u3001\u7d04\u675f\u306e\u6642\u9593\u306b\u9045\u308c\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\ub77d\uc744 \uc78a\uc740 \ud0d3\uc5d0 \uc57d\uc18d \uc2dc\uac04\uc5d0 \ub2a6\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u304b\u3052\u3067",
            "\u305f\u3081\u306b",
            "\u304b\u308f\u308a\u306b",
            "\u305b\u3044\u3067"
          ],
          "answer": 3,
          "point": "\u301c\u305b\u3044\u3067",
          "meaning": "\u305b\u3044\u3067",
          "explanation": "\u301c\u305b\u3044\u3067 - \ub098\uc05c \uacb0\uacfc\uc758 \uc6d0\uc778\uc774\ub098 \ud0d3\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_120",
          "number": 120,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u306e\u306b",
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_121",
          "number": 121,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066",
            "\u305f\u3081\u306b",
            "\u306e\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_122",
          "number": 122,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u306e\u306b",
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_123",
          "number": 123,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066",
            "\u305f\u3081\u306b",
            "\u306e\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_124",
          "number": 124,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u306e\u306b",
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_125",
          "number": 125,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066",
            "\u305f\u3081\u306b",
            "\u306e\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_126",
          "number": 126,
          "question": "\u8cc7\u6599\u3092\u96c6\u3081\u308b\uff08\u3000\uff09\u3001\u56f3\u66f8\u9928\u3078\u884c\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uc790\ub8cc\ub97c \ubaa8\uc73c\uae30 \uc704\ud574 \ub3c4\uc11c\uad00\uc5d0 \uac14\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u305f\u3081\u306b",
            "\u306e\u306b",
            "\u305b\u3044\u3067",
            "\u3068\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u301c\u305f\u3081\u306b",
          "meaning": "\u305f\u3081\u306b",
          "explanation": "\u301c\u305f\u3081\u306b - \ubaa9\uc801 \ub610\ub294 \uac1d\uad00\uc801\uc778 \uc774\uc720\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "time_change_decision",
      "title": "\uc2dc\uac04\u00b7\ubcc0\ud654\u00b7\uacb0\uc815",
      "questions": [
        {
          "id": "gq_127",
          "number": 127,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u3068\u305f\u3093"
          ],
          "answer": 1,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_128",
          "number": 128,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u9593\u306b",
            "\u3068\u305f\u3093",
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_129",
          "number": 129,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u3068\u305f\u3093"
          ],
          "answer": 1,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_130",
          "number": 130,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u9593\u306b",
            "\u3068\u305f\u3093",
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_131",
          "number": 131,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u3068\u305f\u3093"
          ],
          "answer": 1,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_132",
          "number": 132,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u9593\u306b",
            "\u3068\u305f\u3093",
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_133",
          "number": 133,
          "question": "\u5fd8\u308c\u306a\u3044\uff08\u3000\uff09\u3001\u30e1\u30e2\u3057\u3066\u304a\u304d\u307e\u3057\u3087\u3046\u3002",
          "translation": "\uc78a\uc9c0 \uc54a\ub294 \ub3d9\uc548\uc5d0 \uba54\ubaa8\ud574 \ub461\uc2dc\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u3067",
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u3068\u305f\u3093"
          ],
          "answer": 1,
          "point": "\u301c\u3046\u3061\u306b",
          "meaning": "\u3046\u3061\u306b",
          "explanation": "\u301c\u3046\u3061\u306b - \uadf8 \uc0c1\ud0dc\uac00 \uacc4\uc18d\ub418\ub294 \ub3d9\uc548\uc5d0 \ud558\uac70\ub098 \ubcc0\ud654\uac00 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_134",
          "number": 134,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u8cc7\u6599\u3092\u30b3\u30d4\u30fc\u3057\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \uc790\ub8cc\ub97c \ubcf5\uc0ac\ud574 \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u305f\u3093",
            "\u4ee5\u6765",
            "\u9593\u306b",
            "\u3046\u3061\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_135",
          "number": 135,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u90e8\u5c4b\u3092\u4e88\u7d04\u3057\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \ubc29\uc744 \uc608\uc57d\ud574 \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9593\u306b",
            "\u3046\u3061\u306b",
            "\u3068\u305f\u3093",
            "\u4ee5\u6765"
          ],
          "answer": 0,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_136",
          "number": 136,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u7a93\u3092\u958b\u3051\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \ucc3d\ubb38\uc744 \uc5f4\uc5b4 \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u305f\u3093",
            "\u4ee5\u6765",
            "\u9593\u306b",
            "\u3046\u3061\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_137",
          "number": 137,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u4e88\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \uc608\uc815\uc744 \ud655\uc778\ud574 \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9593\u306b",
            "\u3046\u3061\u306b",
            "\u3068\u305f\u3093",
            "\u4ee5\u6765"
          ],
          "answer": 0,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_138",
          "number": 138,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u5bbf\u984c\u3092\u7d42\u308f\u3089\u305b\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \uc219\uc81c\ub97c \ub05d\ub0b4 \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u305f\u3093",
            "\u4ee5\u6765",
            "\u9593\u306b",
            "\u3046\u3061\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_139",
          "number": 139,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u540d\u524d\u3092\u66f8\u3044\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \uc774\ub984\uc744 \uc368 \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9593\u306b",
            "\u3046\u3061\u306b",
            "\u3068\u305f\u3093",
            "\u4ee5\u6765"
          ],
          "answer": 0,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_140",
          "number": 140,
          "question": "\u53cb\u3060\u3061\u3092\u5f85\u3063\u3066\u3044\u308b\uff08\u3000\uff09\u3001\u5f01\u5f53\u3092\u8cb7\u3063\u3066\u304a\u304d\u307e\u3057\u305f\u3002",
          "translation": "\uce5c\uad6c\ub97c \uae30\ub2e4\ub9ac\ub294 \ub3d9\uc548\uc5d0 \ub3c4\uc2dc\ub77d\uc744 \uc0ac \ub450\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u305f\u3093",
            "\u4ee5\u6765",
            "\u9593\u306b",
            "\u3046\u3061\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u9593\u306b",
          "meaning": "\u9593\u306b",
          "explanation": "\u301c\u9593\u306b - \uc5b4\ub5a4 \uae30\uac04 \uc548\uc5d0 \ub2e4\ub978 \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_141",
          "number": 141,
          "question": "\u5bb6\u3092\u51fa\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc9d1\uc744 \ub098\uc120 \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u4ee5\u6765",
            "\u3068\u305f\u3093"
          ],
          "answer": 3,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_142",
          "number": 142,
          "question": "\u99c5\u306b\u7740\u3044\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc5ed\uc5d0 \ub3c4\ucc29\ud55c \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u4ee5\u6765",
            "\u3068\u305f\u3093",
            "\u3046\u3061\u306b",
            "\u9593\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_143",
          "number": 143,
          "question": "\u96fb\u8a71\u3092\u5207\u3063\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc804\ud654\ub97c \ub04a\uc740 \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u4ee5\u6765",
            "\u3068\u305f\u3093"
          ],
          "answer": 3,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_144",
          "number": 144,
          "question": "\u30c9\u30a2\u3092\u958b\u3051\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\ubb38\uc744 \uc5f0 \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u4ee5\u6765",
            "\u3068\u305f\u3093",
            "\u3046\u3061\u306b",
            "\u9593\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_145",
          "number": 145,
          "question": "\u6388\u696d\u304c\u7d42\u308f\u3063\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc218\uc5c5\uc774 \ub05d\ub09c \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u4ee5\u6765",
            "\u3068\u305f\u3093"
          ],
          "answer": 3,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_146",
          "number": 146,
          "question": "\u30e1\u30fc\u30eb\u3092\u9001\u3063\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uba54\uc77c\uc744 \ubcf4\ub0b8 \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u4ee5\u6765",
            "\u3068\u305f\u3093",
            "\u3046\u3061\u306b",
            "\u9593\u306b"
          ],
          "answer": 1,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_147",
          "number": 147,
          "question": "\u5e97\u306b\u5165\u3063\u305f\uff08\u3000\uff09\u3001\u96e8\u304c\u964d\u308a\u51fa\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uac00\uac8c\uc5d0 \ub4e4\uc5b4\uac04 \uc21c\uac04 \ube44\uac00 \ub0b4\ub9ac\uae30 \uc2dc\uc791\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3046\u3061\u306b",
            "\u9593\u306b",
            "\u4ee5\u6765",
            "\u3068\u305f\u3093"
          ],
          "answer": 3,
          "point": "\u301c\u305f\u3068\u305f\u3093",
          "meaning": "\u3068\u305f\u3093",
          "explanation": "\u301c\u305f\u3068\u305f\u3093 - \uc55e \ub3d9\uc791 \uc9c1\ud6c4 \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \uc77c\uc5b4\ub0a8\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_148",
          "number": 148,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_149",
          "number": 149,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057",
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_150",
          "number": 150,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_151",
          "number": 151,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057",
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_152",
          "number": 152,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_153",
          "number": 153,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057",
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_154",
          "number": 154,
          "question": "\u6765\u6708\u304b\u3089\u6bce\u671d\u65e5\u672c\u8a9e\u3092\u52c9\u5f37\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \ub2ec\ubd80\ud130 \ub9e4\uc77c \uc544\uce68 \uc77c\ubcf8\uc5b4\ub97c \uacf5\ubd80\ud558\uae30\ub85c \ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3068\u3053\u308d\u306b\u3057"
          ],
          "answer": 0,
          "point": "\u301c\u3053\u3068\u306b\u3059\u308b",
          "meaning": "\u3053\u3068\u306b\u3057",
          "explanation": "\u301c\u3053\u3068\u306b\u3059\u308b - \ud654\uc790\uc758 \uc758\uc9c0\ub85c \uacb0\uc815\ud55c \uc77c\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_155",
          "number": 155,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057"
          ],
          "answer": 1,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_156",
          "number": 156,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 3,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_157",
          "number": 157,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057"
          ],
          "answer": 1,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_158",
          "number": 158,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 3,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_159",
          "number": 159,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057"
          ],
          "answer": 1,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_160",
          "number": 160,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 3,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_161",
          "number": 161,
          "question": "\u6765\u9031\u3001\u4eac\u90fd\u3078\u51fa\u5f35\u3059\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\ub2e4\uc74c \uc8fc \uad50\ud1a0\ub85c \ucd9c\uc7a5 \uac00\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3088\u3046\u306b\u3057"
          ],
          "answer": 1,
          "point": "\u301c\u3053\u3068\u306b\u306a\u308b",
          "meaning": "\u3053\u3068\u306b\u306a\u308a",
          "explanation": "\u301c\u3053\u3068\u306b\u306a\u308b - \uac1c\uc778 \uc758\uc9c0\ubcf4\ub2e4 \uc815\ud574\uc9c4 \uacb0\uacfc\ub098 \uc608\uc815\uc5d0 \ucd08\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4."
        },
        {
          "id": "gq_162",
          "number": 162,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_163",
          "number": 163,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_164",
          "number": 164,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_165",
          "number": 165,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_166",
          "number": 166,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_167",
          "number": 167,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_168",
          "number": 168,
          "question": "\u7df4\u7fd2\u3057\u3066\u3001\u5c11\u3057\u305a\u3064\u6f22\u5b57\u304c\u8aad\u3081\u308b\uff08\u3000\uff09\u307e\u3057\u305f\u3002",
          "translation": "\uc5f0\uc2b5\ud574\uc11c \uc870\uae08\uc529 \ud55c\uc790\ub97c \uc77d\uc744 \uc218 \uc788\uac8c \ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3053\u3068\u306b\u3057",
            "\u3068\u3053\u308d\u306b\u306a\u308a",
            "\u3088\u3046\u306b\u306a\u308a",
            "\u3053\u3068\u306b\u306a\u308a"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u306b\u306a\u308b",
          "meaning": "\u3088\u3046\u306b\u306a\u308a",
          "explanation": "\u301c\u3088\u3046\u306b\u306a\u308b - \ub2a5\ub825\uc774\ub098 \uc0c1\ud0dc\uc758 \ubcc0\ud654\ub97c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "guess_hearsay",
      "title": "\ucd94\ub7c9\u00b7\uc804\ubb38\u00b7\uc591\ud0dc",
      "questions": [
        {
          "id": "gq_169",
          "number": 169,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u305d\u3046"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_170",
          "number": 170,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306f\u305a",
            "\u305d\u3046",
            "\u3088\u3046",
            "\u3089\u3057\u3044"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_171",
          "number": 171,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u305d\u3046"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_172",
          "number": 172,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306f\u305a",
            "\u305d\u3046",
            "\u3088\u3046",
            "\u3089\u3057\u3044"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_173",
          "number": 173,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u305d\u3046"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_174",
          "number": 174,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u306f\u305a",
            "\u305d\u3046",
            "\u3088\u3046",
            "\u3089\u3057\u3044"
          ],
          "answer": 1,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_175",
          "number": 175,
          "question": "\u7a7a\u304c\u6697\u304f\u3066\u3001\u96e8\u304c\u964d\u308a\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ud558\ub298\uc774 \uc5b4\ub450\uc6cc\uc11c \ube44\uac00 \uc62c \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u305d\u3046"
          ],
          "answer": 3,
          "point": "\u307e\u3059\ud615 + \u305d\u3046\u3060",
          "meaning": "\u305d\u3046",
          "explanation": "\u307e\u3059\ud615 + \u305d\u3046\u3060 - \uac89\ubaa8\uc2b5\uc774\ub098 \uc9d5\uc870\ub97c \ubcf4\uace0 \ud310\ub2e8\ud558\ub294 \uc591\ud0dc \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_176",
          "number": 176,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u59b9\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \uc5ec\ub3d9\uc0dd\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_177",
          "number": 177,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u7530\u4e2d\u3055\u3093\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \ub2e4\ub098\uce74 \uc528\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_178",
          "number": 178,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u90e8\u9577\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \ubd80\uc7a5\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_179",
          "number": 179,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u96a3\u306e\u4eba\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \uc606 \uc0ac\ub78c\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_180",
          "number": 180,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u53cb\u3060\u3061\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \uce5c\uad6c\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_181",
          "number": 181,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u5148\u751f\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \uc120\uc0dd\ub2d8\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_182",
          "number": 182,
          "question": "\u90e8\u5c4b\u304c\u9759\u304b\u3067\u3059\u3002\u7236\u306f\u3082\u3046\u5e30\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc29\uc774 \uc870\uc6a9\ud569\ub2c8\ub2e4. \uc544\ubc84\uc9c0\ub294 \uc774\ubbf8 \ub3cc\uc544\uac04 \uac83 \uac19\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u3088\u3046\u3060",
          "meaning": "\u3088\u3046",
          "explanation": "\u301c\u3088\u3046\u3060 - \uc0c1\ud669\uc774\ub098 \uadfc\uac70\ub97c \ubc14\ud0d5\uc73c\ub85c \ud55c \ucd94\uce21\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_183",
          "number": 183,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 1,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_184",
          "number": 184,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_185",
          "number": 185,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 1,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_186",
          "number": 186,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_187",
          "number": 187,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 1,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_188",
          "number": 188,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3088\u3046",
            "\u305d\u3046",
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044"
          ],
          "answer": 3,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_189",
          "number": 189,
          "question": "\u30cb\u30e5\u30fc\u30b9\u306b\u3088\u308b\u3068\u3001\u660e\u65e5\u306f\u96ea\u304c\u964d\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ub274\uc2a4\uc5d0 \ub530\ub974\uba74 \ub0b4\uc77c\uc740 \ub208\uc774 \uc628\ub2e4\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u3089\u3057\u3044",
            "\u3088\u3046",
            "\u305d\u3046"
          ],
          "answer": 1,
          "point": "\u301c\u3089\u3057\u3044",
          "meaning": "\u3089\u3057\u3044",
          "explanation": "\u301c\u3089\u3057\u3044 - \ub4e4\uc740 \uc815\ubcf4\ub098 \uc804\ud615\uc801\uc778 \uc131\uc9c8\uc744 \ubc14\ud0d5\uc73c\ub85c \ucd94\uce21\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_190",
          "number": 190,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u307f\u305f\u3044",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_191",
          "number": 191,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_192",
          "number": 192,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u307f\u305f\u3044",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_193",
          "number": 193,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_194",
          "number": 194,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u307f\u305f\u3044",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_195",
          "number": 195,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u3089\u3057\u3044",
            "\u306f\u305a"
          ],
          "answer": 0,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_196",
          "number": 196,
          "question": "\u5916\u306b\u4eba\u304c\u96c6\u307e\u3063\u3066\u3044\u307e\u3059\u3002\u4f55\u304b\u4e8b\u6545\u304c\u3042\u3063\u305f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\ubc16\uc5d0 \uc0ac\ub78c\uc774 \ubaa8\uc5ec \uc788\uc2b5\ub2c8\ub2e4. \ubb34\uc2a8 \uc0ac\uace0\uac00 \uc788\uc5c8\ub358 \ubaa8\uc591\uc785\ub2c8\ub2e4.",
          "options": [
            "\u3089\u3057\u3044",
            "\u306f\u305a",
            "\u307f\u305f\u3044",
            "\u305d\u3046"
          ],
          "answer": 2,
          "point": "\u301c\u307f\u305f\u3044\u3060",
          "meaning": "\u307f\u305f\u3044",
          "explanation": "\u301c\u307f\u305f\u3044\u3060 - \ud68c\ud654\uccb4\uc5d0\uc11c \uc0c1\ud669\uc744 \ubcf4\uace0 \uac00\ubccd\uac8c \ucd94\uce21\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_197",
          "number": 197,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u306f\u305a"
          ],
          "answer": 3,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_198",
          "number": 198,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u305d\u3046",
            "\u306f\u305a",
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044"
          ],
          "answer": 1,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_199",
          "number": 199,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u306f\u305a"
          ],
          "answer": 3,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_200",
          "number": 200,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u305d\u3046",
            "\u306f\u305a",
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044"
          ],
          "answer": 1,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_201",
          "number": 201,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u306f\u305a"
          ],
          "answer": 3,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_202",
          "number": 202,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u305d\u3046",
            "\u306f\u305a",
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044"
          ],
          "answer": 1,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_203",
          "number": 203,
          "question": "\u5730\u56f3\u3067\u306f\u99c5\u304b\u3089\u8fd1\u3044\u306e\u3067\u3001\u6b69\u3044\u3066\u5341\u5206\u3067\u7740\u304f\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uc9c0\ub3c4\uc0c1\uc73c\ub85c\ub294 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6b0\ub2c8 \uac78\uc5b4\uc11c 10\ubd84\uc774\uba74 \ub3c4\ucc29\ud560 \uac83\uc785\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u307f\u305f\u3044",
            "\u305d\u3046",
            "\u306f\u305a"
          ],
          "answer": 3,
          "point": "\u301c\u306f\u305a\u3060",
          "meaning": "\u306f\u305a",
          "explanation": "\u301c\u306f\u305a\u3060 - \uadfc\uac70\uac00 \uc788\uc5b4 \ub2f9\uc5f0\ud788 \uadf8\ub7f4 \uac83\uc774\ub77c\uace0 \ud310\ub2e8\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_204",
          "number": 204,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060",
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_205",
          "number": 205,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060",
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060"
          ],
          "answer": 2,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_206",
          "number": 206,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060",
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_207",
          "number": 207,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060",
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060"
          ],
          "answer": 2,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_208",
          "number": 208,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060",
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_209",
          "number": 209,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060",
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060"
          ],
          "answer": 2,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_210",
          "number": 210,
          "question": "\u9053\u304c\u6df7\u3093\u3067\u3044\u308b\u306e\u3067\u3001\u5c11\u3057\u9045\u308c\u308b\uff08\u3000\uff09\u3067\u3059\u3002",
          "translation": "\uae38\uc774 \ub9c9\ud600\uc11c \uc870\uae08 \ub2a6\uc744\uc9c0\ub3c4 \ubaa8\ub985\ub2c8\ub2e4.",
          "options": [
            "\u304b\u3082\u3057\u308c\u306a\u3044",
            "\u306f\u305a\u3060",
            "\u3079\u304d\u3060",
            "\u305d\u3046\u3060"
          ],
          "answer": 0,
          "point": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044",
          "meaning": "\u304b\u3082\u3057\u308c\u306a\u3044",
          "explanation": "\u301c\u304b\u3082\u3057\u308c\u306a\u3044 - \ud655\uc2e4\ud558\uc9c0 \uc54a\uc740 \uac00\ub2a5\uc131\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "particles_context",
      "title": "\uc870\uc0ac\u00b7\ubb38\ub9e5",
      "questions": [
        {
          "id": "gq_211",
          "number": 211,
          "question": "\u79c1\u306f\u3053\u306e\u554f\u984c\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \uc774 \ubb38\uc81c\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_212",
          "number": 212,
          "question": "\u79c1\u306f\u65e5\u672c\u306e\u6587\u5316\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \uc77c\ubcf8 \ubb38\ud654\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_213",
          "number": 213,
          "question": "\u79c1\u306f\u5c06\u6765\u306e\u4ed5\u4e8b\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \uc7a5\ub798\uc758 \uc77c\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_214",
          "number": 214,
          "question": "\u79c1\u306f\u74b0\u5883\u4fdd\u8b77\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \ud658\uacbd \ubcf4\ud638\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_215",
          "number": 215,
          "question": "\u79c1\u306f\u99c5\u524d\u306e\u5de5\u4e8b\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \uc5ed \uc55e \uacf5\uc0ac\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_216",
          "number": 216,
          "question": "\u79c1\u306f\u65b0\u3057\u3044\u5236\u5ea6\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \uc0c8 \uc81c\ub3c4\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 3,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_217",
          "number": 217,
          "question": "\u79c1\u306f\u7559\u5b66\u751f\u6d3b\uff08\u3000\uff09\u8208\u5473\u304c\u3042\u308a\u307e\u3059\u3002",
          "translation": "\uc800\ub294 \uc720\ud559 \uc0dd\ud65c\uc5d0 \uad00\uc2ec\uc774 \uc788\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b",
          "meaning": "\u306b",
          "explanation": "\u301c\u306b\u8208\u5473\u304c\u3042\u308b - \uad00\uc2ec\uc758 \ub300\uc0c1\uc744 \u306b\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_218",
          "number": 218,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u59b9\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \uc5ec\ub3d9\uc0dd\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_219",
          "number": 219,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u7530\u4e2d\u3055\u3093\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \ub2e4\ub098\uce74 \uc528\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 0,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_220",
          "number": 220,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u90e8\u9577\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \ubd80\uc7a5\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_221",
          "number": 221,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u96a3\u306e\u4eba\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \uc606 \uc0ac\ub78c\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 0,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_222",
          "number": 222,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u53cb\u3060\u3061\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \uce5c\uad6c\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_223",
          "number": 223,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u5148\u751f\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \uc120\uc0dd\ub2d8\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u306b",
            "\u3067",
            "\u3092"
          ],
          "answer": 0,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_224",
          "number": 224,
          "question": "\u6c7a\u3081\u308b\u524d\u306b\u7236\uff08\u3000\uff09\u76f8\u8ac7\u3057\u307e\u3059\u3002",
          "translation": "\uacb0\uc815\ud558\uae30 \uc804\uc5d0 \uc544\ubc84\uc9c0\uc640 \uc0c1\ub2f4\ud569\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3092",
            "\u3068",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3068\u76f8\u8ac7\u3059\u308b",
          "meaning": "\u3068",
          "explanation": "\u301c\u3068\u76f8\u8ac7\u3059\u308b - \uc0c1\ub2f4\ud558\uac70\ub098 \ud568\uaed8 \ub9d0\ud558\ub294 \uc0c1\ub300\ub294 \u3068\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_225",
          "number": 225,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u8cc7\u6599\u3092\u30b3\u30d4\u30fc\u3057\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \uc790\ub8cc\ub97c \ubcf5\uc0ac\ud574 \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3092",
            "\u3068",
            "\u3067"
          ],
          "answer": 3,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_226",
          "number": 226,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u90e8\u5c4b\u3092\u4e88\u7d04\u3057\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \ubc29\uc744 \uc608\uc57d\ud574 \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u3067",
            "\u306b",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_227",
          "number": 227,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u7a93\u3092\u958b\u3051\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \ucc3d\ubb38\uc744 \uc5f4\uc5b4 \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3092",
            "\u3068",
            "\u3067"
          ],
          "answer": 3,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_228",
          "number": 228,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u4e88\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \uc608\uc815\uc744 \ud655\uc778\ud574 \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u3067",
            "\u306b",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_229",
          "number": 229,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u5bbf\u984c\u3092\u7d42\u308f\u3089\u305b\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \uc219\uc81c\ub97c \ub05d\ub0b4 \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3092",
            "\u3068",
            "\u3067"
          ],
          "answer": 3,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_230",
          "number": 230,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u540d\u524d\u3092\u66f8\u3044\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \uc774\ub984\uc744 \uc368 \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u3068",
            "\u3067",
            "\u306b",
            "\u3092"
          ],
          "answer": 1,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_231",
          "number": 231,
          "question": "\u56f3\u66f8\u9928\uff08\u3000\uff09\u5f01\u5f53\u3092\u8cb7\u3063\u3066\u304b\u3089\u5e30\u308a\u307e\u3059\u3002",
          "translation": "\ub3c4\uc11c\uad00\uc5d0\uc11c \ub3c4\uc2dc\ub77d\uc744 \uc0ac \ub3cc\uc544\uac11\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3092",
            "\u3068",
            "\u3067"
          ],
          "answer": 3,
          "point": "\u5834\u6240 + \u3067",
          "meaning": "\u3067",
          "explanation": "\u5834\u6240 + \u3067 - \ub3d9\uc791\uc774 \uc774\ub8e8\uc5b4\uc9c0\ub294 \uc7a5\uc18c\ub294 \u3067\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_232",
          "number": 232,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3092",
            "\u306b",
            "\u3067",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_233",
          "number": 233,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3068",
            "\u3092",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_234",
          "number": 234,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3092",
            "\u306b",
            "\u3067",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_235",
          "number": 235,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3068",
            "\u3092",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_236",
          "number": 236,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3092",
            "\u306b",
            "\u3067",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_237",
          "number": 237,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3067",
            "\u3068",
            "\u3092",
            "\u306b"
          ],
          "answer": 2,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_238",
          "number": 238,
          "question": "\u3053\u306e\u753a\u306f\u99c5\uff08\u3000\uff09\u4e2d\u5fc3\u306b\u767a\u5c55\u3057\u307e\u3057\u305f\u3002",
          "translation": "\uc774 \ub9c8\uc744\uc740 \uc5ed\uc744 \uc911\uc2ec\uc73c\ub85c \ubc1c\uc804\ud588\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3092",
            "\u306b",
            "\u3067",
            "\u3068"
          ],
          "answer": 0,
          "point": "\u301c\u3092\u4e2d\u5fc3\u306b",
          "meaning": "\u3092",
          "explanation": "\u301c\u3092\u4e2d\u5fc3\u306b - \uc911\uc2ec\uc774 \ub418\ub294 \ub300\uc0c1\uc744 \u3092\ub85c \ud45c\uc2dc\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_239",
          "number": 239,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u307e\u3067",
            "\u304b\u3089",
            "\u306b",
            "\u3067"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_240",
          "number": 240,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3067",
            "\u307e\u3067",
            "\u304b\u3089"
          ],
          "answer": 3,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_241",
          "number": 241,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u307e\u3067",
            "\u304b\u3089",
            "\u306b",
            "\u3067"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_242",
          "number": 242,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3067",
            "\u307e\u3067",
            "\u304b\u3089"
          ],
          "answer": 3,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_243",
          "number": 243,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u307e\u3067",
            "\u304b\u3089",
            "\u306b",
            "\u3067"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_244",
          "number": 244,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u306b",
            "\u3067",
            "\u307e\u3067",
            "\u304b\u3089"
          ],
          "answer": 3,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_245",
          "number": 245,
          "question": "\u3053\u306e\u30db\u30c6\u30eb\u306f\u99c5\uff08\u3000\uff09\u8fd1\u304f\u3066\u4fbf\u5229\u3067\u3059\u3002",
          "translation": "\uc774 \ud638\ud154\uc740 \uc5ed\uc5d0\uc11c \uac00\uae4c\uc6cc \ud3b8\ub9ac\ud569\ub2c8\ub2e4.",
          "options": [
            "\u307e\u3067",
            "\u304b\u3089",
            "\u306b",
            "\u3067"
          ],
          "answer": 1,
          "point": "\u301c\u304b\u3089\u8fd1\u3044",
          "meaning": "\u304b\u3089",
          "explanation": "\u301c\u304b\u3089\u8fd1\u3044 - \uac70\ub9ac\uc758 \uae30\uc900\uc810\uc740 \u304b\u3089\ub85c \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_246",
          "number": 246,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u304b\u3089",
            "\u307b\u3069",
            "\u307e\u3067\u306b",
            "\u307e\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_247",
          "number": 247,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u307e\u3067\u306b",
            "\u307e\u3067",
            "\u304b\u3089",
            "\u307b\u3069"
          ],
          "answer": 0,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_248",
          "number": 248,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u304b\u3089",
            "\u307b\u3069",
            "\u307e\u3067\u306b",
            "\u307e\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_249",
          "number": 249,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u307e\u3067\u306b",
            "\u307e\u3067",
            "\u304b\u3089",
            "\u307b\u3069"
          ],
          "answer": 0,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_250",
          "number": 250,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u304b\u3089",
            "\u307b\u3069",
            "\u307e\u3067\u306b",
            "\u307e\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_251",
          "number": 251,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u307e\u3067\u306b",
            "\u307e\u3067",
            "\u304b\u3089",
            "\u307b\u3069"
          ],
          "answer": 0,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        },
        {
          "id": "gq_252",
          "number": 252,
          "question": "\u91d1\u66dc\u65e5\uff08\u3000\uff09\u3001\u3053\u306e\u66f8\u985e\u3092\u51fa\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
          "translation": "\uae08\uc694\uc77c\uae4c\uc9c0 \uc774 \uc11c\ub958\ub97c \uc81c\ucd9c\ud574 \uc8fc\uc138\uc694.",
          "options": [
            "\u304b\u3089",
            "\u307b\u3069",
            "\u307e\u3067\u306b",
            "\u307e\u3067"
          ],
          "answer": 2,
          "point": "\u301c\u307e\u3067\u306b",
          "meaning": "\u307e\u3067\u306b",
          "explanation": "\u301c\u307e\u3067\u306b - \ub9c8\uac10 \uc2dc\uc810 \uc774\uc804\uae4c\uc9c0 \uc644\ub8cc\ud574\uc57c \ud568\uc744 \ub098\ud0c0\ub0c5\ub2c8\ub2e4."
        }
      ]
    },
    {
      "id": "honorifics_giving",
      "title": "\uacbd\uc5b4\u00b7\uc218\uc218\ud45c\ud604",
      "questions": [
        {
          "id": "gq_253",
          "number": 253,
          "question": "\u79c1\u304c\u5148\u751f\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \uc120\uc0dd\ub2d8\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059",
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_254",
          "number": 254,
          "question": "\u79c1\u304c\u90e8\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \ubd80\uc7a5\ub2d8\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059",
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_255",
          "number": 255,
          "question": "\u79c1\u304c\u793e\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \uc0ac\uc7a5\ub2d8\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059",
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_256",
          "number": 256,
          "question": "\u79c1\u304c\u304a\u5ba2\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \uc190\ub2d8\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059",
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_257",
          "number": 257,
          "question": "\u79c1\u304c\u5c71\u7530\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \uc57c\ub9c8\ub2e4 \ub2d8\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059",
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_258",
          "number": 258,
          "question": "\u79c1\u304c\u5148\u8f29\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \uc120\ubc30\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059",
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_259",
          "number": 259,
          "question": "\u79c1\u304c\u62c5\u5f53\u8005\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc81c\uac00 \ub2f4\ub2f9\uc790\uaed8 \uc124\uba85\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u8aac\u660e\u306b\u306a\u308a\u307e\u3059",
            "\u8aac\u660e\u3055\u308c\u307e\u3059",
            "\u8aac\u660e\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3054\u8aac\u660e\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b",
          "meaning": "\u3054\u8aac\u660e\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3059\u308b - \uc790\uc2e0 \ub610\ub294 \uc790\uae30 \ucabd \ub3d9\uc791\uc744 \ub0ae\ucdb0 \uc0c1\ub300\ub97c \ub192\uc774\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_260",
          "number": 260,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u5148\u751f\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \uc120\uc0dd\ub2d8\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059",
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_261",
          "number": 261,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u90e8\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \ubd80\uc7a5\ub2d8\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059",
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_262",
          "number": 262,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u793e\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \uc0ac\uc7a5\ub2d8\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059",
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_263",
          "number": 263,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u304a\u5ba2\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \uc190\ub2d8\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059",
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_264",
          "number": 264,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u5c71\u7530\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \uc57c\ub9c8\ub2e4 \ub2d8\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059",
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_265",
          "number": 265,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u5148\u8f29\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \uc120\ubc30\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059",
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_266",
          "number": 266,
          "question": "\u5f8c\u307b\u3069\u3001\u3053\u3061\u3089\u304b\u3089\u62c5\u5f53\u8005\u306b\uff08\u3000\uff09\u3002",
          "translation": "\ub098\uc911\uc5d0 \uc774\ucabd\uc5d0\uc11c \ub2f4\ub2f9\uc790\uaed8 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
            "\u3054\u9023\u7d61\u306b\u306a\u308a\u307e\u3059",
            "\u3054\u9023\u7d61\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u9023\u7d61\u3055\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059",
          "meaning": "\u3054\u9023\u7d61\u3044\u305f\u3057\u307e\u3059",
          "explanation": "\u304a/\u3054 + \u307e\u3059\ud615 + \u3044\u305f\u3059 - \u3059\u308b\ubcf4\ub2e4 \ub354 \uacf5\uc190\ud55c \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_267",
          "number": 267,
          "question": "\u6628\u65e5\u3001\u5148\u751f\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \uc120\uc0dd\ub2d8\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_268",
          "number": 268,
          "question": "\u6628\u65e5\u3001\u90e8\u9577\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \ubd80\uc7a5\ub2d8\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_269",
          "number": 269,
          "question": "\u6628\u65e5\u3001\u793e\u9577\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \uc0ac\uc7a5\ub2d8\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_270",
          "number": 270,
          "question": "\u6628\u65e5\u3001\u304a\u5ba2\u69d8\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \uc190\ub2d8\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_271",
          "number": 271,
          "question": "\u6628\u65e5\u3001\u5c71\u7530\u69d8\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \uc57c\ub9c8\ub2e4 \ub2d8\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_272",
          "number": 272,
          "question": "\u6628\u65e5\u3001\u5148\u8f29\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \uc120\ubc30\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f"
          ],
          "answer": 3,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_273",
          "number": 273,
          "question": "\u6628\u65e5\u3001\u62c5\u5f53\u8005\u306b\u99c5\u307e\u3067\uff08\u3000\uff09\u3002",
          "translation": "\uc5b4\uc81c \ub2f4\ub2f9\uc790\uaed8 \uc5ed\uae4c\uc9c0 \ubc14\ub798\ub2e4 \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u9001\u3063\u3066\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u9001\u3063\u3066\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u301c\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u9001\u3063\u3066\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u301c\u3066\u3044\u305f\u3060\u304f - \uc717\uc0ac\ub78c\uc774 \ud574 \uc900 \uc77c\uc744 \ub0b4\uac00 \ubc1b\uc740 \uc785\uc7a5\uc5d0\uc11c \ub0ae\ucdb0 \ub9d0\ud558\ub294 \uacb8\uc591 \ud45c\ud604\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_274",
          "number": 274,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_275",
          "number": 275,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_276",
          "number": 276,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_277",
          "number": 277,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_278",
          "number": 278,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_279",
          "number": 279,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_280",
          "number": 280,
          "question": "\u4e88\u5b9a\u3092\u5c11\u3057\uff08\u3000\uff09\u3002",
          "translation": "\uc608\uc815\uc744 \uc870\uae08 \ubcc0\uacbd\ud558\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5909\u66f4\u306a\u3055\u3044\u307e\u3059",
            "\u5909\u66f4\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u5909\u66f4\u3057\u3066\u304f\u3060\u3055\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f",
          "meaning": "\u5909\u66f4\u3055\u305b\u3066\u3044\u305f\u3060\u304d\u307e\u3059",
          "explanation": "\u301c\u3055\u305b\u3066\u3044\u305f\u3060\u304f - \uc0c1\ub300\uc758 \ud5c8\ub77d\uc774\ub098 \uc591\ud574\ub97c \uc804\uc81c\ub85c \ub0b4\uac00 \ud558\uaca0\ub2e4\uace0 \uacf5\uc190\ud788 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_281",
          "number": 281,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u4f1a\u793e\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \ud68c\uc0ac\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_282",
          "number": 282,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u4f1a\u5834\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \ud68c\uc7a5\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_283",
          "number": 283,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u53d7\u4ed8\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \uc811\uc218\ucc98\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_284",
          "number": 284,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u99c5\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \uc5ed\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_285",
          "number": 285,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u305d\u3061\u3089\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \uadf8\ucabd\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_286",
          "number": 286,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u7814\u7a76\u5ba4\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \uc5f0\uad6c\uc2e4\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_287",
          "number": 287,
          "question": "\u660e\u65e5\u306e\u4e09\u6642\u306b\u4e8b\u52d9\u6240\u3078\uff08\u3000\uff09\u3002",
          "translation": "\ub0b4\uc77c 3\uc2dc\uc5d0 \uc0ac\ubb34\uc2e4\ub85c \ucc3e\uc544\ubd59\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u53c2\u3089\u308c\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u3044\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u4f3a\u3046",
          "meaning": "\u4f3a\u3044\u307e\u3059",
          "explanation": "\u4f3a\u3046 - \u884c\u304f/\u6765\u308b/\u805e\u304f/\u5c0b\u306d\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \ubc29\ubb38\ud558\uac70\ub098 \uc5ec\ucb59\ub294 \ub3d9\uc791\uc5d0 \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_288",
          "number": 288,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u4f1a\u793e\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \ud68c\uc0ac\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_289",
          "number": 289,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u4f1a\u5834\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \ud68c\uc7a5\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059",
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_290",
          "number": 290,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u53d7\u4ed8\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \uc811\uc218\ucc98\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_291",
          "number": 291,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u99c5\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \uc5ed\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059",
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_292",
          "number": 292,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u305d\u3061\u3089\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \uadf8\ucabd\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_293",
          "number": 293,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u7814\u7a76\u5ba4\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \uc5f0\uad6c\uc2e4\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059",
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_294",
          "number": 294,
          "question": "\u5348\u5f8c\u3001\u79c1\u304c\u4e8b\u52d9\u6240\u3078\uff08\u3000\uff09\u3002",
          "translation": "\uc624\ud6c4\uc5d0 \uc81c\uac00 \uc0ac\ubb34\uc2e4\ub85c \uac00\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53c2\u308a\u307e\u3059",
            "\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u304a\u8d8a\u3057\u306b\u306a\u308a\u307e\u3059",
            "\u4f3a\u308f\u308c\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u53c2\u308b",
          "meaning": "\u53c2\u308a\u307e\u3059",
          "explanation": "\u53c2\u308b - \u884c\u304f/\u6765\u308b\uc758 \uacb8\uc591\uc5b4\ub85c, \uc790\uae30 \ucabd \uc774\ub3d9\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_295",
          "number": 295,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u7530\u4e2d\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u7530\u4e2d\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_296",
          "number": 296,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u5c71\u672c\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u5c71\u672c\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_297",
          "number": 297,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u9234\u6728\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u9234\u6728\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_298",
          "number": 298,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u4f50\u85e4\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u4f50\u85e4\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_299",
          "number": 299,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u4e2d\u6751\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u4e2d\u6751\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_300",
          "number": 300,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u5c0f\u6797\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u5c0f\u6797\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_301",
          "number": 301,
          "question": "\u306f\u3058\u3081\u307e\u3057\u3066\u3001\u9ad8\u6a4b\u3068\uff08\u3000\uff09\u3002",
          "translation": "\ucc98\uc74c \ubd59\uaca0\uc2b5\ub2c8\ub2e4, \u9ad8\u6a4b\ub77c\uace0 \ud569\ub2c8\ub2e4.",
          "options": [
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u7533\u3059",
          "meaning": "\u7533\u3057\u307e\u3059",
          "explanation": "\u7533\u3059 - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc774\ub984\uc744 \ub9d0\ud560 \ub54c \uc790\uc8fc \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_302",
          "number": 302,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u5148\u751f\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \uc120\uc0dd\ub2d8\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_303",
          "number": 303,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u90e8\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \ubd80\uc7a5\ub2d8\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_304",
          "number": 304,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u793e\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \uc0ac\uc7a5\ub2d8\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_305",
          "number": 305,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u304a\u5ba2\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \uc190\ub2d8\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_306",
          "number": 306,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u5c71\u7530\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \uc57c\ub9c8\ub2e4 \ub2d8\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_307",
          "number": 307,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u5148\u8f29\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \uc120\ubc30\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059",
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059"
          ],
          "answer": 0,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_308",
          "number": 308,
          "question": "\u8a73\u3057\u3044\u7406\u7531\u306f\u3001\u3042\u3068\u3067\u62c5\u5f53\u8005\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc790\uc138\ud55c \uc774\uc720\ub294 \ub098\uc911\uc5d0 \ub2f4\ub2f9\uc790\uaed8 \ub9d0\uc500\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u7533\u3057\u307e\u3059",
            "\u3046\u304b\u304c\u3044\u307e\u3059",
            "\u7533\u3057\u4e0a\u3052\u307e\u3059",
            "\u304a\u3063\u3057\u3083\u3044\u307e\u3059"
          ],
          "answer": 2,
          "point": "\u7533\u3057\u4e0a\u3052\u308b",
          "meaning": "\u7533\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u7533\u3057\u4e0a\u3052\u308b - \u8a00\u3046\uc758 \uacb8\uc591\uc5b4\ub85c, \uc0c1\ub300\uc5d0\uac8c \ub9d0\uc500\ub4dc\ub9b0\ub2e4\ub294 \ubc29\ud5a5\uc131\uc774 \uac15\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_309",
          "number": 309,
          "question": "\u3053\u306e\u8cc7\u6599\u3092\u5148\u751f\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \uc790\ub8cc\ub97c \uc120\uc0dd\ub2d8\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_310",
          "number": 310,
          "question": "\u3053\u306e\u6848\u5185\u72b6\u3092\u90e8\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \uc548\ub0b4\uc7a5\ub97c \ubd80\uc7a5\ub2d8\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_311",
          "number": 311,
          "question": "\u3053\u306e\u30e1\u30fc\u30eb\u3092\u793e\u9577\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \uba54\uc77c\ub97c \uc0ac\uc7a5\ub2d8\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_312",
          "number": 312,
          "question": "\u3053\u306e\u5546\u54c1\u3092\u304a\u5ba2\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \uc0c1\ud488\ub97c \uc190\ub2d8\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_313",
          "number": 313,
          "question": "\u3053\u306e\u5831\u544a\u66f8\u3092\u5c71\u7530\u69d8\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \ubcf4\uace0\uc11c\ub97c \uc57c\ub9c8\ub2e4 \ub2d8\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_314",
          "number": 314,
          "question": "\u3053\u306e\u5199\u771f\u3092\u5148\u8f29\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \uc0ac\uc9c4\ub97c \uc120\ubc30\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059"
          ],
          "answer": 1,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_315",
          "number": 315,
          "question": "\u3053\u306e\u540d\u523a\u3092\u62c5\u5f53\u8005\u306b\uff08\u3000\uff09\u3002",
          "translation": "\uc774 \uba85\ud568\ub97c \ub2f4\ub2f9\uc790\uaed8 \ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u304f\u3060\u3055\u3044\u307e\u3059",
            "\u3044\u305f\u3060\u304d\u307e\u3059",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3059",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3059"
          ],
          "answer": 3,
          "point": "\u5dee\u3057\u4e0a\u3052\u308b",
          "meaning": "\u5dee\u3057\u4e0a\u3052\u307e\u3059",
          "explanation": "\u5dee\u3057\u4e0a\u3052\u308b - \u3042\u3052\u308b\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \ub0b4\uac00 \uc717\uc0ac\ub78c\uc774\ub098 \uc190\ub2d8\uc5d0\uac8c \ub4dc\ub9b4 \ub54c \uc501\ub2c8\ub2e4."
        },
        {
          "id": "gq_316",
          "number": 316,
          "question": "\u5148\u751f\u304b\u3089\u8cc7\u6599\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc120\uc0dd\ub2d8\uaed8 \uc790\ub8cc\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f"
          ],
          "answer": 0,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_317",
          "number": 317,
          "question": "\u90e8\u9577\u304b\u3089\u6848\u5185\u72b6\u3092\uff08\u3000\uff09\u3002",
          "translation": "\ubd80\uc7a5\ub2d8\uaed8 \uc548\ub0b4\uc7a5\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f"
          ],
          "answer": 2,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_318",
          "number": 318,
          "question": "\u793e\u9577\u304b\u3089\u30e1\u30fc\u30eb\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc0ac\uc7a5\ub2d8\uaed8 \uba54\uc77c\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f"
          ],
          "answer": 0,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_319",
          "number": 319,
          "question": "\u304a\u5ba2\u69d8\u304b\u3089\u5546\u54c1\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc190\ub2d8\uaed8 \uc0c1\ud488\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f"
          ],
          "answer": 2,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_320",
          "number": 320,
          "question": "\u5c71\u7530\u69d8\u304b\u3089\u5831\u544a\u66f8\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc57c\ub9c8\ub2e4 \ub2d8\uaed8 \ubcf4\uace0\uc11c\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f"
          ],
          "answer": 0,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_321",
          "number": 321,
          "question": "\u5148\u8f29\u304b\u3089\u5199\u771f\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc120\ubc30\uaed8 \uc0ac\uc9c4\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f"
          ],
          "answer": 2,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_322",
          "number": 322,
          "question": "\u62c5\u5f53\u8005\u304b\u3089\u540d\u523a\u3092\uff08\u3000\uff09\u3002",
          "translation": "\ub2f4\ub2f9\uc790\uaed8 \uba85\ud568\ub97c \ubc1b\uc558\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f"
          ],
          "answer": 0,
          "point": "\u3044\u305f\u3060\u304f",
          "meaning": "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
          "explanation": "\u3044\u305f\u3060\u304f - \u3082\u3089\u3046\uc758 \uacb8\uc591\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc5d0\uac8c\uc11c \ubc1b\ub294 \uc77c\uc744 \ub0ae\ucdb0 \ub9d0\ud569\ub2c8\ub2e4."
        },
        {
          "id": "gq_323",
          "number": 323,
          "question": "\u5148\u751f\u304c\u8cc7\u6599\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc120\uc0dd\ub2d8\uaed8\uc11c \uc790\ub8cc\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_324",
          "number": 324,
          "question": "\u90e8\u9577\u304c\u6848\u5185\u72b6\u3092\uff08\u3000\uff09\u3002",
          "translation": "\ubd80\uc7a5\ub2d8\uaed8\uc11c \uc548\ub0b4\uc7a5\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f"
          ],
          "answer": 3,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_325",
          "number": 325,
          "question": "\u793e\u9577\u304c\u30e1\u30fc\u30eb\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc0ac\uc7a5\ub2d8\uaed8\uc11c \uba54\uc77c\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_326",
          "number": 326,
          "question": "\u304a\u5ba2\u69d8\u304c\u5546\u54c1\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc190\ub2d8\uaed8\uc11c \uc0c1\ud488\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f"
          ],
          "answer": 3,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_327",
          "number": 327,
          "question": "\u5c71\u7530\u69d8\u304c\u5831\u544a\u66f8\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc57c\ub9c8\ub2e4 \ub2d8\uaed8\uc11c \ubcf4\uace0\uc11c\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_328",
          "number": 328,
          "question": "\u5148\u8f29\u304c\u5199\u771f\u3092\uff08\u3000\uff09\u3002",
          "translation": "\uc120\ubc30\uaed8\uc11c \uc0ac\uc9c4\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f",
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f"
          ],
          "answer": 3,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_329",
          "number": 329,
          "question": "\u62c5\u5f53\u8005\u304c\u540d\u523a\u3092\uff08\u3000\uff09\u3002",
          "translation": "\ub2f4\ub2f9\uc790\uaed8\uc11c \uba85\ud568\ub97c \uc8fc\uc168\uc2b5\ub2c8\ub2e4.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u308a\u307e\u3057\u305f",
            "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
            "\u3044\u305f\u3060\u304d\u307e\u3057\u305f",
            "\u5dee\u3057\u4e0a\u3052\u307e\u3057\u305f"
          ],
          "answer": 1,
          "point": "\u304f\u3060\u3055\u308b",
          "meaning": "\u304f\u3060\u3055\u3044\u307e\u3057\u305f",
          "explanation": "\u304f\u3060\u3055\u308b - \u304f\u308c\u308b\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc717\uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \ud574 \uc8fc\uac70\ub098 \uc8fc\ub294 \uc77c\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_330",
          "number": 330,
          "question": "\u3069\u3046\u305e\u3001\u304a\u8336\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u304a\u8336\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066",
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_331",
          "number": 331,
          "question": "\u3069\u3046\u305e\u3001\u30b1\u30fc\u30ad\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u30b1\u30fc\u30ad\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066",
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_332",
          "number": 332,
          "question": "\u3069\u3046\u305e\u3001\u663c\u98df\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u663c\u98df\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066",
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_333",
          "number": 333,
          "question": "\u3069\u3046\u305e\u3001\u30b3\u30fc\u30d2\u30fc\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u30b3\u30fc\u30d2\u30fc\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066",
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_334",
          "number": 334,
          "question": "\u3069\u3046\u305e\u3001\u6599\u7406\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u6599\u7406\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066",
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_335",
          "number": 335,
          "question": "\u3069\u3046\u305e\u3001\u304a\u5f01\u5f53\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u304a\u5f01\u5f53\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066",
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066"
          ],
          "answer": 0,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
        },
        {
          "id": "gq_336",
          "number": 336,
          "question": "\u3069\u3046\u305e\u3001\u679c\u7269\u3092\uff08\u3000\uff09\u304f\u3060\u3055\u3044\u3002",
          "translation": "\ubd80\ub514 \u679c\u7269\ub97c \ub4dc\uc138\uc694.",
          "options": [
            "\u5dee\u3057\u4e0a\u3052\u3066",
            "\u7533\u3057\u3066",
            "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
            "\u3044\u305f\u3060\u3044\u3066"
          ],
          "answer": 2,
          "point": "\u53ec\u3057\u4e0a\u304c\u308b",
          "meaning": "\u53ec\u3057\u4e0a\u304c\u3063\u3066",
          "explanation": "\u53ec\u3057\u4e0a\u304c\u308b - \u98df\u3079\u308b/\u98f2\u3080\uc758 \uc874\uacbd\uc5b4\uc785\ub2c8\ub2e4. \uc0c1\ub300\uac00 \uba39\uac70\ub098 \ub9c8\uc2dc\ub294 \ub3d9\uc791\uc744 \ub192\uc785\ub2c8\ub2e4."
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
