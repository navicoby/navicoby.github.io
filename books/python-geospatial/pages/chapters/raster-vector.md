---
title: "17 · 벡터↔래스터 변환"
description: "도형을 셀로 바꾸고 분류된 셀을 도형으로 되돌립니다."
eyebrow: "PART 05 / CHAPTER 17"
---

**학습 목표:** 도형을 셀로 바꾸고 분류된 셀을 도형으로 되돌립니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Rasterize는 폴리곤이나 선을 격자의 값으로 바꾸는 작업입니다. Polygonize는 같은 값을 가진 인접 셀을 묶어 폴리곤을 만드는 작업입니다. 벡터의 경계는 연속적인 좌표로 표현되지만 래스터는 선택한 해상도의 셀 경계에 맞춰지므로 왕복 변환이 항상 원본과 같지는 않습니다.

Rasterio.features가 이 변환을 제공합니다. 불리언 mask는 shapes()에서 추출할 셀을 지정하며, NumPy masked array의 mask와 의미를 혼동하지 않아야 합니다.

## 왜 필요한가

도로·녹지·필지 도형을 DEM과 결합하려면 같은 격자로 바꾸는 과정이 필요합니다. AI가 예측한 녹지 분류 지도를 GIS 편집용 폴리곤으로 전달할 때는 반대 변환이 필요합니다.

## 핵심 API

rasterize([(geometry,value)], out_shape=..., transform=..., fill=...), shapes(array, mask=..., transform=...)를 사용합니다. 여러 도형이 겹칠 때 뒤에 처리한 값이 앞의 값을 덮을 수 있습니다.

## 최소 실행 예제

{{code:chapter17.py}}

## 조경·도시 실무 예제

셀 경계에 정확히 맞는 합성 4㎡ 도형이므로 왕복 면적이 같습니다. 현실의 곡선 경계는 셀 크기에 따라 계단 모양이 됩니다. 면적 변화량과 사용 해상도를 보고서에 기록하세요.

## 시각화와 결과 읽기

원본 경계, 셀 격자, 복원 폴리곤을 겹쳐 비교합니다. 해상도 1m와 5m를 비교하면 작은 화단이 사라지는 이유를 볼 수 있습니다.

## 흔한 오류

transform을 생략하면 결과가 지상 좌표가 아닌 픽셀 좌표로 생성됩니다. 모든 셀을 개별 폴리곤으로 만들면 파일이 커질 수 있습니다. 분류값 0이 배경인지 유효 범주인지 먼저 정하세요.

## 연습문제

box(1.2,1.2,3.2,3.2)로 바꾸고 all_touched=False/True의 셀 수 차이를 비교하세요.

[전체 예제 내려받기](../examples/chapter17.py) · 실행: `python chapter17.py`

## 다음 단계

[18 · DEM으로 경사도와 식재 후보지 읽기](dem-slope.html)로 이어집니다.

## 출처

[Rasterio features](https://rasterio.readthedocs.io/en/stable/topics/features.html). 확인 2026-09-30.
