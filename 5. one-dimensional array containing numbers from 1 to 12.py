import numpy as np

# Create a one-dimensional array from 1 to 12
arr = np.arange(1, 13)

print("Original 1D Array:")
print(arr)

# Reshape into 2 × 6 matrix
matrix_2x6 = arr.reshape(2, 6)
print("\n2 × 6 Matrix:")
print(matrix_2x6)

# Reshape into 3 × 4 matrix
matrix_3x4 = arr.reshape(3, 4)
print("\n3 × 4 Matrix:")
print(matrix_3x4)

# Reshape into 4 × 3 matrix
matrix_4x3 = arr.reshape(4, 3)
print("\n4 × 3 Matrix:")
print(matrix_4x3)
