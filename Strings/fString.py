# Using .format() Method:

name = "Balkrushna"
age = 22
print("My name is {} and I am {} years old ".format(name,age))


# f-Strings
# Introduced in Python 3.6, f-strings are the most concise and readable way to format strings

print(f"My name is {name} and I am {age} years old")

#Without using f-string
print("My name is {name} and I am {age} years old")

#Using expression in f-Strings
num1 = 10
num2 = 20

print(f"The some of {num1} and {num2 } is : {num1+num2}")

#Formatting Numbers
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")