import csv

with open('test.csv','r',encoding='utf-8') as file:
    tekst=csv.DictReader(file)
    sum=0
    for i in tekst:
        if i['gender']=='Female':
            if i['salary']>'7800' and i['salary']<'8500':
                print(i['name'],i['surname'])
                sum+=1
    print(sum)