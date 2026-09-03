# Create and write data to student.txt

name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Roll Number: " + roll_no + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")

print("Student details have been written to student.txt")


# Open and display the complete contents of a file

with open("student.txt", "r") as file:
    contents = file.read()

print(contents)


# Append new student information without deleting previous contents

name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "a") as file:
    file.write("\nName: " + name)
    file.write("\nRoll Number: " + roll_no)
    file.write("\nBranch: " + branch)
    file.write("\nSemester: " + semester)

print("Information appended successfully.")


# Read and display each line separately

with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")


# Count the number of lines in a file

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))



with open("student.txt", "r") as file:
    contents = file.read()

words = contents.split()

print("Total number of words:", len(words))


# Count characters including spaces

with open("student.txt", "r") as file:
    contents = file.read()

print("Total number of characters:", len(contents))


# Read and display lines in reverse order

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end="")


# Count vowels and consonants in a text file

with open("student.txt", "r") as file:
    contents = file.read()

vowels = 0
consonants = 0

for char in contents:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# Count alphabets, digits, spaces, and special characters

with open("student.txt", "r") as file:
    contents = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for char in contents:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    elif char != "\n":
        special += 1

print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of special characters:", special)


# Find the longest word in a text file

with open("student.txt", "r") as file:
    text = file.read()

words = text.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))


# Count how many times each word occurs

with open("student.txt", "r") as file:
    text = file.read()

words = text.lower().split()

word_count = {}

for word in words:
    word = word.strip(".,!?;:")

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
print(word_count)


# Search for a word in a text file

search_word = input("Enter the word to search: ").lower()

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        words = line.lower().split()

        for word in words:
            word = word.strip(".,!?;:")

            if word == search_word:
                count += 1
                if line_number not in line_numbers:
                    line_numbers.append(line_number)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)


# Replace one word with another word

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

with open("student.txt", "r") as file:
    text = file.read()

modified_text = text.replace(old_word, new_word)

with open("new_student.txt", "w") as file:
    file.write(modified_text)

print("Modified text saved in new_student.txt")


# Remove single-line comments from a Python file

with open("program.py", "r") as file:
    lines = file.readlines()

with open("without_comments.py", "w") as file:
    for line in lines:
        stripped_line = line.strip()

        if not stripped_line.startswith("#"):
            file.write(line)

print("Comments removed successfully.")


# Convert text file contents to uppercase

with open("student.txt", "r") as file:
    text = file.read()

with open("uppercase.txt", "w") as file:
    file.write(text.upper())

print("Uppercase text saved in uppercase.txt")


# Student records

with open("students.csv", "r") as file:
    lines = file.readlines()

students = []

for line in lines[1:]:
    roll_no, name, marks = line.strip().split(",")
    students.append((int(roll_no), name, int(marks)))

# Display all records
print("All Student Records:")
for student in students:
    print(student)

# Find student with highest marks
highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest[1], "-", highest[2])

# Calculate average marks
total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage marks:", average)

# Display students scoring more than 80
print("\nStudents scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student[1], "-", student[2])


# Employee records using functions

def read_employees():
    employees = []

    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, department, salary = line.strip().split(",")
            employees.append(
                (int(emp_id), name, department, float(salary))
            )

    return employees


def display_employees(employees):
    print("Employee Records:")
    for emp in employees:
        print(emp)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])
    print("\nHighest-paid employee:")
    print(employee)


def average_salary(employees):
    total = sum(emp[3] for emp in employees)
    average = total / len(employees)
    print("\nAverage salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary, ":")
    for emp in employees:
        if emp[3] > salary:
            print(emp)


employees = read_employees()

display_employees(employees)
highest_paid(employees)
average_salary(employees)

amount = float(input("\nEnter salary: "))
above_salary(employees, amount)


# Calculate attendance percentage

with open("attendance.txt", "r") as file:
    for line in file:
        roll_no, name, present, total = line.strip().split(",")

        present = int(present)
        total = int(total)

        percentage = (present / total) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print("  -> Attendance below 75%")


# Calculate deposits, withdrawals, balance and largest transaction

total_deposits = 0
total_withdrawals = 0
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")

        amount = float(amount)
        transactions.append(amount)

        if transaction.lower() == "deposit":
            total_deposits += amount

        elif transaction.lower() == "withdrawal":
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", final_balance)
print("Largest transaction:", largest_transaction)


# Book Management System

books = []

def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    books.append([book_id, title, author, "Available"])

def search_book():
    bid = input("Enter Book ID: ")
    for book in books:
        if book[0] == bid:
            print(book)
            return
    print("Book not found")

def issue_book():
    bid = input("Enter Book ID: ")
    for book in books:
        if book[0] == bid and book[3] == "Available":
            book[3] = "Issued"
            print("Book issued")
            return
    print("Book not available")

def return_book():
    bid = input("Enter Book ID: ")
    for book in books:
        if book[0] == bid:
            book[3] = "Available"
            print("Book returned")
            return

def display_books():
    for book in books:
        if book[3] == "Available":
            print(book)

# Menu
while True:
    print("\n1.Add  2.Search  3.Issue  4.Return  5.Display  6.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        search_book()
    elif ch == "3":
        issue_book()
    elif ch == "4":
        return_book()
    elif ch == "5":
        display_books()
    elif ch == "6":
        break
    else:
        print("Invalid choice")


# Combine two files into a third file

with open("file1.txt", "r") as file1:
    content1 = file1.read()

with open("file2.txt", "r") as file2:
    content2 = file2.read()

with open("combined.txt", "w") as file3:
    file3.write(content1)
    file3.write("\n")
    file3.write(content2)

print("Contents of both files copied to combined.txt")


# Compare two text files

with open("file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("file2.txt", "r") as file2:
    lines2 = file2.readlines()

same = True

max_lines = max(len(lines1), len(lines2))

for i in range(max_lines):
    line1 = lines1[i].strip() if i < len(lines1) else ""
    line2 = lines2[i].strip() if i < len(lines2) else ""

    if line1 != line2:
        print("Files are different.")
        print("First difference is at line:", i + 1)
        print("File 1:", line1)
        print("File 2:", line2)
        same = False
        break

if same:
    print("Both files have identical contents.")
