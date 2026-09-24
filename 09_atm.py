class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance =", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def details(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


a = ATM("Rahul", 10000)

while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a.check_balance()
    elif choice == 2:
        a.deposit(float(input("Enter amount: ")))
    elif choice == 3:
        a.withdraw(float(input("Enter amount: ")))
    elif choice == 4:
        a.details()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
