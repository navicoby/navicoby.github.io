---
title: "24 · OpenStreetMap과 OSMnx 도로망"
description: "OSM 데이터와 OSMnx 라이브러리의 차이, 그래프와 공간표의 변환을 배웁니다."
eyebrow: "PART 07 / CHAPTER 24"
---

**학습 목표:** OSM 데이터와 OSMnx 라이브러리의 차이, 그래프와 공간표의 변환을 배웁니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

OpenStreetMap(OSM)은 참여자들이 도로·건물·시설 정보를 함께 만드는 지도 데이터 프로젝트입니다. OSMnx는 OSM 자료를 내려받고 도로망을 NetworkX 그래프로 구성하는 Python 라이브러리입니다. OSM 데이터 자체가 완전한 보행 접근성 검증 자료는 아니므로 지역별 누락과 출입 제한을 검토해야 합니다.

OSMnx 도로망은 보통 MultiDiGraph입니다. 노드 공간표에는 x/y 좌표와 고유 인덱스, 간선 공간표에는 (u,v,key) 복합 인덱스가 필요합니다.

## 왜 필요한가

국내 공공자료의 건물·필지와 OSM 도로망을 결합하면 공원 출입구와 주변 주거지의 접근성을 분석할 수 있습니다. 원자료별 시점·정확도·라이선스를 각각 유지합니다.

## 핵심 API

실제 다운로드는 ox.graph.graph_from_point((위도,경도), dist=..., network_type='walk') 등을 사용합니다. ox.convert.graph_to_gdfs와 graph_from_gdfs는 그래프와 표 사이를 변환합니다. 아래는 외부 서비스에 의존하지 않는 합성 그래프 변환 예제입니다.

## 최소 실행 예제

{{code:chapter24.py}}

## 조경·도시 실무 예제

실제 자료 취득 시 작은 대상지부터 요청하고 GraphML로 저장해 반복 다운로드를 줄입니다. 예를 들어 ox.io.save_graphml(G, filepath='walk.graphml')로 보존합니다. 조회 범위를 너무 작게 자르면 경계 밖 우회 경로를 놓칠 수 있습니다.

## 시각화와 결과 읽기

노드와 간선을 별도 레이어로 보세요. 교량·터널이 평면에서 교차해도 연결 노드가 없으면 통과하지 않습니다. OSM을 사용한 공개 지도에는 © OpenStreetMap contributors와 저작권 링크를 표시합니다.

## 흔한 오류

다운로드용 경위도와 투영 그래프의 x/y를 섞지 않습니다. MultiDiGraph를 임의로 단순화하면 평행 간선이 사라집니다. OSM의 누락을 실제 시설 부재로 해석하지 않습니다.

## 연습문제

노드 3을 추가해 연결선을 만들고 표→그래프→표 왕복 후 좌표·길이·방향이 보존되는지 확인하세요.

[전체 예제 내려받기](../examples/chapter24.py) · 실행: `python chapter24.py`

## 다음 단계

[25 · 최단경로와 공원 출입구 접근성](walking-distance.html)로 이어집니다.

## 출처

[OSMnx 공식 API](https://osmnx.readthedocs.io/en/stable/user-reference.html), [OSM 저작권](https://www.openstreetmap.org/copyright). 확인 2026-09-30.
