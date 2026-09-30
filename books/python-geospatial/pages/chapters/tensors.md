---
title: "29 · NumPy에서 PyTorch 텐서로"
description: "지리 배열을 AI 입력 텐서로 바꾸고 채널·배치·NoData를 구분합니다."
eyebrow: "PART 09 / CHAPTER 29"
---

**학습 목표:** 지리 배열을 AI 입력 텐서로 바꾸고 채널·배치·NoData를 구분합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

PyTorch는 텐서 연산과 신경망 학습을 위한 Python 라이브러리입니다. 텐서는 여러 축을 가진 수치 자료이며, NumPy 배열과 비슷하지만 자동 미분과 GPU 연산 등을 지원합니다. CNN의 일반적인 영상 입력은 N×C×H×W입니다. N은 묶음(batch), C는 채널, H/W는 행과 열입니다.

Rasterio가 읽은 (band,row,col) 배열에 batch 축을 추가하면 이 구조로 연결됩니다. 텐서 자체는 CRS와 transform을 기억하지 않으므로 위치 정보는 별도로 보존합니다.

## 왜 필요한가

RGB, 근적외선, DEM을 채널로 쌓으려면 위치와 해상도를 먼저 맞춰야 합니다. 같은 배열 모양만으로 같은 장소임을 보장하지 않습니다. 반사도와 고도는 단위가 달라 채널별 정규화도 필요합니다.

## 핵심 API

torch.from_numpy(), Tensor.unsqueeze(0), dtype=torch.float32, isfinite 등을 사용합니다. from_numpy는 메모리를 공유할 수 있습니다. 학습 자료에서 구한 평균·표준편차를 검증·시험 자료에도 동일하게 적용합니다.

## 최소 실행 예제

{{code:chapter29.py}}

## 조경·도시 실무 예제

두 채널 합성 예제입니다. 실제 입력에는 밴드 순서, 반사도 보정, DEM 단위, NoData 마스크와 타일별 지리참조를 함께 기록하세요. 예제 평균·표준편차는 설명을 위한 값이며 실제 학습자료 통계가 아닙니다.

## 시각화와 결과 읽기

채널마다 작은 회색조 그림을 나란히 놓고 마지막에 겹쳐 쌓이는 구조를 표현하면 입력의 의미가 보입니다.

## 흔한 오류

(H,W,C)를 그대로 Conv2d에 넣으면 채널이 틀립니다. uint16 DN을 변환·정규화 없이 넣지 않습니다. NoData를 0으로 바꿀 때 유효한 0과 구별할 마스크가 필요합니다.

## 연습문제

DEM 채널을 하나 더 추가해 shape을 (1,3,2,2)로 만들고 고도 단위를 적으세요.

[전체 예제 내려받기](../examples/chapter29.py) · 실행: `python chapter29.py`

## 다음 단계

[30 · CNN과 convolution의 작동](convolution.html)로 이어집니다.

## 출처

[PyTorch tensor tutorial](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html). 확인 2026-09-30.
