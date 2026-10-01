import numpy as np

# Create a 4 × 4 NumPy array
arr = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Array:")
print(arr)

# Display the first row
print("\nFirst Row:")
print(arr[0])

# Display the last column
print("\nLast Column:")
print(arr[:, -1])

# Display the diagonal elements
print("\nDiagonal Elements:")
print(np.diag(arr))

# Display the second and third rows
print("\nSecond and Third Rows:")
print(arr[1:3])
