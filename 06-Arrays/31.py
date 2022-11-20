array=[1,2,3,4,5,6,7,8,9,10]
c=0
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]%2!=0:
            c=array[i]
            array[i]=array[j]
            array[j]=c
print(array)