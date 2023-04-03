import random

def syahhuru(tora):
    random.shuffle(tora)

def syurui(tora,v1,v2):
    for i in range(52):
        v1.append(tora[i]%4)
        if v1[i]==0:
            v2.append("♣︎")
        if v1[i]==1:
            v2.append("♠︎")
        if v1[i]==2:
            v2.append("❤︎")
        if v1[i]==3:
            v2.append("♦︎")

def wariate(tora,a1):
    for i in range(52):
        if tora[i]<=4:
            a1.append(1)
        elif tora[i]<=8:
            a1.append(2)
        elif tora[i]<=12:
            a1.append(3)
        elif tora[i]<=16:
            a1.append(4)
        elif tora[i]<=20:
            a1.append(5)
        elif tora[i]<=24:
            a1.append(6)
        elif tora[i]<=28:
            a1.append(7)
        elif tora[i]<=32:
            a1.append(8)
        elif tora[i]<=36:
            a1.append(9)
        elif tora[i]<=52:
            a1.append(0)

def hitoketaP1(a1):
    a2=a1[0]+a1[1]
    if a2>=10:
        a2%=10
    return a2

def hitoketaB1(a1):
    a3=a1[2]+a1[3]
    if a3>=10:
        a3%=10
    return a3

def hyouzi(a2,a3,a1,v2):
    input("トランプを引いてください(enter)")
    print("\u001b[2J\u001b[1;1H", end='')
    print("="*50)
    print("Playerのトランプは["+str(v2[0])+":"+str(a1[0])+"]と["+str(v2[1])+":"+str(a1[1])+"]")
    print("合計は"+str(a1[0]+a1[1])+"で、一桁目は"+str(a2))
    print("="*50)
    print("Bankerのトランプは["+str(v2[2])+":"+str(a1[2])+"]と["+str(v2[3])+":"+str(a1[3])+"]")
    print("合計は"+str(a1[2]+a1[3])+"で、一桁目は"+str(a3))
    print("="*50)
    print(str(a2)+"-"+str(a3))

def Psyori(a2,a3):
        print("="*50)
        print("勝負します。")
        print(str(a2)+"-"+str(a3)+"で")
        if a2==a3:
            print("引き分け")
            return 0
        elif a2<a3:
            print("Babkerの勝ち")
            return 1
        elif a2>a3:
            print("Playerの勝ち")
            return 2
def Bsyori(a2,a3,a1):
    if 0<=a2<=1 and 0<=a3<=3:
        print("Bankerの値は"+str(a3)+"なのでもう一枚引きます。")
        a3=a3+a1[5]
        if a3>=10:
            a3%=10
        print(str(a1[5])+" Bankerの値は"+str(a3))
    elif 2<=a2<=3 and 0<=a3<=4:
        print("Bankerの値は"+str(a3)+"なのでもう一枚引きます。")
        a3=a3+a1[5]
        if a3>=10:
            a3%=10
        print(str(a1[5])+" Bankerの値は"+str(a3))
    elif 4<=a2<=5 and 0<=a3<=5:
        print("Bankerの値は"+str(a3)+"なのでもう一枚引きます。")
        a3=a3+a1[5]
        if a3>=10:
            a3%=10
        print(str(a1[5])+" Bankerの値は"+str(a3))
    elif 6<=a2<=7 and 0<=a3<=6:
        print("Bankerの値は"+str(a3)+"なのでもう一枚引きます。")
        a3=a3+a1[5]
        if a3>=10:
            a3%=10
        print(str(a1[5])+" Bankerの値は"+str(a3))
    elif a2==8 and 0<=a3<=2:
        print("Bankerの値は"+str(a3)+"なのでもう一枚引きます。")
        a3=a3+a1[5]
        if a3>=10:
            a3%=10
        print(str(a1[5])+" Bankerの値は"+str(a3))
    elif a2==9 and 0<=a3<=3:
        print("Bankerの値は"+str(a3)+"なのでもう一枚引きます。")
        a3=a3+a1[5]
        if a3>=10:
            a3%=10
        print(str(a1[5])+" Bankerの値は"+str(a3))
def saisyuusyouri(a2,a3):
    print("="*50)
    print("勝負します。")
    print(str(a2)+"-"+str(a3)+"で")
def syoribunnki(a2,a3):
    if a2==a3:
        print("引き分け")
        return 0
    elif a2<a3:
        print("Babkerの勝ち")
        return 1
    elif a2>a3:
        print("Playerの勝ち")
        return 2

def okane(c1,a1,v1,v2,x):
    while True:
            print("今のポイント:"+str(c1))
            c2=input("何ポイント賭けますか？")
            if c2=="all":
                c2=c1
                return c2
            if not str.isdigit(c2):
                c2=100
                return c2
            elif int(c2)>c1:
                print("\u001b[2J\u001b[1;1H", end='')
                print("所持ポイントより多いいポイントは賭けられません")
                print("もう一度")
            else:
                return c2
def kakekinn():
    c1=10000
    while True:
        a1=[]
        v1=[]
        v2=[]
        x=0
        tora=[i+1 for i in range(52)]
        c2=okane(c1,a1,v1,v2,x)
        c3=input("何にかけますか？ p/b/t: ")
        syahhuru(tora)
        syurui(tora,v1,v2)
        wariate(tora,a1)
        a2=hitoketaP1(a1)
        a3=hitoketaB1(a1)
        hyouzi(a2,a3,a1,v2)
        if 0<=a2<=5:
            print("Playerの値は"+str(a2)+"なのでもう一枚引きます。")
            input("トランプを引いてください")
            a2=a2+a1[4]
        if a2>=10:
            a2%=10
        print(str(a1[4])+" Playerの値は"+str(a2))
        if 8<=a2<=9:
            x=Psyori(a2,a3)
        else:
            Bsyori(a2,a3,a1)
            saisyuusyouri(a2,a3)
            x=syoribunnki(a2,a3)
        if x==0 and c3=="t":
            c1+=int(c2)*8
            print("おめでとう")
        elif x==1 and c3=="b":
            c1+=int(c2)*1.95
            c1=int(c1)
            print("おめでとう")
        elif x==2 and c3=="p":
            c1+=int(c2)*2
            print("おめでとう")
        else:
            c1-=int(c2)
            print("残念はずれ")
        if c1==0:
            print("所持金がなくなりました。")
            print("ゲームオーバー")
            break
        else:
            x1=input("終わりにしますか？ y/n 今のポイント"+str(c1)+": ")
            if x1=="y":
                break

kakekinn()