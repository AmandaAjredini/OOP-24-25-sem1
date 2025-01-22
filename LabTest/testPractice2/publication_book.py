
class Publication(object):
    def __init__(self):
        self.title = input("Please enter a title: ")
        self.price = float(input("Please enter a price: "))

    def __str__(self):
        return (f"Publication:\n"
                f"Title: {self.title}\n"
                f"Price: {self.price:.2f}\n")

class Book(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.page_count = int(input("Please enter the page count: "))

    def __add__(self, other):
        if not isinstance(other, Book):
            raise TypeError("Addition may only occur between 2 books")
        else:
            new_title = input("Please enter a title: ")
            new_price = self.price + other.price
            new_page_count = self.page_count + other.page_count

            new_book = Book.__new__(Book) # create a new Book object without calling the __init__() method, which normally prompts the user for input. This ensures that the user is not asked for the title, price, or page count when the combined book is created.
            new_book.title = new_title
            new_book.price = new_price
            new_book.page_count = new_page_count

            return new_book

    def __str__(self):
        return Publication.__str__(self) + f"No. of Pages: {self.page_count}\n"


# Main Scope
book1 = Book()
print(book1)
print()

book2 = Book()
print(book2)
print()

print(book1 + book2)