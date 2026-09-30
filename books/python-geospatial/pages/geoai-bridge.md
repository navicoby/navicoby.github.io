---
title: GeoAI와 BIM으로 연결하기
description: 배열·그래프·객체를 연결하기 전에 좌표, 시간, 해상도와 평가 단위를 맞춥니다.
eyebrow: NEXT / SPATIAL AI
---

GeoAI로 넘어가는 출발점은 더 큰 모델보다 **정렬된 입력과 검증 가능한 정답**입니다. 공간분석으로 만드는 거리·경사·토지피복 특성이 좋은 기준선이 될 수 있습니다. 이 페이지는 후속 장의 설계 안내이며 학습된 모델이나 검증된 분류 성능을 제공하는 페이지는 아닙니다.

## 표·배열·그래프·객체

| 자료 | 표현 | 연결 전에 확인 |
|---|---|---|
| Sentinel-2·DEM | band × row × col 배열 | CRS·격자·해상도·촬영일·유효마스크 |
| 토지이용·건물·필지 | GeoDataFrame | geometry·분류 코드·ID·기준일 |
| OSM 도로망 | 유향 다중 그래프 | node/edge·접근 제한·길이·연결성 |
| BIM/IFC | 객체·속성·관계·3D 형상 | 객체 ID·단위·local placement·지리참조·수직 datum |

공통 10m 격자가 필요하면 DEM·도로거리·건물피복률을 그 격자에 집계합니다. 이때 건물 세부형상을 10m로 축약하면서 무엇을 잃는지 명시합니다. 반대로 10m 위성영상을 1m로 늘려도 1m 관측 정보가 생기지 않습니다.

## NumPy에서 PyTorch로

입력 `X`는 일반적으로 `[N, C, H, W]`의 float32입니다. 예를 들어 C는 B02/B03/B04/B08, 고도, 경사, 도로거리 채널입니다. 채널마다 단위와 유효마스크가 다르므로 훈련 자료에서 구한 통계로 정규화하고 결측값 정책을 문서화합니다.

다중 클래스 segmentation 타깃 `y`는 `[N, H, W]`의 정수 클래스 ID입니다. 모델 출력은 `[N, K, H, W]`의 logits이며 `CrossEntropyLoss(ignore_index=...)`에는 보통 softmax 전 logits를 넣습니다. 클래스 ID의 범위와 NoData ID를 검사합니다. 바이너리 문제라면 출력·타깃과 손실 구성이 달라집니다. [PyTorch CrossEntropyLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html), [Dataset/DataLoader](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)

## CNN에서 U-Net으로

convolution은 작은 커널을 움직이며 주변 패턴을 결합하는 연산입니다. stride는 이동 간격, padding은 경계 처리, receptive field는 한 출력이 참고하는 입력 범위입니다. 커널을 지나며 원래 픽셀과 출력 픽셀의 공간 대응이 어떻게 변하는지 추적합니다.

U-Net은 해상도를 줄이며 문맥을 읽는 encoder와 해상도를 복원하는 decoder를 연결하고, skip connection으로 공간 세부정보를 전달합니다. 원 논문은 생의학 영상 문제에서 제안됐으며, 위성영상에 쓰려면 입력 밴드·라벨·해상도·훈련 구성을 새로 정해야 합니다. [Ronneberger et al., 2015](https://arxiv.org/abs/1505.04597)

단순 NDVI 임계값이나 지도학습 기준선부터 비교합니다. 신경망이 더 복잡하다는 이유만으로 설계 판단에 더 적합한 것은 아닙니다. 분할 결과의 작은 객체를 분석할 때는 [scikit-image label/regionprops](https://scikit-image.org/docs/stable/api/skimage.measure.html)를 활용할 수 있지만 지도 좌표와 셀 면적을 함께 복원해야 합니다.

## 평가를 먼저 설계하기

- 인접하거나 겹치는 타일을 무작위로 훈련·시험에 나누면 같은 공간 패턴이 양쪽에 들어갈 수 있습니다. 지역을 분리하고 필요하면 완충 거리를 둡니다.
- 같은 지역의 다른 날짜로 일반화하려는 경우 시점도 분리합니다. 정규화·증강 선택에 시험 데이터를 사용하지 않습니다.
- overall accuracy만 보고하지 않고 클래스별 IoU/F1·혼동행렬·공간 오류 지도를 봅니다. 배경 비율이 크면 단순 정확도가 과장됩니다.
- 라벨 제작 시점과 영상 촬영일, 경계 혼합픽셀, 구름과 그림자, 라벨 라이선스를 기록합니다.
- 모델의 예측·설계 적합도·법적 가능성은 서로 다른 판단입니다. 현장 검증과 실무 규정을 별도로 확인합니다.

## BIM과 연결하는 최종 실습

3,000㎡ 가상공원에 대해 지형 후보 영역, 주변 보행 접근성, 위성 기반 주변 식생 요약을 만들고 설계 객체의 속성에 분석 ID·날짜·출처를 연결합니다. IFC 위치는 local placement와 지도 변환을 확인하며 지형의 수직 datum까지 일치시킵니다. 관련 스키마의 출발점은 [buildingSMART IFC 4.3](https://ifc43-docs.standards.buildingsmart.org/)입니다.

최종 결과물은 “AI가 선택한 정답 부지”가 아니라 **입력·가정·후보 순위·민감도·오류를 추적할 수 있는 설계 검토 자료**입니다. 가중치를 바꿨을 때 후보 순위가 뒤집히는지 확인하고, 지도·표·IFC 객체를 같은 분석 ID로 연결합니다.

이어 읽기: [전체 35장 로드맵](roadmap.html), 기존 사이트의 [조경 IFC 4.3](/landscape-ifc4_3/)과 [소공원 BIM 실습](/pocket-park/). 공식 문서 확인일은 2026-09-30입니다.
