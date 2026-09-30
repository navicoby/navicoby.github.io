"""Analytical checks for units, boundaries, masks and radiometry."""
import numpy as np
import geopandas as gpd
import pytest
from shapely.geometry import Point, box
from rasterio.transform import from_origin, Affine
from buffer_join import analyze
from dem_slope import terrain
from sentinel2_ndvi import ndvi
from sentinel2_ndvi import real
import rasterio


def test_park_and_distances():
    park, buildings, zone, hits, nearest = analyze()
    assert park.area.iloc[0] == 3000
    assert hits.park_id.notna().sum() == 2
    np.testing.assert_allclose(nearest.distance_m, [10, 10, 50])


def test_boundary_and_multiple_match():
    points = gpd.GeoDataFrame(geometry=[Point(1, 0.5)], crs=5179)
    zones = gpd.GeoDataFrame({"id": [1, 2]}, geometry=[box(0,0,1,1), box(1,0,2,1)], crs=5179)
    assert len(points.sjoin(zones, predicate="within")) == 0
    assert len(points.sjoin(zones, predicate="intersects")) == 2


def test_plane_and_aspect():
    r, c = np.indices((10, 12))
    z = .1*(c+.5)*2 + .2*(10-(r+.5))*3
    slope, aspect, shade = terrain(z, from_origin(0,30,2,3))
    np.testing.assert_allclose(slope[1:-1,1:-1], np.degrees(np.arctan(np.hypot(.1,.2))))
    np.testing.assert_allclose(aspect[1:-1,1:-1], 206.565051177)
    assert np.isnan(slope[0]).all()
    assert np.nanmin(shade) >= 0 and np.nanmax(shade) <= 1


def test_nodata_and_flat():
    z = np.ones((9,9))
    z[4,4] = np.nan
    slope, aspect, _ = terrain(z, from_origin(0,9,1,1))
    assert np.isnan(slope[4,4]) and np.isnan(slope[3,4])
    assert np.isnan(slope[4,5]) and np.isfinite(slope[3,3])
    assert np.isnan(aspect).all()


def test_rotated_grid_rejected():
    with pytest.raises(ValueError):
        terrain(np.ones((3,3)), Affine(1,.1,0,0,-1,3))


def test_radiometry_and_cloud():
    result = ndvi(np.array([[2000,2000]]), np.array([[6000,6000]]),
                  np.array([[4,9]]), quantification=10000, red_offset=-1000, nir_offset=-1000)
    assert result[0,0] == pytest.approx(2/3)
    assert np.isnan(result[0,1])


def test_ndvi_zero_denominator():
    result = ndvi(np.array([[0.]]), np.array([[0.]]), np.array([[4]]),
                  quantification=1, red_offset=0, nir_offset=0)
    assert np.isnan(result[0,0])


def test_real_raster_preserves_grid_masks_and_rejects_misalignment(tmp_path):
    profile = dict(driver="GTiff", width=3, height=3, count=1,
                   crs="EPSG:5179", transform=from_origin(953000,1952000,10,10),
                   dtype="uint16", nodata=0)
    red = np.full((3,3), 2000, dtype="uint16")
    red[0,0] = 0
    for name, array in [("red", red), ("nir", np.full((3,3),6000)),
                        ("scl", np.full((3,3),4))]:
        with rasterio.open(tmp_path / f"{name}.tif", "w", **profile) as dst:
            dst.write(array.astype("uint16"), 1)
    paths = [tmp_path / f"{name}.tif" for name in ("red","nir","scl")]
    real(*paths, tmp_path / "out.tif", 10000, -1000, -1000)
    with rasterio.open(tmp_path / "out.tif") as src:
        values = src.read(1, masked=True)
        assert src.transform == profile["transform"]
        assert values.mask[0,0]
        assert values[1,1] == pytest.approx(2/3)
    profile["transform"] = from_origin(953005,1952000,10,10)
    with rasterio.open(paths[2], "w", **profile) as dst:
        dst.write(np.full((3,3),4,dtype="uint16"),1)
    with pytest.raises(ValueError, match="transform"):
        real(*paths, tmp_path / "out2.tif", 10000, -1000, -1000)
