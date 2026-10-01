import numpy as np

# Create an array of 10 integers
arr = np.array([10, 25, 55, 40, 75, 30, 90, 45, 60, 20])

print("Original Array:")
print(arr)

# Replace elements greater than 50 with 0
arr[arr > 50] = 0

print("\nArray after replacing values greater than 50 with 0:")
print(arr)
