import json 

def f(age,course,avarage):
    ile=0
    with open('test.json','r',encoding='utf-8') as file:
        text= json.load(file)
        for i in text:
            if i['age']>=age:
                for j in i['studies']['courses']:
                    if j['name']==course:
                        if sum(j['grades'])/len(j['grades'])>=avarage:
                            ile+=1
    return ile

print(f(21, "statistics", 4))