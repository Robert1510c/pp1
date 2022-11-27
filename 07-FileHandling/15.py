with open('30line.txt','r',encoding='utf-8') as f:
    x=0
    y=0
    for i in f:
        print(i, end='')
        x+=1
        y+=1
        if x==5:
            if y==30:
                print()
                print("Koniec")
            else:
                input("Wciśnij enter: ")
            x=0
print()

        

