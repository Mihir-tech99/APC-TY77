import pandas as pd

data = {
    "Amit": 45000,
    "Priya": 62000,
    "Rahul": 48000,
    "Sneha": 75000,
    "Vijay": 55000
}

series = pd.Series(data)

print("Series:")
print(series)
print("\nHighest salary:", series.max())
print("Lowest salary:", series.min())
print("Average salary:", series.mean())
print("\nEmployees earning more than 50000:")
print(series[series > 50000])
