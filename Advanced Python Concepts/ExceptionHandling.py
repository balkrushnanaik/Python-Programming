# while True:
#     try:
#         num1 = int(input("Enter a number: "))
#         num2 = int(input("Enter another number: "))
#
#         print(f"The division of {num1} and {num2} is {num1 / num2}")
#
#     except ZeroDivisionError:
#         print("You cannot divide by zero")
#
#
#     except ValueError:
#         print("You cannot use string in this code")

# n = 10
# try:
#     res = n / 0
# except Exception as e:
#     print(e)
# else:
#     print(res)

try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")









