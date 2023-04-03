kare_ = []
ryouri_zairyou_zisyo = {'kare-':123}
while True:
    zairyou = input("材料を入力してください (スペース区切り)>>").split()
    zairyou_kakunin = ",".join(zairyou)
    print(f"材料は{zairyou_kakunin}です")
    kakunin = input("修正しますか? y/n")
    if kakunin == "n":
        break
zairyou_zisyo = {}
for i in zairyou:
    ryou = int(input(f"{i}は何gですか？"))
    zairyou_zisyo[i] = ryou
print(zairyou_zisyo)
