import sys
from importlib.metadata import version
import numpy as np

elevation = np.array([[10, 12], [14, 16]], dtype="float32")
print("Python:", sys.executable)
print("NumPy:", version("numpy"))
print("shape/dtype:", elevation.shape, elevation.dtype)
print("mean:", elevation.mean())
print("column means:", elevation.mean(axis=0))
assert elevation.mean() == 13
