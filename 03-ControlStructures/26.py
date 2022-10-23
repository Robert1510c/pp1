pin="0805"
count=0

for i in range(1,4):
    x=str(input("Wprowadź pin: "))    
    if x==pin:
        print('True')
        break
    else:
        count+=1
        print('False')
        continue
if count==3:
    print("Sorry, your payment card has been blocked.")

