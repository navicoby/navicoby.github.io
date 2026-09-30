---
title: "25 · 최단경로와 공원 출입구 접근성"
description: "출입구와 도로 연결을 포함해 주거지에서 공원까지의 보행거리를 계산합니다."
eyebrow: "PART 07 / CHAPTER 25"
---

**학습 목표:** 출입구와 도로 연결을 포함해 주거지에서 공원까지의 보행거리를 계산합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Snapping은 점을 가까운 네트워크 위치에 연결하는 처리입니다. 가장 가까운 노드로만 연결하면 길 중간에 있는 실제 출입구의 위치가 부정확해질 수 있습니다. 정밀 분석에서는 가까운 간선에 점을 투영하고 간선을 나누며 통행 가능한 연결선을 검증합니다.

출발지 연결 거리 + 네트워크 거리 + 도착 출입구 연결 거리를 합해야 출입구까지의 거리라는 의미가 분명해집니다. 연결선이 벽이나 하천을 가로지르면 사용할 수 없습니다.

{{diagram:walking}}

## 왜 필요한가

공원 중심점까지 거리가 짧아도 담장과 출입구 때문에 실제 보행거리가 길 수 있습니다. 공원 면 전체를 목적지로 잡는 버퍼와 출입구 기반 보행 분석을 구별해야 합니다.

## 핵심 API

OSMnx distance.nearest_nodes는 그래프 CRS의 X/Y를 받습니다. NetworkX shortest_path_length는 도로상의 경로 길이를 계산합니다. 아래 예제는 연결선의 통행 가능성을 미리 확인했다고 가정한 합성 자료입니다.

## 최소 실행 예제

{{code:chapter25.py}}

## 조경·도시 실무 예제

건물 대표점 대신 실제 출입구가 있으면 우선 사용합니다. 여러 공원 출입구가 있으면 각 출입구까지의 가능한 거리를 비교하고 최솟값을 선택합니다. 도로망과 연결되지 않은 건물은 누락 비율도 보고합니다.

## 시각화와 결과 읽기

연결선은 점선, 실제 네트워크 경로는 굵은 실선으로 표시하세요. 출입구가 어느 쪽 담장에 있는지 보여 주면 우회 이유를 이해하기 쉽습니다.

## 흔한 오류

노드 스냅 거리만 더해도 실제 통행 가능성이 보장되는 것은 아닙니다. 동일 건물을 여러 출입구에 연결한 결과를 중복 집계하지 않습니다. length의 단위가 m인지 확인합니다.

## 연습문제

출입구를 하나 더 추가하고 최솟값이 어떻게 변하는지 비교하세요. 대문이 폐쇄되는 시간대가 있다면 어떤 속성을 추가할지 적으세요.

[전체 예제 내려받기](../examples/chapter25.py) · 실행: `python chapter25.py`

## 다음 단계

[26 · 서비스권·등시간권과 보행 가정](service-area.html)로 이어집니다.

## 출처

[OSMnx distance/routing](https://osmnx.readthedocs.io/en/stable/user-reference.html), [NetworkX shortest_path_length](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html). 확인 2026-09-30.
