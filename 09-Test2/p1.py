
def f(player1,player2):
    sum1=0
    sum2=0
    for i in player1:
        if i=='A' or i=='K' or i=='Q' or i=='J' or i=='T':
            i=10
        else:
            i=i
        i=int(i)
        sum1+=i
    for a in player2:
        if a=='A' or a=='K' or a=='Q' or a=='J' or a=='T':
            a=10
        else:
            a=a
        a=int(a)
        sum2+=a
    if sum1>sum2:
        return True
    else:
        return False

print(f("987","AT4"))

    

    