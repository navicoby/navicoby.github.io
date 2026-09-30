from shapely.geometry import box, LineString

parcel = box(0, 0, 20, 20)
building = box(5, 5, 15, 15)
green = box(0, 15, 20, 20)
road_centerline = LineString([(-10, 0), (30, 0)])
green_ratio = parcel.intersection(green).area / parcel.area
distance_to_centerline = building.distance(road_centerline)
assert green_ratio == 0.25
assert distance_to_centerline == 5.0
print("녹지율:", green_ratio)
print("도로 중심선까지 평면거리(m):", distance_to_centerline)
