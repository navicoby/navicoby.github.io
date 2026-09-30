---
title: "08 · clip·overlay·intersection·dissolve"
description: "도형을 자르고 겹치고 묶는 네 연산의 차이를 같은 예제로 비교합니다."
eyebrow: "PART 02 / CHAPTER 08"
---

**학습 목표:** 도형을 자르고 겹치고 묶는 네 연산의 차이를 같은 예제로 비교합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

clip은 경계 안에 있는 부분만 남깁니다. overlay는 두 자료의 공간 중첩 결과와 양쪽 속성을 함께 만듭니다. intersection은 도형끼리의 공통 부분을 계산합니다. dissolve는 같은 속성값에 속하는 여러 도형을 하나로 합치고 속성값도 집계합니다.

공간조인은 보통 원래 도형을 유지하면서 속성을 붙입니다. 반대로 overlay는 새 경계로 도형을 나눌 수 있습니다. 행 수가 늘거나 면적이 줄어드는 것은 연산 목적에 따라 정상입니다.

## 왜 필요한가

필지별 녹지 면적을 계산하려면 녹지가 어느 필지에 걸치는지만 아는 것으로 부족합니다. 필지 경계에서 녹지를 나누고 그 면적을 합산해야 합니다.

## 핵심 API

gpd.clip(data, mask), gpd.overlay(a, b, how='intersection'), a.geometry.intersection(도형), gdf.dissolve(by=열, aggfunc=...)를 사용합니다. 두 GeoSeries의 이항 연산은 인덱스 정렬이 개입하므로 임의의 행끼리 짝짓지 않습니다.

## 최소 실행 예제

{{code:chapter08.py}}

## 조경·도시 실무 예제

합성 필지 두 개의 녹지 면적은 각각 25㎡입니다. 필지 면적은 각각 100㎡이므로 녹지율은 25%입니다. 실무 자료에서는 필지 중복, 녹지 중첩, 경계 틈을 검사한 뒤 분모를 정합니다.

## 시각화와 결과 읽기

필지 경계는 검은 선, 녹지는 반투명 녹색, 잘린 조각은 서로 다른 색으로 표시하세요. 원본과 조각을 나란히 두면 도형 분할을 이해하기 쉽습니다.

## 흔한 오류

서로 다른 CRS로 연산하면 잘못된 결과가 나옵니다. overlay 결과의 선·점 접촉은 keep_geom_type 설정에 따라 제외될 수 있습니다. dissolve의 기본 집계가 모든 숫자 열의 합계를 의미하지는 않습니다.

## 연습문제

녹지를 box(5,0,18,5)로 바꾸고 필지별 녹지율과 전체 녹지 면적을 손으로 먼저 계산하세요.

[전체 예제 내려받기](../examples/chapter08.py) · 실행: `python chapter08.py`

## 다음 단계

[09 · Matplotlib·단계구분도·히트맵](map-design.html)로 이어집니다.

## 출처

[GeoPandas overlay](https://geopandas.org/en/stable/docs/user_guide/set_operations.html), [GeoPandas dissolve](https://geopandas.org/en/stable/docs/user_guide/aggregation_with_dissolve.html). 확인 2026-09-30.
