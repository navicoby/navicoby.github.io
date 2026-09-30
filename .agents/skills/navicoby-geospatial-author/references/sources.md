# 자료와 재현성

현재 조사 노트는 저장소의 `books/python-geospatial/pages/stack.md`와 `data-sources.md`, 위성영상 절차는 `chapters/sentinel2-ndvi.md`를 읽는다. 재집필할 때 접근 가능한 공식 자료로 재확인하고 날짜를 갱신한다. 오래된 조사일을 현재 확인일처럼 바꾸지 않는다.

데이터 manifest 필수 필드:

```yaml
dataset: 실제 상품/자료명
provider: 제공기관
source_url: 데이터 상세 URL
acquired_at: 다운로드 시각
observed_at: 자료 기준일 또는 촬영일
format: SHP / GPKG / GeoParquet / IMG / GeoTIFF / SAFE-JP2
crs: EPSG 또는 WKT
vertical_datum: 높이 기준 또는 해당 없음/미확인
resolution: 래스터 픽셀 크기와 단위
license_url: 해당 자료의 이용조건 URL
license_checked_at: 확인일
redistribution: 원본/파생물 각각의 허용 여부
processing: 재투영·리샘플링·마스킹·필드 매핑
sha256: 취득 파일의 해시
```

위성영상에는 platform, product ID, processing baseline, tile, cloud cover, band별 scale/offset, grid transform, 적용한 SCL 클래스, AOI 유효픽셀 비율을 추가한다. API키·액세스 토큰·서명 URL은 기록하지 않는다.

NGII DEM의 메타데이터 목록과 실제 고도 래스터를 구별한다. VWorld 데이터 API·WMS/WFS·다운로드 파일은 서로 같은 상품/권한이라고 가정하지 않는다. 공공데이터포털은 종종 실제 다운로드 사이트로 연결하는 카탈로그이다. 포털 전체를 단일 라이선스로 표현하지 않는다. 연속지적은 법적 경계 확정이나 측량 성과의 대체가 아니다.

OSM 데이터는 ODbL와 attribution 조건을 확인한다. 일반 OSM 타일 서버의 서비스 정책은 데이터 라이선스와 별개이다. 대량 수집·오프라인 타일 프리패치를 예제 기본값으로 만들지 않는다. 공공데이터와 OSM을 결합한 결과의 배포 조건을 별도로 검토한다.

Copernicus 데이터에는 적용된 이용조건에 따른 연도·수정 여부 출처 문구를 남긴다. 원본 SAFE와 harmonized 서비스의 반사도 변환을 혼동하지 않는다. 본 프로젝트의 합성 예제는 실제 기관 자료를 사용했다고 표기하지 않는다.
