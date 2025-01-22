
class Book(object):
    def __init__(self, title: str, author: str, available: bool, price: float):
        self.title = title
        self.author = author
        self.available = available
        self.price = price

    def __str__(self):
        return (f"{self.title} by {self.author}\n"
                f"Available :{self.available}\n"
                f"Price: {self.price:.2f}\n")

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.available}, {self.price}"

class Library(object):
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, available: bool, price: float):
        book = Book(title, author, available, price)
        self.books.append(book)

    def borrow_book(self, title: str):
        for book in self.books:
            if title == book.title:
                if book.available:
                    book.available = False
                    print(f"You have successfully borrowed '{title}'.")
                else:
                    print(f"'{title}' is already reserved.")
                return
        print(f"Book '{title}' does not exist.")

    def return_book(self, title: str):
        for book in self.books:
            if title == book.title:
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{title}'.")
                else:
                    print(f"'{title}' was not borrowed.")
                return

        print(f"Book '{title}' does not exist.")

    def list_books(self):
        print("Library Inventory:")
        for book in self.books:
            print(book)
        print()

    def __str__(self):
        books_str = ''
        for book in self.books:
            books_str += f"{book.title} by {book.author}\n"

        return books_str


# Main Scope
l1 = Library()

l1.add_book("The BFG", "Roald Dahl", True, 12.99)
l1.add_book("Matilda", "Roald Dahl", False, 10.99)
l1.add_book("Harry Potter", "J.K. Rowling", True, 15.99)

l1.list_books()

l1.borrow_book("The BFG")
#l1.list_books()

l1.return_book("The BFG")
#l1.list_books()

l1.borrow_book("Matilda")
#l1.list_books()

l1.borrow_book("Nonexistent Book")