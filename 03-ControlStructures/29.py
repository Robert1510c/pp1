x=1
sum=0
quantity=0
mean=0
count=0

while x !=0:
    x=int(input("Enter number: "))
    sum+=x
    count+=1

print("Suma wynosi: ", sum, "Średnia wynosi: ", sum/(count-1), "Ilość liczb: ", count-1)