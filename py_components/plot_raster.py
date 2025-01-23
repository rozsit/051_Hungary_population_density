
import rasterio
import matplotlib.pyplot as plt
import numpy as np


def plot_raster(input_raster, output_image):
    with rasterio.open(input_raster) as src:
        data = np.log1p(src.read(1))
    plt.figure(figsize=(13, 11))
    plt.imshow(data, cmap='magma')
    plt.title('Population Density of Hungary')
    plt.axis('off')
    plt.savefig(output_image, dpi=600, bbox_inches='tight')
    plt.show()
