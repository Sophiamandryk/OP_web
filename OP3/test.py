
"""test"""
import numpy as np
from PIL import Image, ImageOps
from compression import GrayscaleImage

# img = GrayscaleImage.from_file("picture.jpg")
# compressed_data = img.lzw_compression()
# print("Compressed size:", len(compressed_data))
# print("Original size:", img.nrows * img.ncols)


img = GrayscaleImage.from_file("picture.jpg")
compressed_data = img.lzw_compression()
img.lzw_decompression(compressed_data)
img.save("decompressed.jpg")
