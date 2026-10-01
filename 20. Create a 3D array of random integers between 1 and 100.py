import numpy as np

# Create a 3D array of random integers between 1 and 100
arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(arr)

# Replace all values greater than 50 with 0
arr[arr > 50] = 0

print("\nArray after replacing values greater than 50 with 0:")
print(arr)
