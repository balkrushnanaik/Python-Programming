# #Tuple Creation
# num = (10,20,40,90,45,89,10,20,10,40,10)
#
# print(num)
#
# #Accessing particular elements in Tuple
# print(num[2])
#
# #Tuple Unpacking
#
# a, b, c, d, e, f, g, h, i, j, k = num
# print(a, b, c, d, e, f)
#
# print(type(num))
#
# #Methods in Tuple
#
# #Count(x)- Returns the number of times x appears in the tuple
#
# print(num.count(10))
#
# #Index(x)- Returns the index of the first occurrence of x
#
# print(num.index(10))
#
#
# # Tuples in Python
# # Tuples are ordered but Immutable collections(Cannot be changed after creation)
#
# #Tuple with one element (Comma required)

tup = tuple(('Vaibhav','Ganesh'))
print(type(tup))
print(tup)

for names in tup:
    print(names)

tup1 = (1,2,3,4,5)
tup2 = ('Liya','Jiya')
tup3 = tup1 + tup2
print(type(tup3))
print(tup3)

del tup3
