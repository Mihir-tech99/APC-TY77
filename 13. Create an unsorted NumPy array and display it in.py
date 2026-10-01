import numpy as np

# Create an unsorted NumPy array
arr = np.array([45, 12, 78, 23, 9, 56, 34, 67])

print("Original Array:")
print(arr)

# Ascending order
ascending = np.sort(arr)

# Descending order
descending = np.sort(arr)[::-1]

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)
