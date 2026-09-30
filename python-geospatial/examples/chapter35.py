from pathlib import Path
import json
import numpy as np
import geopandas as gpd
from shapely.geometry import box

park = gpd.GeoDataFrame({"name":["synthetic park"]},
    geometry=[box(953000,1952000,953060,1952050)], crs=5179)
candidates = gpd.GeoDataFrame(
    {"id":["A","B"], "slope_deg":[5.,12.], "walk_m":[300.,150.]},
    geometry=[box(953000,1952000,953020,1952020),
              box(953030,1952000,953050,1952020)], crs=5179)
# Educational preferences, not species-specific suitability standards.
metrics = np.column_stack([
    1 - candidates["slope_deg"].to_numpy()/20,
    1 - candidates["walk_m"].to_numpy()/500])
candidates["score"] = metrics @ np.array([0.6,0.4])
candidates.drop(columns="geometry").to_csv("candidate-results.csv", index=False)
manifest = {"synthetic":True, "park_area_m2":float(park.area.iloc[0]),
            "crs":"EPSG:5179", "weights":[0.6,0.4],
            "missing_factors":["soil","drainage","species","field survey"],
            "winner":candidates.loc[candidates.score.idxmax(),"id"]}
Path("analysis-manifest.json").write_text(
    json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
assert manifest["park_area_m2"] == 3000
assert np.allclose(candidates.score, [0.61,0.52])
assert manifest["winner"] == "A"
print(manifest)
