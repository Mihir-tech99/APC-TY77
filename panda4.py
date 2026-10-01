import pandas as pd

data = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 95,
    "Sneha": 68,
    "Vijay": 92
}

series = pd.Series(data)

print("Average attendance:", series.mean())
print("\nAttendance below 75%:")
print(series[series < 75])
print("\nAttendance above 90%:")
print(series[series > 90])
print("\nHighest attendance:", series.max())
