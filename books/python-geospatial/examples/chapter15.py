import numpy as np
from rasterio.io import MemoryFile
from rasterio.transform import from_origin

z = np.array([[10, 11, -9999], [12, 13, 14]], dtype="float32")
profile = dict(driver="GTiff", height=2, width=3, count=1,
               dtype="float32", crs="EPSG:5179",
               transform=from_origin(953000, 1952000, 2, 2), nodata=-9999)
with MemoryFile() as memory:
    with memory.open(**profile) as dst:
        dst.write(z, 1)
    with memory.open() as src:
        arr = src.read(1, masked=True)
        assert arr.count() == 5
        assert src.res == (2, 2)
        print("shape:", arr.shape, "valid mean:", float(arr.mean()))
        print("upper-left cell center:", src.xy(0, 0))
