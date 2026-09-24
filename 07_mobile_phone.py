class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)

    def discount_price(self):
        return self.price * 0.90


m = MobilePhone("Samsung", "A55", "128GB", 30000)

m.display()
print("Price after discount =", m.discount_price())
