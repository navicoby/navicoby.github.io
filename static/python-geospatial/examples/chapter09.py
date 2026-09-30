import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import box

zones = gpd.GeoDataFrame(
    {"trees": [10, 20]},
    geometry=[box(0, 0, 100, 100), box(120, 0, 320, 100)], crs=5179
)
zones["trees_per_ha"] = zones["trees"] / (zones.area / 10000)
fig, ax = plt.subplots(figsize=(7, 3))
zones.plot(column="trees_per_ha", legend=True, vmin=0, vmax=20,
           cmap="YlGn", edgecolor="black", ax=ax)
ax.set_aspect("equal")
ax.set_title("Synthetic tree density (trees/ha)")
fig.savefig("density.svg", bbox_inches="tight")
plt.close(fig)
assert zones["trees_per_ha"].tolist() == [10, 10]
print("density.svg")
