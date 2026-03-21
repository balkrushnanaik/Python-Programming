def Divide(num1, num2):

    try:
        answer = num1 / num2
        return answer
    except Exception as e:
        print("You cannot do:",e)

    finally:
        print("This line will be print everytime")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
Divide(num1, num2)