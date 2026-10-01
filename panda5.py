import pandas as pd

df = pd.read_csv("students.csv")

df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

print("\nTotal and average marks:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with average marks greater than 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())
