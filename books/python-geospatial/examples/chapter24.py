import geopandas as gpd
import osmnx as ox
from shapely.geometry import Point, LineString

nodes = gpd.GeoDataFrame(
    {"osmid":[1,2], "x":[0.0,100.0], "y":[0.0,0.0]},
    geometry=[Point(0,0), Point(100,0)], crs=5179).set_index("osmid")
edges = gpd.GeoDataFrame(
    {"u":[1,2], "v":[2,1], "key":[0,0], "length":[100.0,100.0]},
    geometry=[LineString([(0,0),(100,0)]), LineString([(100,0),(0,0)])],
    crs=5179).set_index(["u","v","key"])
g = ox.convert.graph_from_gdfs(nodes, edges)
restored_nodes, restored_edges = ox.convert.graph_to_gdfs(g)
assert len(restored_nodes) == 2 and len(restored_edges) == 2
print("합성 양방향 도로:", len(restored_edges), "directed edges")
