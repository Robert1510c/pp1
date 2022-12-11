import csv 
import re

with open('test.csv','r',encoding='utf-8',newline='') as file:
    tekst=csv.reader(file, delimiter=' ',quotechar='|')
    for i in tekst:
        for j in i:
            men=re.findall(r'Mal',j)
    print(men)
    