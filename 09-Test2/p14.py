dict={
    'arr1': [2,6,5],
    'arr2': [7,1],
    'arr3': [2,9,8,1]
}
arr=[]
for x,y in dict.items():
    for i in range(0,len(y)):
        if y[i]>=5 and y[i]<=10:
            arr.append(y[i])
arr.sort()
print(arr)
sum=0
for n in range(0,len(arr)):
    sum+=arr[n]
print(sum)