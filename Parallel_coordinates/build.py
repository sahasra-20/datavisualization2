# Bundles the page and both CSVs into one self-contained index.html.
import json, pathlib

here = pathlib.Path(__file__).parent
page = (here / "parallel_coordinates.html").read_text(encoding="utf-8")

# Road first so it is the default tab. json.dumps safely escapes the CSV text as a JS string.
csvs = [(here / f).read_text(encoding="utf-8")
        for f in ("road_parallel.csv", "weather_parallel.csv")]
data = "<script>const EMBEDDED = " + json.dumps(csvs) + ";</script>\n"

# EMBEDDED must be defined before the main script runs, so inject it just before that script.
marker = "<script>\n/* ---------- state ---------- */"
assert marker in page, "main <script> marker not found"
(here / "index.html").write_text(page.replace(marker, data + marker, 1), encoding="utf-8")
print("Wrote index.html")