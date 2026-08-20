# Program 22: Store and display employee information
employees = (
    (101, "Amit", 30000),
    (102, "Rahul", 35000),
    (103, "Sneha", 40000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()
