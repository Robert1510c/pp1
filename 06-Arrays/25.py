def occurs(number, array):
    for i in range(0,len(array)):
        if array[i]==number:
            return True
        

print(occurs(23,[15,38,7,23,14]))