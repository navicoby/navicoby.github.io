"""NDVI from supplied, co-registered Sentinel-2 L2A bands, or synthetic demo.

Real mode takes B04/B08 and SCL already aligned to the exact same grid.
For raw SAFE DN, read offsets/quantification from product XML; do not guess.
For an already reflectance-scaled service use quantification=1 and offsets=0.
"""
from pathlib import Path
import argparse
import numpy as np
import rasterio
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# start:minimal
def ndvi(red, nir, scl, *, quantification, red_offset, nir_offset):
    if quantification <= 0:
        raise ValueError("quantification must be positive")
    if red.shape != nir.shape or red.shape != scl.shape:
        raise ValueError("Align band and SCL grids before calculation")
    red = np.ma.asarray(red, dtype="float32")
    nir = np.ma.asarray(nir, dtype="float32")
    # Conservative policy: only vegetation, bare/not-vegetated and water.
    valid = (~np.ma.getmaskarray(red) & ~np.ma.getmaskarray(nir)
             & ~np.ma.getmaskarray(scl)
             & np.isin(np.ma.getdata(scl), [4, 5, 6]))
    r = (red.filled(np.nan) + red_offset) / quantification
    n = (nir.filled(np.nan) + nir_offset) / quantification
    valid &= np.isfinite(r) & np.isfinite(n) & ((n+r) > 1e-6)
    result = np.full(red.shape, np.nan, dtype="float32")
    np.divide(n-r, n+r, out=result, where=valid)
    return result
# end:minimal


def real(red_path, nir_path, scl_path, out, quantification, red_offset, nir_offset):
    with rasterio.open(red_path) as red, rasterio.open(nir_path) as nir, rasterio.open(scl_path) as scl:
        if red.width * red.height > 25_000_000:
            raise ValueError("Crop to a small AOI first: this example reads arrays into memory")
        if red.crs is None or any((s.crs != red.crs or s.transform != red.transform
                or s.shape != red.shape) for s in (nir, scl)):
            raise ValueError("CRS, transform and shape must all match the B04 grid")
        bands = [s.read(1, masked=True) for s in (red, nir, scl)]
        # DN=0 is no data for original SAFE; the input raster mask may omit it.
        if quantification != 1:
            bands[:2] = [np.ma.masked_where(a == 0, a) for a in bands[:2]]
        data = ndvi(*bands, quantification=quantification,
                    red_offset=red_offset, nir_offset=nir_offset)
        profile = red.profile.copy()
        profile.update(driver="GTiff", dtype="float32", nodata=-9999, count=1)
        out.parent.mkdir(parents=True, exist_ok=True)
        with rasterio.open(out, "w", **profile) as dst:
            dst.write(np.where(np.isfinite(data), data, -9999).astype("float32"), 1)
        print(f"Valid pixels: {np.isfinite(data).mean():.1%}; output: {out}")


def demo(out):
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(42)
    row, col = np.indices((60, 80))
    green = ((col-38)/22)**2 + ((row-30)/16)**2 < 1
    red = np.where(green, .08, .22) + rng.normal(0, .008, green.shape)
    nir = np.where(green, .45, .28) + rng.normal(0, .008, green.shape)
    scl = np.where(green, 4, 5)
    scl[:12, :20] = 9  # Synthetic cloud patch.
    result = ndvi(red, nir, scl, quantification=1, red_offset=0, nir_offset=0)
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    im = ax.imshow(result, cmap="RdYlGn", vmin=-1, vmax=1, extent=(0, 800, 0, 600))
    fig.colorbar(im, ax=ax, label="NDVI (unitless)")
    ax.set(title="SYNTHETIC · spectral exercise, not a satellite observation",
           xlabel="East (m) · 10 m cells", ylabel="North (m)")
    fig.savefig(out / "ndvi.svg", metadata={"Date": None})
    plt.close(fig)
    print(f"Synthetic valid pixels: {np.isfinite(result).mean():.1%}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--demo", action="store_true")
    p.add_argument("--out", type=Path, required=True)
    for name in ("red", "nir", "scl"):
        p.add_argument("--"+name, type=Path)
    for name in ("quantification", "red-offset", "nir-offset"):
        p.add_argument("--"+name, type=float)
    a = p.parse_args()
    if a.demo:
        demo(a.out)
    elif any(v is None for v in (a.red, a.nir, a.scl, a.quantification, a.red_offset, a.nir_offset)):
        p.error("Real mode requires --red --nir --scl --quantification --red-offset --nir-offset")
    else:
        real(a.red, a.nir, a.scl, a.out, a.quantification, a.red_offset, a.nir_offset)
