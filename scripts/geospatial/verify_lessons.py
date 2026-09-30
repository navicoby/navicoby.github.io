"""Run all offline teaching examples in a temporary output directory."""
from pathlib import Path
from tempfile import TemporaryDirectory
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "books/python-geospatial/examples"

def main():
    scripts = sorted(EXAMPLES.glob("chapter[0-9][0-9].py"))
    if len(scripts) != 32:
        raise SystemExit(f"Expected 32 foundation examples; found {len(scripts)}")
    env = {**os.environ, "PYTHONUTF8":"1", "MPLBACKEND":"Agg"}
    failures = []
    with TemporaryDirectory(prefix="geospatial-lessons-") as folder:
        for script in scripts:
            result = subprocess.run([sys.executable, str(script)], cwd=folder,
                env=env, capture_output=True, text=True, encoding="utf-8", timeout=90)
            if result.returncode:
                failures.append(script.name + "\n" + result.stdout + result.stderr)
            else:
                print("PASS", script.name, flush=True)
        # Companion map wrapper requires chapter 10 output in the same folder.
        for expected in ["density.svg", "field-map.html", "map-page.html",
                         "candidate-results.csv", "analysis-manifest.json"]:
            if not (Path(folder)/expected).is_file():
                failures.append("Missing lesson artifact: " + expected)
        for filename, args in [
            ("buffer_join.py", ["--out", "extended-vector"]),
            ("dem_slope.py", ["--out", "extended-terrain"]),
            ("sentinel2_ndvi.py", ["--demo", "--out", "extended-satellite"]),
        ]:
            result = subprocess.run([sys.executable, str(EXAMPLES/filename), *args],
                cwd=folder, env=env, capture_output=True, text=True, encoding="utf-8", timeout=90)
            if result.returncode:
                failures.append(filename + "\n" + result.stdout + result.stderr)
            else:
                print("PASS", filename, flush=True)
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: all 35 chapter examples; no real-data download or model training claimed.")

if __name__ == "__main__":
    main()
