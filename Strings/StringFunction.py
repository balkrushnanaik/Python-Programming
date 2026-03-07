name = 'balkrushna naik' # Blank is also count #Strings are immutable
print(name)


# Common string methods in python
print(name.upper(),name) #
print(name.lower())
print(name.capitalize()) # First letter will capitalize
print(name.title())

#Removing Whitespace

text = "  hello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"

#Finding and Replacing

text = "Python is fun"
print(text.find("is"))   # Output: 7
print(text.replace("fun", "awesome"))  # Output: "Python is awesome"

#Splitting and Joining

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"

#Checking String Properties

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False

#Useful Built-in String Functions

text = "Hello, Python!"
print(len(text))  # Output: 14

print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'