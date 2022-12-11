import csv
import re

with open('test.csv','r',encoding='utf-8', newline='') as file:
    count=-1
    tekst=csv.reader(file, delimiter=' ', quotechar='|')
    for row in tekst:
        x=(', '.join(row))
        mails=re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',x,re.IGNORECASE)
        print(mails)
        count+=1
        
    print(count)
        
