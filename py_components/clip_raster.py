
import rasterio
from rasterio.mask import mask


def clip_raster(input_raster, geometry, output_file):
    with rasterio.open(input_raster) as src:
        out_image, out_transform = mask(src, [geometry], crop=True)
        out_meta = src.meta.copy()
        out_meta.update({
            'driver': 'GTiff',
            'height': out_image.shape[1],
            'width': out_image.shape[2],
            'transform': out_transform
        })
        with rasterio.open(output_file, 'w', **out_meta) as dest:
            dest.write(out_image)
