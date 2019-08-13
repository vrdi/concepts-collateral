"""Converts the Pennsylvania shapefile to a GeoJSON file and removes most columns."""
import geopandas as gpd

gdf = gpd.read_file('PA_VTD/PA_VTD.shp')
scrubbed = gpd.GeoDataFrame()
scrubbed['geometry'] = gdf['geometry']
scrubbed['id'] = gdf.index
with open('PA_vtd_scrubbed.json', 'w') as f:
    f.write(scrubbed.to_json())
