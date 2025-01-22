
class Book(object):
     def __init__(self, name: str, publisher: str, price: float, author: str, isbn: str):
          self.name = name
          self.publisher = publisher
          self.price = price
          self.author = author
          self.isbn = isbn
          self.ratings = {} # Dictionary to store user ratings

     def add_rating(self, user, rating):
          ''' Adds a rating to a book '''
          if 1 <= rating <= 5:
               self.ratings[user] = rating
          else:
               raise ValueError("Rating must be between 1 and 5.")

     def average_rating(self):
          ''' Returns the average rating of a book '''
          if self.ratings:
               return sum(self.ratings.values()) / len(self.ratings)
          return None

     def get_price(self):
          ''' Returns the price of a book '''
          if not isinstance(self, Book):
               raise TypeError("Not a book. Please enter a type of book to see the price.")

          return self.price

     def update_price(self, new_price):
          ''' Updates the price of a book '''
          if new_price <= 0:
               raise ValueError("Price must be a positive number")
          self.price = new_price

     def discount(self, percentage):
          if not (0 < percentage < 100):
               raise ValueError("Discount percentage must be between 0 and 100")
          self.price -= self.price * (percentage/100)

     def __gt__(self, other):
          ''' Compares the price of two books and displays which is more expensive '''
          if not isinstance(other, Book):
               raise TypeError("Comparison can only occur between two books.")

          return self.price > other.price

     def __eq__(self, other):
          ''' Compares the ISBN of two books and displays if they are the same book '''

          if not isinstance(other, Book):
               raise TypeError("Comparison can only occur between two books.")

          return self.isbn == other.isbn

     def __str__(self):
          return (f"Book\n"
                  f"Average Rating: {self.average_rating()}\n"
                  f"Name: {self.name}\n"
                  f"Author: {self.author}\n"
                  f"Publisher: {self.publisher}\n"
                  f"ISBN: {self.isbn}\n"
                  f"Price: {self.price:.2f}\n")

class PuzzleBook(Book):
     def __init__(self, name: str, publisher: str, price: float, author: str, isbn: str, puzzle_type: str, difficulty: str, sample_puzzle: str):
          Book.__init__(self, name, publisher, price, author, isbn)
          self.puzzle_type = puzzle_type
          self.difficulty = difficulty
          self.sample_puzzle = sample_puzzle

     def __str__(self):
          return Book.__str__(self) + (f"Puzzle Type: {self.puzzle_type}\n"
                                       f"Difficulty: {self.difficulty}\n"
                                       f"Sample Puzzle: {self.sample_puzzle}\n")



# Main Scope
b1 = Book("The BFG", "The Book Co.", 12.99, "Roald Dahl", "978-3-16-148410-0")
b2 = Book("Matilda", "The Book Co.", 12.99, "Roald Dahl", "978-3-16-148410-1")

print(b1)
print(b2)

print(b1.get_price())
print(b1 > b2)
print(b1 == b2)

pb1 = PuzzleBook("Ultimate Sudoku", "PuzzlePress", 19.99, "Puzzle Master", "789-0123456789", "Sudoku", "Hard", "3x3 Sudoku Grid")
print(pb1)

print(pb1 > b1)
b1.add_rating("Mandy123", 5)
b1.add_rating("Poppy9090", 3)
print(b1.average_rating())
print(b1)

b2.update_price(10.99)
print(b2)

b1.discount(10)
print(b1)