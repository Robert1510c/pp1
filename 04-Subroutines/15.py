import mymath


def game():
    if mymath.read_number() == mymath.generate_number():
        print("You won!")
        return True
    else:
        print("You lost!")
        return False

status = game()

while status==False:
    status = game()
