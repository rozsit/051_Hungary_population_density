from py_components.create_geojson import create_geojson
from py_components.clip_raster import clip_raster
from py_components.reproject_raster import reproject_raster
from py_components.plot_raster import plot_raster
from py_components.cleanup_files import cleanup_temp_files
import geopandas as gpd

# Load Hungary geometry
hungary_shapefile = 'data/ne_10m_admin_0_countries.shp'
# you need to download from here:
raster_file = 'data/GHS_POP_E2020_GLOBE_R2023A_4326_30ss_V1_0.tif'
# https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2020_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2020_GLOBE_R2023A_4326_30ss_V1_0.zip
hungary_raster = 'data/hungary_population.tif'

# Filter for Hungary and create GeoJSON
hungary_gdf = gpd.read_file(hungary_shapefile)
hungary_geom = hungary_gdf[hungary_gdf.SOVEREIGNT ==
                           'Hungary'].geometry.unary_union
create_geojson('data/hungary.geojson', hungary_geom, hungary_gdf.crs)

# Clip raster directly to Hungary boundaries
clip_raster(raster_file, hungary_geom, hungary_raster)

# Reproject raster to local CRS
reprojected_raster = 'data/hungary_population_reprojected.tif'
reproject_raster(hungary_raster, reprojected_raster, 'EPSG:23700')

# Plot the final raster
plot_raster(reprojected_raster, 'Population_density_of_Hungary.png')

# Clean up temporary files (except the final PNG)
temp_files = ['data/hungary.geojson', hungary_raster, reprojected_raster]
cleanup_temp_files(temp_files)
