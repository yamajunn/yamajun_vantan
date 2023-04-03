print('print(', end='')
for i in range(50):
    print('*gamen_list['+str(200*i+1)+':'+str(200*i+200)+']+"\\n"+', end='')
print('"\\033[200A",end="")')