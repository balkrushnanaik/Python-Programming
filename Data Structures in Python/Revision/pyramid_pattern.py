n = int(input("Enter any number"))

# Pyramid Pattern
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)