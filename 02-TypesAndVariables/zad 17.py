cm=float(input("Wprowadź wzrost: "))
feet=(cm//30.48)
reszta=(round(cm-feet*30.48,2))
inches=(round(reszta/2.54,0))
print(feet, reszta, inches)
print(f"Wzrost w stopach + calach: {feet}'{inches}")