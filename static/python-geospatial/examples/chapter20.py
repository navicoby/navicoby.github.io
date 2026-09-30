import json
from pathlib import Path

request_plan = {
    "provider_docs": "https://documentation.dataspace.copernicus.eu/APIs/STAC.html",
    "bbox_wgs84": [126.9, 37.5, 127.0, 37.6],
    "datetime": "2025-05-01T00:00:00Z/2025-05-31T23:59:59Z",
    "desired_level": "L2A",
    "desired_bands": ["B04", "B08", "SCL"],
    "collection_id": None,
    "note": "실제 collection/asset 이름을 확인한 뒤 채웁니다."
}
Path("satellite-search-plan.json").write_text(
    json.dumps(request_plan, ensure_ascii=False, indent=2), encoding="utf-8")
assert request_plan["bbox_wgs84"][0] < request_plan["bbox_wgs84"][2]
print("검색 계획만 작성. 실제 영상 다운로드 또는 API 호출은 수행하지 않음.")
