from cmath import sqrt


a=float(input("Pierwszy bok: "))
b=float(input("Drugi bok: "))
c=float(input("Trzeci bok: "))

s=(a+b+c)/2
print(s)
A=(s*(s-a)*(s-b)*(s-c))**0.5
print(A)