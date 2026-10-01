import numpy as np

# Create two NumPy arrays
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# Horizontal concatenation
horizontal = np.concatenate((arr1, arr2), axis=1)

# Vertical concatenation
vertical = np.concatenate((arr1, arr2), axis=0)

print("\nHorizontal Concatenation:")
print(horizontal)

print("\nVertical Concatenation:")
print(vertical)
