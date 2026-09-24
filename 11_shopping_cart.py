class ShoppingCart:
    def __init__(self, name, cart_id):
        self.name = name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)

    def total(self):
        total = 0
        for product in self.products:
            total += product[1]
        print("Total Bill =", total)

    def __del__(self):
        print("Shopping cart destroyed")


cart = ShoppingCart("Rahul", 101)

cart.add_product("Pen", 20)
cart.add_product("Book", 100)

cart.total()
