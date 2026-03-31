print("Welcome to the Food Lucky Draw")
food = input("Enter any number to win Food:")

match food:
    case "1":
        print("You won Pizza! \"Congratulations!\" " )
    case "2":
        print("You won Vada Pav! \"Congratulations!\" ")
    case "3":
        print("You won Burger! \"Congratulations!\" ")
    case _:
        print("You won Nothing! \"Congratulations!\" ")
