def bubblesort(array):
    c=0
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                c=array[i]
                array[i]=array[j]
                array[j]=c
    return array

print(bubblesort([2,1,5,4,89,3]))
