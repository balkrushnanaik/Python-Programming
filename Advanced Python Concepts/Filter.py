number = 9

def greater_than_number(x):
    if x > number:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

new = list(filter(greater_than_number,a))
print(new)
