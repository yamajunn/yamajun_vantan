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

trump=trump_shuffle()
trump_suuzi=trump_wariate(trump)
trump_zokusei=trump__zokusei(trump)
hyouzi(trump_zokusei,trump_suuzi)
player_motihuda,player_zokusei=p_list(trump_suuzi,trump_zokusei)
dealer_motihuda,dealer_zokusei=d_list(trump_suuzi,trump_zokusei)
p_straight_flush_kaunnto=straight_p(player_motihuda)
p_suit=suit_p(player_zokusei)
p_four_cards=four_cards_p(player_motihuda)
p_full_house=full_house_p(player_motihuda)
p_three_card=three_card_p(player_motihuda)
p_pair=pair_p(player_motihuda)
player=yakugime_p(player_motihuda,p_straight_flush_kaunnto,p_suit,p_four_cards,p_full_house,p_three_card,p_pair)