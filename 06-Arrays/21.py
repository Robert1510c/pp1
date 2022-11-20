
def compare(arr1,arr2):
    if len(arr1)==len(arr2):
        for i in range(0,len(arr1)):
            for j in range(0,len(arr2)):
                if arr1[i]==arr2[j]:
                    return True
                else:
                    return False
    else:
        return False
    if compare==True:
        return 1
print(compare(["water","book","sky"],["water","book","sky"]))