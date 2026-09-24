class FoodOrder:
    def __init__(self, order_id, customer, food, quantity, price):
        self.order_id = order_id
        self.customer = customer
        self.food = food
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        print("Total Bill =", total + tax)

    def __del__(self):
        print("Order completed")


o = FoodOrder(101, "Rahul", "Pizza", 2, 300)
o.total_bill()
