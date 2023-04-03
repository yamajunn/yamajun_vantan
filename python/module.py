# text = input("何を記録しますか?>>")
# with open("diary.txt","a") as file:
#     file.write(text + "\n")
# from math import *
# print(f"円周率は{pi}です")
# print(f"小数点以下を切り捨てれば{floor(pi)}です")
# print(f"小数点以下を切り上げれば{ceil(pi)}です")
# from http.client import HTTPConnection
# conn = HTTPConnection("www.python.org")
import random

def count(answer,prediction,num_1,num_2,num_3):
    hit_count,bone_count = 0,0
    if answer[num_1] == prediction[num_1]:
        hit_count = 1
    elif answer[num_1] == prediction[num_2] or answer[num_1] == prediction[num_3]:
        bone_count = 1
    return hit_count,bone_count

print("数当てゲームを始めます。3桁の数字を当ててください!")
num_list,answer,death_number = [0,1,2,3,4,5,6,7,8,9],[],[]
random.shuffle(num_list)
for i in range(3):
    answer.append(num_list[i])
print(answer)
for i in range(3):
    death_number.append(num_list[3])
print(death_number)

life = 3
while True:
    print(f"あなたのライフは{life}です")
    life -= 1

    prediction = []
    for i in range(3):
        num = int(input(f"{i+1}行目の予想を入力(0~9)>>"))
        prediction.append(num)
    print(prediction)

    hit_count,bone_count,death_hit_count = 0,0,0
    hit,bone=count(answer,prediction,0,1,2)
    hit_count += hit
    bone_count += bone
    hit,bone=count(answer,prediction,1,2,0)
    hit_count += hit
    bone_count += bone
    hit,bone=count(answer,prediction,2,0,1)
    hit_count += hit
    bone_count += bone
    hit,bone=count(death_number,prediction,0,1,2)
    death_hit_count += hit
    hit,bone=count(death_number,prediction,1,2,0)
    death_hit_count += hit
    hit,bone=count(death_number,prediction,2,0,1)
    death_hit_count += hit

    life += hit_count
    life -= death_hit_count
    print(f"ヒットは{hit_count}ボーンは{bone_count}")
    if life <= 0:
        print("ライフが0です ゲームオーバー")
        break
    if hit_count == 3:
        print("正解です!")
        break
    ru_pu = input("続けますか？ 1:続ける 2:終了>>")
    if ru_pu == 2:
        print(f"正解は{answer}です。")
        break
death_number_count = 2
while True:
    death_number_count -= 1
    death_number_cuection = int(input("デスナンバーを入力してください"))
    if death_number_cuection == death_number[0]:
        print("正解　おめでとう")
        break
    else:
        if death_number_cuection >= death_number[0]:
            print("もっと小さいです")
        elif death_number_cuection <= death_number[0]:
            print("もっと大きいです")
    if death_number_count <= 0:
        print("ゲームオーバー")
        break