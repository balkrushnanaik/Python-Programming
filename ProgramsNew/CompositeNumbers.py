num = int(input("Enter a number: "))

for i in range(2, num):
    if num > 1:
     if num % i == 0:
        print("Composite Number")
        break
    else:
        print("Not a composite number:", i)

else:
    print("Not composite number",num)