'''A set is a well-defined, unordered collection of distinct objects (elements), such as numbers, letters, or items, usually enclosed in curly braces
. Sets cannot contain duplicate elements, and they are typically represented by capital letters.'''

print(__doc__)

#Sets are great for eliminating duplicate values

my_set = {1,2,3,4,5,6,7,8,9}
print(my_set)

#Methods

my_set.remove(5)
print(my_set)
my_set.add(5)
print(my_set)
my_set.add(6)
print(my_set)
my_set.add(7)
print(my_set)

my_set.discard(6)
print(my_set)
my_set.discard(7)
print(my_set)


#Set operations
