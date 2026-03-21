num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num2 == 0:
    raise ValueError("You cannot divide by zero")

print(f"{num1} / {num2} = {num1 / num2}")