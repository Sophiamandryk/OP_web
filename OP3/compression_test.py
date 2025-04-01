
"""test"""
import numpy as np
from PIL import Image, ImageOps
from compression import GrayscaleImage

# Load an image into the GrayscaleImage class
image_obj = GrayscaleImage.from_file("billie.jpg")

# Display basic properties
print(f"Width: {image_obj.width()}")
print(f"Height: {image_obj.length()}")

# Check pixel value at (100, 100)
print(f"Pixel at (100,100): {image_obj.getitem(100, 100)}")

# Modify a pixel value and check again
image_obj.setitem(100, 100, 255)
print(f"New pixel at (100,100): {image_obj.getitem(100, 100)}")

# Clear the image with a specific intensity (e.g., 128)
image_obj.clear(128)
print(f"Pixel after clearing (100,100): {image_obj.getitem(100, 100)}")

# Convert back to image and show
output_img = Image.fromarray(image_obj.pixels)
output_img.show()  # Opens the image in the default viewer

# Save the modified image
output_img.save("billie_gray_modified_1.jpg")
print("Modified image saved as 'billie_gray_modified_1.jpg'")
