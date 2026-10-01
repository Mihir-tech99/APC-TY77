import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

# Display the array
print("3D Array:")
print(arr)

# Display number of dimensions
print("\nNumber of dimensions:", arr.ndim)

# Display shape
print("Shape:", arr.shape)

# Display size
print("Size:", arr.size)
