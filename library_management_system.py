class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        

    def display_books(self):
        print (f"Book list is as :{self.books}")
        print(f"Total books in the library is {self.no_of_books}")

obj = Library()
obj.add_book("Chemistry")
obj.add_book("Physics")
obj.add_book("Maths")
obj.display_books()