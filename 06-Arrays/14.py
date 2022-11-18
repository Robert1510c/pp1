array=[
    [True,False],
    [True,True],
    [False,False]
]
for i in array:
    for j in i:
        if j==True:
            j=not j
            print(j)
        elif j==False:
            j=not j
            print(j)

