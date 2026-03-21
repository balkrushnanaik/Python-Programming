while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        print(f"The division of {num1} and {num2} is {num1 / num2}")

    except ZeroDivisionError:
        print("You cannot divide by zero")


    except ValueError:
        print("You cannot use string in this code")




