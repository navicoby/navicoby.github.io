---
title: "31 · Semantic segmentation과 라벨"
description: "픽셀별 범주 분류와 객체 구분의 차이, 라벨과 손실함수를 배웁니다."
eyebrow: "PART 09 / CHAPTER 31"
---

**학습 목표:** 픽셀별 범주 분류와 객체 구분의 차이, 라벨과 손실함수를 배웁니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

Semantic segmentation은 각 픽셀에 녹지·건물·도로 같은 범주를 지정하는 작업입니다. 같은 범주의 개별 나무를 각각 구별하는 instance segmentation과 다릅니다. 라벨은 학습·평가에 쓰는 참조 분류이고, logits는 모델이 출력한 정규화 전 범주 점수입니다.

scikit-image는 영상 처리 라이브러리입니다. measure.label은 연결된 영역에 번호를 붙여 후처리할 수 있지만 붙어 있는 개별 수목을 저절로 분리해 주는 것은 아닙니다.

## 왜 필요한가

조경 분석에서 '녹지 총면적'과 '나무 개체 수'는 다른 산출물입니다. 라벨 정의를 먼저 정하지 않으면 학습 목표와 최종 지표가 어긋납니다.

## 핵심 API

CrossEntropyLoss 입력은 보통 (N,C,H,W) float logits, 목표는 (N,H,W) long 범주 ID입니다. ignore_index는 평가 불가 셀을 제외합니다. loss 전에 softmax를 적용하지 않습니다.

## 최소 실행 예제

{{code:chapter31.py}}

## 조경·도시 실무 예제

대각선으로만 맞닿은 두 셀은 4방향 연결에서 서로 다른 영역입니다. 실제 면적은 셀 수에 셀 면적을 곱해 계산합니다. 항공사진 시점과 라벨 시점이 다르면 신축·벌채 지점을 오답으로 만들 수 있습니다.

## 시각화와 결과 읽기

원본 영상, 정답 라벨, 예측 범주, 오류 마스크를 같은 범위로 배치합니다. 범주 색은 모든 지도에서 동일하게 유지합니다.

## 흔한 오류

라벨을 bilinear로 확대하면 범주가 섞입니다. ignore_index=255인 셀을 평가 분모에 넣지 않습니다. 연결 영역 개수를 곧바로 나무 수로 보고하지 않습니다.

## 연습문제

connectivity=2로 바꾸고 영역 수가 달라지는 이유를 설명하세요.

[전체 예제 내려받기](../examples/chapter31.py) · 실행: `python chapter31.py`

## 다음 단계

[32 · U-Net의 구조와 작은 구현](unet.html)로 이어집니다.

## 출처

[PyTorch CrossEntropyLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html), [scikit-image measure](https://scikit-image.org/docs/stable/api/skimage.measure.html). 확인 2026-09-30.
