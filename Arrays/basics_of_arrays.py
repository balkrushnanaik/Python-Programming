# Python Program to Learn Arrays

# Import array module
import array as arr

# Create an integer array
numbers = arr.array('i', [10, 20, 30, 40, 50])

# Display array
print("Original Array:")
for i in numbers:
    print(i, end=" ")

print("\n")

# Access elements
print("First Element:", numbers[0])
print("Third Element:", numbers[2])

# Add element at the end
numbers.append(60)
print("\nArray after append:")
print(numbers)

# Insert element
numbers.insert(2, 25)
print("\nArray after insertion:")
print(numbers)

# Remove element
numbers.remove(40)
print("\nArray after removing 40:")
print(numbers)

# Update element
numbers[1] = 15
print("\nArray after updating:")
print(numbers)

# Length of array
print("\nLength of Array:", len(numbers))

# Traversing array
print("\nTraversing Array:")
for value in numbers:
    print(value)