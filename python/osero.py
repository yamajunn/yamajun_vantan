isi_list = [0 for i in range(64)]
# for i in range(8):
#     for j in range(8):
#         isi_list.append([0,i,j])


isi_list[27] = 2
isi_list[28] = 1
isi_list[35] = 1
isi_list[36] = 2

# print(isi_list)

count = 0
isi_count = 0
while True:
    num = 1
    print(f'○:{isi_list.count(1)} ●:{isi_list.count(2)}')
    print('   0 . 1 . 2 . 3 . 4 . 5 . 6 . 7 .')
    print(' +---+---+---+---+---+---+---+---+')
    print('0|',end='')
    for i in range(64):
        if isi_list[i] == 0:
            print('   ',end='')
        elif isi_list[i] == 2:
            print(' ● ',end='')
        elif isi_list[i] == 1:
            print(' ○ ',end='')
        print('|',end='')
        if num % 8 == 0:
            print()
            print(' +---+---+---+---+---+---+---+---+')
            if num == 64:
                break
            print(f'{i//8+1}|',end='')
        num += 1
    
    select_position = list(map(int,input('座標>>').split(',')))
    select_position.append(isi_count%2+1)
    if select_position[2] == 1:
        select_position.append(2)
        print(' ● の番')
    else:
        select_position.append(1)
        print(' ○ の番')

    isi_list [select_position[1]*8+select_position[0]] = select_position[2]
    print(isi_list)

    for i in range(64):  # 左
        if isi_list[i] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - (i+1)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] - j-1] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] - 1] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - (i+1)] == 0:
            break

    for i in range(select_position[0]):  # 左
        if isi_list[select_position[1]*8+select_position[0] - 1] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - (i+1)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] - j-1] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] - 1] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - (i+1)] == 0:
            break

    for i in range(7 - select_position[0]):  # 右
        if isi_list[select_position[1]*8+select_position[0] + 1] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + (i+1)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] + j+1] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] + 1] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + (i+1)] == 0:
            break
    
    for i in range(select_position[1]):  # 上
        if isi_list[select_position[1]*8+select_position[0] - 8] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - ((i+1)*8)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] - ((j+1)*8)] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] - 8] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - ((i+1)*8)] == 0:
            break
    
    for i in range(7 - select_position[1]):  # 下
        if isi_list[select_position[1]*8+select_position[0] + 8] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + ((i+1)*8)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] +((j+1)*8)] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] + 8] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + ((i+1)*8)] == 0:
            break
    
    for i in range(min(select_position[0],select_position[1])):  # 左上
        if isi_list[select_position[1]*8+select_position[0] - 9] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - ((i+1)*9)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] - (j+1)*9] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] - 9] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - ((i+1)*9)] == 0:
            break

    for i in range(min(7 - select_position[1],select_position[0])):  # 左下
        if isi_list[select_position[1]*8+select_position[0] + 7] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + ((i+1)*7)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] + (j+1)*7] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] + 7] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + ((i+1)*7)] == 0:
            break
    
    for i in range(min(7 - select_position[0],select_position[1])):  # 右上
        if isi_list[select_position[1]*8+select_position[0] - 7] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - ((i+1)*7)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] - (j+1)*7] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] - 7] == select_position[3] and isi_list[select_position[1]*8+select_position[0] - ((i+1)*7)] == 0:
            break
    
    for i in range(min(7 - select_position[1],7 - select_position[0])):  # 右下
        if isi_list[select_position[1]*8+select_position[0] + 9] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + ((i+1)*9)] == select_position[2]:
            for j in range(i):
                isi_list[select_position[1]*8+select_position[0] + (j+1)*9] = select_position[2]
            break
        if isi_list[select_position[1]*8+select_position[0] + 9] == select_position[3] and isi_list[select_position[1]*8+select_position[0] + ((i+1)*9)] == 0:
            break
    # def uragaesi(for_num, isi_list, list_num1, select_position, list_num2, list_num3, j):
    #     for i in range(for_num):
    #         if isi_list[list_num1] == select_position[3] and isi_list[list_num2] == select_position[2]:
    #             for l in range(i):
    #                 j = l
    #                 isi_list[list_num3] = select_position[2]
    #                 return isi_list
    #             break
    #         if isi_list[list_num1] == select_position[3] and isi_list[list_num2] == 0:
    #             break
    # isi_list = uragaesi(select_position[0], isi_list, select_position[1]*8+select_position[0] - 1, select_position, select_position[1]*8+select_position[0] - (i+1), select_position[1]*8+select_position[0] - j-1)
    # isi_list = uragaesi(7 - select_position[0], isi_list, select_position[1]*8+select_position[0] + 1, select_position, select_position[1]*8+select_position[0] + (i+1), select_position[1]*8+select_position[0] + j+1)
    # isi_list = uragaesi(select_position[1], isi_list, select_position[1]*8+select_position[0] - 8, select_position, select_position[1]*8+select_position[0] - ((i+1)*8), select_position[1]*8+select_position[0] - ((j+1)*8))
    # isi_list = uragaesi(7 - select_position[1], isi_list, select_position[1]*8+select_position[0] + 8, select_position, select_position[1]*8+select_position[0] + ((i+1)*8), select_position[1]*8+select_position[0] +((j+1)*8))
    # isi_list = uragaesi(min(select_position[0],select_position[1]), isi_list, select_position[1]*8+select_position[0] - 9, select_position, select_position[1]*8+select_position[0] - ((i+1)*9), select_position[1]*8+select_position[0] - (j+1)*9)
    # isi_list = uragaesi(min(7 - select_position[1],select_position[0]), isi_list, min(7 - select_position[1],select_position[0]), select_position, select_position[1]*8+select_position[0] + ((i+1)*7), select_position[1]*8+select_position[0] + (j+1)*7)
    # isi_list = uragaesi(min(7 - select_position[0],select_position[1]), isi_list, select_position[1]*8+select_position[0] - 7, select_position, select_position[1]*8+select_position[0] - ((i+1)*7), select_position[1]*8+select_position[0] - (j+1)*7)
    # isi_list = uragaesi(min(7 - select_position[1],7 - select_position[0]), isi_list, select_position[1]*8+select_position[0] + 9, select_position, select_position[1]*8+select_position[0] + ((i+1)*9), select_position[1]*8+select_position[0] + (j+1)*9)

    if count == 64:
        break
    count += 1
    isi_count += 1
    # os.system('clear')

