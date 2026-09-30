---
title: "20 · Copernicus Browser·STAC·영상 취득"
description: "영상 검색 조건과 실제 다운로드 기록을 재현 가능한 목록으로 남깁니다."
eyebrow: "PART 06 / CHAPTER 20"
---

**학습 목표:** 영상 검색 조건과 실제 다운로드 기록을 재현 가능한 목록으로 남깁니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Copernicus Browser는 지도에서 위치·날짜·제품을 검색하고 영상을 확인하는 서비스입니다. STAC(SpatioTemporal Asset Catalog)은 공간·시간 자료의 목록을 표현하는 규약입니다. Item은 한 관측 자료의 메타데이터를, asset은 밴드나 메타데이터 파일 등의 연결 정보를 담습니다. STAC 검색 결과 자체가 영상 배열은 아닙니다.

검색 API와 다운로드 인증은 별개일 수 있습니다. 제공기관별 컬렉션 ID, asset 이름, 인증 방식은 공식 문서와 실제 응답을 확인해야 합니다.

## 왜 필요한가

'서울의 맑은 영상'이라는 기록만으로는 동일 분석을 재현할 수 없습니다. 관측일, 제품 ID, 처리 기준선, 구름 조건, 대상지 경계와 다운로드 파일 목록을 남겨야 합니다.

## 핵심 API

실제 취득은 Browser에서 대상지와 L2A·기간을 선택 → 구름과 그림자를 눈으로 확인 → 제품/밴드 다운로드 → 메타데이터 저장 순서입니다. STAC 자동화에서는 /collections와 /search의 현재 명세를 확인합니다. 아래 코드는 네트워크 없이 검색 조건 파일만 만듭니다.

## 최소 실행 예제

{{code:chapter20.py}}

## 조경·도시 실무 예제

[Copernicus Browser](https://browser.dataspace.copernicus.eu/)에서 대상지를 검색하고 관측일이 다른 두 장을 비교하세요. 타일 전체 구름 비율이 낮아도 공원 위에 구름이 있을 수 있으므로 대상지에서 확인합니다. 실제 다운로드한 제품 ID와 파일 해시를 분석 기록에 추가합니다.

## 시각화와 결과 읽기

전체 RGB, 대상지 확대, 구름/SCL 마스크를 나란히 비교합니다. 공개 페이지에 실제 관측 영상과 합성 실습 그림을 분명하게 구별해 표시합니다.

## 흔한 오류

계정 토큰을 노트북이나 HTML에 저장하지 않습니다. STAC asset 주소가 영구 공개 다운로드 URL이라고 가정하지 않습니다. 현재 가이드의 검색 계획 파일을 실제 취득 완료 증거로 쓰지 않습니다.

## 연습문제

본인 대상지의 검색 조건을 정하고 실제 제품 하나의 ID·관측시각·처리 수준·구름 정보를 기록하세요. 다운로드에 필요한 조건은 제공자 문서에서 확인하세요.

[전체 예제 내려받기](../examples/chapter20.py) · 실행: `python chapter20.py`

## 다음 단계

[21 · 밴드·SCL·반사도 보정·정렬](satellite-bands.html)로 이어집니다.

## 출처

[Copernicus STAC API](https://documentation.dataspace.copernicus.eu/APIs/STAC.html), [Copernicus Browser 안내](https://documentation.dataspace.copernicus.eu/Applications/Browser.html). 확인 2026-09-30.
