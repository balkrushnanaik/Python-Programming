import numpy as np
# print(np.__version__)

# a = np.array([1,2,3,4,4,5,6,6,8])
# print(a)

# print(a.max())
# print(a[0])
# print(a[-3:])

b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(b)


#Arithmetic Operation
print(f"Square of each number: \n {b**2}")

# Statistical Operations
print(f"The mean of the list is : {np.mean(b)}")
print(f"Standard deviation of list is : {np.std(b)}")

#Shape and Size

print(b.shape)
print(b.size)
print(b.ndim)

# Reshaping Array

# Sorting
print(np.sort(b))

# Add or Delete
print(np.delete(b, 0))
