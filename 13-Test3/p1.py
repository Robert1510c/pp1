def f(x):
    if x<=5:
        y=(str('"'+'/'*x+'"'))
    else:
        n=x//5
        a=x-n*5
        y=(str('"'+('/'*5+'-')*n+'/'*a+'"'))
        if y[-2]=='-':
            y=y[:-2]+'"'
    return y 




print(f(120))
