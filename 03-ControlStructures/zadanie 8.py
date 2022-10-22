Paul=21
Annie=18

if Paul and Annie >=18:
    print("Oboje dorośli")
elif Paul>=18 and Annie<18:
    print("Paul jest pełnoletni, Annie nie")
elif Annie>=18 and Paul<18:
    print("Annie jest pełnoletni, Paul nie")
else:
    print("oboje niepełnoletni")
