
import geopandas as gpd


def create_geojson(output_file, geometry, crs):
    gdf = gpd.GeoDataFrame({'geometry': [geometry]}, crs=crs)
    gdf.to_file(output_file, driver='GeoJSON')
