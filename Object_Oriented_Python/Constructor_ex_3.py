print("\n\n      ___Book Market___          \n")
class Book:
    def __init__(self,title, author, book_price):
        self.title=title
        self.author=author
        self.book_price=book_price

    # def product_list():
    #     list_of_books=[{"Title":"ATOMIC HABITS","Author":"James Clear","price":534},
    #                    {"HARRY PORTER","J.K. Rowling",2569},
    #                    {"The ALCHEMIST","Al Khawarizmi",894},
    #                    {"1984","George orwell",182},
    #                    {"SAPIENS","Y.N Harari",510}]
    #     for i in list_of_books:
    #         print(i)
    
    def display(self):
        print("Title: ", self.title)
        print("Author: ",self.author)
        print("Price: ",self.book_price)
        print("after discount of 20%: ", round((self.book_price-self.book_price*0.2),2))
        print("")

v=Book("ATOMIC HABITS","James Clear",534)
w=Book("HARRY PORTER","J.K. Rowling",2569)
x=Book("The ALCHEMIST","Al Khawarizmi",894)
y=Book("1984","George orwell",182)
z=Book("SAPIENS","Y.N Harari",510)

list=[v,w,x,y,z]
for i in list:
    i.display()
# v.display()
# w.display()
# x.display()
# y.display()
# z.display()
