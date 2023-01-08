def f(d):
    arr=[]
    for i in d:
        if i[1]=="in":
            arr.append(i[0])
        else:
            arr.remove(i[0])
        
    arr.sort()
    return arr

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars)) 
