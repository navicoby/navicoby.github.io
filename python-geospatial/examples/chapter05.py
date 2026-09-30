from pathlib import Path
from tempfile import TemporaryDirectory
import geopandas as gpd
from shapely.geometry import box

parks = gpd.GeoDataFrame(
    {"name": ["가상공원"], "area_m2": [3000]},
    geometry=[box(953000, 1952000, 953060, 1952050)], crs=5179
)
with TemporaryDirectory() as folder:
    root = Path(folder)
    parks.to_file(root / "parks.gpkg", layer="parks", driver="GPKG")
    parks.to_parquet(root / "parks.parquet", index=False)
    parks.to_crs(4326).to_file(root / "parks.geojson", driver="GeoJSON")
    restored = gpd.read_file(root / "parks.gpkg", layer="parks")
    fast = gpd.read_parquet(root / "parks.parquet")
    assert restored.crs == parks.crs == fast.crs
    assert restored.geometry.area.iloc[0] == 3000
    print(restored[["name", "area_m2"]])
