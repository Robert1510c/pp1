def f(arr):
    if any(not isinstance(row,list) for row in arr):
        return False

    if any(len(row) != len(arr[0]) for row in arr):
        return False


    if len(arr) != len(arr[0]):
        return False

    for i in range(len(arr)):
        if arr[i][0] != i+1:
            return False
    
    for j in range(len(arr[0])):
        if arr[0][j] != j+1:
            return False

    x=len(arr)
    for i in range(x):
        for j in range(len(arr[i])):
            if(arr[i][j]==(i+1)*(j+1))==False:
                return False
            else:
                return True

print(f(([[1,2,3],[2,4,6],[3,6,9]])))
