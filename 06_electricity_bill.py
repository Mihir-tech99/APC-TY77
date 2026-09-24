class ElectricityBill:
    def __init__(self, number, name, units):
        self.number = number
        self.name = name
        self.units = units

    def calculate(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = 100 * 2 + (self.units - 100) * 3
        else:
            bill = 100 * 2 + 100 * 3 + (self.units - 200) * 5

        print("Consumer:", self.name)
        print("Bill =", bill)


e = ElectricityBill(101, "Rahul", 250)
e.calculate()
