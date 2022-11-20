array1=[2,3,2,5,8,1,9,8]
array2=[]

for i in array1:
    if array1.count(i)<2:
        array2.append(i)
print(array2)