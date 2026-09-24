class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Percentage:", percentage, "%")


s1 = Student(1, "Rahul", [80, 75, 90])
s2 = Student(2, "Amit", [70, 85, 80])

s1.display()
s2.display()
