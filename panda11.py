import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Vijay"],
    "Product": ["Laptop", "Phone", "Monitor", "Keyboard", "Tablet"],
    "Quantity": [1, 2, 3, 5, 2],
    "Price": [60000, 30000, 12000, 1500, 20000],
    "Discount": [5000, 2000, 1000, 500, 1500]
}

df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:")
print(df)
print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])
print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("\nAverage order value:", df["Final_Amount"].mean())
