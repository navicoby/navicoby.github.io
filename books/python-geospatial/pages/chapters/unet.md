---
title: "32 · U-Net의 구조와 작은 구현"
description: "U-Net의 축소·확대·skip connection을 작은 실행 모델로 확인합니다."
eyebrow: "PART 09 / CHAPTER 32"
---

**학습 목표:** U-Net의 축소·확대·skip connection을 작은 실행 모델로 확인합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

U-Net은 영상 분할에 널리 쓰이는 신경망 구조입니다. 인코더는 공간 크기를 줄이며 특징을 모으고, 디코더는 크기를 다시 키워 픽셀별 출력을 만듭니다. Skip connection은 같은 수준의 인코더 특징을 디코더로 전달해 위치 정보를 보완합니다.

여기의 TinyUNet은 원 논문의 전체 구조를 재현한 것이 아니라 한 번의 축소와 확대를 가진 교육용 변형입니다. 네 채널 입력을 가정하며 2개 범주의 logits를 출력합니다.

## 왜 필요한가

넓은 문맥과 세부 경계가 함께 중요한 건물·녹지 분할에 이러한 구조를 적용할 수 있습니다. 하지만 해상도, 라벨 품질, 지역 차이를 해결하는 작업이 모델 구조 선택만큼 중요합니다.

## 핵심 API

nn.Module, Conv2d, MaxPool2d, torch.nn.functional.interpolate, torch.cat, CrossEntropyLoss, loss.backward()를 사용합니다. 이 예제는 순전파와 기울기 계산만 확인하며 학습된 정확도를 주장하지 않습니다.

## 최소 실행 예제

{{code:chapter32.py}}

## 조경·도시 실무 예제

여기서 네 채널은 향후 RGB+근적외선 또는 영상+DEM 등의 구성을 시험할 공간입니다. 실제로 채널을 통합하려면 16장의 격자 정렬과 29장의 정규화를 먼저 적용하세요. 훈련·검증·시험 지역을 나눈 다음 optimizer.step을 반복하는 학습 절차로 확장합니다.

## 시각화와 결과 읽기

입력 4×16×16 → 특징 8×16×16 → 축소 16×8×8 → 확대 16×16×16 → 연결 24×16×16 → 출력 2×16×16 순으로 읽습니다. 화살표의 숫자는 채널×높이×너비입니다.

## 흔한 오류

마지막 출력 채널은 범주 수와 같아야 합니다. feature map 보간과 범주 라벨 보간을 혼동하지 않습니다. 무작위 입력에서 loss가 계산된다는 사실은 실제 분류 성능을 의미하지 않습니다.

## 연습문제

입력 채널을 5로 바꾸고 DEM 채널을 넣기 위해 바꿔야 할 부분을 찾아보세요. 목표 범주를 3개로 바꾸면 출력과 라벨의 조건은 어떻게 달라질까요?

[전체 예제 내려받기](../examples/chapter32.py) · 실행: `python chapter32.py`

## 다음 단계

[33 · 공간 분할·IoU·오류 지도](geoai-validation.html)로 이어집니다.

## 출처

[U-Net 원 논문·저자 자료](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/), [PyTorch nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html). 확인 2026-09-30.
