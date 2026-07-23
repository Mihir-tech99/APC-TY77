# Program to evaluate student performance

marks = float(input("Enter percentage: "))

if marks >= 90:
    print("Performance: Excellent")
elif marks >= 80:
    print("Performance: Very Good")
elif marks >= 70:
    print("Performance: Good")
elif marks >= 60:
    print("Performance: Average")
else:
    print("Performance: Poor")