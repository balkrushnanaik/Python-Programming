# Positional Argument

def add(a,b):
    return a+b
ans = add(3,4)
print(ans)

# Default Argument

def sub(a,b,c=10):
    return a-b-c
ans = sub(3,4,5)
print(ans)

#Keyword Argument

def mult(a,b):
    return a*b
ans = mult(b=19,a=10)
print(ans)