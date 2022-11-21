import random
file=open('random.txt','w',encoding='utf-8')
for i in range(1,51):
    x=str(random.randint(100,999))
    file.write(x)
    file.write('\n')