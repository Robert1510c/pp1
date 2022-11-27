with open('numbers1to50.txt','w') as file:
    for i in range(0,51):
        i=str(i)
        file.write(i)
        file.write('\n')