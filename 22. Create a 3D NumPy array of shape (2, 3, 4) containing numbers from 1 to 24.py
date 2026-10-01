import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

# Flatten the array
flattened = arr.flatten()

# Display original and flattened arrays
print("Original 3D Array:")
print(arr)

print("\nFlattened 1D Array:")
print(flattened)
