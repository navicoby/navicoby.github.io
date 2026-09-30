---
title: "30 · CNN과 convolution의 작동"
description: "작은 필터가 이웃 셀을 읽는 방식과 CNN의 학습을 구분합니다."
eyebrow: "PART 09 / CHAPTER 30"
---

**학습 목표:** 작은 필터가 이웃 셀을 읽는 방식과 CNN의 학습을 구분합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

CNN(Convolutional Neural Network)은 작은 필터를 여러 위치에 적용해 특징을 추출하는 신경망입니다. Convolution 층은 주변 셀의 값에 가중치를 곱해 더합니다. PyTorch Conv2d의 연산은 엄밀히는 필터를 뒤집지 않는 교차상관입니다. 실무에서는 이 층을 통상 convolution 층이라고 부릅니다.

커널 크기는 한 번에 보는 주변 범위, stride는 이동 간격, padding은 가장자리 처리입니다. 신경망 학습에서는 필터 가중치를 자료로부터 조정하지만, 아래 예제는 평균 필터를 직접 고정합니다.

## 왜 필요한가

도로나 수관의 패턴은 한 셀의 값뿐 아니라 주변 모양과 관계가 있습니다. 다만 같은 3×3 커널이라도 1m 영상과 10m 영상에서 보는 지상 범위는 다릅니다.

## 핵심 API

torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, bias)와 torch.no_grad()를 사용합니다. 입력과 출력의 채널 수 및 공간 크기를 계산해 보세요.

## 최소 실행 예제

{{code:chapter30.py}}

## 조경·도시 실무 예제

출력 5는 1~9의 평균입니다. 지형 평활화의 개념을 이해하는 데 쓸 수 있지만 이 필터가 식재 적합성을 학습한 것은 아닙니다. 실제 CNN에는 여러 층과 비선형 활성화, 손실함수, 학습자료가 필요합니다.

## 시각화와 결과 읽기

3×3 입력과 동일한 1/9 가중치 아홉 개를 나란히 그리고 합산이 5가 되는 과정을 설명하세요.

## 흔한 오류

padding=1의 바깥 0은 실제 관측값이 아닙니다. NoData가 주변 연산에 퍼질 수 있습니다. 필터 출력이 보기 좋다고 분석 정확도가 입증되는 것은 아닙니다.

## 연습문제

가운데 가중치만 1, 나머지는 0으로 바꾸고 평균 필터와 차이를 설명하세요.

[전체 예제 내려받기](../examples/chapter30.py) · 실행: `python chapter30.py`

## 다음 단계

[31 · Semantic segmentation과 라벨](segmentation.html)로 이어집니다.

## 출처

[PyTorch Conv2d](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html). 확인 2026-09-30.
