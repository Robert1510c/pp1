file=open('films.txt','w',encoding='utf-8')
array=['Harry Potter','Guardians of the galaxy','Lord of the rings','Bad boys','Men in black']
for i in range(0,len(array)):
    file.write(array[i])
    file.write('\n')


file.close()