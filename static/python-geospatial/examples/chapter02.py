import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon

gdf = gpd.GeoDataFrame(
    {"name": ["tree", "path", "park"]},
    geometry=[Point(10, 10), LineString([(0, 0), (60, 50)]),
              Polygon([(0, 0), (60, 0), (60, 50), (0, 50)])],
    crs="EPSG:5179",
)
print(gdf[["name", "geometry"]])
print(gdf.geom_type.tolist())
assert gdf.geometry.iloc[2].area == 3000
