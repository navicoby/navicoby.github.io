---
title: "BIM / SLAM / Landscape AI 리서치 리포트 #1"
date: 2026-03-07
draft: false
tags: ["BIM", "SLAM", "Landscape", "AI", "Research"]
---

> 수집일: 2026-03-08 | 수집 범위: 이번 주 | 분야: BIM / SLAM / Landscape AI

---

## 🏗️ BIM (Building Information Modeling)

### 📄 논문

**Indoor Scan-to-BIM Automation: From Mobile Perception to 3D Building Modelling**
- 출처: ScienceDirect (2025.12)
- AI 기반 실내 Scan-to-BIM 워크플로우 전반을 다룬 리뷰 논문. 모바일 LiDAR 포인트 클라우드 생성, 건축 시맨틱 세그멘테이션, 요소 모델링까지 SLAM과 딥러닝의 최신 동향을 정리함.
- 🔗 https://www.sciencedirect.com/science/article/abs/pii/S092658052500771X

**Predictive Hybrid Scan-to-BIM Method for Heritage Building Documentation**
- 저자: Salah, R., Géczy, N. et al. | 출처: Scientific Reports (2026)
- 문화재 건축물의 Scan-to-BIM 정확도와 완성도를 향상시키는 예측 기반 하이브리드 방법론 제안. UAV 사진측량과 지상 레이저 스캐닝 융합 접근.
- 🔗 https://www.nature.com/articles/s41598-026-38200-8

### 📰 기사

**AEC Trends 2026: BIM 6.0, Digital Twins & AI의 통합**
- 출처: Tesla Outsourcing Services (2026.03)
- 2026년 AEC 산업은 BIM, 디지털 트윈, IoT, AI가 단일 통합 플랫폼으로 수렴하는 전환점. GSA는 연방 프로젝트에 '단일 진실 공급원(Single Source of Truth)' 워크플로우를 공식 의무화함.
- 🔗 https://www.teslaoutsourcingservices.com/blog/the-2026-aec-technology-bim-ai-digital-twins/

**Scan-to-BIM 2026 트렌드: AI 자동화와 디지털 트윈**
- 출처: ViBIM Global (2025.10)
- AI·ML이 포인트 클라우드 처리를 자동화하여 수동 모델링 작업량을 대폭 감소. Hexagon 조사에 따르면 기업의 62%가 디지털 트윈에서 예측 유지보수와 에너지 관리 분야에서 유의미한 가치를 경험 중.
- 🔗 https://vibimglobal.com/blog/trends-in-scan-to-bim/

**Cintoo, FEDER 펀딩 수주: AI 기반 Scan-to-Digital Twin 개발**
- 출처: Cintoo (2026.03)
- 프랑스 스타트업 Cintoo가 포인트 클라우드에서 BIM 모델을 자동 생성하고 시맨틱 레이어를 추가하는 기술 개발에 €1,524,018 지원 확보. 밸브, 펌프 등 산업 장비의 자동 인식 포함.
- 🔗 https://cintoo.com/en/news/cintoo-receives-funding-from-feder

---

## 🤖 SLAM (Simultaneous Localization and Mapping)

### 📄 논문

**3DGS-SLAM: LiDAR 포인트 클라우드와 비전 융합 기반 동적 장면 처리**
- 출처: MDPI Applied Sciences (2025.04)
- LiDAR와 카메라 데이터를 통합한 3D Gaussian Splatting 기반 SLAM 시스템. 불확실성 기반 3D 세그멘테이션으로 동적 객체를 제거하고 정적 맵 재건 품질을 향상. 슬라이딩 윈도우 키프레임 전략으로 연산 부하 절감.
- 🔗 https://www.mdpi.com/2076-3417/15/8/4190

**LiV-GS: 실외 환경 LiDAR-Vision 통합 3DGS SLAM**
- 출처: arXiv / IEEE (2024.11)
- 대규모 실외 환경에서 이산 LiDAR 데이터와 연속 Gaussian 맵을 직접 정렬하는 최초의 방법. 7.98 FPS의 실시간 Novel View Synthesis 달성. LiDAR 시야 밖 영역도 조건부 Gaussian 제약으로 복원 가능.
- 🔗 https://arxiv.org/html/2411.12185v1

**Gaussian-LIC: LiDAR-Inertial-Camera 융합 실시간 포토리얼리스틱 SLAM**
- 출처: arXiv / ICRA 2025
- LiDAR, IMU, 카메라를 긴밀하게 융합한 실시간 포토리얼리스틱 SLAM 시스템. 실외 무한 장면 확장 시 발생하는 기존 RGB-D 기반 시스템의 한계를 극복. 하늘 모델링과 카메라 노출 변화 처리 포함.
- 🔗 https://arxiv.org/abs/2404.06926

### 📰 기사 / 리소스

**Awesome-3DGS-SLAM: 2026년 최신 논문 큐레이션 리스트**
- 출처: GitHub (KwanWaiPang)
- 이미지, 이벤트 카메라, LiDAR 기반 3DGS SLAM 논문 종합 정리. 2026년 발표 논문으로 EAGS-SLAM(IEEE Sensors Journal), DAGS-SLAM(arXiv), LD3DGS-SLAM(IOTJ), WaterSplat-SLAM(수중 환경, RAL) 등 포함.
- 🔗 https://github.com/KwanWaiPang/Awesome-3DGS-SLAM

---

## 🌿 Landscape + AI

### 📄 논문

**AI 기반 지속가능 조경 설계: Generative-Critical 멀티에이전트 프레임워크**
- 출처: MDPI Urban Science (2026.01)
- '생성-비판' 멀티에이전트 워크플로우로 설계안을 반복 최적화하는 AI 의사결정 지원 프레임워크 제안. 전문가 지식 베이스와 정량적 스코어카드로 미적 형태와 생태 기능 간 간극 해소. 문화 공원 사례 연구 및 전문가 10인 평가 검증.
- 🔗 https://www.mdpi.com/2413-8851/10/1/56

**GAN + Stable Diffusion 통합 공원 생성 설계 파이프라인**
- 출처: ScienceDirect (2025.07)
- 위성 원격탐사로 도시 환경 정보를 추출하고, GAN으로 외부 맥락 기반 설계안을 생성한 뒤 Stable Diffusion으로 해상도를 64배 확장하는 완전 자동화 워크플로우 제안.
- 🔗 https://www.sciencedirect.com/science/article/pii/S0264275125004822

**AIGC in Landscape Design: 기회와 도전 리뷰**
- 출처: ScienceDirect (2025.10)
- 사이트 분석, 설계 개념 생성, 파라메트릭 최적화, 식재 선택, 시공 관리 전반에서 AI 생성 콘텐츠의 적용 현황 정리. 데이터 품질, 설계 전문성, 생태 지속가능성 등 주요 과제 제시.
- 🔗 https://www.sciencedirect.com/science/article/pii/S2666651025000178

### 📰 기사

**2026년 조경 설계사를 위한 AI 툴 Top 리스트**
- 출처: Rendair AI (2026)
- Rendair AI(스케치→포토리얼 렌더링), Autodesk Forma(미기후 분석), TestFit(사이트 레이아웃 자동화) 등 실무 워크플로우별 최적 AI 도구 정리. Polycam → SketchUp → Rendair AI 조합의 현장 실무 활용 사례 포함.
- 🔗 https://rendair.ai/blog/tools-top-ai-tools-for-landscape-designers-in-2026

---

## 💡 이번 주 핵심 트렌드

1. **Scan-to-BIM의 AI 자동화 가속** — 포인트 클라우드에서 IFC 기반 BIM 모델로의 변환이 딥러닝으로 점점 자동화되고 있으며, 디지털 트윈의 기반 데이터로 자리잡는 중.

2. **3DGS가 SLAM의 새 표준으로** — NeRF 대비 빠른 렌더링 속도와 높은 표현력을 가진 3D Gaussian Splatting이 실내·실외 SLAM 시스템의 맵 표현 방식으로 빠르게 확산 중.

3. **LiDAR + 카메라 멀티모달 융합** — 단일 센서의 한계를 극복하기 위해 LiDAR의 정밀 깊이와 카메라의 텍스처를 결합하는 멀티모달 SLAM이 주류로 자리잡는 추세.

4. **조경 AI의 생태 기능 통합 과제** — 기존 AIGC 도구들이 시각적 생성에 편중된 반면, 2026년에는 생태 기능과 지속가능성을 설계 초기 단계부터 정량적으로 통합하려는 연구 흐름이 두드러짐.

5. **BIM 6.0 통합 생태계** — 설계·시공·운영이 단일 클라우드 플랫폼에서 실시간으로 연결되는 BIM 6.0 패러다임이 대형 AEC 기업의 표준으로 빠르게 확산 중.
