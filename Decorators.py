# Decorator is a function that takes a function, it creates a new function inside its body(wrapper).
# Then it returns that new function

def decorator(func): # Function decorator not return anything
    def wrapper():
        print("I am going to execute this function")
        func()
        print("I have executed this function")
    return wrapper
def say_hello():
    print("Hello Guys")

# say_hello()

f = decorator(say_hello)
f()






