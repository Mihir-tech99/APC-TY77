def read_employees():
    employees = []

    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")

            employees.append(
                (int(emp_id), name, dept, float(salary))
            )

    return employees


def display_employees(employees):
    print("Employee Records:")

    for emp in employees:
        print(emp)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])
    print("\nHighest Paid Employee:")
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Department:", employee[2])
    print("Salary:", employee[3])

def average_salary(employees):
    total = sum(emp[3] for emp in employees)
    average = total / len(employees)

    print("\nAverage Salary:", average)

def above_salary(employees, salary):
    print("\nEmployees earning above", salary)

    for emp in employees:
        if emp[3] > salary:
            print(emp[1], emp[3])

# Main program
employees = read_employees()

display_employees(employees)

highest_paid(employees)

average_salary(employees)

salary = float(input("\nEnter salary limit: "))
above_salary(employees, salary)