class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross = self.basic_salary + hra + da

        print("HRA =", hra)
        print("DA =", da)
        print("Gross Salary =", gross)


e = Employee(101, "Rahul", 30000)
e.calculate()
