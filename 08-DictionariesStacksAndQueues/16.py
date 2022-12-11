import json

with open('students.json','r',encoding='utf-8') as file:
    data=json.load(file)
    for i in data:
        x= {'first_name': i['first_name'],
        'last_name': i['last_name'],
        'id': i['id']}
        with open('limited.json','w') as file2:
            for key,value in x.items():
                file2.write(key)
                file2.write(value)
        

    
            