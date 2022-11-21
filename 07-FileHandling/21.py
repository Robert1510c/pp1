file=open('power.txt','a',encoding='utf-8')
for i in range(1,11):
    file.write(f'{i, i**2, i**3}\n')
        

file.close()