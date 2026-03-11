coordinates = (10, 20)
print(coordinates)

print("Try to modify tuple")
# coordinates[0] = 50
# print(coordinates)

print('Convert tuple to list')
corlist =list(coordinates)
print(corlist)
corlist[0] = 50
print(corlist)

coordinates = tuple(corlist)
print(coordinates)

