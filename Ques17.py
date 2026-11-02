with open("students.txt", "r") as file:
    lines = file.readlines()

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    students.append((int(roll), name, float(marks)))

# Display all records
print("All Student Records:")
for student in students:
    print(student)

# Find student with highest marks
highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print("Roll No:", highest[0])
print("Name:", highest[1])
print("Marks:", highest[2])

# Calculate average marks
total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage Marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student[1], student[2])