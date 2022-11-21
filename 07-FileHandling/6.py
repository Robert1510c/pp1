file = open('countries.txt','r', encoding='utf-8') #instrukcja przypisania
file_content = file.read()
print( file_content )
file.close()
