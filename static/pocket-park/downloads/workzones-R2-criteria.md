# 소공원 공구 구분 및 IFC 4.3 객체표현 기준

R2-ZONING-REVIEW · 프로젝트 정의 기준 · 2026-09-25

이 연구에서 공구는 계약·발주 단위가 아닌 시공계획의 관리 구역을 뜻함

4개 공구는 비교를 위한 연구 매개변수이며 법정·KCS 의무 개수가 아니다.

## Z01 관목 군락의 완결성

식재 설계의 군락 단위를 경계로 나누지 않는다. 경계 후보는 군락 사이 빈 공간을 이용한다.

확인: 12개 군락 각각 단일 공구에 포함

## Z02 수목·시설물 작업 단위

수목 하부 영역, 퍼걸러 및 해당 휴게 포장, 진입 포장은 한 작업 단위로 묶는다.

확인: 수목 하부 반경0.75m 16개 및 포장 포켓5개 분할0; 0.75m는 설계 영역이며 장비 안전반경이 아님

## Z03 전 부지·연결계통 작업 유지

표토·부지정지, 집수정·우수관 관저고 조정, 경계석 일괄 설치는 공구 개수만으로 분할하지 않는다.

확인: 부지정지·배수는 기존 SITE 작업. 경계석 일괄안은 다음 공정 판본에 통일 필요

## Z04 공구 경계의 공간 일관성

4개 관리 공구는 부지 안에서 서로 겹치지 않고 틈 없이 전체를 덮는 연결된 영역으로 만든다.

확인: 합계2000㎡, 중복0㎡, 누락0㎡, 분리된 조각0

## Z05 반입·장비 동선

진입구와 공유 운반로는 별도 공용 자원으로 관리한다. 공구가 다르다는 이유만으로 병행을 허용하지 않는다.

확인: 보행로2m 유지; 장비 폭·회전·적치·안전거리 검증은 별도 필요

## Z06 포장 이음·검측 단위

벤치·퍼걸러 포켓은 통째로 유지하고, 포장 경계를 지나는 공구선은 블록 모듈과 시공 이음을 고려한다.

확인: 200mm 모듈을 고려한 횡단 위치; 최종 줄눈·검측 상세는 미확정

## Z07 물량과 작업량 재배분

개체는 개수로, 면적 작업은 실제 교차 면적으로 산정한다. 면적을 동일하게 맞추지 않으며 직종별 작업시간과 병목을 함께 본다.

확인: 16교목·677관목·6벤치·1퍼걸러 및 잔디·포장 총량 보존

## Z08 관리 공구와 실제 작업면 구분

A~D는 관리 단위다. 북측·동측처럼 큰 공구는 관목 군락·포장 구간을 세부 작업면으로 정의하고 작업반을 배정한다.

확인: 군락12개를 세부 작업면 후보로 기록. 병행 행동의 작업면 단위 구현은 후속

## 공구별 물량

| 공구 | 면적(㎡) | 교목 | 관목 | 벤치 | 퍼걸러 |
|---|---:|---:|---:|---:|---:|
| A 서측 벤치·식재 | 467.61 | 2 | 63 | 3 | 0 |
| B 북측·동측 식재 | 563.44 | 9 | 301 | 0 | 0 |
| C 남서 진입·식재 | 553.63 | 2 | 181 | 1 | 0 |
| D 동남 휴게·시설 | 415.32 | 3 | 132 | 2 | 1 |

## IFC 표현

| 대상 | 엔티티 | PredefinedType | 개수 |
|---|---|---|---:|
| 기존 R1 공구 참조 | IfcSpatialZone | CONSTRUCTION | 4 |
| 보행로 포장 | IfcPavement | FLEXIBLE | 4 |
| 진입·휴게 포장 | IfcPavement | FLEXIBLE | 3 |
| 잔디 | IfcGeographicElement | VEGETATION | 4 |
| 관목 식재면 | IfcGeographicElement | VEGETATION | 4 |
| 수목 하부 멀칭 | IfcCovering | USERDEFINED | 4 |
| 교목 | IfcGeographicElement | VEGETATION | 16 |
| 개별 관목 | IfcGeographicElement | VEGETATION | 677 |
| 벤치 | IfcFurniture | USERDEFINED | 6 |
| 퍼걸러 | IfcElementAssembly | USERDEFINED | 1 |
| 우수관 | IfcPipeSegment | RIGIDSEGMENT | 4 |
| 집수정 | IfcDistributionChamberElement | SUMP | 4 |
| 화강석 경계석 | IfcKerb | USERDEFINED | 4 |
| 임시 접근로 참조 | IfcBuildingElementProxy | USERDEFINED | 5 |
| 지형 | IfcGeographicElement | TERRAIN | 1 |
| 주변 보도 참조 | IfcBuildingElementProxy | USERDEFINED | 1 |
| 주변 도로 참조 | IfcBuildingElementProxy | USERDEFINED | 1 |
| 제안 R2 공구 | IfcSpatialZone | CONSTRUCTION | 4 |

교목·관목·잔디 세부 분류는 Landscape_ObjectClass.Category에 기록하는 사용자 분류이다. TREE 등은 IFC 표준 열거값이 아니다. 개별 관목과 관목 식재면을 중복 개수로 합산하지 않는다.

공구는 IfcSpatialZone/CONSTRUCTION, 객체의 추가 공간 참조는 IfcRelReferencedInSpatialStructure, 작업은 IfcTask를 사용한다. 원본743개 객체와92개 작업시간을 유지하면서 제안 공구4개를 추가했다. 기존 R1 공구4개는 일정 참조용으로 구분했다. 제안 구역은 ScheduleApplies=False이다.

## 적용 범위

본 검토는 공구와 객체표현 검토이며 새 공정시간이나 강화학습 성과가 아니다. 공유 동선, 장비 작업영역, 반입·검측 조건을 작업면에 연결하고 경계석 일괄 공정을 통일한 뒤 재계산해야 한다. 장비 안전반경·수리성능·현장 검증은 미수행이다.

참고: [조경 IFC 4.3 해설](https://spatialflare.com/landscape-ifc4_3/), [IfcSpatialZone](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcSpatialZone.htm), [IfcGeographicElementTypeEnum](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcGeographicElementTypeEnum.htm).
