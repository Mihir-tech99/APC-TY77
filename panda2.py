import pandas as pd

data = {
    "Laptop": 60000,
    "Phone": 30000,
    "Monitor": 12000,
    "Keyboard": 1500,
    "Mouse": 800
}

series = pd.Series(data)

print("Products and prices:")
print(series)

series = series * 1.10

print("\nPrices after 10% increase:")
print(series)
print("\nMost expensive product:")
print(series[series == series.max()])
print("\nProducts costing more than 1000:")
print(series[series > 1000])
