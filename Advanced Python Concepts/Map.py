numbers = [1,2,3,4,5]
print(type(numbers))

def square(num):
    return num * num

new = list(map(square, numbers))
print(new)

