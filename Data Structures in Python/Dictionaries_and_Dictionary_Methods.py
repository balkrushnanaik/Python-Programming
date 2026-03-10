my_details = {"Name":"Balkrushna Naik", "Age": 23, "Graduate":False,
              "isStudent":True, "Hobbies":["Playing Cricket, Traveling, Mobile Games"]}

print(type(my_details))
print(my_details)
print(my_details["Name"])
print(my_details["Age"])
print(my_details["Hobbies"])
print(my_details["isStudent"])

#Methods

print(my_details.keys())
print(my_details.values())
print(my_details.items())

# print(my_details.clear())
print(my_details)
print(my_details.pop("isStudent"))
print(my_details)

# Dictionary Comprehensions:

table_of_5 = {i: 5*i for i in range(1,11)}
print(table_of_5)

print(table_of_5.keys())
print(table_of_5.values())

square_of_first_10 = {i: i**2 for i in range(1,11)}
print(square_of_first_10)
