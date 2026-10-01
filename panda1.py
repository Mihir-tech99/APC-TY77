import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Vijay"],
    "Python": [80, 72, 90, 65, 85],
    "DBMS": [75, 80, 88, 70, 92],
    "Mathematics": [82, 78, 85, 68, 90]
}

df = pd.DataFrame(data)
df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print(df)
print("\nStudents with average above 75:")
print(df[df["Average"] > 75])
