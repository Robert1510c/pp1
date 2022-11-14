array=[2,3,7,5,4]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1])
print(array[-2])
print(array[0]+array[-1])
x=len(array)//2
print(array[x])
for i in array:
    print(i, end=" ")
print()
for i in array[0:x+1]:
    print(i, end=" ")



