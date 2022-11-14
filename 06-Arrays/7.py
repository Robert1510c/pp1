array=[1,2,3,4,5]
array[0]=array[0]-1
array[-1]=array[-1]+4
x=len(array)-3
array[x]=array[x]*2
print(array)
for i in range(0,len(array)):
    array[i]=array[i]+3
print(array)