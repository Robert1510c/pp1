a=[1,2,5]
b=int(input("Podaj kwotę: "))
c=0
x=2
while(x>=0):
    c=b//a[x]
    b-=(c*a[x])
    if(c>0):
        print(f'{c} razy {a[x]}PLN')
    x-=1