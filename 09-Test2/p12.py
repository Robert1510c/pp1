a1=[23,7,16,34,44]
a2=[1,18,79,20,6,111,74]

x1=[]
x2=[]

for i in range(0,len(a1)):
    if a1[i]>=10 and a1[i]<=99:
        x1.append(a1[i])

for n in range(0,len(a2)):  
    if a2[n]>=10 and a2[n]<=99: 
        x2.append(a2[n])

if len(x1)==len(x2):
    print(True)
else:
    print(False)        