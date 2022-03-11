#!/usr/bin/env python3
import shutil
import sys
from PIL import Image
import numpy as np

GLYPH_SIZE_RATIO = 1/2.

ramp0  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ramp1 = "@#S%?*+;:,."

def main() -> int:
    # scalef = getMaxScaleAtTerminal()
    imgdata = getGreyScaleDataFromImage(sys.argv[1], 0.20)
    charImgStr = renderGreyScaleDataToASCII(imgdata, ramp1)
    print(charImgStr)
    with open("result.txt", "w") as file:
        file.write(charImgStr)
    return 0

def getMaxScaleAtTerminal(imgx : int, imgy : int) -> float:
    x,y = shutil.get_terminal_size()
    return min(imgx/x, imgy/y)

def getGreyScaleDataFromImage(filepath: str, pixel_to_column_ratio: float = 0.12) -> np.array:
    img = Image.open(filepath)
    x = img.size[0] * pixel_to_column_ratio;
    y = img.size[1] * pixel_to_column_ratio * GLYPH_SIZE_RATIO
    img = img.resize([ int(x), int(y)])
    img = img.convert("L")
    imgdata = np.asarray(img)
    np.linalg.norm(imgdata)
    imgdata *= 255
    return imgdata 

def renderGreyScaleDataToASCII(data: np.array, ramp: str) -> str:
    result = ""
    for y in range(0, data.shape[0]):
        for x in range(0, data.shape[1]):
            px = data[y][x]
            char = ramp[min(len(ramp)-1, min(px, 255)//len(ramp))]
            result += char
        result += "\n"
    return result

if __name__ == "__main__":
    main()