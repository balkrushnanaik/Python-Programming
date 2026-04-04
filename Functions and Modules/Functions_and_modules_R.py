# Syntax

def greeting(name):
    return f'Hello, {name}!'
print(greeting('Bob'))
print(greeting('Alice'))

#Types of Argument
# 1. Positional Argument
def add(x, y):
    return x + y
print(add(1, 2))

# 2.Default Argument
def greet(name="Default"):
    return f'Hello, {name}!'
print(greet('Bob'))

#3. Keyword Argument

def wish(name,age):
    return f'Hello, {name}!, you are {age} years old'
print(wish('Bob',22))