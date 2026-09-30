---
title: 실행 환경과 최신 API 메모
description: 문서 조사와 실제 실행 환경을 구별하고 오래된 예제의 함정을 정리합니다.
eyebrow: TOOLS / REPRODUCIBILITY
---

**공식 문서 조사일: 2026-09-30.** 아래 버전은 이 초안의 로컬 검증 환경입니다. 모든 시스템에서의 호환성 보증이나 “언제나 최신”이라는 뜻은 아닙니다. Windows CPython **3.13.5**에서 검증했습니다. GPU/PyTorch 학습 환경은 별도 단계입니다.

## 실습 환경 만들기

저장소 루트에서 다음을 실행합니다. Windows에서 Python 실행 파일이 `py`라면 첫 명령의 `python`을 `py -3.13`으로 바꿉니다.

```text
python -m venv .venv
```

Windows PowerShell:

```text
.venv/Scripts/python.exe -m pip install -r books/python-geospatial/requirements.txt
.venv/Scripts/python.exe books/python-geospatial/examples/buffer_join.py
```

macOS/Linux:

```text
.venv/bin/python -m pip install -r books/python-geospatial/requirements.txt
.venv/bin/python books/python-geospatial/examples/buffer_join.py
```

활성화 없이 환경 내부 Python을 직접 호출할 수 있습니다. 설치가 GDAL/PROJ native dependency에서 막히면 지원되는 Python 버전의 wheel 여부를 확인하거나 새 conda-forge 환경에서 주요 공간 패키지를 함께 설치합니다. 운영체제가 다른 환경은 별도 검증합니다.

## 검증 버전과 주요 API

| 도구 | 실행 버전 | 핵심 사용법·주의 |
|---|---|---|
| GeoPandas | 1.2.0 | GeoDataFrame, read_file, to_crs, sjoin, sjoin_nearest, clip, overlay, dissolve |
| Shapely | 2.1.2 | Point/LineString/Polygon, intersection, buffer, 유효성; vectorized 연산 활용 |
| pyogrio / pyarrow | 0.13.0 / 25.0.1 | GDAL I/O와 Arrow 경로, 필요한 열/범위만 읽기 |
| Rasterio | 1.5.1 | open/read/write, masks, transform, reproject, features |
| NumPy | 2.5.3 | 마스킹·broadcast·gradient·정규화, 배열의 단위와 축 순서 |
| Matplotlib | 3.11.2 | 지도·범례·colorbar·SVG 출력 |
| Folium | 0.20.0 | Map, Marker/Popup, MarkerCluster, GeoJson, LayerControl |
| NetworkX | 3.7 | 가중 최단경로, 연결요소, 도달 가능한 노드 |
| OSMnx | 2.1.1 | graph_from_point, projection.project_graph, convert.graph_to_gdfs, routing.shortest_path |
| PyTorch / scikit-image | 선택 단계·이번 실행 미포함 | Dataset/DataLoader, Conv2d, 분할 손실 / label·regionprops |

GeoPandas stable 문서의 표시 버전과 설치된 배포 버전이 다를 수 있습니다. Folium `latest` 문서는 조사 시 **1.0.0rc1**을 표시했으므로 실습은 설치·검증한 안정 배포 0.20.0을 사용했습니다. 실제 전체 의존성은 저장소의 `requirements-lock.txt`에 기록합니다.

## 형식을 목적에 맞게 선택하기

| 형식 | 우선 용도 | 제약 |
|---|---|---|
| Shapefile | 기존 공공자료 취득·호환 | 여러 파일, 필드명/타입·인코딩 제약, 프로젝트 기본 저장으로는 주의 |
| GeoJSON | 작은 웹지도 교환 | 텍스트 크기, 경위도/WGS84 출력, 큰 데이터에 비효율 |
| GeoPackage | GIS 편집·레이어 교환 | SQLite 기반, 레이어 이름 관리 |
| GeoParquet | 반복 분석·열 중심 보관 | 일반 Parquet와 구별, geometry/CRS 메타데이터와 reader 호환 확인 |
| GeoTIFF / COG | 분석 래스터 / 부분 원격 읽기 | 원본 보관·압축·NoData·overviews, 서버의 range 지원 |
| SAFE / JP2 | Sentinel 원본과 메타데이터 | 폴더·XML 함께 보존, JP2 driver 확인 |

`gpd.read_file(..., engine="pyogrio", use_arrow=True)`는 pyarrow가 있는 환경의 선택지입니다. `read_parquet`/`to_parquet`은 geometry와 CRS를 함께 보존하는 GeoParquet 경로입니다. schema version·geometry encoding을 명시적으로 바꿀 때는 수신 도구의 지원도 확인합니다. [GeoPandas I/O](https://geopandas.org/en/stable/docs/user_guide/io.html), [pyogrio](https://pyogrio.readthedocs.io/en/latest/introduction.html), [GeoParquet 1.1 명세](https://geoparquet.org/releases/v1.1.0/)

## 오래된 예제에서 바꿀 부분

- `sjoin(op="within")` 대신 `predicate="within"`을 사용합니다.
- 새 도형 합치기 코드는 `union_all()`을 우선합니다. dissolve는 속성 집계 규칙도 함께 지정합니다.
- 제거된 `geopandas.datasets`에 기대지 않고 가상 자료나 출처가 명확한 파일을 제공합니다.
- Shapely 2 geometry를 가변 객체처럼 수정하는 코드나 PyGEOS backend를 전제로 한 코드를 옮기지 않습니다.
- OSMnx 1.x 블로그 코드를 그대로 복사하지 않고 2.x 공식 API와 좌표 인수를 확인합니다.

## OSM 보행망으로 연결하는 확장 코드

다음은 **인터넷 연결과 Overpass 응답이 필요한 실자료 확장**입니다. 이번 오프라인 샘플 검증에 다운로드 실행은 포함하지 않았습니다. 한 공원 주변 작은 범위로 시작하고 반복 호출 대신 저장한 그래프를 재사용합니다.

```python
from pathlib import Path
import osmnx as ox
import networkx as nx

out = Path("generated/network")
out.mkdir(parents=True, exist_ok=True)
ox.settings.use_cache = True
G = ox.graph.graph_from_point(
    (37.5665, 126.9780), dist=1000, network_type="walk"
)
G = ox.projection.project_graph(G)
nodes, edges = ox.convert.graph_to_gdfs(G)
origin = next(iter(G.nodes))  # 개념 예제. 실무에서는 실제 출입구를 스냅.
distance = nx.single_source_dijkstra_path_length(
    G, origin, cutoff=800, weight="length"
)
ox.io.save_graphml(G, filepath=out / "walk.graphml")
print("800m 이내 도달 노드:", len(distance))
```

`length` 가중치는 m입니다. 노드 도달집합은 보행권 폴리곤 자체가 아닙니다. 도로의 일부 구간, 교차로·횡단, 출입구 스냅, 단절을 고려해 service area를 만듭니다. 일정 속도 4.8km/h를 가정하면 10분은 800m지만 경사·보행자 특성·신호 지연을 무시한 가정입니다. 임의 노드로 시작한 예제를 실제 공원 접근성 결과로 제시하지 않습니다. [OSMnx API](https://osmnx.readthedocs.io/en/stable/user-reference.html), [NetworkX 최단경로](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html)

## 시각화 선택

Matplotlib choropleth는 원시 건수·면적당 밀도·인구당 비율을 구분하고 색 구간을 고정합니다. Folium HeatMap은 줌과 화면 반경에 영향을 받는 표시 방식으로, 면적당 밀도나 KDE 분석 결과와 동일하지 않습니다. 분포를 평가하려면 분석 단위·대역폭·정규화를 먼저 정하고 결과를 지도에 그립니다. [GeoPandas plotting](https://geopandas.org/en/stable/docs/user_guide/mapping.html), [Folium HeatMap](https://python-visualization.github.io/folium/latest/user_guide/plugins/heatmap.html)
