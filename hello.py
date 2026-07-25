a = int(input("Enter a number between 1 to 10: "))
match a:
    case 1:
        print("You won a 3$")
    case 3:
        print("You won a doll")
    case 7:
        print("You got a refrigerator")
    case _:
        print("Better Luck next time")