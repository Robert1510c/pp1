with open('GrainsAndBread.txt','r') as firstfile, open('MeatAndFish.txt','r') as secondfile, open('shoppinglist.txt','a') as finalfile:
    text1=firstfile.read()
    text2=secondfile.read()
    finalfile.write(text1)
    finalfile.write(text2)