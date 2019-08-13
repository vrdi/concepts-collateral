## Reproducing visualizations
The scrubbed Pennsylvania GeoJSON file was generated from the Pennsylvania shapefile using `scrub_pa_metadata.py`; this GeoJSON file was uploaded to [mapshaper](https://mapshaper.org/) and simplified to 0.31% resolution using the "Visvalingam / weighted area" method. Resulting line intersections were repaired.
The resulting TopoJSON file was saved as `PA_vtd.json`.