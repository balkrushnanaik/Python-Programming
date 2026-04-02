# Demonstration of Python String Methods

text = "  Hello World Python Programming 123  "

print("Original String:", text)

# Case conversion
print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("capitalize():", text.capitalize())
print("swapcase():", text.swapcase())

# Searching methods
print("find('Python'):", text.find("Python"))
print("index('World'):", text.index("World"))
print("count('o'):", text.count("o"))

# Checking methods (return True/False)
print("isalnum():", text.isalnum())
print("isalpha():", text.isalpha())
print("isdigit():", text.isdigit())
print("islower():", text.islower())
print("isupper():", text.isupper())
print("istitle():", text.istitle())
print("isspace():", text.isspace())

# Replace and split
print("replace():", text.replace("Python", "Java"))
print("split():", text.split())
print("rsplit():", text.rsplit())

# Join method
words = ["Python", "is", "easy"]
print("join():", " ".join(words))

# Remove spaces
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

# Starts and ends with
print("startswith('Hello'):", text.strip().startswith("Hello"))
print("endswith('123'):", text.strip().endswith("123"))

# Partition
print("partition('World'):", text.partition("World"))

# Center, ljust, rjust
print("center(40):", text.strip().center(40, "*"))
print("ljust(40):", text.strip().ljust(40, "-"))
print("rjust(40):", text.strip().rjust(40, "-"))

# Formatting
name = "Balkrushna"
age = 20
print("format(): My name is {} and age is {}".format(name, age))

# zfill
num = "45"
print("zfill(5):", num.zfill(5))