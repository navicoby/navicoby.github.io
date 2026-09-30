import geopandas as gpd
from shapely.geometry import Point

original = gpd.GeoSeries([Point(126.978, 37.5665)], crs=4326)
projected = original.to_crs(5179)
restored = projected.to_crs(4326)
print("metres:", projected.iloc[0])
print("degrees:", restored.iloc[0])
assert abs(restored.x.iloc[0] - original.x.iloc[0]) < 1e-7
