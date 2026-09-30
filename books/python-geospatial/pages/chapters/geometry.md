---
title: "06 · 속성 조회와 geometry 연산"
description: "속성 조건과 공간 도형을 함께 다루고 geometry 메서드의 결과를 읽습니다."
eyebrow: "PART 02 / CHAPTER 06"
---

**학습 목표:** 속성 조건과 공간 도형을 함께 다루고 geometry 메서드의 결과를 읽습니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

속성은 건물 용도·높이처럼 표에 저장하는 값이고, geometry는 위치와 모양입니다. GeoDataFrame은 일반 열과 활성 geometry 열을 함께 갖습니다. Shapely는 Point·LineString·Polygon 등의 도형을 만들고 길이, 면적, 교차 관계를 계산하는 Python 라이브러리입니다. GeoPandas는 이 도형을 표의 여러 행에 적용하도록 돕습니다.

area는 폴리곤 면적, length는 선 길이 또는 폴리곤 둘레입니다. centroid는 무게중심이어서 오목한 폴리곤 밖으로 나갈 수 있습니다. representative_point()는 도형 내부의 대표점이 필요할 때 사용합니다.

## 왜 필요한가

건물 전체를 분석하기 전에 주거용·특정 면적 이상 건물처럼 분석 대상을 정의해야 합니다. 속성 조건을 먼저 기록하면 결과가 어떤 모집단을 설명하는지 분명해집니다.

## 핵심 API

gdf.loc[조건, 열]로 선택, geometry.area/length로 수치 계산, representative_point()로 내부점 생성, is_valid로 도형 유효성을 확인합니다. Shapely 연산은 평면 연산이므로 면적 계산 전에 투영 CRS를 선택합니다.

## 최소 실행 예제

{{code:chapter06.py}}

## 조경·도시 실무 예제

위 좌표는 미터 단위 계산 연습을 위한 합성 격자이며 실제 EPSG:5179 위치를 뜻하지 않습니다. 건축물 자료의 용도 코드는 제공기관 코드표로 해석하고, 층수에서 추정한 높이는 실측 높이와 별도 열에 기록하세요.

## 시각화와 결과 읽기

선택 전 건물을 회색, 선택된 건물을 녹색으로 겹쳐 그리면 필터가 공간적으로 어떤 대상을 남겼는지 확인할 수 있습니다.

## 흔한 오류

geometry가 비어 있는 경우와 누락된 경우를 구분합니다. 경위도에서 area를 계산하지 않습니다. make_valid()는 복구 후 도형 종류와 면적이 달라질 수 있으므로 자동 적용 결과를 확인해야 합니다.

## 연습문제

높이 12m 이상 조건을 추가해 결과가 0개가 되는 이유를 설명하세요. 누락 높이를 0m로 바꾸면 어떤 오해가 생기는지 적으세요.

[전체 예제 내려받기](../examples/chapter06.py) · 실행: `python chapter06.py`

## 다음 단계

[07 · 공원 주변 건물을 찾는 버퍼와 공간조인](buffer-join.html)로 이어집니다.

## 출처

[GeoPandas 자료 구조](https://geopandas.org/en/stable/docs/user_guide/data_structures.html), [Shapely 설명서](https://shapely.readthedocs.io/en/stable/manual.html). 확인 2026-09-30.
