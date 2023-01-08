import random

class Arrays():

    @staticmethod
    def create_array(number_of_array_elements,value_of_array_elements):
        arr=[]
        for i in range(number_of_array_elements):
            arr.append(value_of_array_elements)
        return arr
    
    @staticmethod
    def create_array_with_random(number_of_array_elements,elem_from,elem_to):
        arr=[]
        for i in range(number_of_array_elements):
            arr.append(random.randint(elem_from,elem_to))
        return arr

    @staticmethod
    def array(elem,value_from,value_to):
        arr=[]
        for i in range(elem+1):
            for x in range(value_from,value_to):
                arr.append(x)
        return arr


print(Arrays.create_array(5,3))
print(Arrays.array(5,1,5))

        