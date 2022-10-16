czas=float(input("Podaj liczbę godzin: "))
stawka=float(input("Podaj stawkę godzinową: "))

Wynagrodzenie=(czas*stawka)

if czas<=40:
    Wynagrodzenie=(czas*stawka)
else:
    Wynagrodzenie=(40*stawka + (czas-40)*stawka*1.5)


print(Wynagrodzenie)