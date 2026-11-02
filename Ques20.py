total_deposits = 0
total_withdrawals = 0
balance = 0

transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction_type, amount = line.strip().split(",")

        amount = float(amount)

        transactions.append(amount)

        if transaction_type == "D":
            total_deposits += amount
            balance += amount

        elif transaction_type == "W":
            total_withdrawals += amount
            balance -= amount


largest = max(transactions)

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest)