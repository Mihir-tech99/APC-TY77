import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vijay"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 90, 80, 100],
    "Classes_Attended": [85, 70, 65, 72, 95]
}

df = pd.DataFrame(data)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)
print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])
