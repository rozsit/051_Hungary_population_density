
import rasterio
from rasterio.warp import calculate_default_transform, reproject


def reproject_raster(input_path, output_path, target_crs):
    with rasterio.open(input_path) as src:
        transform, width, height = calculate_default_transform(
            src.crs, target_crs, src.width, src.height, *src.bounds)
        metadata = src.meta.copy()
        metadata.update({
            'crs': target_crs,
            'transform': transform,
            'width': width,
            'height': height
        })
        with rasterio.open(output_path, 'w', **metadata) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=target_crs
                )
