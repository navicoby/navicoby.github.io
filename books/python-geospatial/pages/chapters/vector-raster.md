---
title: "02 · 벡터·래스터와 GeoDataFrame"
description: "점·선·면과 격자가 같은 장소를 어떻게 다르게 표현하는지 배웁니다."
eyebrow: "PART 01 / CHAPTER 02"
---

**목표:** Vector/Raster와 GeoDataFrame의 구조를 설명합니다. **선수:** 01장. **실습:** 30분, 외부 파일 없는 가상 도형.

## 개념

벡터(vector)는 좌표로 도형을 정의합니다. Point는 수목·출입구처럼 위치를, LineString은 길의 중심선처럼 연결을, Polygon은 공원 경계처럼 영역을 나타냅니다. 같은 수목도 도시 지도에서는 점으로, 수관 분석에서는 면으로 표현할 수 있습니다. 도형은 대상 자체가 아니라 분석 목적에 맞춘 표현입니다.

래스터(raster)는 공간을 규칙적인 셀로 나누고 각 셀에 값을 둡니다. DEM의 값은 고도, 위성영상의 밴드 값은 보정 전 DN 또는 반사도일 수 있습니다. 숫자 배열만으로는 어느 땅인지 알 수 없고 CRS와 transform이 함께 있어야 합니다.

GeoDataFrame은 pandas의 표에 geometry 열과 CRS를 더한 자료구조입니다. 한 행이 한 객체, 일반 열은 이름·용도·면적 같은 속성, 활성 geometry 열은 Shapely 도형을 담습니다. GeoSeries는 도형 열 하나입니다. 서로 다른 geometry 타입을 담을 수 있지만 파일 형식과 분석 함수의 제약을 확인해야 합니다.

{{diagram:vector-raster}}

## 왜 필요한가

공원 안내 포인트로 공원 면적을 계산할 수 없습니다. 반대로 공원 경계 폴리곤만으로 실제 출입구 위치를 알 수 없습니다. 어떤 표현을 받았는지 확인해야 다음 연산이 의미를 가집니다.

## 핵심 API

`Point`, `LineString`, `Polygon`은 Shapely가 만들고 `gpd.GeoDataFrame`은 속성과 결합합니다. `gdf.geometry`, `gdf.crs`, `gdf.geom_type`으로 공간표의 구조를 확인합니다.

## 최소 실행 예제

{{code:chapter02.py}}

도형 타입은 Point·LineString·Polygon이며 마지막 면적은 3,000㎡입니다. 이 좌표는 모양을 배우는 가상 값이고 한국의 실제 위치를 나타내지 않습니다.

## 조경·도시 실무 예제

수목대장은 tree_id·수종·흉고직경과 Point, 보행로는 path_id·폭·포장과 LineString, 식재구역은 bed_id·관리유형과 Polygon으로 구성합니다. DEM은 별도 래스터로 두고 대상별 고도·경사를 추출해 속성표로 연결합니다.

## 시각화

아래 대응을 그림의 범례에도 유지합니다.

| 실제 대상 | 벡터 표현 | 래스터로 바꾸면 |
|---|---|---|
| 수목 위치 | 점 | 수목이 속한 셀 표시 |
| 보행로 | 선 | 경로가 지나는 셀 표시 |
| 공원 경계 | 면 | 공원 내부 셀 마스크 |
| 고도 | 등고선으로 표현 가능 | 셀마다 높이 |

## 흔한 오류

좌표 두 개가 있다고 항상 위도·경도는 아닙니다. Polygon의 좌표 순서와 닫힘, 여러 부분으로 된 MultiPolygon, 구멍이 있는 면도 확인합니다. 빈 geometry와 값이 없는 geometry는 서로 다릅니다.

## 연습문제

한 수목을 Point와 수관 Polygon 두 방식으로 만들고, 각각 답할 수 있는 질문을 두 개씩 적으세요. 1m 셀과 10m 셀에서 같은 식재구역의 경계가 어떻게 달라지는지도 생각해 보세요.

## 다음 단계

도형에 단위를 부여하는 [03장 CRS](crs.html)로 이어집니다.

## 출처

[GeoPandas 자료구조](https://geopandas.org/en/stable/docs/user_guide/data_structures.html), [Shapely 도형 설명](https://shapely.readthedocs.io/en/stable/manual.html). 확인 2026-09-30.
