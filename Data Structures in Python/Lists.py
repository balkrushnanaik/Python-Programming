# #Lists are ordered, mutable(Changeable) collections of items.
# marks = [10, 20, 30, 40, 50]
#
# # We can also create mixed list
#
# mixed = [10, "Hello", True, 4.9]
#
# print(marks)
#
# print(marks[0])
# print(marks[1])
# print(marks[1:4])
#
# print(mixed)
# print(mixed[2])

# Using list() constructor
num = list((1,2,3,4,5,6))
print(type(num))
print(num)

name = 'Balkrushna'
names = list(('Balkrushna','Vaibhav','Dhanraj','Sid'))
print(names)
print(names[0])

for item in names:
    print(item)
if name in names:
    print('Present')
else:
    print('Absent')

a = [2] * 10
b = ['Hello'] * 5
print(*b, sep=' ')
print(a)