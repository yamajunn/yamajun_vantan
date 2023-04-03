import random
z3=10000  # 財布
while True:
    z1=0  # 賭け金
    while True:
        print("============================================================================")
        z1=input(str(z3)+"ポイント中何ポイントベットしますか？(数字でお願いします)->")
        if z1=="1248163264128256512":
            z3+=1000000000000
            z1=input(str(z3)+"ポイント中何ポイントベットしますか？(数字でお願いします)->")
        if z1=="all":
            z1=z3
        elif str.isdigit(z1):
            z1=int(z1)
        elif type(z1)==str:
            z1=100
            print("文字で入力されたので100円ベットしました。")
        if z1<=z3:
            break
        else:
            print("所持金以上のポイントは賭けられません")
    z3-=z1  # 賭けた
    print("あなたの所持ポイントは"+str(z3)+"ポイントです")
    a1=[]  # プレイヤーがどのトランプを出したか記録する[?]
    a2=[]  # ディーラーがどのトランプを出したか記録する[?]
    a4=0  # "トランプをまだ引きますか？はい/いいえ->"を出さないときにそれ以外を動かすため
    a5=0  # "1を11にしますか？はい/いいえ->"のやつ
    a7=0  # ディーラーの最終合計(?)
    a8=0  # プレイヤーの最終合計(?)
    a9=0  # ディーラーが終わらせた合図(1~2)
    a10=0  # プレイヤーが終わらせた時の合図(1~2)
    a11=0  # "トランプをまだ引きますか？はい/いいえ->"がでないようにするカウント(0~1)
    x1=0  # トランプのリストの番号を割り当てる(0~51)
    x2=0  # トランプがどの属性か確か割り当てるときに使う(1~4になる)
    x3=0  # 最初にトランプを2回引かせるためのカウント(0~2)
    x4=0  # 引いたトランプ内の番号を割り当てる(0~51)?
    x5=0  # ディーラーが終わったら引かないやつ
    x6=0  # プレイヤーが1+10が出た時
    x7=0  # ディーラーが1+10が出た時
    b10=0
    b11=0
    c1=[]
    c2=[]

    num=[]
    for i in range(52):  #ランダムなリストを作るやつら
        num.append(i+1)
        #num.append(1)
    random.shuffle(num)

    while True:#
        if x3<2:  # 最初は2回引かせる、次から1回ずつ
            if a11==0:
                print("============================================================================")
                player=input("トランプを引いてください(Enter)")
                print("\u001b[2J\u001b[1;1H", end='')
            if num[x1]<=4:
                a1.append(1)
            elif num[x1]<=8:
                a1.append(2)
            elif num[x1]<=12:
                a1.append(3)
            elif num[x1]<=16:
                a1.append(4)
            elif num[x1]<=20:
                a1.append(5)
            elif num[x1]<=24:
                a1.append(6)
            elif num[x1]<=28:
                a1.append(7)
            elif num[x1]<=32:
                a1.append(8)
            elif num[x1]<=36:
                a1.append(9)
            elif num[x1]<=52:
                a1.append(10)
            print("============================================================================")
            print("あなたのトランプは ",end="")  # トランプの属性を割り当てる~~~↓↓↓~~~
            if (num[x1]+4)%4==0:
                print("ダイヤの"+str(a1[x2]))
                c1.append("d"+str(a1[x2]))
            elif (num[x1]+4)%4==1:
                print("ハートの"+str(a1[x2]))
                c1.append("h"+str(a1[x2]))
            elif (num[x1]+4)%4==2:
                print("スペードの"+str(a1[x2]))
                c1.append("s"+str(a1[x2]))
            elif (num[x1]+4)%4==3:
                print("クローバーの"+str(a1[x2]))
                c1.append("k"+str(a1[x2]))  # ~~~↑↑↑~~~
            # print(c1)
            print(a1)
            x1+=1

            if x5==0:
                if num[x1]<=4:
                    a2.append(1)
                elif num[x1]<=8:
                    a2.append(2)
                elif num[x1]<=12:
                    a2.append(3)
                elif num[x1]<=16:
                    a2.append(4)
                elif num[x1]<=20:
                    a2.append(5)
                elif num[x1]<=24:
                    a2.append(6)
                elif num[x1]<=28:
                    a2.append(7)
                elif num[x1]<=32:
                    a2.append(8)
                elif num[x1]<=36:
                    a2.append(9)
                elif num[x1]<=52:
                    a2.append(10)
                print("ディーラーのトランプは ",end="")  # トランプの属性を割り当てる~~~↓↓↓~~~
                if (num[x1]+4)%4==0:
                    #print("ダイヤの"+str(a2[x2]))
                    c2.append("d"+str(a2[x2]))
                elif (num[x1]+4)%4==1:
                    #print("ハートの"+str(a2[x2]))
                    c2.append("h"+str(a2[x2]))
                elif (num[x1]+4)%4==2:
                    #print("スペードの"+str(a2[x2]))
                    c2.append("s"+str(a2[x2]))
                elif (num[x1]+4)%4==3:
                    #print("クローバーの"+str(a2[x2]))
                    c2.append("k"+str(a2[x2]))  # ~~~↑↑↑~~~
                print("???")
                #print(c2)
                #print(a2)
            x1+=1
            x2+=1
            x3+=1
        else:
            if a1[x4]==1:  # 1が出たとき11にするか決めるやつ(プレイヤー)
                if sum(a1)+10<=21:
                    a5=input("1を11にしますか？y/n->")
                if a5=="y":
                    a1[x4]=11
                    a5=0
            elif a1[x4+1]==1:  # 1が出たとき11にするか決めるやつ(プレイヤー)
                if sum(a1)+10<=21:
                    a5=input("1を11にしますか？y/n->")
                if a5=="y":
                    a1[x4+1]=11
                    a5=0
            if sum(a1)==21:
                x6+=1
            if sum(a2)+10<=21:
                if a2[x4]==1:  # 1が出たとき11にするか決めるやつ(ディーラー)
                    a2[x4]=11
                elif a2[x4+1]==1:  # 1が出たとき11にするか決めるやつ(ディーラー)
                    a2[x4+1]=11
            if sum(a2)==21:
                x7+=1
            print("あなたのトランプの合計"+str(sum(a1)))
            #print("ディーラーのトランプの合計"+str(sum(a2)))
            print("ディーラーのトランプの合計???")
            print("============================================================================")
            x4+=1
            x3=1
            if a7==0:  # 完了しているか判断
                if sum(a2)>=22:
                    a7=sum(a2)
                    a9+=2  # ディーラーが22以上になった時の終わり
                elif a7==21:
                    a7=sum(a2)
                    break
                elif 15<=sum(a2)<=21:  # ディーラーがちゃんと終わった時
                    a7=sum(a2)
                    a9+=1
                    x5+=1
            if x6==1 and x7==1:  # ディーラーとプレイヤーが21出した時
                a8=21
                a7=21
                break
            elif x6==1:  # プレイヤーだけ21出した時
                a8=21
                if a7==0:
                    a7=sum(a2)
                break
            elif x7==1:  # ディーラーだけ21出した時
                if a8==0:
                    a8=sum(a1)
                a7=21
                break
            if a9==1 and a10==1:  # 両方終わらせた時の終わり
                break
            if a9==2:  # ディーラーが22以上の時の終わり
                if not a10==1:
                    a8=sum(a1)
                break
            elif a10==2:  # プレイヤーが22以上の時の終わり
                if not a9==1:
                    a7=sum(a2)
                break
            if a8==0:  # 完了しているか判断
                if sum(a1)>=22:
                    a8=sum(a1)
                    print(a1)
                    a10+=2  # プレイヤーが22以上になった時の終わり
                elif a11==0:
                    if sum(a1)<=20:  # もう21だったら表示しない
                        a6=input("トランプをまだ引きますか？y/n->")
                        print("\u001b[2J\u001b[1;1H", end='')
                    else:
                        a4+=1
                    if a6=="n"or a4==1:  # プレイヤーが完了
                        a8=sum(a1)
                        print(a1)
                        a10+=1
                        a11+=1
                        a6=0
                        a4=0
            if a9==1 and a10==1:  # 両方終わらせた時の終わり
                break
            if a9==2:  # ディーラーが22以上の時の終わり
                if not a10==1:
                    a8=sum(a1)
                break
            elif a10==2:  # プレイヤーが22以上の時の終わり
                if not a9==1:
                    a7=sum(a2)
                break
    print("\u001b[2J\u001b[1;1H", end='')
    print("============================================================================")
    print("終了")
    print(a1)
    print(a2)
    print("あなたのトランプの最終合計"+str(a8))
    print("ディーラーのトランプの最終合計"+str(a7))
    if a8<22 and a7<22 and a8>a7:
        print(str(a8)+"-"+str(a7)+"であなたの勝ち")
        z3+=z1*2
    elif a8<22 and a7<22 and a8<a7:
        print(str(a8)+"-"+str(a7)+"であなたの負け")
    elif a8<22 and a7<22 and a8==a7:
        print(str(a8)+"-"+str(a7)+"で引き分け")

    if a8>=22 and a7>=22:
        print(str(a8)+"-"+str(a7)+"どちらも22以上になりました。引き分け")
    elif a8>=22:
        print(str(a8)+"-"+str(a7)+"あなたが22以上になりました。あなたの負け")
    elif a7>=22:
        print(str(a8)+"-"+str(a7)+"ディーラーが22以上になりました。あなたの勝ち")
        z3+=z1*2
    print("============================================================================")
    print("あなたのポイントは"+str(z3)+"ポイントです")
    if z3>=1:
        z2=input("終わりにしますか？y/n->")
        print("============================================================================")
        if z2=="y":
            print("あなたのポイントは"+str(z3)+"ポイントです")
            break
        print("\u001b[2J\u001b[1;1H", end='')
    elif z3<=0:
        print("ゲームオーバー")
        break