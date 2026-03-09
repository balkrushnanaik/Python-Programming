def average(a,b,c):
    # a and b are local Variables
    ans= (a+b+c)/2
    y = 10   # It creates a local variable called y which is destroyed after this function returns

    return ans


z=10 # It is a global Variable
print(average(10,10,10))

print(z)

def greet():
    global a
    a = 15
    return 'This is a Global Variable greet'

print(greet())
print(a)

