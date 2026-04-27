num = int(input("Enter a number: "))
original = num
result = 0

n = len(str(num))   # number of digits

while num > 0:
    digit = num % 10
    result += digit ** n
    num = num // 10

if original == result:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")