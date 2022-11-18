array=[1,2,3,4,5,6,7,8]
sum_even=0
sum_odd=0
i=0
while i<len(array):
    if array[i]%2==0:
        sum_even+=array[i]
    else:
        sum_odd+=array[i]
    i+=1

        

print(sum_even)
print(sum_odd)