import os
import cv2
import numpy as np

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

    image_list = []

    # 色の変更
    for i in range(h):
        for j in range(w):
            b, g, r, a = img[i, j]
            image_list.append(a)
            if a != 0:
                img[i, j] = change_color
            # else:
            #     img[i, j] = change_color2
    
    image_t_f_list = []
    hight_list = []
    hight_list2 = []
    for i in range(h):
        if i % 16 == 0:
            hight_list.append(i)
            hight_list2.append(i+15)

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
        if i // 16 in hight_list and image_list[i] != 0:
            image_t_f_list[i] = True
        if i // 16 in hight_list2 and image_list[i] != 0:
            image_t_f_list[i] = True

    for i in range(h):
        for j in range(w):
            if image_t_f_list[i*w + j]:
                img[i, j] = change_color2

    

    cv2.imwrite(f'block/{file}',img)
