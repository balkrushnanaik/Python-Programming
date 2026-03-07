'''Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears'''

text = "i love python programming"
print(text.strip())
print(text.title())
print(text.find('o'))


#Check if the string "123abc" is alphanumeric.

text = "123abc"

print(text.isalnum())
print(text.isalpha())
