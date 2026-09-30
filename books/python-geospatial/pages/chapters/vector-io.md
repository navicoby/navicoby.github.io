---
title: "05 · 공간 파일 입출력과 GeoParquet"
description: "공간 자료를 파일로 저장하고 다시 읽으며 형식마다 보존되는 정보를 비교합니다."
eyebrow: "PART 02 / CHAPTER 05"
---

**학습 목표:** 공간 자료를 파일로 저장하고 다시 읽으며 형식마다 보존되는 정보를 비교합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

파일 형식은 데이터를 저장하는 규칙입니다. GeoPackage(.gpkg)는 한 파일에 여러 벡터 레이어를 담을 수 있는 SQLite 기반 형식이고, GeoJSON은 웹에서 널리 쓰는 JSON 기반 형식입니다. Shapefile은 .shp뿐 아니라 .shx·.dbf·.prj 등 여러 파일이 함께 움직이는 오래된 형식입니다. GeoParquet은 열 단위 저장 형식인 Parquet에 공간 정보를 담는 규약으로, 속성 분석과 대량 자료 저장에 유용합니다.

GeoPandas의 read_file/to_file은 공간 파일 입출력 창구입니다. pyogrio는 GDAL/OGR를 통해 실제 읽기와 쓰기를 수행하는 엔진이고, pyarrow는 Arrow/Parquet 처리를 돕는 라이브러리입니다. 포맷과 이를 읽는 라이브러리를 구분하세요.

## 왜 필요한가

공공자료를 받은 원본, 정제한 분석 자료, 웹 게시용 자료는 요구 조건이 다릅니다. 작업용은 GeoPackage 또는 GeoParquet을 우선 검토하고, 웹용 GeoJSON은 WGS84 경위도로 내보냅니다. Shapefile의 열 이름·인코딩 제약 때문에 원본 속성이 잘리는지 확인해야 합니다.

## 핵심 API

gpd.read_file(path, engine='pyogrio') → GeoDataFrame. gdf.to_file(path, layer=..., driver='GPKG') → 파일. gpd.read_parquet/to_parquet → 공간 Parquet. use_arrow=True는 pyarrow가 필요하며 읽기 속도 이득은 자료와 작업에 따라 다릅니다.

## 최소 실행 예제

{{code:chapter05.py}}

## 조경·도시 실무 예제

예제는 실제 위치를 분석하지 않는 합성 공원입니다. 임시 폴더는 종료 시 지워집니다. 실무에서는 raw/에 원본을 보존하고 processed/에 변환 결과를 저장하세요. 같은 공원을 GeoPackage·GeoJSON·GeoParquet으로 내보낸 뒤 CRS, 행 수, 열 이름, NULL 값을 비교합니다.

## 시각화와 결과 읽기

파일 확장자만 비교하지 말고 읽어 온 도형을 같은 축에 겹쳐 그리세요. 위치가 어긋나면 좌표계 변환 여부부터 확인합니다.

## 흔한 오류

GeoJSON에 미터 좌표를 그대로 넣으면 웹지도가 엉뚱한 위치를 표시합니다. Parquet 일반 파일이 모두 GeoParquet은 아닙니다. Shapefile을 .shp만 복사하면 속성이나 좌표계 정보가 사라질 수 있습니다.

## 연습문제

공원을 3개로 늘리고 각 형식으로 왕복 저장하세요. 행 수, CRS, 면적 합을 검증하는 assert를 추가하세요.

[전체 예제 내려받기](../examples/chapter05.py) · 실행: `python chapter05.py`

## 다음 단계

[06 · 속성 조회와 geometry 연산](geometry.html)로 이어집니다.

## 출처

[GeoPandas 입출력](https://geopandas.org/en/stable/docs/user_guide/io.html), [GeoParquet](https://geoparquet.org/), [pyogrio](https://pyogrio.readthedocs.io/en/latest/). 확인 2026-09-30.
