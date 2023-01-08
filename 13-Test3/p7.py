class C():

    @staticmethod
    def m1(n):
        n=str(n)
        x=""
        for i in n:
            if int(i)%2!=0:
                pass
            else:
                x+=i
        return int(x)

    @staticmethod
    def m2(n):
        n=str(n)
        for i in range(1,len(n)):
            if n[i]<n[i-1]:
                return False
            
        return True

    @staticmethod
    def m3(n):
        n=str(n)
        arr=[]
        for i in range(0,10):
            arr.append(str(i))
        for i in n:
            if i in arr:
                arr.remove(i)

        arr.sort()
        x="".join(arr)
        return x




print(C.m1(4231564))
print(C.m1(79381))
print(C.m2(125579))
print(C.m2(4557879))
print(C.m3(23557))
print(C.m3(12340))