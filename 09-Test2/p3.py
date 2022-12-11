
def f(array2D):
    array2=[]
    x=0
    for i in range(0,len(array2D)):
        for j in range(0,len(array2D[i])):
            array2.append(array2D[i][j])
    z=0  
    array3=[]
    for a in range(0,len(array2D[i])):
        z=array2[a]+array2[a+len(array2D[i])]+array2[a+(len(array2D[i])*2)]
        array3.append(z)   
    return array3
        
print(f([[3,6,2,7,8],[9,5,4,0,6],[2,8,0,9,3]]))


