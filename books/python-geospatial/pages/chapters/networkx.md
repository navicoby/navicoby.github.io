---
title: "23 · NetworkX와 노드·간선·가중치"
description: "길의 모양과 연결 구조를 구분하고 길이 가중치로 경로를 계산합니다."
eyebrow: "PART 07 / CHAPTER 23"
---

**학습 목표:** 길의 모양과 연결 구조를 구분하고 길이 가중치로 경로를 계산합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

NetworkX는 노드와 간선으로 이루어진 그래프를 만들고 분석하는 Python 라이브러리입니다. 노드는 교차로·출입구 같은 연결점, 간선은 그 사이의 연결입니다. 가중치는 길이·시간·비용처럼 연결을 통과하는 데 드는 값입니다. Graph는 무방향, DiGraph는 방향, MultiDiGraph는 같은 두 노드 사이 여러 방향 간선까지 표현합니다.

그래프는 지도와 다릅니다. 좌표가 없어도 연결을 분석할 수 있지만, 지도에 그리려면 노드 위치와 간선 geometry가 필요합니다.

## 왜 필요한가

가장 적은 도로 구간을 지나는 경로와 가장 짧은 경로는 다릅니다. 보행 접근성은 간선 개수 대신 거리나 시간의 합을 최소화해야 합니다.

## 핵심 API

nx.Graph(), add_edge(..., length=...), nx.shortest_path(..., weight='length'), nx.shortest_path_length(..., weight='length')를 사용합니다. 해당 가중치 속성이 없는 간선은 기본 비용 1로 처리될 수 있으므로 누락을 먼저 검사합니다.

## 최소 실행 예제

{{code:chapter23.py}}

## 조경·도시 실무 예제

직접 연결된 400m 길보다 교차로를 거치는 250m 길이 짧습니다. 합성 네트워크에 횡단보도 대기 시간을 넣으면 거리 최단경로와 시간 최단경로를 비교할 수 있습니다.

## 시각화와 결과 읽기

노드를 원, 간선을 선으로 그리고 각 간선에 가중치와 단위를 적으세요. 실제 도로처럼 보이게 그려도 연결되지 않은 교차점은 통과할 수 없습니다.

## 흔한 오류

weight를 생략하면 간선 수가 기준이 됩니다. 일방통행을 무방향 그래프로 바꾸면 통행 가능성이 달라집니다. 끊어진 그래프에서는 도달 가능한 경로가 없을 수 있습니다.

## 연습문제

home→park의 길이를 200m로 바꾸고 경로가 어떻게 바뀌는지 확인하세요.

[전체 예제 내려받기](../examples/chapter23.py) · 실행: `python chapter23.py`

## 다음 단계

[24 · OpenStreetMap과 OSMnx 도로망](osmnx.html)로 이어집니다.

## 출처

[NetworkX 그래프 소개](https://networkx.org/documentation/stable/tutorial.html), [NetworkX 최단경로](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html). 확인 2026-09-30.
