import os
import cv2
import numpy as np
from PIL import Image
import copy

img = cv2.imread('base.png', flags = cv2.IMREAD_UNCHANGED)
h, w = img.shape[:2]
img = cv2.resize(img, (int(w*2), int(h*2)))
h, w = h*2, w*2

for i in range(h):
        for j in range(w):
            b, g, r, a = img[i, j]
            if a > 125:
                img[i, j] = 0, 0, 0, 255
            else:
                img[i, j] = 0, 0, 0, 0

cv2.imwrite('base2.png',img)
