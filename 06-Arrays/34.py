array1=[1,2,3]
array2=[1,5,6,7,2,31]
array3=[]
for i in range(0,len(array1)):
    for j in range(0,len(array2)):
        if array1[i]==array2[j]:
            array3.append(array1[i])

if array3==array1:
    print(True)
else:
    print(False)