# JLPT Subtitle Static Web App

이 프로젝트는 `로컬에서 자막 -> 학습용 데이터/정적 사이트 생성`을 하고, 생성된 `site/` 폴더를 GitHub에 커밋해서 Pages로 배포하는 구조입니다.

## 흐름

1. `input_script/` 에 `.srt` 자막 파일을 넣습니다.
2. 필요하면 `web_sync_offsets.json` 에 작품별 기본 sync 값을 적습니다.
3. 로컬에서 `python build_webapp.py` 를 실행합니다.
4. 생성된 `site/` 폴더까지 함께 커밋하고 push 합니다.
5. GitHub Actions 는 `site/` 를 그대로 GitHub Pages 에 배포합니다.

## 로컬 생성

```bash
pip install -r requirements.txt
python build_webapp.py
```

자주 쓰는 옵션:

```bash
python build_webapp.py --disable-translation
python build_webapp.py --rebuild-db
python build_webapp.py --only "Bocchi the Rock! - S01E01.srt"
```

## 남겨둔 주요 폴더/파일

- `input_script/`: 원본 자막
- `_N3/`: JLPT 기준 자료
- `site_src/`: 웹앱 템플릿
- `site/`: 배포용 결과물
- `build_webapp.py`: 로컬 빌드 스크립트
- `.github/workflows/deploy-pages.yml`: 배포 워크플로
- `web_sync_offsets.json`: 작품별 기본 sync 값

## 웹앱 기능

- 작품 목록 클릭 재생
- 현재 문장 / 해석 크게 표시
- N5~N3 단어, 문법, 문형 하이라이트
- 다음 JLPT 포인트까지 남은 시간 표시
- sync 조절
- 기기별 localStorage sync 저장
- 휴대폰 가로 보기용 90도 회전

## 참고

- `site/` 는 로컬에서 만든 뒤 커밋하는 대상입니다.
- GitHub Actions 는 빌드가 아니라 배포만 담당합니다.
- 번역은 네트워크 상태에 따라 실패할 수 있습니다.
