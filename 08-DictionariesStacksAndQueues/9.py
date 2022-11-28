from datetime import date


phone = {
    'Model': 'S10',
    'Release date': 2019,
    'Previous owners': ['Jhon', 'Zbigniew'],
    'Waterproof': True,
    'Numbers of previous owners': {'Jhon': 313213214, 'Zbigniew': 97185126},
    }

for x,y in phone.items():
    print(f'{x} : {y}')