import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Priya", "Rahul", "Sneha", "Vijay"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Flu", "Diabetes"],
    "Medical_Charges": [60000, 25000, 85000, 15000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:")
print(df[df["Age"] > 60])
print("\nAverage medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())
print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])
