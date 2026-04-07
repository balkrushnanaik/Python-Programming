
#Write a Python program to perform operations on list such as append, insert, remove, sort and reverse.

data = [1,2,3,4,5,6,7,8,9]
print(f"The type of data is:{type(data)}")

data.append(10)
print(f"Data after use append method:\n {data}")

data.insert(0,20)
print(f"Data after use insert method:\n {data}")

data.remove(7)
print(f"Data after use remove method:\n {data}")

print(f"Data before the sort method:\n {data}")
data.sort()
print(f"Data after sort method:\n {data}")

