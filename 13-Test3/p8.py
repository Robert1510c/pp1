class C():
    def __init__(self,dictionary):
        self.dict=dictionary

    def m(self,n):
        arr=[]
        for key,value in self.dict.items():
            sum=0
            for i in value:
                sum+=i
            if sum/len(value)>=n:
                arr.append(key)
        arr.sort()
        studenci=','.join(arr)
        print(studenci)



s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
s.m(4)
s.m(3)
s.m(5)
