# 디지털 조경학 · Digital Landscape Architecture

김수영 저자의 출간 준비 원고를 읽는 독립 웹판입니다. 공개 경로는 `/digital-landscape-architecture/`입니다.

## 원고와 웹 표시의 분리

- `manuscript.md`: 저자가 지정한 Google Drive Markdown 원고의 원본 스냅샷입니다. 해시가 `source-manifest.json`과 일치해야 빌드합니다.
- `review-pages.json`: 저자가 지정한 189쪽 검토보완 PDF의 텍스트, 목차와 링크입니다. 원본 PDF 자체는 이 폴더에 포함하지 않습니다.
- `figures.json`: 원고의 그림 참조, PDF 쪽수와 웹 이미지의 대응표입니다. 실제 이미지 50개는 `static/digital-landscape-architecture/assets/figures/`에 있습니다. PDF 이미지를 무손실 WebP로 변환했습니다. 원래 SVG 소스가 제공된 것으로 표시하지 않습니다.
- `supplements.json`: PDF 6–14장의 추가 설명 9개를 원문 그대로 전사하고 해당 페이지 및 삽입 위치를 기록했습니다. 생성된 페이지에서도 PDF 보완 설명으로 구분합니다.

웹 변환은 원고의 장·단위·문단·표·코드·참고문헌을 유지합니다. Pandoc 편집 속성, 내부 링크와 웹 접근성을 위한 표시만 변환합니다. 원고에 언급된 별도 실행파일은 제공되지 않았으므로 다운로드 링크를 만들지 않습니다. 단순 계산과 미실행 실험에 관한 원고의 한정 조건을 지우지 않습니다.

## 빌드

Python 3.12 이상에서 다음을 실행합니다.

```sh
python -m pip install markdown-it-py==4.2.0 beautifulsoup4==4.14.3
python scripts/build_digital_landscape.py
python tests/test_digital_landscape.py
hugo --minify
python scripts/apply_site_chrome.py --public public
python scripts/build_digital_landscape.py --register-home public/index.html
```

15개 장별 페이지, 책 소개, 참고문헌, 도판 목록, 판본 안내의 19개 페이지와 63단위 검색 색인을 생성합니다. GitHub Actions 배포 과정에서도 같은 빌더와 검사를 실행합니다. 생성 HTML을 직접 고치기보다 원고·보완 설명 또는 빌더를 고쳐 다시 생성합니다.

새 원고로 교체할 때에는 기존 스냅샷과 비교해 저자의 개정을 확인한 뒤 판본·해시·장 구성·도판 대응을 함께 갱신합니다. 내용이 바뀌었는데 해시 검사만 우회하지 않습니다. 출판용 교정, 사실 검증, 미제공 실험자료의 확인은 웹 표시 변환과 별도 작업입니다.

## 화면과 권리

기존 SPATIALFLARE 로고 및 공통 메뉴를 사용하고 밝은 배경 `#f5f6f2`와 어두운 본문을 유지합니다. 모바일 목차, 글자 크기 조절, 전체 본문 검색, 도판 확대가 있습니다. 노트 입력·저장·분석 추적 기능은 없습니다.

저자 원고의 권리는 저자에게 있습니다. 외부 문헌과 인용 자료는 각각 원고에 표시된 출처와 권리관계를 따르며 이 README가 별도 재이용 허락을 부여하지 않습니다. Google Drive 원본 및 공유 권한은 변경하지 않았습니다.
