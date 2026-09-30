---
title: "14 · 건물·도로·필지·녹지의 관계"
description: "건물 footprint와 필지·도로·녹지의 관계를 면적과 거리로 설명합니다."
eyebrow: "PART 04 / CHAPTER 14"
---

**학습 목표:** 건물 footprint와 필지·도로·녹지의 관계를 면적과 거리로 설명합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Footprint는 건물이 지면에 차지하는 외곽 형상입니다. 건물 연면적이나 층별 BIM 형상과 같지 않습니다. 용도·높이·층수는 별도의 속성이고, 데이터 제품에 따라 없거나 정의가 다릅니다. 건물과 도로의 최단 평면거리는 접근성 지표의 하나지만 실제 출입구에서 걷는 거리를 대신하지 않습니다.

필지 녹지율은 '필지 내부 녹지 면적 ÷ 필지 면적'입니다. 건폐율을 논할 때는 법정 산정 기준에 필요한 건축면적과 대상 대지를 확인해야 하므로 단순 footprint 비율을 법정 수치로 단정하지 않습니다.

## 왜 필요한가

조경 배치에서는 녹지가 얼마나 있는지와 건물·보행로에서 어디에 있는지가 모두 중요합니다. 같은 면적의 녹지라도 연결성과 출입구 위치에 따라 이용 조건이 달라집니다.

## 핵심 API

Shapely intersection, area, distance는 두 도형의 공간관계를 수치화합니다. 여러 건물을 가까운 도로와 연결할 때는 GeoPandas sjoin_nearest(..., distance_col=...)를 사용할 수 있으며 같은 거리의 동률은 여러 행이 됩니다.

## 최소 실행 예제

{{code:chapter14.py}}

## 조경·도시 실무 예제

400㎡ 합성 필지의 녹지는 100㎡입니다. 도로 중심선까지 거리는 5m지만 차도 경계나 실제 출입구까지 거리는 아닙니다. 실무에서는 출입구, 담장, 횡단보도, 보행 가능 연결선을 별도 자료로 연결합니다.

## 시각화와 결과 읽기

필지 경계·건물·녹지·도로 중심선을 각기 다른 선과 면으로 그리고, 5m 거리선이 무엇을 연결하는지 명시하세요.

## 흔한 오류

건물 높이에 지붕·옥탑이 포함되는지 확인하지 않으면 음영 분석이 달라집니다. 건물 용도와 토지이용 분류를 같은 코드로 취급하지 않습니다. 건물 footprint만으로 일조 시간을 정확히 계산할 수 없습니다.

## 연습문제

도로를 y=-5로 이동시키고 거리 변화와 녹지율 변화를 비교하세요. 보행 출입구를 추가하면 필요한 데이터가 무엇인지 적으세요.

[전체 예제 내려받기](../examples/chapter14.py) · 실행: `python chapter14.py`

## 다음 단계

[15 · Rasterio란 무엇인가: band·격자·NoData](raster-basics.html)로 이어집니다.

## 출처

[Shapely distance](https://shapely.readthedocs.io/en/stable/reference/shapely.distance.html), [GeoPandas nearest join](https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin_nearest.html). 확인 2026-09-30.
