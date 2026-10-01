import pandas as pd

data = {
    "P001": 65,
    "P002": 45,
    "P003": 72,
    "P004": 30,
    "P005": 68
}

series = pd.Series(data)

print("Average age:", series.mean())
print("\nOldest patient:")
print(series[series == series.max()])
print("\nYoungest patient:")
print(series[series == series.min()])
print("\nPatients above 60 years:")
print(series[series > 60])
