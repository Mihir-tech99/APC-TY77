import numpy as np

# Create a 4 × 4 matrix
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Calculate sum of each row
row_sum = np.sum(matrix, axis=1)

# Calculate sum of each column
column_sum = np.sum(matrix, axis=0)

# Display the matrix
print("Matrix:")
print(matrix)

# Display row sums
print("\nSum of each row:")
print(row_sum)

# Display column sums
print("\nSum of each column:")
print(column_sum)
