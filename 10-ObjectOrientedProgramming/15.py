import random

class Thermometer():
    def __init__(self):
        self.temperature=0

    def zmierz(self):
        self.temperature=round(random.uniform(34,42),1)

    def temp(self):
        if self.temperature<37:
            print(f"Temperatura równa: {self.temperature}C")
        elif self.temperature>=37 and self.temperature<41:
            print(f'Temperatura równa: {self.temperature}C (fever)')
        else:
            print(f'CRITICAL TEMPERATURE: {self.temperature}C')

term1=Thermometer()
term1.zmierz()
term1.temp()
