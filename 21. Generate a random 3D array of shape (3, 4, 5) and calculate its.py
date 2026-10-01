import numpy as np

# Generate a random 3D array of shape (3, 4, 5)
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Random 3D Array:")
print(arr)

# Calculate statistical values
print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
