with open('films.txt','r') as firstfile, open('copy.txt','a') as secondfile:
    text=firstfile.read()
    secondfile.write(text)