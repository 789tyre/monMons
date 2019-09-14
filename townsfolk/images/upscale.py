from PIL import Image

for i in range(8):
    img = Image.open(str(i) + ".png")
    img = img.resize((1020,1020),0)
    img.save("upscaled/{}_resized.png".format(i))
