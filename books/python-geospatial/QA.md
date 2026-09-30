# 검증 기록 · v0.2 · 2026-09-30

## 실행 환경

Windows, CPython 3.13.5. 세부 패키지는 requirements-lock.txt. Hugo extended 0.167.0, 저장소의 기존 PaperMod submodule 사용.

## 계산 결과

- buffer_join.py 실행: 공원 3,000㎡, 30m 내 고유 건물 2동, 최단거리 10/10/50m. GPKG·GeoJSON·GeoParquet 및 SVG/Folium HTML 생성.
- dem_slope.py 실행: 전체 3,000㎡, 유효 경사도 2,763㎡, 교육용 10° 이하 후보 2,334㎡. DEM·경사 GeoTIFF, 후보 GPKG 및 SVG 생성.
- sentinel2_ndvi.py 합성 모드 실행: 유효픽셀 95%. 실제 관측자료 아님.
- pytest: **8 passed**. 기하 면적·거리, 경계와 다중 매칭, 알려진 평면의 경사/향, NoData 전파, 회전 격자 거부, 반사도 offset·구름, 0분모, 실제 파일 경로의 합성 GeoTIFF 입출력·정렬 불일치 거부를 검증.

## 출판·화면

- skill-creator quick_validate: 통과. Windows 기본 cp949 문제는 UTF-8 모드로 검사하여 해결.
- Markdown → HTML: 51페이지 생성(10부 소개·35장 본문·6개 보조 안내). 부·장 번호와 제목은 curriculum.json 단일 원본 사용.
- Hugo --minify: 성공.
- 기존 static navigation 검사: 최상위 정적 프로젝트 **15개 모두 메인에 연결**.
- 신규 링크 검사: 51페이지 내부 링크·앵커·이미지 대체 텍스트, 모든 장의 제목·현재 부 펼침·현재 장 표시·이전/다음 연결 통과. 예전 roadmap#part-7 링크를 실제 7부 소개로 수정.
- 브라우저: 51페이지 × 320/375/768/1280px = 204개 조합에서 문서 가로 넘침 및 빈 제목 없음. 모바일 목차에 현재 5부와 15장 표시 확인.
- 1280px와 375px 랜딩 스크린샷 시각 검토. 모바일 접는 목차, 코드 복사, 코드 줄바꿈 상태 변경, Folium 지도 iframe 및 Leaflet 확대/축소 컨트롤 확인.
- 기본 배경 레이어가 없는 Folium 지도에서 MarkerCluster의 maxZoom 오류를 발견하여 Leaflet map 옵션으로 수정. 새 브라우저 탭에서 마커 3개·레이어 컨트롤 표시 및 오류 로그 없음 확인.

## 설명용 개념도 추가 검사

- 2026-09-30: 용어 안내 및 02·03·07·18·21·25·32장에 8개 개념도, 총 16개 SVG 패널 추가.
- 좌표 변환 수치, 20개 공원 셀, 경사각, NDVI, 직선 200m/보행 280m를 생성기에서 계산·검산. TinyUNet 그림은 본문 코드의 각 단계 채널·공간 크기에 맞춤.
- 개념도 8페이지 × 320/375/768/1280px = 32개 조합에서 문서 가로 넘침 없음. 작은 화면에서 비교 패널이 세로 배치됨을 확인.
- SVG 16개를 직접 열어 텍스트 영역의 잘림·겹침 검사 통과. 두 줄 상자의 줄 간격을 조정한 뒤 다시 검사함.
- 벡터/래스터 데스크톱, CRS 모바일, 위성영상 처리 화면을 시각 검토. 대체 텍스트·title/desc·크게 보기 링크 제공.
- 51페이지 내부 링크·앵커·현재 장 탐색, 최상위 15개 메인 연결, Hugo 빌드 및 스킬 형식 검사 통과. 기존 분석 예제는 변경하지 않음.

## 경고·미확인 범위

- Rasterio 내부 from_origin에서 affine의 곱셈 연산에 대한 PendingDeprecationWarning이 발생. 현재 테스트 통과. 예제는 공식 from_origin API를 사용하며 후속 라이브러리 업데이트 시 재확인.
- 기존 Hugo 설정 languageCode 및 PaperMod Language 필드 관련 deprecated 경고 발생. 신규 섹션의 오류는 아니며 이번에는 기존 테마·전역 설정을 수정하지 않음.
- 32개 신규 chapterNN.py와 기존 확장 3개, 총 35개 장의 오프라인 예제를 임시 폴더에서 실행: 전부 통과. GeoPackage/Parquet 왕복, Rasterio mask/rasterize, NetworkX/OSMnx 합성 그래프 변환, PyTorch 텐서·Conv2d·손실·TinyUNet 순전파/역전파·scikit-image 연결영역, 후보지 점수를 포함.
- NGII/VWorld 인증 다운로드, 실제 Sentinel-2 원본 취득, OSMnx Overpass 다운로드, 실제 자료 PyTorch 훈련은 미실행. CPU 최소 예제와 구분해서 표시.
- VWorld·NSDI 직접 웹 접근이 되지 않아 포털 통합 날짜·현재 세부 메뉴를 확정하지 않음. 공식 공공데이터 상세·메타데이터를 대체 근거로 제공.
- 외부 링크 전체의 장기 가용성, 스크린리더 전수 감사, 모든 모바일 기기·Safari 검증을 뜻하지 않음.
