---
title: 전체 목차와 학습 로드맵
description: 공간데이터 기초에서 도시 분석, 위성영상, GeoAI와 BIM까지 이어지는 10부 35장.
eyebrow: READ / BUILD / CONNECT
---

**10부 · 35장 계획 · 실행 가능한 샘플 3장.** 표의 “계획”은 집필 예정이며 현재 본문이 있다는 뜻이 아닙니다. 각 부는 개념, 실습, 결과물의 순서로 진행합니다.

## Part 1. 공간데이터라는 언어

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 01 | 조경 질문을 데이터 질문으로 바꾸기: 위치·범위·시간·평가 단위 | 공원 분석 질문지 / 계획 |
| 02 | Vector/Raster, Point·LineString·Polygon, GeoSeries·GeoDataFrame | 동일 대상의 표·도형·격자 비교 / 계획 |
| 03 | CRS·EPSG·투영·단위, set_crs와 to_crs, 수직 기준 | 좌표계 검토표 / 계획 |
| 04 | Python 환경, 경로, NumPy·pandas, 재현성과 manifest | [환경 안내](stack.html), 본장 계획 |

## Part 2. GeoPandas와 Shapely

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 05 | Shapefile·GeoJSON·GeoPackage·GeoParquet, pyogrio/Arrow, 필드 선택 | 형식별 왕복 입출력 / 계획 |
| 06 | 속성 조회, geometry, 면적·길이, 유효성, representative_point | 정리된 공원·건물 테이블 / 계획 |
| 07 | buffer, spatial join, nearest join, 경계와 다중 매칭 | [3,000㎡ 공원 주변 건물](chapters/buffer-join.html) / 샘플 공개 |
| 08 | clip·overlay·intersection·dissolve·union_all | 필지별 녹지 교차면적 / 계획 |

## Part 3. 공간 시각화와 웹지도

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 09 | Matplotlib 지도, choropleth의 분모·분류·범례, heatmap과 KDE 차이 | 밀도·비율 지도 / 계획 |
| 10 | Folium Marker·Popup·MarkerCluster·GeoJSON·LayerControl | 조사 지점 웹지도 / 계획 |
| 11 | 지도 간소화, iframe, 모바일, 출처와 오프라인 대안 | 출판용 반응형 지도 / 계획 |

## Part 4. 한국 공간자료와 도시 벡터

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 12 | NGII·VWorld·국가공간정보포털·서울·공공데이터포털 비교 | [자료 가이드](data-sources.html), 본장 계획 |
| 13 | 자료 취득·파일 검사·한글 인코딩·라이선스·manifest | 재현 가능한 취득 기록 / 계획 |
| 14 | 건물 footprint·용도·높이·층수, 도로·필지와의 관계 | 건물-도로-녹지 분석 / 계획 |

## Part 5. Raster와 지형

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 15 | Rasterio, band·resolution·transform·NoData, DEM/DSM | 고도 래스터 검사표 / 계획 |
| 16 | masking·cropping·window·재투영·격자 정렬 | 대상지 + 주변부 DEM / 계획 |
| 17 | rasterize·polygonize, 셀 중심/all_touched, 정보 손실 | 벡터↔래스터 비교 / 계획 |
| 18 | slope·aspect·hillshade, 결측값·경계·단위 | [경사도 기반 후보지](chapters/dem-slope.html) / 샘플 공개 |

## Part 6. Sentinel-2A와 위성영상

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 19 | Sentinel-2A 및 Sentinel-2 자료군, Landsat·Sentinel-1의 역할, 공간/분광/시간 해상도 | 센서 선택표 / 계획 |
| 20 | Copernicus Browser·STAC, L1C/L2A, SAFE·JP2·COG, 촬영일·구름·타일 | 취득 후보 목록 / 계획 |
| 21 | RGB·NIR·SWIR, SCL, scale/offset, 10/20/60m 정렬·합성 | 유효픽셀 마스크 / 계획 |
| 22 | NDVI·NDWI·NDBI, 공원 주변 녹지·계절 변화, 지표의 한계 | [NDVI와 구름 마스킹](chapters/sentinel2-ndvi.html) / 샘플 공개 |

## Part 7. 도시 네트워크

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 23 | NetworkX: node·edge·weight, 유향·다중 그래프, 연결요소 | 길이 가중 그래프 / 계획 |
| 24 | OSM·OSMnx: 도로망 취득·graph_to_gdfs·보행 태그·캐시 | 검토된 보행망 / 계획 |
| 25 | shortest path·스냅·walking distance·공원 출입구 | 출입구까지 거리표 / 계획 |
| 26 | service area·isochrone, 속도와 경사, 단절·횡단 | 5/10/15분 보행권 / 계획 |

## Part 8. 조경·도시 분석 프로젝트

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 27 | 녹지 접근성·건물 밀도·필지별 피복·인구 분모, MAUP | 도시권 비교 지도 / 계획 |
| 28 | 2,000~4,000㎡ 공원 후보지 평가: 경사·접근·녹지·제약, 가중치 민감도 | 순위와 불확실성 보고서 / 계획 |

## Part 9. GeoAI의 기초와 검증

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 29 | raster → NumPy → PyTorch, NCHW, dtype·정규화·NoData | 정렬된 입력 텐서 / 계획 |
| 30 | convolution·kernel·stride·padding·receptive field | 경계 검출과 CNN 개념 / 계획 |
| 31 | semantic segmentation, raster 라벨, 클래스·ignore_index | 토지피복 학습 세트 / 계획 |
| 32 | U-Net encoder·decoder·skip, baseline 비교, 추론 타일 경계 | 작은 분할 모델 / 계획 |
| 33 | 공간/시점 분할, 누수, IoU·F1, 클래스 불균형·불확실성 | 재현 가능한 평가 / 계획 |

## Part 10. GIS → BIM → Spatial AI

| 장 | 내용 | 결과·상태 |
|---|---|---|
| 34 | 위성·DEM·토지이용·도로·건물·IFC: 좌표·시간·해상도·의미 연결 | [통합 방향](geoai-bridge.html), 본장 계획 |
| 35 | 최종 프로젝트: 공원 대상지 분석에서 설계·모니터링까지 | 지도 + 데이터 + 보고서 + 재현 환경 / 계획 |

## 권장 학습 경로

**기초 경로 · 8~10주:** 주 3~5시간을 가정한 학습 계획입니다. 1~2주는 Part 1–2, 3주는 지도, 4주는 공공데이터, 5~6주는 DEM과 위성영상, 7~8주는 보행망·후보지, 9~10주는 GeoAI 기초로 진행합니다. 시간은 난도·자료 취득에 따라 달라지며 성취 보장이 아닙니다.

**조경 실무 경로:** 03 → 05 → 07 → 12–18 → 24–28. 좌표·단위 오류 없이 한 대상지의 분석 묶음을 만드는 것을 먼저 목표로 합니다.

**GeoAI 연구 경로:** 기초 경로 → 19–22 → 29–35. 동일 지역의 시점이 다른 영상과 공간적으로 분리된 평가 지역을 확보한 뒤 모델을 학습합니다.

## 부별 통과 기준

- 벡터: CRS와 면적 단위를 설명하고, 중복 매칭 때문에 집계가 달라지는 경우를 재현할 수 있습니다.
- 래스터: NoData·격자 정렬·수직 단위를 설명하고 알려진 평면의 경사도를 검산할 수 있습니다.
- 위성: 제품 ID·획득일·L2A 처리값·SCL 정책을 남기고 AOI 유효픽셀 비율을 보고할 수 있습니다.
- 네트워크: 직선거리와 보행거리의 차이, 단절된 경로의 의미를 설명할 수 있습니다.
- GeoAI: 입력·정답·분할·평가지표를 재현하고 성능을 지도와 함께 해석할 수 있습니다.
