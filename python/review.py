# print("お支払いは"+str(int(input("料金を入力>>") /int(input("人数を入力>>")))+"円です")
# num=1
# float=0.5
# flag=num+float<2
# print(type(flag))
# name="松田光太"
# age=23
# height=175.6
# print("私の名前は"+name+"で、年齢は"+str(age)+"歳で、身長は"+str(height)+"cmです")
# print("私の名前は{}で、年齢は{}歳で、身長は{}cmです".format(name,age,height))
# print(f"私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです")
# taijuu=int(input("体重(kg)>>"))
# sinntyou=int(input("身長(cm)>>"))/100
# bmi=taijuu/sinntyou/sinntyou
# if bmi<18.5:
#     bunnrui="低体重"
# elif bmi<25:
#     bunnrui="普通体重"
# elif bmi<30:
#     bunnrui="肥満(1度)"
# elif bmi<35:
#     bunnrui="肥満(2度)"
# elif bmi<40:
#     bunnrui="肥満(3度)"
# else:
#     bunnrui="肥満(4度)"
# print("あなたのBMIは"+str(round(bmi,1))+"で、"+bunnrui)
# member=["工藤","松田","浅木"]
# print(member.pop(1))
# member.remove("浅木")
# print(member)
# print(member[-2:])
# scores={"network":60,"database":80,"security":50}
# print(sum(scores.values()))
# scores=(70,80,55)
# print(scores[1])
# print(sum(scores))
# print(type(scores))
# members=("松田",)
# print(type(members))
# scores={70,80,55,80}
# scores.add(99)
# print(sum(scores))
# print(type(scores))
# list=[1,2,3,4,5,5]
# print(set(list))
# matuda_scores={"network":60,"database":80,"security":50}
# asagi_scores={"network":80,"database":75,"security":92}
# member_scores={"松田":matuda_scores,"浅木":asagi_scores}
# print(member_scores["松田"]["security"])
# A={1,2,3,4}
# B={2,3,4,5}
# print(A|B)#被ってるやつをなくす
# print(A&B)#被っているやつだけ
# print(A-B)#Aの中でBにないやつ
# print(A^B)#被ってないやつ

# kyouka=["国語","算数","理科","社会","英語","情報"]
# def kekka():
#     gou=[]
#     iroiro=[]
#     name=input("名前は")
#     for i in kyouka:
#         gou.append(int(input(f"{i}の点数は")))
#     iroiro.extend([name,sum(gou)/len(kyouka),sum(gou)])
#     return iroiro

# tennsuu={}
# sai=[]
# ninnzuu=int(input("何人いますか？"))
# for i in range(ninnzuu):
#     iroiro=kekka()
#     tennsuu[iroiro[0]]=iroiro[1],iroiro[2]
#     sai.append(iroiro[2])

# kurasu=0
# for i in tennsuu.keys():
#     print(f"{i}の平均点は{tennsuu[i][0]}点、合計値は{tennsuu[i][1]}点")
#     kurasu+=tennsuu[i][1]
# print(f"クラスの平均点は{kurasu/ninnzuu}点")
# print(f"最高点は{max(sai)}点、最低点は{min(sai)}")

# def seikaku():
#     sei=[]
#     sei={input("あなたの趣味を5つ>>"),input(" "*17+">>"),input(" "*17+">>"),input(" "*17+">>"),input(" "*17+">>")}
#     return sei

# sei_1=seikaku()
# sei_2=seikaku()
# input("心の準備が出来たら Enter キーを押してください")
# aisyou=len(sei_1&sei_2)/len(sei_1|sei_2)
# print(f"あなたと相手の愛称は{aisyou*100}%です")

# scores = [80,100,20,60]
# i = 1
# print(100 in scores and not not not not not not not not i != 0)

# inital="K"
# if inital=="K":
#     print("True_1")

# point=100
# if 80 <= point <= 256:
#     print("True_2")

# bmi=17
# if bmi < 20 or bmi > 25:
#     print("True_3")

# year=84
# if year%4 == 0:
#     print("True_4")

# day=25
# num=[28,30,31]
# if not day in num:
#     print("True_5")

# for year in range(3000):
#     if year % 4 == 0:
#         if year % 100 == 0 and not year % 400 == 0:
#             print(f"{year}年は平年")
#         else:
#             print(f"{year}年は閏年")

# isError=False
# n=80
# if isError == False and n < 100:
#     print("ンボおおおおおお")

# num = int(input("数>>"))
# hanntei = num % 2 ==0
# if hanntei:
#     print("偶数")
# else:
#     print("奇数")

# mozi = input("あいさつ>>")
# if mozi == "こんにちは":
#     print("ようこそ!")
# elif mozi == "景気は?":
#     print("ぼちぼちです")
# elif mozi == "さようなら":
#     print("お元気で!")
# else:
#     print("どうしました?")

# num=0
# list=[]
# while True:
#     list.append(num)
#     if list[len(list)-1]==100:
#         break
#     num+=2
# print(list)

# list_2=[]
# for i in list:
#     list_2.append(i*10)
# print(list_2)

# ages = [28,50,"秘密",20,78,25,22,10,"無回答",33]
# samples = list()
# for data in ages:
#     if not isinstance(data,int):
#         continue
#     if data < 20 or data >= 30:
#         continue
#     samples.append(data)
# print(samples)

# count=1
# while True:
#     print("カレーを召し上がれ")
#     print(f"カレーを{count}皿食べました")
#     bunnki=input("おかわりはいかがですか?(y/n)>>")
#     if bunnki=="y":
#         count+=1
#         continue
#     else:
#         print("ご馳走様でした")
#         break

# for i in range(10):
#     print(10-i)
# print("Lift off!")

# for i in range(9):
#     if (i+1)%2==0:
#             continue
#     for j in range(9):
#         if (i+1)*(j+1)>=50:
#             continue
#         print(f"{(i+1)*(j+1)},",end="")
#     print()

# temp = [7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
# for i in range(10):
#     print(f"{temp[i]},",end="")
# print()
# temp_new=[]
# temp_new=temp
# temp_new[5]="N/A"
# count_1=0
# count_2=0
# for i in range(10):
#     print(f"{temp_new[i]},",end="")
# print()
# for i in temp_new:
#     if type(i)==float:
#         count_1+=i
#         count_2+=1
# print(count_1/count_2)

# student_list = ["浅木","松田"]
# count = 0
# for student in student_list:
#     print(f"{student}さんの試験結果を入力してください")
#     network = int(input("ネットワークの得点>>"))
#     database = int(input("データベースの得点>>"))
#     security = int(input("セキュリティの得点>>"))
#     if student == "浅木":
#         asagi_scores = [network,database,security]
#         asagi_avg = sum(asagi_scores) / len(asagi_scores)
#     else:
#         matsuda_scores = [network,database,security]
#         matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
# print(f"浅木さんの平均点は{asagi_avg}です")
# print(f"松田さんの平均点は{matsuda_avg}です")

# def hello():
#     print("Hello world!")

# hello()

# def hello(name_1,name_2):
#     hi = (f"Hello {name_1},{name_2}!")
#     return hi

# hi=hello(input(),input())

# print(hi)

# def tasizan(num_1,num_2,kigou):
#     if kigou == "+":
#         kotae = num_1 + num_2
#     elif kigou == "-":
#         kotae = num_1 - num_2
#     elif kigou == "*":
#         kotae = num_1 * num_2
#     elif kigou == "/":
#         kotae = num_1 / num_2
#     return kotae

# print(tasizan(int(input("number_1>>")),int(input("number_2>>")),input("+ or - or * or / >>")))

# def circle(hankei):  # 円の面積
#     menseki = hankei * hankei * 3.14
#     return menseki

# menseki = circle(int(input("円の半径")))

# if menseki.is_integer():
#     print(f"円の面積は{int(menseki)}cm^2です")
# else:
#     print(f"円の面積は{menseki}cm^2です")

# def trapezoid(joutei,katei,takasa):  # 台形の面積
#     menseki_trapezoid = (joutei + katei) * takasa /2
#     print(menseki_trapezoid)

# trapezoid(int(input("上底>>")),int(input("下底>>")),int(input("高さ>>")))

# def plus_and_minus(a,b):
#     return a+b,a-b

# a,b=plus_and_minus(3,5)
# print(a,b)

# name = "松田"
# def hello():
#     global name
#     name="浅木"
#     print(f"こんにちは{name}さん")

# hello()
# print(name)

# def weather():
#     print("今日は晴れです")

# weather()

# def calc_circle_area(hankei):
#     return hankei*hankei*3.14

# menseki=calc_circle_area(10)
# print(menseki)

# def is_leapyear(year):
#     if year%400==0 or (year%4==0 and year%100!=0):
#         print(f"西暦{year}年は、うるう年です")
#     else:
#         print(f"西暦{year}年は、うるう年ではありません")

# is_leapyear(int(input("year>>")))

# def take_bus():
#     print("バスに乗ります")

# def walk():
#     print("ちょっと歩きます")

# def run():
#     print("走ります!")
#     walk()

# print("行ってきます")
# walk();take_bus();run();run()
# print("ただいま")

# def int_input(msg):
#     return int(input(f"{msg}を入力してください>>"))

# def calc_payment(amount,people):
#     dnum=amount/people
#     pay=dnum//100*100
#     if dnum>pay:
#         return int(pay+100)
#     else:
#         return int(pay)

# def show_payment(amount,people,pay):
#     payorg=amount-pay*(people-1)
#     print("***支払額***")
#     print(f"一人当たり{pay}円{people-1}人、幹事は{payorg}円です")

# amount=int_input("支払い総額")
# people=int_input("参加人数")
# pay=calc_payment(amount,people)
# show_payment(amount,people,pay)

# common
import pandas as pd
import numpy as np

# init part(データの読み込みと前処理)
file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
online_retail_data = pd.ExcelFile(file_url)
online_retail_data_table = online_retail_data.parse('Online Retail')

# 採点の都合上、文字列型に変換
online_retail_data_table['cancel_flg'] = online_retail_data_table.InvoiceNo.map(lambda x:str(x)[0])

# InvoiceNoの先頭が5であるものとIDがNullでないものが対象
target_online_retail_data_tb = online_retail_data_table[(online_retail_data_table.cancel_flg == '5') 
                                                        & (online_retail_data_table.CustomerID.notnull())]

target_online_retail_data_tb = target_online_retail_data_tb.assign(TotalPrice=target_online_retail_data_tb.Quantity * target_online_retail_data_tb.UnitPrice)

def homework(target_online_retail_data_tb, n):
    my_result = target_online_retail_data_tb
    return my_result

my_result = homework(target_online_retail_data_tb, 5)
print(my_result)