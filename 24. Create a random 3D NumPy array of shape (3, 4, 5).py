import numpy as np

# Create a random 3D array of shape (3, 4, 5)
arr = np.random.randint(1, 101, size=(3, 4, 5))

# Flatten the array
flattened = arr.flatten()

# Calculate average
average = np.mean(flattened)

# Display original and filtered elements
print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)

print("\nElements greater than 50:")
print(flattened[flattened > 50])

print("\nEven numbers:")
print(flattened[flattened % 2 == 0])

print("\nAverage:", average)

print("\nElements less than average:")
print(flattened[flattened < average])
