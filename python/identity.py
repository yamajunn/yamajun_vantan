# scores1 = [80,40,50]
# scores2 = [80,40,50]

# scores1 = scores2
# scores1[0] = 90
# print(scores1[0])
# print(scores2[0])

# def add_suffix(names):
#     for i in range(len(names)):
#         names[i] = names[i] + "さん"
#     return names

# before_names = ["松田","浅木","工藤"]
# after_names = add_suffix(before_names.copy())
# print(f"さん付け後:{after_names}")
# print(f"さん付け前:{before_names}")

# name = "松田"

# namea = "スーパー"+name
# print(name)

# def welcome(u):
#     print(f"ようこそ{u['name']}さん")
#     u["age"] = u["age"] + 1
#     print(f"あなたは来年{u['age']}だから大吉です！")

# username = input("名前を入力してください>>")
# userage = int(input("年齢を入力してください>>"))
# user = {"name":username,"age":userage}
# welcome(user.copy())
# print(f"{user['age']}歳の{user['name']}さん、またプレイしてね")