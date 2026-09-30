---
title: 한국 공공데이터·OSM·위성영상 수집 안내
description: 자료의 종류, 실제 취득 경로, 형식과 이용조건을 구분합니다.
eyebrow: DATA / PROVENANCE
---

**조사일: 2026-09-30.** “공개 포털에 있다”와 “원본을 제한 없이 재배포할 수 있다”는 다른 조건입니다. 포털명만 적지 말고 실제 상품 상세 페이지·기준일·이용조건을 남깁니다. 아래 가이드는 취득 경로를 조사한 것이며 인증이 필요한 원본 파일을 다운로드·검수한 기록은 아닙니다.

## 어느 기관에서 시작할까

| 기관·서비스 | 우선 찾을 자료 | 형식·취득 방식 | 확인할 사항 |
|---|---|---|---|
| [NGII 국토정보플랫폼](https://map.ngii.go.kr/) | DEM·수치지형도·정사영상 | 자료별 IMG/SHP 등, 도엽·지역 선택 다운로드 | 로그인·대용량 다운로드 도구, 표고기준·격자간격 |
| [VWorld](https://www.vworld.kr/) | GIS건물통합·연속지적·행정구역 등 | 상품별 SHP 다운로드, 별도 Data API/WMS/WFS | 인증키·서비스별 응답 형식·이용조건 |
| [국가공간정보포털](https://www.nsdi.go.kr/) | 국가 공간정보 목록·이전 안내 | 기존 자료명·링크를 찾는 출발점 | 이번 직접 접근 미확인. 이전 경로를 현재 다운로드 경로로 단정하지 않음 |
| [공공데이터포털](https://www.data.go.kr/) | 기관별 공간자료의 카탈로그·API | SHP/CSV/API 또는 외부 사이트 연결 | 카탈로그와 실제 파일 저장소 구별 |
| [서울 열린데이터광장](https://data.seoul.go.kr/) | 공원·생활인구·시설·행정 통계 | 상품별 CSV/XLS/JSON/XML/API | 주소·점 좌표인지 면 경계인지 확인 |
| [OpenStreetMap](https://www.openstreetmap.org/) | 보행 가능한 길·출입구·시설·건물 | OSMnx/Overpass, GraphML·GPKG로 보관 | 편집 누락·태그·접근 제한·ODbL |
| [Copernicus Data Space](https://dataspace.copernicus.eu/) | Sentinel-2A 등 위성영상 | Browser·STAC, SAFE/JP2 및 서비스별 asset | 제품 레벨·촬영일·cloud/SCL·인증·이용조건 |

VWorld와 국가공간정보포털의 메뉴·운영 통합 상태는 이번 웹 도구에서 직접 확인하지 못했습니다. 통합 시점을 단정하지 않고, 아래 공공데이터포털의 공식 상세 자료에서 연결되는 현재 취득 경로를 우선합니다.

## 자료별 실제 시작점

| 목적 | 확인한 공식 상세 자료 | 형식과 처리 방향 |
|---|---|---|
| 건물 footprint·속성 | [국토교통부 GIS건물통합정보](https://www.data.go.kr/data/15083092/fileData.do) | SHP. 건물 도형과 건축물대장 속성의 결합 자료. 필드 설명을 보고 용도·높이·층수·식별자를 매핑 |
| 필지 | [연속지적 전국 파일](https://www.data.go.kr/data/15125044/fileData.do), [연속지적 API](https://www.data.go.kr/data/15056910/openapi.do) | 파일은 SHP, API 카탈로그는 JSON/XML. 같은 명칭이라도 배포물별 이용조건이 다름 |
| 지형 | [NGII DEM](https://www.data.go.kr/data/15059920/fileData.do) | 카탈로그 표기 IMG. 실제 자료의 CRS·표고기준·격자간격을 확인한 뒤 Rasterio/GDAL에서 읽기 |
| 도로·행정경계 | [NGII 수치지도 V2.0](https://www.data.go.kr/data/15059719/fileData.do) 및 VWorld 자료 검색 | 수치지도 레이어의 실제 분류·스키마 확인. 경계는 행정동/법정동과 기준일을 구별 |
| 공원 위치·기초 속성 | [서울시 주요 공원현황 OA-394](https://data.seoul.go.kr/dataList/OA-394/S/1/datasetView.do) | 항목·좌표·제공 형식을 현 페이지에서 재확인. 공원 경계 폴리곤이 제공된다고 가정하지 않음 |
| 보행망 | [OSMnx 공식 사용 안내](https://osmnx.readthedocs.io/en/stable/getting-started.html) | 작은 AOI의 `network_type="walk"`, GraphML 저장. 길의 연결과 현장 접근 가능성 검토 |
| 위성영상 | [Sentinel-2 제품 명세](https://sentiwiki.copernicus.eu/web/s2-products), [STAC 카탈로그](https://documentation.dataspace.copernicus.eu/APIs/STAC.html) | L2A B04/B08 + SCL, 작은 AOI로 자른 뒤 격자와 반사도 보정 확인 |

**DEM 데이터와 DEM 성과 목록을 구별하세요.** 도엽·원점·취득방법·격자간격을 나열한 목록은 실제 고도값 배열이 아닙니다. “CSV를 받았는데 높이 래스터가 없다”면 상품을 잘못 선택했을 수 있습니다.

## 라이선스 조사에서 발견한 차이

[GIS건물통합정보 공식 메타데이터](https://www.data.go.kr/catalog/15083092/fileData.json)는 SHP와 공공누리 제1유형(출처표시)을 명시합니다. 반면 [연속지적 전국 파일 메타데이터](https://www.data.go.kr/catalog/15125044/fileData.json)는 제4유형(출처표시·상업적 이용금지·변경금지), [연속지적 API 메타데이터](https://www.data.go.kr/catalog/15056910/openapi.json)는 이용허락 제한 없음으로 표시되어 있습니다. **이 차이를 한 자료의 포괄적 허용으로 합쳐 해석하지 않습니다.** 실제 취득 파일·API 약관의 최신 조건을 확인하고 충돌하면 제공기관에 확인합니다. 이번 묶음에는 이들 원본 파일을 재배포하지 않습니다.

OSM 데이터 이용에는 [ODbL 및 attribution](https://www.openstreetmap.org/copyright)이 적용되고, 배경 타일 이용에는 별도의 [타일 서버 정책](https://operations.osmfoundation.org/policies/tiles/)이 있습니다. 공공데이터와 OSM을 결합해 데이터베이스를 배포할 때는 각 이용조건을 검토합니다. 웹지도에 출처를 보이지 않게 숨기지 않습니다.

연속지적은 참고용 경계이며 권리·면적 확정이나 지적측량의 대체 자료로 쓰지 않습니다. 건물 높이·도로 접근성은 현황과 다를 수 있으므로 설계 결정에는 현장·원자료 확인이 필요합니다.

## 한국 자료와 OSM을 함께 쓰는 실습 흐름

1. 서울의 검증한 공원 경계와 주변 1km 건물 자료를 준비합니다.
2. 공원·건물·행정경계를 같은 m 단위 CRS로 정렬하고 기준일 차이를 기록합니다.
3. OSM 보행망을 대상지보다 넓게 취득해 공원 출입구와 주변 건물을 연결합니다. 취득 범위 경계 때문에 경로가 잘리지 않게 합니다.
4. 행정 통계는 집계 구역·분모를 맞춰 조인합니다. 건물 수를 거주 인구로 대체하지 않습니다.
5. DEM과 Sentinel-2는 원래 해상도와 시점을 유지한 채 공통 분석 격자로 변환하고 유효마스크를 저장합니다.
6. 결과와 함께 매칭률, 결측률, 유효픽셀 비율, 끊긴 경로 수를 보고합니다.

## 취득 기록 템플릿

```yaml
dataset: GIS건물통합정보의 실제 다운로드 상품명
provider: 국토교통부
source_url: https://www.data.go.kr/data/15083092/fileData.do
acquired_at: 실제 다운로드 일시
observed_at: 파일의 기준일
format: SHP
crs: 원자료 메타데이터로 확인한 EPSG 또는 WKT
vertical_datum: 높이를 사용할 경우 확인
license_url: 취득 상품의 이용조건 URL
redistribution: 원본과 파생물의 허용 여부를 각각 기록
processing: 필드 매핑, 재투영, 결측 처리
sha256: 원본 파일 해시
```

SHP는 `.shp`, `.shx`, `.dbf`, `.prj`와 인코딩 정보 등을 함께 보관합니다. 주소 문자열·좌표 값의 형식만 보고 CRS를 추측하지 않습니다. 인코딩 변경 후 원문 한글과 대조합니다. 비밀키는 환경변수로 읽고 공개 노트북·정적 HTML에서 제거합니다.
