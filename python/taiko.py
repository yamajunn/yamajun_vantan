import cv2

# 画像を読み込み
img = cv2.imread('images/Lake2.jpg')
img = cv2.resize(img, (400, 500))

# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 画像の大きさを取得
height, width = gray.shape[:2]

# 文字セット
char = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,"

# 画像の中身を1文字ずつ出力
for h in range(height):
    for w in range(width):
        pixel = gray[h,w]
        print(char[pixel//25], end=" ")
    print()
