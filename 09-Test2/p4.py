
def f(dictionary,x,y):
    sum=0
    for key,value in dictionary.items():
        for i in range(0,len(value)):
            if value[i]>=x and value[i]<=y:
                sum+=value[i]
    return sum

print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))