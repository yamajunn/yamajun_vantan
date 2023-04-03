import random
def trump_shuffle():
    trump=[i+1 for i in range(52)]
    random.shuffle(trump)
    return trump

def trump_wariate(trump):
    # トランプ　１〜１３　割り当て
    trump_suuzi=[]
    trump_suuzi_wariate=4
    trump_suuzi_banngou=1
    for i in range(52):
        for j in range(13):
            if trump_suuzi_wariate-4<trump[i]<=trump_suuzi_wariate:
                trump_suuzi.append(trump_suuzi_banngou)
            trump_suuzi_wariate+=4
            trump_suuzi_banngou+=1
        trump_suuzi_banngou=1
        trump_suuzi_wariate=4
    return trump_suuzi

def trump__zokusei(trump):
    #　トランプ　属性　割り当て
    trump_zokusei=[]
    for i in range(52):
        if trump[i]%4==1:
            trump_zokusei.append("♠︎")
        if trump[i]%4==2:
            trump_zokusei.append("❤︎")
        if trump[i]%4==3:
            trump_zokusei.append("♦︎")
        if trump[i]%4==0:
            trump_zokusei.append("♣︎")
    return trump_zokusei

def hyouzi(trump_zokusei,trump_suuzi):
    print("プレイヤーのトランプ: "+str(trump_zokusei[0])+str(trump_suuzi[0])+" : "+str(trump_zokusei[1])+str(trump_suuzi[1])+" : "+str(trump_zokusei[2])+str(trump_suuzi[2])+" : "+str(trump_zokusei[3])+str(trump_suuzi[3])+" : "+str(trump_zokusei[4])+str(trump_suuzi[4]))
    print("ディーラーのトランプ: "+str(trump_zokusei[5])+str(trump_suuzi[5])+" : "+str(trump_zokusei[6])+str(trump_suuzi[6])+" : "+str(trump_zokusei[7])+str(trump_suuzi[7])+" : "+str(trump_zokusei[8])+str(trump_suuzi[8])+" : "+str(trump_zokusei[9])+str(trump_suuzi[9]))
    print("="*50)

def p_list(trump_suuzi,trump_zokusei):
    #　プレイヤー　引いたやつ　リスト化
    player_motihuda=[]
    player_zokusei=[]
    for i in range(5):
        player_motihuda.append(trump_suuzi[i])
        player_zokusei.append(trump_zokusei[i])
    return (player_motihuda,player_zokusei)

def irekae(player_motihuda,player_zokusei,trump_suuzi,trump_zokusei):
    #　持ち札を入れ替える
    trump_irekae=list(map(int,input("何番目のトランプを入れ替えますか？1~5(スペース区切りで複数選択可) :").split()))
    for i in range(len(trump_irekae)):
        player_motihuda[trump_irekae[i]-1]=trump_suuzi[9+i]
        player_zokusei[trump_irekae[i]-1]=trump_zokusei[9+i]
    print("プレイヤーのトランプ :"+str(player_zokusei[0])+str(player_motihuda[0])+" : "+str(player_zokusei[1])+str(player_motihuda[1])+" : "+str(player_zokusei[2])+str(player_motihuda[2])+" : "+str(player_zokusei[3])+str(player_motihuda[3])+" : "+str(player_zokusei[4])+str(player_motihuda[4]))
    print("="*50)
    player_motihuda.sort()
    for i in range(5):
        if player_motihuda[i]==1:
            player_motihuda[i]=14
    return (player_motihuda,player_zokusei)

def d_list(trump_suuzi,trump_zokusei):
    #　ディーラー　引いたやつ　リスト化
    dealer_motihuda=[]
    dealer_zokusei=[]
    for i in range(5):
        if trump_suuzi[i+4]==1:
            dealer_motihuda.append(14)
        else:
            dealer_motihuda.append(trump_suuzi[i+4])
        dealer_zokusei.append(trump_zokusei[i+4])
    dealer_motihuda.sort()
    return (dealer_motihuda,dealer_zokusei)


def straight_p(player_motihuda):
    #　ストレートしているかどうか (p_straight_flush_kaunnto==4 の時はしている)
    p_straight_flush_kaunnto=0
    for i in range(4):
        if player_motihuda[i]+1 == player_motihuda[i+1]:
            p_straight_flush_kaunnto+=1
    return p_straight_flush_kaunnto

def suit_p(player_zokusei):
    #　スートが一種類かどうか (suit==True の時はしている)
    p_suit=all(val == player_zokusei[0] for val in player_zokusei)
    return p_suit
    
def four_cards_p(player_motihuda):
    #　フォーカードかどうか (four_cards==4 の時はしている)
    p_four_cards = player_motihuda.count(player_motihuda[0])
    p_four_cards_2 = player_motihuda.count(player_motihuda[4])
    if p_four_cards<=p_four_cards_2:
        p_four_cards=p_four_cards_2
    return p_four_cards

def full_house_p(player_motihuda):
    #　フルハウスしているかどうか (full_house==5 の時はしている)
    p_full_house_1=player_motihuda.count(player_motihuda[0])
    p_full_house_2=player_motihuda.count(player_motihuda[4])
    p_full_house=p_full_house_1+p_full_house_2
    return p_full_house

def three_card_p(player_motihuda):
    #　スリーカードしているかどうか (three_card==3 の時はしている)
    p_three_card=[]
    p_three_card.append(player_motihuda.count(player_motihuda[0]))
    p_three_card.append(player_motihuda.count(player_motihuda[2]))
    p_three_card.append(player_motihuda.count(player_motihuda[4]))
    p_three_card=max(p_three_card)
    return p_three_card

def pair_p(player_motihuda):
    #　何ペアになっているか (p_pair　で見れる)
    p_pair=[]
    p_pair.append(player_motihuda.count(player_motihuda[0]))
    p_pair.append(player_motihuda.count(player_motihuda[2]))
    p_pair.append(player_motihuda.count(player_motihuda[4]))
    p_pair=p_pair.count(2)
    return p_pair

def yakugime_p(player_motihuda,p_straight_flush_kaunnto,p_suit,p_four_cards,p_full_house,p_three_card,p_pair):
    #　プレイヤーの役を出す
    print("プレイヤー : ",end="")
    player=0
    if p_straight_flush_kaunnto==4 and p_suit==True and player_motihuda[0]==10:
        print("ロイヤルストレートフラッシュ!!")
        player=9
    elif p_straight_flush_kaunnto==4 and p_suit==True:
        print("ストレートフラッシュ")
        player=8
    elif p_four_cards==4:
        print("フォーカード")
        player=7
    elif p_full_house==5:
        print("フルハウス")
        player=6
    elif p_suit==True:
        print("フラッシュ")
        player=5
    elif p_suit==True:
        print("ストレート")
        player=4
    elif p_three_card==3:
        print("スリーカード")
        player=3
    elif p_pair==2:
        print("ツーペア")
        player=2
    elif p_pair==1:
        print("ワンペア")
        player=1
    elif p_pair==0:
        print("ノーハンド")
        player=0
    else:
        print("error")
    return player

def straight_d(dealer_motihuda):
    #　ストレートしているかどうか (p_straight_flush_kaunnto==4 の時はしている)
    d_straight_flush_kaunnto=0
    for i in range(4):
        if dealer_motihuda[i]+1 == dealer_motihuda[i+1]:
            d_straight_flush_kaunnto+=1
    if dealer_motihuda==[2,3,4,5,14]:
        d_straight_flush_kaunnto=4
    return d_straight_flush_kaunnto

def suit_d(dealer_zokusei):
    #　スートが一種類かどうか (suit==True の時はしている)
    d_suit=all(val == dealer_zokusei[0] for val in dealer_zokusei)
    return d_suit

def four_cards_d(dealer_motihuda):
    #　フォーカードかどうか (four_cards==4 の時はしている)
    d_four_cards = dealer_motihuda.count(dealer_motihuda[0])
    d_four_cards_2 = dealer_motihuda.count(dealer_motihuda[4])
    if d_four_cards<=d_four_cards_2:
        d_four_cards=d_four_cards_2
    return d_four_cards

def full_house_d(dealer_motihuda):
    #　フルハウスしているかどうか (full_house==5 の時はしている)
    d_full_house_1=dealer_motihuda.count(dealer_motihuda[0])
    d_full_house_2=dealer_motihuda.count(dealer_motihuda[4])
    d_full_house=d_full_house_1+d_full_house_2
    return d_full_house

def three_card_d(dealer_motihuda):
    #　スリーカードしているかどうか (three_card==3 の時はしている)
    d_three_card=[]
    d_three_card.append(dealer_motihuda.count(dealer_motihuda[0]))
    d_three_card.append(dealer_motihuda.count(dealer_motihuda[2]))
    d_three_card.append(dealer_motihuda.count(dealer_motihuda[4]))
    d_three_card=max(d_three_card)
    return d_three_card

def pair_d(dealer_motihuda):
    #　何ペアになっているか (p_pair　で見れる)
    d_pair=[]
    d_pair.append(dealer_motihuda.count(dealer_motihuda[0]))
    d_pair.append(dealer_motihuda.count(dealer_motihuda[2]))
    d_pair.append(dealer_motihuda.count(dealer_motihuda[4]))
    d_pair=d_pair.count(2)
    return d_pair

def yakugime_d(dealer_motihuda,d_straight_flush_kaunnto,d_suit,d_four_cards,d_full_house,d_three_card,d_pair):
    #　ディーラーの役を出す
    print("ディーラー : ",end="")
    dealer=0
    if d_straight_flush_kaunnto==4 and d_suit==True and dealer_motihuda[0]==10:
        print("ロイヤルストレートフラッシュ!!")
        dealer=9
    elif d_straight_flush_kaunnto==4 and d_suit==True:
        print("ストレートフラッシュ")
        dealer=8
    elif d_four_cards==4:
        print("フォーカード")
        dealer=7
    elif d_full_house==5:
        print("フルハウス")
        dealer=6
    elif d_suit==True:
        print("フラッシュ")
        dealer=5
    elif d_suit==True:
        print("ストレート")
        dealer=4
    elif d_three_card==3:
        print("スリーカード")
        dealer=3
    elif d_pair==2:
        print("ツーペア")
        dealer=2
    elif d_pair==1:
        print("ワンペア")
        dealer=1
    elif d_pair==0:
        print("ノーハンド")
        dealer=0
    else:
        print("error")
    return dealer

def syouhai(player,dealer,player_motihuda,dealer_motihuda):
    #　勝敗を決める
    if player>dealer:
        print("プレイヤーの勝利")
        return 1
    elif player<dealer:
        print("ディーラーの勝利")
        return 2
    elif player==dealer:
        print("同じ役")
        if player==9:  # ロイヤルストレートフラッシュ
            print("同点")
            return 3
        elif player==8: #  ストレートフラッシュ
            if player_motihuda[1]>dealer_motihuda[1]:
                print("プレイヤーの勝利")
                return 1
            elif player_motihuda[1]<dealer_motihuda[1]:
                print("ディーラーの勝利")
                return 2
            elif player_motihuda[1]==dealer_motihuda[1]:
                    print("同点")
                    return 3
        elif player==7:  # フォーカード
            if player_motihuda[0]>dealer_motihuda[0]:
                print("プレイヤーの勝利")
                return 1
            elif player_motihuda[0]<dealer_motihuda[0]:
                print("ディーラーの勝利")
                return 2
            elif player_motihuda[0]==dealer_motihuda[0]:
                print("同点")
                return 3
        elif player==6:  # フルハウス
            if player_motihuda.count(player_motihuda[0])==3:
                pl_pair=player_motihuda[0]
            elif player_motihuda.count(player_motihuda[3])==3:
                pl_pair=player_motihuda[3]

            if dealer_motihuda.count(dealer_motihuda[0])==3:
                de_pair=dealer_motihuda[0]
            elif dealer_motihuda.count(dealer_motihuda[3])==3:
                de_pair=dealer_motihuda[3]
            if pl_pair>de_pair:
                print("プレイヤーの勝利")
                return 1
            elif pl_pair<de_pair:
                print("ディーラーの勝利")
                return 2
            elif pl_pair==de_pair:
                    print("同点")
                    return 3
        elif player==5:  # フラッシュ
            if max(player_motihuda)>max(dealer_motihuda):
                print("プレイヤーの勝利")
                return 1
            elif max(player_motihuda)<max(dealer_motihuda):
                print("ディーラーの勝利")
                return 2
            elif max(player_motihuda)==max(dealer_motihuda):
                print("同点")
                return 3
        elif player==4:  # ストレート
            if player_motihuda[1]>dealer_motihuda[1]:
                print("プレイヤーの勝利")
                return 1
            elif player_motihuda[1]<dealer_motihuda[1]:
                print("ディーラーの勝利")
                return 2
            elif player_motihuda[1]==dealer_motihuda[1]:
                    print("同点")
                    return 3
        elif player==3:  # スリーカード
            if player_motihuda.count(player_motihuda[0])==3:
                pl_pair=player_motihuda[0]
            elif player_motihuda.count(player_motihuda[3])==3:
                pl_pair=player_motihuda[3]
            if dealer_motihuda.count(dealer_motihuda[0])==3:
                de_pair=dealer_motihuda[0]
            elif dealer_motihuda.count(dealer_motihuda[3])==3:
                de_pair=dealer_motihuda[3]
            if pl_pair>de_pair:
                print("プレイヤーの勝利")
                return 1
            elif pl_pair<de_pair:
                print("ディーラーの勝利")
                return 2
            elif pl_pair==de_pair:
                    print("同点")
                    return 3
        elif player==2:  # ツーペア
                pl_pair_list=[]
                if player_motihuda.count(player_motihuda[0])==2:
                    pl_pair_list.append(player_motihuda[0])
                elif player_motihuda.count(player_motihuda[2])==2:
                    pl_pair_list.append(player_motihuda[2])
                elif player_motihuda.count(player_motihuda[4])==2:
                    pl_pair_list.append(player_motihuda[4])
                de_pair_list=[]
                if dealer_motihuda.count(dealer_motihuda[0])==2:
                    de_pair_list.append(dealer_motihuda[0])
                elif dealer_motihuda.count(dealer_motihuda[2])==2:
                    de_pair_list.append(dealer_motihuda[2])
                elif dealer_motihuda.count(dealer_motihuda[4])==2:
                    de_pair_list.append(dealer_motihuda[4])
                if max(pl_pair_list)>max(de_pair_list):
                    print("プレイヤーの勝利")
                    return 1
                elif max(pl_pair_list)<max(de_pair_list):
                    print("ディーラーの勝利")
                    return 2
                elif max(pl_pair_list)==max(de_pair_list):
                    print("同点")
                    return 3
        elif player==1:  # ワンペア
            if player_motihuda.count(player_motihuda[0])==2:
                pl_pair=player_motihuda[0]
            elif player_motihuda.count(player_motihuda[2])==2:
                pl_pair=player_motihuda[2]
            elif player_motihuda.count(player_motihuda[4])==2:
                pl_pair=player_motihuda[4]
            if dealer_motihuda.count(dealer_motihuda[0])==2:
                de_pair=dealer_motihuda[0]
            elif dealer_motihuda.count(dealer_motihuda[2])==2:
                de_pair=dealer_motihuda[2]
            elif dealer_motihuda.count(dealer_motihuda[4])==2:
                de_pair=dealer_motihuda[4]
            if pl_pair>de_pair:
                print("プレイヤーの勝利")
                return 1
            elif pl_pair<de_pair:
                print("ディーラーの勝利")
                return 2
            elif pl_pair==de_pair:
                print("同点")
                return 3
        elif player==0:  # ノーハンド
            print("同点")
            return 3
def poker():
    syozi_poinnto=10000
    while True:  # ゲームを続けるときのループ
        while True:  # 所持ポイントより多いいポイントを賭けようとしたときのループ
            kakekinn=input("何ポイント賭けますか :現在のポイント:"+str(syozi_poinnto)+" : ")
            if kakekinn=="all":
                kakekinn=syozi_poinnto
            elif kakekinn.isdigit()==True:
                kakekinn=int(kakekinn)
            elif type(kakekinn)==str:
                kakekinn=100
            if kakekinn>syozi_poinnto:
                print("所持ポイント以上は賭けられません")
            else:
                break
        input("それではゲームスタート!(enter)")
        # プレイヤーの処理↓
        trump=trump_shuffle()
        trump_suuzi=trump_wariate(trump)
        trump_zokusei=trump__zokusei(trump)
        hyouzi(trump_zokusei,trump_suuzi)
        player_motihuda,player_zokusei=p_list(trump_suuzi,trump_zokusei)
        player_motihuda,player_zokusei=irekae(player_motihuda,player_zokusei,trump_suuzi,trump_zokusei)
        dealer_motihuda,dealer_zokusei=d_list(trump_suuzi,trump_zokusei)
        p_straight_flush_kaunnto=straight_p(player_motihuda)
        p_suit=suit_p(player_zokusei)
        p_four_cards=four_cards_p(player_motihuda)
        p_full_house=full_house_p(player_motihuda)
        p_three_card=three_card_p(player_motihuda)
        p_pair=pair_p(player_motihuda)
        player=yakugime_p(player_motihuda,p_straight_flush_kaunnto,p_suit,p_four_cards,p_full_house,p_three_card,p_pair)
        # ディーラーの処理↓
        d_straight_flush_kaunnto=straight_p(dealer_motihuda)
        d_suit=suit_p(dealer_zokusei)
        d_four_cards=four_cards_p(dealer_motihuda)
        d_full_house=full_house_p(dealer_motihuda)
        d_three_card=three_card_p(dealer_motihuda)
        d_pair=pair_p(dealer_motihuda)
        dealer=yakugime_d(dealer_motihuda,d_straight_flush_kaunnto,d_suit,d_four_cards,d_full_house,d_three_card,d_pair)
        kekka=syouhai(player,dealer,player_motihuda,dealer_motihuda)
        # 賭けの処理↓
        if kekka==1:
            print("おめでとう")
            syozi_poinnto+=kakekinn
            print("あなたの所持ポイントは :"+str(syozi_poinnto)+"ポイントです。")
        elif kekka==2:
            print("残念")
            syozi_poinnto-=kakekinn
            print("あなたの所持ポイントは :"+str(syozi_poinnto)+"ポイントです。")
        elif kekka==3:
            print("引き分け")
        if syozi_poinnto==0:
            print("ポイントが0になりました")
            print("ゲームオーバー")
            break
        mada_yaruka=input("まだ続けますか？(y/n)")
        if mada_yaruka=="n":
            break

poker()