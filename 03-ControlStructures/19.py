x=float(input("Podaj wiek psa: "))

if x<=2:
    print(f"The dog's age in dog’s years is {x*10.5} ")
else:
    print(f"The dog's age in dog’s years is {2*10.5+(x-2)*4}")