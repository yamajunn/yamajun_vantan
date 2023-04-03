# import random

# class Hero:
#     name = " "
#     hp = 0
#     def __init__(self,hp):
#         self.hp = hp
#     def sleep(self,hours):
#         print("="*50)
#         print(f"{self.name}は{hours}時間寝た!")
#         self.hp += hours
#         print(f"{self.name}のHPは現在{self.hp}です")
#         print("="*50)
    
#     def re_name(self,rename):
#         self.name = rename
    
#     def attack(self,target,enemy_hp):

#         def attack_damage(attacker,target,hp):
#             attack_damage = random.randint(1,20)
#             print(f"{attacker}は{target}に{attack_damage}ダメージ与えた")
#             hp -= attack_damage
#             if hp <=0:
#                 hp = 0
#             print(f"{target}のHPは{hp}です")
#             return hp

#         print(f"{target}が現れた!!")
#         input("Enter>>")

#         while True:
#             damage = random.randint(1,10)
#             print("="*50)

#             self.hp = attack_damage(target,self.name,self.hp)
#             print("="*50)
#             input("Enter>>")
#             if self.hp <= 0:
#                 print(f"{self.name}は死んだ")
#                 input("Enter>>")
#                 print("ゲームオーバー")
#                 break

#             print(f"{self.name}のHPは現在{self.hp}です")
#             print(f"{target}のHPは{enemy_hp}です")
#             print("="*50)
#             input("Enter>>")

#             attack = input("攻撃する/寝る/逃げる(1/2/3)>>")
#             print("="*50)
#             if attack == "1":
#                 enemy_hp = attack_damage(self.name,target,enemy_hp)
#                 input("Enter>>")
#                 if enemy_hp <= 0:
#                     print("="*50)
#                     print(f"{target}を倒した")
#                     print("勝利した事でHPが増えた!")
#                     self.hp += 30
#                     break
#             elif attack == "2":
#                 sleep = random.randint(1,24)
#                 print(f"{self.name}は{sleep}時間寝た")
#                 self.hp += sleep
#                 print(f"{self.name}のHPは現在{self.hp}です")
#                 print("="*50)
#             elif attack == "3":
#                 print("="*50)
#                 print(f"{self.name}は逃げた")
#                 break

# print("すっきりファンタジーXII 〜金色の理想郷")
# h2 = Hero(100)
# h2.re_name(input("name>>"))
# h2.sleep(random.randint(1,10))
# h2.attack("松田",20)
# print(f"{h2.name}のHPは現在{h2.hp}です")

class Enemy:
    name = "名前"
    hp = "HP"
    attack = "攻撃力"
    defn = "防御力"
    dex = "素早さ"
    def __init__(self,name,hp,min_attack,max_attack,defn,dex):
        self.name = name
        self.hp = hp
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.defn = defn
        self.dex = dex
    
    def talk(self):
        speak = input("何を言いますか?")
        print(f"あなた「{speak}」")
        print(f"{self.name}「ｷｼｪｪｪｪｪｪｪｪｪｪｪｪｪｪｪｪｪｪｪ!!」")

h = Enemy("悪魔",100,1,10,20,15)
h.talk()