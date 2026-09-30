# 파이썬 공간데이터 사이언스 — GeoPandas에서 Spatial AI까지

navicoby.github.io에 연결하는 학습·출판 프로젝트입니다. 2026-09-30 공개 초안 v0.1. 10부 35장 목차와 샘플 3장, 데이터 수집·환경·GeoAI/BIM 안내를 포함합니다.

## 바로 보기

- 발행 주소: https://navicoby.github.io/python-geospatial/
- 집필 스킬: `../../.agents/skills/navicoby-geospatial-author/SKILL.md`
- 집필 규칙: `CONTRIBUTING.md`
- 모바일 가이드: `../../.agents/skills/navicoby-geospatial-author/references/mobile.md`
- 원본 목차: `pages/roadmap.md`

샘플은 버퍼·공간조인, DEM 경사도, Sentinel-2/NDVI입니다. 외부 자료 접근 없이 실행할 수 있는 합성 데이터와 실제 자료로 옮기는 절차를 분리했습니다. Sentinel-2 실제 원본 취득 및 PyTorch 학습은 이번 실행 검증 범위에 포함하지 않았습니다.

## 기존 저장소 검사 결과

검사 기준 commit: `538cf951be7cc60e97bee27bb91a15e55dd830cc` (main).

- `hugo.toml`: Hugo, PaperMod theme, baseURL `https://navicoby.github.io/`.
- `layouts/index.html`: 별도 메인 템플릿, Literature/Projects/Notes로 정적 학습 콘텐츠 연결.
- `static/`: 독립 HTML 학습서·연구 프로젝트가 공존.
- `.github/workflows/deploy.yml`: main push → Hugo → 정적 페이지 메인 연결 검사 → gh-pages 배포.
- `scripts/check_static_navigation.py`: 최상위 정적 페이지의 메인 링크와 빌드 포함 여부 검사.
- 새 섹션은 기존 패턴의 `static/python-geospatial/`을 사용하며 메인 Literature에 링크를 추가합니다. 기존 PaperMod와 배포 workflow는 유지합니다.

## 실제 파일 구조

```text
.agents/skills/navicoby-geospatial-author/
  SKILL.md
  references/{chapter-template,mobile,sources}.md
books/python-geospatial/
  README.md  CONTRIBUTING.md  QA.md
  pages.json
  pages/
    index.md  roadmap.md  data-sources.md  stack.md  geoai-bridge.md
    chapters/{buffer-join,dem-slope,sentinel2-ndvi}.md
  examples/{buffer_join,dem_slope,sentinel2_ndvi,test_analysis}.py
  templates/page.html
  requirements.txt  requirements-build.txt  requirements-lock.txt
scripts/geospatial/{build,check}.py
static/python-geospatial/
  index.html  roadmap.html  data-sources.html  stack.html  geoai-bridge.html
  chapters/*.html
  assets/{book.css,book.js,learning-path.svg,buffer.svg,terrain.svg,ndvi.svg}
  maps/park-map.html
  examples/*.py, requirements*.txt
layouts/index.html  # 메인 진입 링크 추가
```

Markdown이 집필 원본이며 빌더가 HTML을 생성합니다. CSS/JS/SVG 개념도는 `static`의 공통 자산을 직접 관리합니다. 계산 그림과 Folium 지도는 실행 예제로 다시 생성합니다. Hugo 빌드에서는 Python 실행이나 데이터 다운로드가 필요하지 않습니다.

## 재현과 빌드

저장소 루트에서 Python 3.13 가상환경을 만듭니다. Windows는 `.venv/Scripts/python.exe`, macOS/Linux는 `.venv/bin/python`을 사용합니다. 아래 `python`은 활성 환경의 실행 파일을 뜻합니다.

```text
python -m pip install -r books/python-geospatial/requirements.txt
python -m pip install -r books/python-geospatial/requirements-build.txt
python books/python-geospatial/examples/buffer_join.py --out generated/vector
python books/python-geospatial/examples/dem_slope.py --out generated/terrain
python books/python-geospatial/examples/sentinel2_ndvi.py --demo --out generated/satellite
python -m pytest books/python-geospatial/examples/test_analysis.py -q
python scripts/geospatial/build.py
hugo --minify
python scripts/check_static_navigation.py --public public
python scripts/geospatial/check.py --public public
```

계산 그림을 바꾼 경우 `generated/vector/buffer.svg`, `generated/terrain/terrain.svg`, `generated/satellite/ndvi.svg`를 `static/python-geospatial/assets/`에, `generated/vector/park-map.html`을 `static/python-geospatial/maps/`에 복사한 뒤 빌드합니다. 실제 공공데이터 원본·인증키는 static에 복사하지 않습니다.

로컬 미리보기: `hugo server` 후 표시된 주소에서 `/python-geospatial/`을 엽니다. PaperMod submodule이 비어 있다면 `git submodule update --init --recursive`를 먼저 실행합니다.

`requirements-lock.txt`는 이번 Windows 환경의 전체 설치 목록입니다. 다른 OS에서는 상위 requirements로 새 환경을 만든 뒤 실행 검증하고 별도 lock을 기록합니다. PyTorch 설치는 사용할 CPU/GPU·CUDA 환경에 맞게 공식 설치 안내에서 선택합니다.

## 새 챕터 요청 예시

> $navicoby-geospatial-author 스킬을 사용해 25장 ‘공원 출입구까지의 보행거리’를 작성하라. 한국 공공 공원 데이터와 OSMnx를 사용하고, 작은 오프라인 그래프 예제와 실제 자료 취득 확장을 구분하라. 현재 저장소 구조를 확인한 뒤 목차와 모바일 페이지를 갱신하라.

저장소의 `.agents/skills/`를 인식하는 환경에서는 프로젝트 스킬로 사용합니다. 다른 ChatGPT Work 환경에서는 `SKILL.md`와 `references/`를 함께 제공하고 해당 스킬을 적용하도록 요청합니다. 특정 앱의 자동 설치·발견을 이 파일만으로 보장하지 않습니다.

## 출처와 권리

조사 링크와 확인 범위는 발행되는 `data-sources.md`, `stack.md` 및 각 장에 있습니다. 코드·그림의 합성 데이터는 이 프로젝트를 위해 작성했습니다. 외부 기관의 실제 데이터가 포함됐다고 표기하지 않습니다. OSM 배경지도는 attribution과 타일 정책을 따릅니다. 프로젝트 전체에 새로운 포괄적 오픈 라이선스를 임의로 부여하지 않았습니다. 외부 자료의 이용조건은 해당 자료에 따릅니다.
