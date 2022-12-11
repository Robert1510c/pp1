import json

with open('student.json','w',encoding='utf-8') as file:
    dict= {
        'age':18,
        'name':'Zbigniew',
        'kierunek': 'Informatyka',
        'przedmioty': ['Programowanie','Teoria','Architektura'],
        'Oceny': {
            'Programowanie': [3,4,5],
            'Teoria': [1,3,5],
            'Architektura': [4,4,4]
        }
    }
    x=json.dumps(dict, indent=4)
    file.write(x)