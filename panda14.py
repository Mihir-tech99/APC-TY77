import pandas as pd

data = {
    "Amit": 72,
    "Priya": 88,
    "Rahul": 91,
    "Sneha": 68,
    "Vijay": 79
}

series = pd.Series(data)

print("Series:")
print(series)
print("\nMarks of Priya:", series["Priya"])
print("Maximum marks:", series.max())
print("Minimum marks:", series.min())
print("Average marks:", series.mean())
print("\nStudents scoring more than 75:")
print(series[series > 75])
