array=[15,8,31,47,2,19]

sum=0
x=len(array)
print(x)
i=0
while i<=x-1:
    sum+=array[i]
    i+=1
mean=sum/(len(array))
print(sum)
print(mean)