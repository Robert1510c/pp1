import csv

with open('test.csv','r',encoding='utf-8', newline='') as file:
    tekst=csv.DictReader(file)
    for i in tekst:
        print(type(i))
        print(i['name'],i['surname'],i['salary'])