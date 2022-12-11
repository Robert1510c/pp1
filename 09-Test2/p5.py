import re

def f(first_letter,last_letter):
    with open('test.txt','r',encoding='utf-8') as file:
        file_context=file.read()
        words=re.findall(rf'\b{first_letter}\w*{last_letter}\b',file_context,re.IGNORECASE)
        return len(words)
        

print(f("w", "d") )