class Book:
    def __init__(self,title, author, book_price):
        self.title=title
        self.author=author
        self.book_price=book_price
        print("___Book Market___")

    def display(self):
        print("Title of a book",self.title)
        print("Author of a book",self.author)
        print("Price of a book",self.price)
        print("After discount of 20%: ",self.price*0.2)