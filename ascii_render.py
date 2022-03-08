#!/usr/bin/env python3
from email.mime import image
import shutil
import sys
from PIL import Image
import numpy as np

size = shutil.get_terminal_size()
print(f"Size: {size}")
GLYPH_SIZE_RATIO = 1/2.

ar = [ "@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "." ]
rmp  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

img = Image.open(sys.argv[1])

ratio = img.size[0] / img.size[1]

x = size.columns
y = img.size[1] / (img.size[0] / size.columns) * GLYPH_SIZE_RATIO

img = img.resize([ int(x), int(y)])
img = img.convert("L")

imgdata = np.asarray(img)

np.linalg.norm(imgdata)
imgdata *= 255
img.putdata(imgdata.flatten())
# img.show()
# print(f"Shape {imgdata.shape}")

for y in range(0, imgdata.shape[0]):
    for x in range(0, imgdata.shape[1]):
        px = imgdata[y][x]
        # char = rmp[len(rmp) -1- px//len(rmp)]
        char = ar[px//len(ar)]

        print(char, end="")
    print()
        # print("h", end="")