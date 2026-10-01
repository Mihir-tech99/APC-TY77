import numpy as np

# Create a NumPy array of integers from 1 to 20
arr = np.arange(1, 21)

# Use Boolean indexing to separate even and odd numbers
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

# Display the results
print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)
