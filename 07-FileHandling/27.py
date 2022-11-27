import re

with open('grades.txt','r',encoding='utf-8') as file:
    file_context=file.read()
    sum=0
    grades=re.findall("\d+\.\d+",file_context)
    for i in grades:
        print(i)
        i=float(i)
        sum+=i

mean=sum/len(grades)
print(mean)
print(sum)