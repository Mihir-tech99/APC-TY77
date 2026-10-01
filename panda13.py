import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Monitor", "Tablet", "Printer"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Office"],
    "Price": [60000, 30000, 12000, 20000, 9000],
    "Quantity": [2, 3, 5, 4, 2]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])
print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("\nAverage sales:", df["Total_Sales"].mean())
