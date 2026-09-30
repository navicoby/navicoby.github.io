"""Synthetic 3,000 m² park; no real parcels/buildings are represented."""
from pathlib import Path
import argparse
import json
import geopandas as gpd
from shapely.geometry import box
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster


# start:minimal
def analyze():
    # Synthetic coordinates placed in a metre-based Korean projected CRS.
    x, y = 953000, 1952000
    park = gpd.GeoDataFrame(
        {"park_id": ["P01"]},
        geometry=[box(x, y, x + 60, y + 50)], crs="EPSG:5179",
    )
    buildings = gpd.GeoDataFrame(
        {"building_id": ["B01", "B02", "B03"],
         "use": ["residential", "community", "residential"]},
        geometry=[box(x-20, y+10, x-10, y+20),
                  box(x+70, y+10, x+80, y+20),
                  box(x+110, y+10, x+120, y+20)], crs=park.crs,
    )
    zone = park.copy()
    zone.geometry = park.buffer(30)  # 30 m from the park FOOTPRINT
    hits = buildings.sjoin(zone, how="left", predicate="intersects")
    nearest = buildings.sjoin_nearest(
        park, how="left", max_distance=100, distance_col="distance_m",
    )
    # Count distinct IDs because multiple parks could match one building.
    count = hits.loc[hits["park_id"].notna(), "building_id"].nunique()
    print(f"Park area: {park.area.iloc[0]:.0f} m²; nearby buildings: {count}")
    print(nearest[["building_id", "distance_m"]].to_string(index=False))
    return park, buildings, zone, hits, nearest
# end:minimal


def export(out):
    out.mkdir(parents=True, exist_ok=True)
    park, buildings, zone, hits, nearest = analyze()
    park.to_file(out / "park.gpkg", layer="park", driver="GPKG", engine="pyogrio")
    buildings.to_parquet(out / "buildings.parquet", index=False)
    park.to_crs(4326).to_file(out / "park.geojson", driver="GeoJSON")
    fig, ax = plt.subplots(figsize=(8, 4.6), layout="constrained")
    zone.plot(ax=ax, color="#d9e9df", edgecolor="#87ac98")
    park.plot(ax=ax, color="#357955", edgecolor="#173d2b")
    buildings.plot(ax=ax, color="#b5bcb6", edgecolor="#4d5e53")
    for _, row in nearest.iterrows():
        p = row.geometry.centroid
        ax.annotate(f"{row.building_id}\n{row.distance_m:.0f} m", (p.x, p.y),
                    xytext=(0, 15), textcoords="offset points", ha="center")
    ax.set_title("SYNTHETIC · 3,000 m² park + 30 m buffer")
    ax.set_xlabel("Easting (m) · EPSG:5179")
    ax.set_ylabel("Northing (m)")
    ax.ticklabel_format(style="plain", useOffset=False)
    fig.savefig(out / "buffer.svg", metadata={"Date": None})
    plt.close(fig)
    center = park.to_crs(4326).geometry.iloc[0].centroid
    # Leaflet map option is needed when no base layer is initially visible.
    m = folium.Map(location=[center.y, center.x], zoom_start=18, maxZoom=19,
                   tiles=None, scrollWheelZoom=False, control_scale=True)
    m.get_root().html.add_child(folium.Element(
        '<div style="position:fixed;top:12px;left:60px;right:60px;z-index:1000;'
        'text-align:center;font:14px sans-serif;background:#f5f8f2;padding:10px;'
        'border:1px solid #afbfad;pointer-events:none">'
        '가상공원 실습 · 실제 지형·건물이 아닙니다</div>'
    ))
    folium.TileLayer("OpenStreetMap", name="OSM basemap (optional)", show=False).add_to(m)
    for frame, name, color in [(zone, "Synthetic 30 m buffer", "#9abbaa"),
                                (park, "Synthetic park", "#2c734e"),
                                (buildings, "Synthetic buildings", "#536459")]:
        folium.GeoJson(json.loads(frame.to_crs(4326).to_json()), name=name,
                       style_function=lambda feature, c=color: {
                           "color": c, "fillColor": c, "fillOpacity": 0.35},
                       tooltip=folium.GeoJsonTooltip(fields=[frame.columns[0]])).add_to(m)
    cluster = MarkerCluster(name="Synthetic building markers").add_to(m)
    points = buildings.copy()
    points.geometry = points.representative_point()
    for _, row in points.to_crs(4326).iterrows():
        folium.Marker([row.geometry.y, row.geometry.x],
                      popup=folium.Popup(f"Synthetic {row.building_id}", max_width=220)).add_to(cluster)
    folium.LayerControl().add_to(m)
    m.save(out / "park-map.html")
    (out / "vector-results.json").write_text(json.dumps({
        "synthetic": True, "park_area_m2": float(park.area.iloc[0]),
        "nearby_buildings": int(hits.loc[hits.park_id.notna(), "building_id"].nunique()),
        "distances_m": nearest.distance_m.tolist(),
    }, indent=2), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("generated/vector"))
    export(parser.parse_args().out)
