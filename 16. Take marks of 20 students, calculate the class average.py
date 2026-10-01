import numpy as np

# Marks of 20 students
marks = np.array([
    65, 78, 82, 55, 90,
    72, 88, 60, 95, 70,
    84, 76, 68, 92, 58,
    80, 74, 85, 63, 89
])

# Calculate class average
average = np.mean(marks)

# Display the marks and average
print("Marks of 20 students:")
print(marks)

print("\nClass Average:", average)

# Display students who scored above average
above_average = marks[marks > average]

print("\nMarks above the class average:")
print(above_average)
