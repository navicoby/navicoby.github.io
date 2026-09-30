---
title: "15 · Rasterio란 무엇인가: band·격자·NoData"
description: "래스터를 파일·배열·지상 좌표의 세 층으로 이해합니다."
eyebrow: "PART 05 / CHAPTER 15"
---

**학습 목표:** 래스터를 파일·배열·지상 좌표의 세 층으로 이해합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Rasterio는 GeoTIFF 같은 지리참조 래스터를 읽고 쓰는 Python 라이브러리입니다. 공간 파일을 여는 일은 Rasterio가, 읽어 온 셀을 계산하는 일은 주로 NumPy가 맡습니다. NumPy는 같은 자료형의 숫자를 다차원 배열로 저장하고 빠르게 계산하는 라이브러리입니다.

래스터는 행·열로 나눈 격자이고, band는 각 위치에서 측정한 값의 한 층입니다. DEM은 고도 값을 담는 래스터의 예입니다. resolution은 셀의 지상 크기, NoData는 관측되지 않았거나 분석에서 제외할 값을 뜻합니다. CRS와 transform이 있어야 배열의 행·열을 실제 지상 위치에 연결할 수 있습니다.

## 왜 필요한가

숫자 배열을 PNG로만 저장하면 좌표와 NoData 정보가 사라집니다. 분석 결과를 GIS에서 다시 쓰려면 배열뿐 아니라 위치·단위·유효값 정보를 보존해야 합니다.

## 핵심 API

rasterio.open(), src.read(1, masked=True), src.crs, src.transform, src.res, src.nodata, src.profile을 확인합니다. Rasterio의 밴드 번호는 1부터, NumPy 인덱스는 0부터 시작합니다.

## 최소 실행 예제

{{code:chapter15.py}}

## 조경·도시 실무 예제

2m 격자의 합성 고도 6셀 중 하나는 NoData입니다. 유효한 다섯 셀 평균은 12m입니다. 실제 DEM의 표고 기준이 정표고인지 타원체고인지도 확인해야 BIM 높이와 비교할 수 있습니다.

## 시각화와 결과 읽기

위에서 아래로 증가하는 행 번호와 북쪽으로 증가하는 지상 y좌표는 방향이 반대일 수 있습니다. 배열 모서리와 셀 중심을 구별해 그림에 표시하세요.

## 흔한 오류

NoData=-9999를 일반 고도로 평균 내면 틀립니다. read()는 (band,row,col), read(1)은 (row,col)입니다. 해상도 단위는 항상 m가 아니라 CRS에 따릅니다.

## 연습문제

셀 크기를 5m로 바꾸고 같은 배열의 지상 면적이 얼마나 달라지는지 계산하세요.

[전체 예제 내려받기](../examples/chapter15.py) · 실행: `python chapter15.py`

## 다음 단계

[16 · 마스킹·자르기·재투영·격자 정렬](raster-crop.html)로 이어집니다.

## 출처

[Rasterio 읽기](https://rasterio.readthedocs.io/en/stable/topics/reading.html), [Rasterio 지리참조](https://rasterio.readthedocs.io/en/stable/topics/georeferencing.html), [NumPy 소개](https://numpy.org/doc/stable/user/whatisnumpy.html). 확인 2026-09-30.
