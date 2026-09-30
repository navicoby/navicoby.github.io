---
title: "16 · 마스킹·자르기·재투영·격자 정렬"
description: "대상지 자르기와 좌표 변환을 구분하고 분석 격자를 맞춥니다."
eyebrow: "PART 05 / CHAPTER 16"
---

**학습 목표:** 대상지 자르기와 좌표 변환을 구분하고 분석 격자를 맞춥니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Masking은 대상지 바깥 값을 제외하는 작업이고 cropping은 배열의 범위를 줄이는 작업입니다. 재투영은 좌표계를 바꾸며, 리샘플링은 새 격자에 들어갈 값을 계산합니다. 같은 CRS라고 해서 두 래스터의 셀이 서로 맞는 것은 아닙니다. 셀 크기·행열 수·원점·범위를 함께 확인해야 합니다.

연속값 DEM은 작업 목적에 따라 bilinear 같은 보간을 검토합니다. 토지피복 분류·SCL 같은 범주값은 nearest를 써야 존재하지 않는 분류 번호를 만들지 않습니다.

## 왜 필요한가

DEM, NDVI, 도로 마스크를 셀 단위로 합산할 때 한 셀씩 어긋나 있으면 서로 다른 장소의 값을 결합합니다. 기준 래스터 하나의 격자로 다른 자료를 정렬하는 것이 안전합니다.

## 핵심 API

rasterio.mask.mask(src, shapes, crop=True)는 잘린 배열과 새 transform을 반환합니다. rasterio.warp.reproject는 src/dst의 CRS·transform과 Resampling을 명시해 정렬합니다. 경계 도형을 래스터 CRS로 먼저 변환합니다.

## 최소 실행 예제

{{code:chapter16.py}}

## 조경·도시 실무 예제

합성 4×4 격자의 중앙 2×2를 자릅니다. 저장할 때 width·height·transform을 새 값으로 갱신해야 원래 위치에 놓입니다. 대형 Sentinel 영상은 전체를 메모리에 올리기보다 대상지 주변을 먼저 자르세요.

## 시각화와 결과 읽기

원본 전체 경계와 잘린 배열의 경계를 함께 표시하고, 두 결과가 지상 좌표에서 정확히 겹치는지 확인합니다.

## 흔한 오류

crop 결과에 원본 transform을 쓰면 위치가 이동합니다. EPSG 번호만 같고 해상도가 다른 자료를 NumPy에서 바로 곱하지 않습니다. all_touched는 경계 셀 포함 규칙을 바꾸므로 면적에 영향을 줍니다.

## 연습문제

경계를 box(0,0,2,2)로 바꾸고 값과 transform을 손으로 예상한 뒤 확인하세요.

[전체 예제 내려받기](../examples/chapter16.py) · 실행: `python chapter16.py`

## 다음 단계

[17 · 벡터↔래스터 변환](raster-vector.html)로 이어집니다.

## 출처

[Rasterio mask](https://rasterio.readthedocs.io/en/stable/topics/masking-by-shapefile.html), [Rasterio 재투영](https://rasterio.readthedocs.io/en/stable/topics/reproject.html). 확인 2026-09-30.
