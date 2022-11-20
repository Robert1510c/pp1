x=float(input("Podaj liczbe: "))
array=[1,2,3,9,5,56,32,102,2137]

for i in range(0,len(array)):
    if array[i]>x:
        print(array[i])