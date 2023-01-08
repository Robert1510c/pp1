import re

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
arr=[]
for i in cars:
    for j in i:
        arr.append(j)
x=""
for i in arr:
    x+=i+' '
cars_in=re.findall(r'[A-Z,1-9]+\sin',x)
cars_out=re.findall(r'[A-Z,1-9]+\sout',x)

a=''
for i in cars_in:
    a+=i+' '

b=''
for i in cars_out:
    b+=i+' '


tablice_in=re.findall(r'[A-Z,1-9]{5}',a)
print(tablice_in)

tablice_out=re.findall(r'[A-Z,1-9]{5}',b)
print(tablice_out)

in_dict=dict((i,tablice_in.count(i))for i in tablice_in)
print(in_dict)

out_dict=dict((i,tablice_out.count(i))for i in tablice_out)
print(out_dict)




#print(cars_in)
#print(cars_out)