import re

with open('films.txt','r',encoding='utf-8') as file:
    file_context=file.read()
    words=re.findall(r'\b\w{6,}\b',file_context)

print(words)