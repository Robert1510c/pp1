a=[13,7,4,16,3,12,8,88]
a2=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        if a[i]>8:
            x=a[i]
            a2.append(x)

print(len(a2))
