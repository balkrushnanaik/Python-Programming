""" Tuples are ordered but immutable collections (cannot be changed after creation)"""
print(__doc__)
number = (10,30,15,14,23,23,45,12,56)
print(type(number))

print(number)
print(number.count(23))

''' Other Useful Tuple Operations in Python'''
print(__doc__)
print(f"The length of the tuple is :{len(number)}")
print(f"The sorted tuple is :{sorted(number)}")

