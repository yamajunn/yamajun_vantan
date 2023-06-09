import os
import cv2
import numpy as np
from PIL import Image
import copy

path = "./images1"
files = os.listdir(path)
base = cv2.imread('base.png')


for file in files:
    # 画像の読み込み
    img = cv2.imread(f'images1/{file}', flags = cv2.IMREAD_UNCHANGED)

    # if img.shape[0] != 16:
    #     img = img[0:16, 0:16]

    # 指定色
    target_color = (0, 0, 0, 0)

    # 変更後の色
    change_color = (0, 0, 0, 255)
    change_color2 = (255, 255, 255, 255)

    # 画像の縦横
    h, w = img.shape[:2]

    img = cv2.resize(img, (int(w*4), int(h*4)))

    h, w = h*4, w*4
    image_list = []

    for i in range(h):
        for j in range(w):
            b, g, r, a = img[i, j]
            if a > 125:
                img[i, j] = 0, 0, 0, 255
            else:
                img[i, j] = 0, 0, 0, 0
            b, g, r, a = img[i, j]
            image_list.append(a)
    
    image_t_f_list = []
    hight_list = []
    hight_list2 = []
    for i in range(h):
        if i % w == 0:
            hight_list.append(i)
            hight_list2.append(i+w-1)

    for i in range(h*w):
        if (i != 0 and image_list[i] == 255 and image_list[i-1] == 0) or (i != h*w-1 and image_list[i] == 255 and image_list[i+1] == 0):
            # or (image_list[i] == 255 and image_list[i-15] == 0) or (i <= 240 and image_list[i] == 255 and image_list[i+15] == 0)
            image_t_f_list.append(True)
        else:
            image_t_f_list.append(False)
        if i % w == 0 and image_list[i] != 0:
            image_t_f_list[i] = True
        if i % w == w-1 and image_list[i] != 0:
            image_t_f_list[i] = True
        if i // w in hight_list and image_list[i] != 0:
            image_t_f_list[i] = True
        if i // w in hight_list2 and image_list[i] != 0:
            image_t_f_list[i] = True

    for i in range(h):
        for j in range(w):
            if image_t_f_list[i*w + j]:
                img[i, j] = change_color2

    

    cv2.imwrite(f'block/{file}',img)
