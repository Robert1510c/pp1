import random
def rand_elem(array):
    x=random.randint(0,len(array))
    y=random.randint(0,len(array))
    return array[x], array[y]

print(rand_elem([1,2,3,4,5,6,7,8,9,10,12,15,16,26,635464,324]))