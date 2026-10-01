import numpy as np

# Create a 3D array containing numbers from 1 to 27
arr = np.arange(1, 28).reshape(3, 3, 3)

# Flatten the array
flattened = arr.flatten()

# Display the arrays
print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)

# Calculate statistics
print("\nSum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))
