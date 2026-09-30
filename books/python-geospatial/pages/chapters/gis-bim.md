---
title: "34 · GIS와 IFC/BIM의 좌표·속성 연결"
description: "GIS의 지도 좌표와 BIM의 로컬 좌표를 연결할 때 필요한 정보를 정리합니다."
eyebrow: "PART 10 / CHAPTER 34"
---

**학습 목표:** GIS의 지도 좌표와 BIM의 로컬 좌표를 연결할 때 필요한 정보를 정리합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

BIM은 시설의 형상과 속성을 연결해 다루는 정보 모델링 방식입니다. IFC는 이러한 모델을 교환하는 개방형 데이터 표준이며 Python 라이브러리가 아닙니다. IfcOpenShell은 IFC 파일을 읽고 처리하는 데 사용할 수 있는 도구입니다. GeoPandas는 기본적으로 2차원 공간표를 다루므로 IFC의 층별·부재별 3차원 의미를 모두 대신하지 않습니다.

BIM 로컬 좌표를 GIS에 맞추려면 길이 단위, 원점 이동, 회전, 축척, 좌표계와 높이 기준을 확인합니다. IFC의 IfcMapConversion 등 지리참조 정보가 있는지 점검하고 임의의 원점으로 배치하지 않습니다.

## 왜 필요한가

건물 footprint·DEM·출입구와 BIM 외부공간을 결합하려면 위치가 맞아야 합니다. 수평으로 잘 맞더라도 높이 기준이 다르면 지형과 건물이 떠 있거나 묻힐 수 있습니다.

## 핵심 API

아래 NumPy 예제는 mm 로컬 좌표를 m로 바꾸고 회전·평행이동하는 평면 계산만 보여 줍니다. 실제 IFC 파싱이나 IFC 지리참조의 완전 구현은 아닙니다.

## 최소 실행 예제

{{code:chapter34.py}}

## 조경·도시 실무 예제

실제 프로젝트는 측량 기준점, 설계 좌표계, IFC의 단위·MapConversion·ProjectedCRS, DEM 높이 기준을 대조합니다. 검증된 건물 외곽선과 출입구를 GIS에 내보낸 뒤 주변 도로망과 연결합니다.

## 시각화와 결과 읽기

로컬 원점과 GIS 원점을 구분하고, 회전 전·후의 x/y축을 화살표로 그리세요. 최소 두 점의 거리만 확인하지 말고 독립 기준점의 위치 잔차도 확인합니다.

## 흔한 오류

mm를 m로 해석하면 크기가 1,000배 달라집니다. 모델의 TrueNorth와 좌표 변환 회전을 무조건 동일하게 취급하지 않습니다. Z가 있는 Shapely 도형도 일반 공간 연산은 평면 기준입니다.

## 연습문제

회전을 0°로 바꾸고 결과를 비교하세요. 실제 자료에서 수평 CRS와 수직 기준을 어느 문서에서 확인할지 체크 표를 만드세요.

[전체 예제 내려받기](../examples/chapter34.py) · 실행: `python chapter34.py`

## 다음 단계

[35 · 최종 실습: 공원 분석 묶음 만들기](capstone.html)로 이어집니다.

## 출처

[buildingSMART IfcMapConversion](https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcMapConversion.html), [IfcOpenShell 문서](https://docs.ifcopenshell.org/), [Shapely 좌표와 평면 분석](https://shapely.readthedocs.io/en/stable/manual.html). 확인 2026-09-30.
