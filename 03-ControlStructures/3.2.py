czas=input("Podaj liczbę godzin: ")
stawka=input("Podaj stawkę godzinową: ")
try:
    czas=float(czas)
    stawka=float(stawka)
    if czas<=40:
        Wynagrodzenie=(czas*stawka)
    else:
        Wynagrodzenie=(40*stawka + (czas-40)*stawka*1.5)
except:
    quit()
    print("Błąd, podaj wartość numeryczną")
    

print(Wynagrodzenie)