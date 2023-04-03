import random
kati=0
make=0
atti=0
while True:
    player=input("ジャンケンを入力してください->")
    janken=["グー!!!","チョキ!!!","パー!!!"]
    num=random.randint(0,2)
    hoi=random.randint(0,3)
    print("PCの手 :"+janken[num])
    print("プレイヤーの手 :"+player)

    if player=="グー"or player=="ぐー"or player=="0":
        jan=0
    elif player=="チョキ"or player=="ちょき"or player=="1":
        jan=1
    elif player=="パー"or player=="ぱー"or player=="2":
        jan=2

    if jan==num:
        print("あいこ　(๑>◡<๑)")
        print("もう一度　*\(^o^)/*")
    elif jan==0:
        if num==1:
            print("勝ち! (*ﾟ▽ﾟ*)")
            print("あっちむいて〜　٩( ᐛ )و")
            dotti=input("どちらに指を向けますか？->")
            print("ほい!!("+dotti+")")
            if dotti=="上"or dotti=="うえ"or dotti=="↑":
                atti=0
            elif dotti=="左"or dotti=="ひだり"or dotti=="←":
                atti=1
            elif dotti=="下"or dotti=="した"or dotti=="↓":
                atti=2
            elif dotti=="右"or dotti=="みぎ"or dotti=="→":
                atti=3
            
            if hoi==0:
                kotti="上"
            elif hoi==1:
                kotti="左"
            elif hoi==2:
                kotti="下"
            elif hoi==3:
                kotti="右"

            if atti==hoi:
                print("PC("+kotti+")(๑>◡<๑)")
                print("あなたの勝ち!! (*ﾟ∀ﾟ*)")
                kati+=1
            else:
                print("PC("+kotti+")(๑>◡<๑)")
                print("残念はずれ　(・ω・｀)")
        elif num==2:
            print("負け　:;(∩´﹏`∩);:")
            print("あっちむいて　٩( ᐛ )و")
            dotti=input("どちらに頭を向けますか？->")
            print("ほい!!("+dotti+")")
            if dotti=="上"or dotti=="うえ"or dotti=="↑":
                atti=0
            elif dotti=="左"or dotti=="ひだり"or dotti=="←":
                atti=1
            elif dotti=="下"or dotti=="した"or dotti=="↓":
                atti=2
            elif dotti=="右"or dotti=="みぎ"or dotti=="→":
                atti=3
            if hoi==0:
                kotti="上"
            elif hoi==1:
                kotti="左"
            elif hoi==2:
                kotti="下"
            elif hoi==3:
                kotti="右"

            if atti==hoi:
                print("PC("+kotti+")(๑>◡<๑)")
                print("あなたの負け (・ω・｀)")
                make+=1
            else:
                print("PC("+kotti+")(๑>◡<๑)")
                print("セーフ　（＾Ｏ＾☆♪")
    elif jan==1:
        if num==0:
            print("負け　:;(∩´﹏`∩);:")
            print("あっちむいて　٩( ᐛ )و")
            dotti=input("どちらに頭を向けますか？->")
            print("ほい!!("+dotti+")")
            if dotti=="上"or dotti=="うえ"or dotti=="↑":
                atti=0
            elif dotti=="左"or dotti=="ひだり"or dotti=="←":
                atti=1
            elif dotti=="下"or dotti=="した"or dotti=="↓":
                atti=2
            elif dotti=="右"or dotti=="みぎ"or dotti=="→":
                atti=3
            if hoi==0:
                kotti="上"
            elif hoi==1:
                kotti="左"
            elif hoi==2:
                kotti="下"
            elif hoi==3:
                kotti="右"

            if atti==hoi:
                print("PC("+kotti+")")
                print("あなたの負け (・ω・｀)")
                make+=1
            else:
                print("PC("+kotti+")")
                print("セーフ　（＾Ｏ＾☆♪")
        elif num==2:
            print("勝ち! (*ﾟ▽ﾟ*)")
            print("あっちむいて　٩( ᐛ )و")
            dotti=input("どちらに指を向けますか？->")
            print("ほい!!("+dotti+")")
            if dotti=="上"or dotti=="うえ"or dotti=="↑":
                atti=0
            elif dotti=="左"or dotti=="ひだり"or dotti=="←":
                atti=1
            elif dotti=="下"or dotti=="した"or dotti=="↓":
                atti=2
            elif dotti=="右"or dotti=="みぎ"or dotti=="→":
                atti=3
            if hoi==0:
                kotti="上"
            elif hoi==1:
                kotti="左"
            elif hoi==2:
                kotti="下"
            elif hoi==3:
                kotti="右"

            if atti==hoi:
                print("PC("+kotti+")(๑>◡<๑)")
                print("あなたの勝ち")
                kati+=1
            else:
                print("PC("+kotti+")(๑>◡<๑)")
                print("残念はずれ (・ω・｀)")
    elif jan==2:
        if num==0:
            print("勝ち! (*ﾟ▽ﾟ*)")
            print("あっちむいて　٩( ᐛ )و")
            dotti=input("どちらに指を向けますか？->")
            print("ほい!!("+dotti+")")
            if dotti=="上"or dotti=="うえ"or dotti=="↑":
                atti=0
            elif dotti=="左"or dotti=="ひだり"or dotti=="←":
                atti=1
            elif dotti=="下"or dotti=="した"or dotti=="↓":
                atti=2
            elif dotti=="右"or dotti=="みぎ"or dotti=="→":
                atti=3
            if hoi==0:
                kotti="上"
            elif hoi==1:
                kotti="左"
            elif hoi==2:
                kotti="下"
            elif hoi==3:
                kotti="右"

            if atti==hoi:
                print("PC("+kotti+")(๑>◡<๑)")
                print("あなたの勝ち")
                kati+=1
            else:
                print("PC("+kotti+")(๑>◡<๑)")
                print("残念はずれ (・ω・｀)")
        elif num==1:
            print("負け　:;(∩´﹏`∩);:")
            print("あっちむいて　٩( ᐛ )و")
            dotti=input("どちらに頭を向けますか？->")
            print("ほい!!("+dotti+")")
            if dotti=="上"or dotti=="うえ"or dotti=="↑":
                atti=0
            elif dotti=="左"or dotti=="ひだり"or dotti=="←":
                atti=1
            elif dotti=="下"or dotti=="した"or dotti=="↓":
                atti=2
            elif dotti=="右"or dotti=="みぎ"or dotti=="→":
                atti=3
            if hoi==0:
                kotti="上"
            elif hoi==1:
                kotti="左"
            elif hoi==2:
                kotti="下"
            elif hoi==3:
                kotti="右"

            if atti==hoi:
                print("PC("+kotti+")(๑>◡<๑)")
                print("あなたの負け (・ω・｀)")
                make+=1
            else:
                print("PC("+kotti+")(๑>◡<๑)")
                print("セーフ　（＾Ｏ＾☆♪")
    if kati==3:
        print("あなたの勝ち!! ٩( ᐛ )و")
        break
    if make==3:
        print("あなたの負け (・ω・｀)")
        break
    if kati or make<3:
        print("3回勝負、もう一度!")
        print(str(kati)+"-"+str(make))
