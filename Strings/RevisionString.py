text = "I am happy"

print(text[5:10])
print(text[:10])

print(text[5:])
print(text[:])

# String Indexing
# Output will be n (last character )
print(text[-1])

# String Slicing

# String Reversing
print(text[::-1])

#Finding ad replacing
print(text.find("happy"))
print(text.replace("happy","Angry"))

fruits = "Apple, Banana, Pineapple, Mango"
print(fruits[::-1])
fruit = fruits.split(",")
print(fruit)

#Useful Built in string functions

print(len(fruit))
