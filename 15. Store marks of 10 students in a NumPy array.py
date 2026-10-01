import numpy as np

# Store marks of 10 students
marks = np.array([75, 82, 68, 90, 55, 73, 88, 64, 95, 80])

# Calculate statistics
highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)
median = np.median(marks)
standard_deviation = np.std(marks)

# Display results
print("Marks:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Median:", median)
print("Standard Deviation:", standard_deviation)
