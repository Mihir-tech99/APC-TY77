# Program 12: Accept five numbers, store in list and convert to tuple
numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)
