import re

with open('costam.txt','r',encoding='utf-8') as file:
    text=file.readlines()
    sum=0
    sum2=0
    for i in text:
        x=re.findall(r'c',i,re.IGNORECASE)
        print(x)
        if len(x)>0:
            sum2+=1
        for n in range(1,1000):
            if x==['c']*n:
                sum+=1
print(sum)
print(sum2)