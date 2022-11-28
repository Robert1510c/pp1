import json

dict={
    'Film name': 'Harry Potter',
    'Release date': 2003,
    'Actors': ['Daniel Radcliff','Emma Watson', "Rupert Grint"],
    'Main characters': {'main villain': 'Voldemort', 'main character':'Potter'},
    'Autor': "Ktos"
}
with open('favourite.json','w') as file:
    json.dump(dict,file,indent= 1)