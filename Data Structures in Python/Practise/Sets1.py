print("Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)")
my_set = {1, 2, 3, 3, 4}

print(my_set)
print("It removes the duplicate element 3")

print("Add 5 to the set, remove 2, and check if 4 is in the set.")
my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

if 4 in my_set:
    print("4 is in the set")
else:
    print("4 is not in the set")


set1 = {1, 2, 7, 4}
print(set1)
set2 = {5, 2, 7, 1}
print(set2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

