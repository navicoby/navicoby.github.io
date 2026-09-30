import json
from pathlib import Path

plan = [
    {"topic": "건물", "format": "SHP / API별 확인",
     "need": ["geometry", "용도 코드", "높이의 정의"],
     "portal": "https://www.data.go.kr/data/15083092/fileData.do"},
    {"topic": "DEM", "format": "제품별 확인 후 GeoTIFF 작업본",
     "need": ["셀 크기", "수평·수직 기준", "NoData"],
     "portal": "https://map.ngii.go.kr/"},
    {"topic": "보행 도로", "format": "OSM → GraphML / GeoPackage",
     "need": ["통행 가능 여부", "연결성", "length"],
     "portal": "https://www.openstreetmap.org/"},
]
Path("acquisition-plan.json").write_text(
    json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8"
)
assert len(plan) == 3
print("취득 계획만 저장했습니다. 실제 다운로드는 하지 않았습니다.")
