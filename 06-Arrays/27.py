array=[5,1,9,6,1]
c=0
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            c=array[i]
            array[i]=array[j]
            array[j]=c

print(array[-1]-array[0])