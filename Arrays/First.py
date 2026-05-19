# Simple Example of Array in Python

import array as arr

# Create an array
numbers = arr.array('i', [1, 2, 3, 4, 5])

# Print array
print("Array Elements:")
for i in numbers:
    print(i)

# Access element
print("First Element:", numbers[0])

# Add new element
numbers.append(6)

print("Updated Array:")
print(numbers)