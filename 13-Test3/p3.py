import re

def f1(t):
    liczby=re.findall(r'\d+',t)
    imiona=re.findall(r'[A-Z][a-z]+',t)
    dictionary=dict(zip(imiona,liczby))
    return dictionary


def f2(d):
    sum=0
    for key,value in d.items():
        value=int(value)
        sum+=value
    return sum

    
print(f1("Mark is 24 and Ann is 27")) 
print(f2(f1("Mark is 24 and Ann is 27")))