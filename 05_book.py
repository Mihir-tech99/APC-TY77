class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.book_id, self.title, self.author, self.price)


b1 = Book(1, "Python", "Guido", 500)
b2 = Book(2, "Java", "James", 600)
b3 = Book(3, "C++", "Bjarne", 550)

b1.display()
b2.display()
b3.display()
