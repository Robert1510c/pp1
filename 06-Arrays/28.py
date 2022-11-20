c=0
def median(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                c=array[i]
                array[i]=array[j]
                array[j]=c
    return array[len(array)//2]

print(median([6,8,3,1,0,5,7]))