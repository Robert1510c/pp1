def f(human_age):
    if human_age<=2:
        return human_age*10
    else:
        x=2*10+(human_age-2)*4
        return x

print(f(10))