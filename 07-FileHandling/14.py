plik=str(input("Podaj plik: "))

with open(plik,'r') as f:
    text=len(f.readlines())

print(text)