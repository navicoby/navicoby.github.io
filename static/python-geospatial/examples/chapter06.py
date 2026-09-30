import geopandas as gpd
from shapely.geometry import box

buildings = gpd.GeoDataFrame(
    {"use": ["주거", "상업"], "height_m": [9.0, 18.0]},
    geometry=[box(0, 0, 10, 12), box(20, 0, 25, 10)], crs=5179
)
buildings["area_m2"] = buildings.geometry.area
selected = buildings.loc[
    (buildings["use"] == "주거") & (buildings["area_m2"] >= 100)
].copy()
selected["label_point"] = selected.geometry.representative_point()
assert len(selected) == 1
assert selected["area_m2"].iloc[0] == 120
print(selected[["use", "height_m", "area_m2"]])
