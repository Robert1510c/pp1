array1=[4,36,12,28,9,44,5]
array2=[5,1,36]
array3=[]
array4=[]
for i in range(0,len(array1)):
    for j in range(0,len(array2)):
        if array1[i]!=array2[j]:
            array3.append(array1[i])

for i in array3:
    if array3.count(i)>2:
        array4.append(i)
    print(array4)

array5=[]
for a in array4:
    if a not in array5:
        array5.append(a)

print(array5)
