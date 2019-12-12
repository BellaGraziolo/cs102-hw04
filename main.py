import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")

for i in range(1, width // 12):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, 250, 250))
for i in range(1, width // 12):
    for j in range(1, height // 12):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, g, b))
for i in range(1, width // 12):
    for j in range(height // 12, height // 6):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (255, 255, int(b/2)))
for i in range(width // 12, (2 * width) // 3):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (255, g, 100))
for i in range((2 * width) // 3, width):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (240, 170, b))

new_img.save(output_path)
