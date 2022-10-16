import math
a=input("Podaj wartość między 0.0 a 1.0: ")
try:
    a=float(a)
    if a<0.0 or a>1.0:
        print("Niepoprawna wartość")
    else:
        if round(a,1)==0.9:
            print("5,0")
        elif round(a,1)==0.8:
            print("4,5")
        elif round(a,1)==0.7:
            print("4.0")
        elif round(a,1)==0.6:
            print("3,5")
        elif round(a,1)==0.5:
            print("3,0")
        else:
            print("2,0")
except:
    print("Niepoprawna wartość")