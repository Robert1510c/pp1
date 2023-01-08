dictionary={"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]}

for key,value in dictionary.items():
    sum=0
    for i in value:
        sum+=i
    if sum/len(value)>=4:
        print(key)
