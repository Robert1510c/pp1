def power(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n>1:
        return x * x**(n-1)

print(power(5,3))