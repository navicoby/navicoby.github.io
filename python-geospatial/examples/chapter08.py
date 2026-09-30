import geopandas as gpd
from shapely.geometry import box

parcels = gpd.GeoDataFrame(
    {"parcel": ["A", "B"]},
    geometry=[box(0, 0, 10, 10), box(10, 0, 20, 10)], crs=5179
)
green = gpd.GeoDataFrame(
    {"kind": ["녹지"]}, geometry=[box(5, 0, 15, 5)], crs=5179
)
pieces = gpd.overlay(parcels, green, how="intersection")
pieces["green_m2"] = pieces.area
total = pieces.dissolve(by="kind", aggfunc={"green_m2": "sum"})
assert pieces["green_m2"].tolist() == [25.0, 25.0]
assert total.geometry.area.iloc[0] == 50
print(pieces[["parcel", "green_m2"]])
