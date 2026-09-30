"""Synthetic 60 x 50 m terrain, north-up metre grid; central differences."""
from pathlib import Path
import argparse
import json
import numpy as np
import rasterio
from rasterio.transform import from_origin
from rasterio.features import rasterize, shapes
from shapely.geometry import box, shape
import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# start:minimal
def terrain(z, transform):
    """Return slope degrees, downslope aspect N=0/E=90, hillshade 0..1.

    Caller must establish metre units in XY and elevation. This function rejects
    rotated/south-up grids and removes the outer one-cell boundary.
    """
    if (transform.a <= 0 or transform.e >= 0
            or transform.b != 0 or transform.d != 0):
        raise ValueError("Reproject to a north-up, unrotated metre grid first")
    z = np.ma.asarray(z, dtype="float64").filled(np.nan)
    if z.ndim != 2 or min(z.shape) < 3:
        raise ValueError("Need at least 3 x 3 cells")
    # Rows increase southward: negative y spacing recovers northward dz/dy.
    dz_dy, dz_dx = np.gradient(z, transform.e, transform.a)
    valid = np.isfinite(z)
    stencil = np.zeros_like(valid)
    stencil[1:-1, 1:-1] = (
        valid[1:-1, 1:-1] & valid[:-2, 1:-1] & valid[2:, 1:-1]
        & valid[1:-1, :-2] & valid[1:-1, 2:]
    )
    magnitude = np.hypot(dz_dx, dz_dy)
    slope = np.degrees(np.arctan(magnitude))
    aspect = (np.degrees(np.arctan2(-dz_dx, -dz_dy)) + 360) % 360
    aspect[magnitude < 1e-12] = np.nan  # Flat terrain has no downslope direction.
    azimuth, altitude = np.radians(315), np.radians(45)
    light = np.array([np.sin(azimuth)*np.cos(altitude),
                      np.cos(azimuth)*np.cos(altitude), np.sin(altitude)])
    shade = np.clip((-dz_dx*light[0] - dz_dy*light[1] + light[2])
                    / np.sqrt(1 + magnitude**2), 0, 1)
    return tuple(np.where(stencil, a, np.nan) for a in (slope, aspect, shade))
# end:minimal


def export(out):
    out.mkdir(parents=True, exist_ok=True)
    x0, y0 = 953000, 1952000
    transform = from_origin(x0, y0 + 50, 1, 1)
    row, col = np.indices((50, 60))
    x, y = col + 0.5, 50 - (row + 0.5)
    z = 20 + 0.04*x + 0.08*y + 3*np.exp(-((x-38)**2+(y-28)**2)/100)
    z[10:13, 10:13] = np.nan  # Unknown cells, never zero elevation.
    profile = dict(driver="GTiff", height=50, width=60, count=1,
                   dtype="float32", crs="EPSG:5179", transform=transform, nodata=-9999)
    with rasterio.open(out / "dem.tif", "w", **profile) as dst:
        dst.write(np.where(np.isfinite(z), z, -9999).astype("float32"), 1)
    with rasterio.open(out / "dem.tif") as src:
        if not src.crs.is_projected or src.crs.linear_units != "metre":
            raise ValueError("This example requires horizontal metre units")
        slope, aspect, shade = terrain(src.read(1, masked=True), src.transform)
    park = box(x0, y0, x0+60, y0+50)
    inside = rasterize([(park, 1)], out_shape=z.shape, transform=transform,
                       all_touched=False, dtype="uint8").astype(bool)
    eligible = inside & np.isfinite(slope) & (slope <= 10)
    polygons = [shape(g) for g, value in shapes(eligible.astype("uint8"),
                mask=eligible, transform=transform) if value == 1]
    gpd.GeoDataFrame({"rule": ["slope <= 10 degrees (teaching only)"]*len(polygons)},
                    geometry=polygons, crs=profile["crs"]).to_file(
                        out / "candidates.gpkg", layer="candidates", driver="GPKG")
    with rasterio.open(out / "slope.tif", "w", **profile) as dst:
        dst.write(np.where(np.isfinite(slope), slope, -9999).astype("float32"), 1)
    fig, axes = plt.subplots(1, 3, figsize=(11, 4), layout="constrained")
    for ax, array, title, cmap in zip(axes, [z, slope, eligible.astype(float)],
            ["Elevation (m)", "Slope (degrees)", "Teaching rule: slope ≤ 10°"],
            ["terrain", "YlOrBr", "Greens"]):
        if title.startswith("Teaching"):
            array[~np.isfinite(slope)] = np.nan
        im = ax.imshow(array, extent=(0, 60, 0, 50), origin="upper", cmap=cmap)
        fig.colorbar(im, ax=ax, shrink=.65)
        ax.set(title=title, xlabel="East (m)", ylabel="North (m)")
    fig.suptitle("SYNTHETIC · 3,000 m² park / 1 m grid")
    fig.savefig(out / "terrain.svg", metadata={"Date": None})
    plt.close(fig)
    result = {"synthetic": True, "total_area_m2": 3000,
              "valid_slope_area_m2": int(np.isfinite(slope).sum()),
              "candidate_area_m2": int(eligible.sum()), "threshold_degrees": 10}
    (out / "terrain-results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("generated/terrain"))
    export(parser.parse_args().out)
