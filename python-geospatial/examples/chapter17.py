import numpy as np
from rasterio.features import rasterize, shapes
from rasterio.transform import from_origin
from shapely.geometry import box, shape

transform = from_origin(0, 4, 1, 1)
source = box(1, 1, 3, 3)
grid = rasterize([(source, 1)], out_shape=(4,4),
                 transform=transform, fill=0, dtype="uint8")
polygons = [shape(g) for g, value in shapes(
    grid, mask=grid == 1, transform=transform) if value == 1]
assert int(grid.sum()) == 4
assert sum(p.area for p in polygons) == 4
print(grid)
print("polygon area:", sum(p.area for p in polygons))
