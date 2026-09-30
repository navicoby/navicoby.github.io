import numpy as np
from rasterio.io import MemoryFile
from rasterio.transform import from_origin
from rasterio.mask import mask
from shapely.geometry import box, mapping

data = np.arange(16, dtype="float32").reshape(4, 4)
profile = dict(driver="GTiff", height=4, width=4, count=1,
               dtype="float32", crs="EPSG:5179", nodata=-9999,
               transform=from_origin(0, 4, 1, 1))
with MemoryFile() as mem:
    with mem.open(**profile) as dst:
        dst.write(data, 1)
    with mem.open() as src:
        crop, transform = mask(src, [mapping(box(1, 1, 3, 3))],
                               crop=True, filled=False)
        assert crop.shape == (1, 2, 2)
        assert crop[0].tolist() == [[5, 6], [9, 10]]
        assert transform.c == 1 and transform.f == 3
        print(crop[0], transform)
