import folium
from folium.plugins import MarkerCluster

m = folium.Map(location=[37.5665, 126.9780], zoom_start=15,
               tiles=None, maxZoom=19)
group = MarkerCluster(name="합성 조사점").add_to(m)
for lat, lon, label in [
    (37.5665, 126.9780, "연습 지점 A"),
    (37.5670, 126.9790, "연습 지점 B"),
]:
    folium.Marker([lat, lon], popup=label).add_to(group)
folium.GeoJson(
    {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": "합성 연결선"},
        "geometry": {"type": "LineString",
                     "coordinates": [[126.9780, 37.5665], [126.9790, 37.5670]]}
    }]}, name="연습 선").add_to(m)
folium.LayerControl().add_to(m)
m.save("field-map.html")
print("field-map.html: synthetic points; no background tiles")
