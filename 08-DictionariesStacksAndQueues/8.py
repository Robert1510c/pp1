person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person['name'])
print(person['hobby'])
person['surname']='Nowak'
print(person['surname'])
person['maried']=False
print(person['maried'])
person['gender']='male'
print(person['gender'])
person['hobby'].append('bicycle')
print(person['hobby'])
person['phone']['work phone'] = '31313131444'
print(person['phone'])


