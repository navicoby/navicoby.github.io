---
title: "10 · Folium으로 인터랙티브 지도 만들기"
description: "Folium의 Marker·Popup·MarkerCluster·레이어가 하는 일을 이해합니다."
eyebrow: "PART 03 / CHAPTER 10"
---

**학습 목표:** Folium의 Marker·Popup·MarkerCluster·레이어가 하는 일을 이해합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Folium은 Python에서 웹지도용 HTML과 JavaScript를 생성하는 라이브러리입니다. 실제 브라우저 지도는 JavaScript 라이브러리 Leaflet이 그립니다. Marker는 위치 표식, Popup은 눌렀을 때 보이는 설명창, MarkerCluster는 가까운 표식을 묶어 복잡함을 줄이는 기능입니다. GeoJSON 레이어는 선이나 면을 포함한 공간 도형을 웹지도에 올립니다.

HTML로 저장한 지도에는 Python 실행 환경이 필요하지 않지만 지도 타일과 JavaScript를 외부에서 불러오면 인터넷 연결이 필요합니다.

## 왜 필요한가

현장 조사 지점에 사진·수종·점검 결과를 연결하면 표만 읽을 때보다 위치 관계를 파악하기 쉽습니다. 공개 지도에는 개인 정보와 민감한 위치를 포함하지 않습니다.

## 핵심 API

folium.Map(location=[위도,경도]), Marker(...).add_to(...), Popup, plugins.MarkerCluster, GeoJson, LayerControl, Map.save를 사용합니다. GeoJSON 좌표 순서는 경도·위도이지만 Folium location은 위도·경도입니다.

## 최소 실행 예제

{{code:chapter10.py}}

## 조경·도시 실무 예제

예제 지점은 실제 조사 결과가 아닙니다. 배경 타일을 넣지 않아도 표식과 선은 표시됩니다. 실제 공개 지도에는 제공자 약관에 맞는 출처 표시를 넣고, 외부 타일 요청량과 공개 가능 범위를 확인하세요.

## 시각화와 결과 읽기

[3,000㎡ 공원 실습 지도](../maps/park-map.html)는 실제 클릭 가능한 예입니다. 군집을 확대하고 표식을 눌러 설명창을 읽어 보세요. 군집은 화면 표시 기능이며 통계적 군집 분석 결과가 아닙니다.

## 흔한 오류

위도·경도 순서가 뒤집히면 위치가 틀립니다. 사용자 입력을 Popup HTML에 넣을 때는 이스케이프합니다. tiles=None에 MarkerCluster를 쓰면 Leaflet 지도 옵션 maxZoom을 명시해 무한 확대 범위를 피합니다.

## 연습문제

두 지점의 Popup에 조사 날짜와 수종을 넣고, 지도 아래에 동일한 내용을 표로 적으세요.

[전체 예제 내려받기](../examples/chapter10.py) · 실행: `python chapter10.py`

## 다음 단계

[11 · 웹지도 게시와 모바일 읽기](web-maps.html)로 이어집니다.

## 출처

[Folium 공식 문서](https://python-visualization.github.io/folium/latest/), [Leaflet Map 옵션](https://leafletjs.com/reference.html#map-maxzoom). 확인 2026-09-30.
