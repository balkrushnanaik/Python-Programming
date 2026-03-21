from functools import reduce

numbers = [1,2,3,4,5,6]

def add(a,b):
    return a + b

new = reduce(add,numbers)
print(new)

