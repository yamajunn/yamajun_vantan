from colorama import init
from colorama import Fore, Back
import time
import os
import random
import readchar
from timeout_decorator import timeout, TimeoutError
import copy

def input_count(time_, r_l, block_input, count):  # --------------------
    if block_input == 0:
        kabe_count_a = 4
        kabe_count_d = 4
    elif block_input == 1:
        kabe_count_a = 4
        kabe_count_d = 3
    elif block_input == 2:
        kabe_count_a = 4
        kabe_count_d = 3
    elif block_input == 3:
        kabe_count_a = 4
        kabe_count_d = 3
    elif block_input == 4:
        kabe_count_a = 4
        kabe_count_d = 3
    elif block_input == 5:
        kabe_count_a = 4
        kabe_count_d = 3
    elif block_input == 6:
        kabe_count_a = 3
        kabe_count_d = 3
    
    TIMEOUT_SEC = time_

    @timeout(TIMEOUT_SEC)
    def input_with_timeout():
        return readchar.readchar()

    if __name__ == '__main__':
        try:

            input_str = input_with_timeout()

            if input_str == 'a' and r_l > -kabe_count_a:
                r_l -= 1
            elif input_str == 'd' and r_l < kabe_count_d:
                r_l += 1
            elif input_str == 's':
                count = 18

        except TimeoutError:
            pass
    return (r_l, count)  # --------------------

count = 0
r_l = 0
block_input = random.randint(0,6)
list_base = [['+' for i in range(10)] for i in range(20)]
time_sta = time.time()

while True:  # --------------------
    # block_input = 0
    r_l, count = input_count(0.3, r_l, block_input, count)

    list = copy.deepcopy(list_base)
    
    if block_input == 0:  # □
        list[count][4+r_l] = '■'
        list[count][5+r_l] = '■'
        list[count+1][4+r_l] = '■'
        list[count+1][5+r_l] = '■'
    elif block_input == 1:  # 凸
        list[count][5+r_l] = '■'
        list[count+1][4+r_l] = '■'
        list[count+1][5+r_l] = '■'
        list[count+1][6+r_l] = '■'
    elif block_input == 2:  # ≥
        list[count][4+r_l] = '■'
        list[count][5+r_l] = '■'
        list[count+1][5+r_l] = '■'
        list[count+1][6+r_l] = '■'
    elif block_input == 3:  # ≤
        list[count][6+r_l] = '■'
        list[count][5+r_l] = '■'
        list[count+1][5+r_l] = '■'
        list[count+1][4+r_l] = '■'
    elif block_input == 4:  # _,
        list[count][6+r_l] = '■'
        list[count+1][4+r_l] = '■'
        list[count+1][5+r_l] = '■'
        list[count+1][6+r_l] = '■'
    elif block_input == 5:  # ,_
        list[count][4+r_l] = '■'
        list[count+1][4+r_l] = '■'
        list[count+1][5+r_l] = '■'
        list[count+1][6+r_l] = '■'
    elif block_input == 6:  # _
        list[count+1][3+r_l] = '■'
        list[count+1][4+r_l] = '■'
        list[count+1][5+r_l] = '■'
        list[count+1][6+r_l] = '■'
    
    os.system('clear')
    print(Fore.BLACK + '□ '*22)
    for i in range(20):
        print(Fore.BLACK + '□',end="")
        if i >= 4:
            print(Fore.BLACK + ' □'*5 + ' ' + ' '.join(list[i]) + ' □' + ' '*8,end="")
        else:
            print(Fore.BLACK + ' '*9 + '□ ' + ' '.join(list[i]) + ' □' + ' '*8,end="")
        print(Fore.BLACK + ' □')
    print(Fore.BLACK + '□ '*22)

    time_end = time.time()

    if time_sta - time_end <= -0.1:
        if count < 18:
            if block_input == 0 and list[count+2][4+r_l] == '+' and list[count+2][5+r_l] == '+':
                count += 1
            elif block_input == 1 and list[count+2][4+r_l] == '+' and list[count+2][5+r_l] == '+' and list[count+2][6+r_l] == '+':
                count += 1
            elif block_input == 2 and list[count+2][5+r_l] == '+' and list[count+2][6+r_l] == '+':
                count += 1
            elif block_input == 3 and list[count+2][5+r_l] == '+' and list[count+2][4+r_l] == '+':
                count += 1
            elif block_input == 4 and list[count+2][4+r_l] == '+' and list[count+2][5+r_l] == '+' and list[count+2][6+r_l] == '+':
                count += 1
            elif block_input == 5 and list[count+2][4+r_l] == '+' and list[count+2][5+r_l] == '+' and list[count+2][6+r_l] == '+':
                count += 1
            elif block_input == 6 and list[count+2][3+r_l] == '+' and list[count+2][4+r_l] == '+' and list[count+2][5+r_l] == '+' and list[count+2][6+r_l] == '+':
                count += 1
            else:
                count = 0
                r_l = 0
                list_base = copy.deepcopy(list)
                block_input = random.randint(0,6)
                for i in range(20):
                    if not '+' in list[i]:
                        list.pop(i)
                        list.insert(0, ['+' for i in range(10)])
                        list_base = copy.deepcopy(list)
        else:
            count = 0
            r_l = 0
            list_base = copy.deepcopy(list)
            block_input = random.randint(0,6)
            for i in range(20):
                if not '+' in list[i]:
                    list.pop(i)
                    list.insert(0, ['+' for i in range(10)])
                    list_base = copy.deepcopy(list)
            
        time_sta = time.time()
    # time.sleep(1)  # --------------------