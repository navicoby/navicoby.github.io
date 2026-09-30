import numpy as np

red_dn = np.array([2000, 3000, 4000], dtype="float32")
nir_dn = np.array([5000, 5000, 5000], dtype="float32")
scl = np.array([4, 9, 6], dtype="uint8")
quantification = 10000.0
example_offset = -1000.0
red = (red_dn + example_offset) / quantification
nir = (nir_dn + example_offset) / quantification
valid = np.isin(scl, [4, 5, 6]) & ((nir + red) != 0)
index = np.full(red.shape, np.nan, dtype="float32")
np.divide(nir-red, nir+red, out=index, where=valid)
assert np.isclose(index[0], 0.6)
assert np.isnan(index[1])
print(index)
