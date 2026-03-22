def add(*args):
    # Args will be a tuple of all the values passes to sum
    total = 0
    for i in args:
        total += i
    return total

print(add(1,2,3,4,5,6,7,8,9))

