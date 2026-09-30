---
title: "04 · 설치·import·배열과 재현 환경"
description: "설치할 때의 환경, 코드를 실행할 때의 환경, 배열의 역할을 익힙니다."
eyebrow: "PART 01 / CHAPTER 04"
---

**목표:** 라이브러리를 설치·불러오고 실행 환경을 기록합니다. **선수:** 01장. **실습:** 30~45분.

## 개념

가상환경은 프로젝트마다 Python 패키지 조합을 분리하는 공간입니다. 다른 프로젝트에서 필요한 버전과 충돌하지 않도록 둡니다. 터미널은 명령을 실행하는 창, `.py`는 Python 코드 파일, 노트북은 코드와 출력·설명을 셀 단위로 담는 문서입니다.

NumPy는 여러 숫자를 일정한 형태로 담는 ndarray와 빠른 배열 계산을 제공합니다. pandas는 행·열·열 이름이 있는 표를 다루며, GeoPandas는 그 표에 지리 도형을 연결합니다. 배열의 `shape`는 행열 크기, `dtype`은 정수·실수 등의 저장 형식입니다.

## 왜 필요한가

패키지를 설치했는데 `ModuleNotFoundError`가 나오면 설치한 Python과 실행한 Python이 다를 수 있습니다. `python -m pip`로 현재 Python에 설치하고 실행 파일 경로를 확인하는 습관이 도움이 됩니다.

## 핵심 API와 설치

저장소 루트에서 `python -m venv .venv`를 실행합니다. Windows에서는 다음처럼 활성화 없이 환경 내부 Python을 직접 사용할 수 있습니다.

```text
.venv/Scripts/python.exe -m pip install -r books/python-geospatial/requirements.txt
.venv/Scripts/python.exe books/python-geospatial/examples/chapter04.py
```

macOS/Linux는 `.venv/bin/python`을 사용합니다. 실행 환경의 버전은 [환경 안내](../stack.html)에 고정해 두었습니다. GeoAI 실습에는 추가 `requirements-ai.txt`가 필요합니다.

## 최소 실행 예제

{{code:chapter04.py}}

`import numpy as np`의 np는 관습적인 별명이며 새 라이브러리가 아닙니다. `mean`은 평균, `axis=0`은 행 방향을 줄여 열별 값을 만든다는 뜻입니다. 코드가 저장되는 폴더와 현재 실행 폴더는 다를 수 있으므로 파일 경로도 확인합니다.

## 조경·도시 실무 예제

한 프로젝트에 `data/raw`, `data/processed`, `generated`를 구별하고 원본을 보존합니다. 패키지 버전, 원자료 기준일, 난수 seed, 실행 명령을 보고서 옆에 기록합니다. 코드만 같아도 입력 데이터가 바뀌면 결과는 바뀝니다.

## 시각화

배열을 먼저 출력해 행·열 순서를 이해하세요. 화면 위쪽 행이 지리적 북쪽인지 여부는 배열만으로 알 수 없고 래스터 transform을 봐야 합니다. 이후 15장에서 배열과 위치를 연결합니다.

## 흔한 오류

`pip install`을 Python 코드 셀에 일반 문장처럼 쓰면 문법 오류가 납니다. 터미널 명령과 Python 문장을 구별하세요. 정수 배열에 결측을 표현하려고 `NaN`을 넣을 때는 실수형 변환 또는 별도 mask가 필요합니다.

## 연습문제

다른 모양의 배열을 만들고 `shape`, 전체 평균, 행별 평균, 열별 평균을 비교하세요. 현재 실행 파일 경로를 확인한 뒤 설치 환경과 같은지 점검하세요.

## 다음 단계

[2부](../parts/vector.html)에서 GeoPandas와 Shapely를 실제 파일 작업에 사용합니다.

## 출처

[Python venv](https://docs.python.org/3/library/venv.html), [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html). 확인 2026-09-30.
