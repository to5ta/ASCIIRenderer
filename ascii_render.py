#!/usr/bin/env python3
from cgitb import reset
from email.mime import image
import shutil
import sys
from PIL import Image
import numpy as np

size = shutil.get_terminal_size()
print(f"Size: {size}")
GLYPH_SIZE_RATIO = 1/2.

ar = [ "@#S%?*+;:,." ]
rmp  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def main():
    imgdata = getGreyScaleDataFromImage(sys.argv[1])
    charImgStr = renderGreyScaleDataToASCII(imgdata, ar)
    print(charImgStr)
    with open("result.txt", "w") as file:
        file.write(charImgStr)

def getGreyScaleDataFromImage(filepath: str, pixel_to_column_ratio: float = 0.05):
    img = Image.open(filepath)
    x = img.size[0] * pixel_to_column_ratio;
    y = img.size[1] * pixel_to_column_ratio * GLYPH_SIZE_RATIO
    img = img.resize([ int(x), int(y)])
    img = img.convert("L")
    imgdata = np.asarray(img)
    np.linalg.norm(imgdata)
    imgdata *= 255
    return imgdata 

def renderGreyScaleDataToASCII(imgdata: np.array, ramp: str):
    result = ""
    for y in range(0, imgdata.shape[0]):
        for x in range(0, imgdata.shape[1]):
            px = imgdata[y][x]
            char = ramp[min(len(ramp)-1, min(px, 255)//len(ramp))]
            result += char
        result += "\n"
    return result

if __name__ == "__main__":
    main()