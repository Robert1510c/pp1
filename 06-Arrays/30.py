def minmax(array):
    c=0
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                c=array[i]
                array[i]=array[j]
                array[j]=c
    return array[0], array[-1]
print(minmax([4,2,8,4,7,9,5]))