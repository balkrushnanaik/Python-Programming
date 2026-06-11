numbers = [11,20,30,40,21,31,42,56,76,67]

def even(x):
    return x % 2 == 0

evens = list(filter(even,numbers))
print(f'Even Numbers: {evens}')

# The filter() function is used to select elements from a list based on a condition.
# filter(function, iterable)

# Lambda Function

odds = list(filter(lambda x: x % 2 == 1,numbers))
print(f'Numbers are: {odds}')

