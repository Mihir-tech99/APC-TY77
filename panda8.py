import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Priya", "Rahul", "Sneha", "Vijay"],
    "Department": ["CSE", "IT", "HR", "CSE", "Finance"],
    "Salary": [55000, 48000, 62000, 75000, 45000],
    "Experience": [3, 5, 7, 10, 2]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])
print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
