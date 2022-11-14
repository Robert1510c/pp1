arr=[-15,8,-31,47,-2,19]
x=len(arr)
max=arr[0]
min=arr[0]
for i in range(0,x):
    if arr[i]>max:
        max=arr[i]
for i in range(0,x):
    if arr[i]<min:
        min=arr[i]
print(max)
print(min)
