import geopandas as gpd
from shapely.geometry import box

data = gpd.GeoDataFrame(
    {"id": ["A", "A", "B"], "height_m": [9.0, 9.0, None]},
    geometry=[box(0,0,10,10), box(0,0,10,10), box(20,0,30,10)],
    crs=5179
)
report = {
    "rows": len(data),
    "duplicate_id_rows": int(data["id"].duplicated(keep=False).sum()),
    "missing_height_rows": int(data["height_m"].isna().sum()),
    "invalid_geometry_rows": int((~data.geometry.is_valid).sum()),
}
assert report["duplicate_id_rows"] == 2
assert report["missing_height_rows"] == 1
print(report)
print("검사만 수행했으며 자동 삭제·0 대체는 하지 않았습니다.")
