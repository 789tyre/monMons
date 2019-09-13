from random import randint
from PIL import Image

img = Image.new("RGB", (255,255))
blue = 0
for i in range(255):
    for j in range(255):
        img.putpixel((i, j), (i, j, blue))
    blue += 1


img.save("image.png")
