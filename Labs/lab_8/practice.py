class ShoppingCart(object):

    currency_values = ["EUR", "USD", "GBP"]

    def __init__(self, items: dict = None, currency: str = "EUR"):
        """Initializes an empty shopping cart."""

        if currency not in ShoppingCart.currency_values:
            print("Currency not valid.")
            exit()

        self.currency = currency

        if items == None:
            self.items = {}
        else:
            self.items = items

    def add_item(self, name, price, quantity=1):
        """Adds an item to the cart or updates its quantity if already present."""
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name):
        """Removes an item from the cart."""
        if name in self.items:
            del self.items[name]
        else:
            print(f"Item '{name}' not found in the cart.")

    def get_total(self) -> float:
        """Calculates the total cost of items in the cart."""
        total = 0  # Initialize total cost to 0

        for value in self.items.values():  # Iterate over all items in the cart
            total += value  # Add the cost of the current item to total

        return total  # Return the calculated total

    def get_currency(self) -> float:
        return self.currency

    def set_currency(self, new_currency) -> None:
        rate_map = {("EUR", "USD"): 0.9, ("USD", "EUR"): 1.1}

        # find correct rate
        for pair, value in rate_map.items():
            if pair[0] == self.currency and pair[1] == new_currency:
                rate = value

        # update the prices
        for item in self.items:
            self.items[item] = self.items[item] * rate

        self.currency = new_currency

    def discount(self, amount):
         # update the prices
        for item in self.items:
            self.items[item] = self.items[item]  * (1 - amount)

    def __str__(self):
        result_str = ""
        if len(self.items) == 0:
            result_str = "Shopping cart is empty"
            return result_str
        else:
            result_str += "Items\n"

            if self.currency == "EUR":
                symbol = "€"

            if self.currency == "USD":
                symbol = "$"



        for item, value in self.items.items():
            result_str += f"{item:<10s}: {value}-{symbol}\n"

        return result_str 


# Example usage:
cart = ShoppingCart()
cart.add_item("Laptop", 1000, 1)
cart.add_item("Smartphone", 500, 2)


cart.add_item("Laptop", 1000, 1)  # Add another laptop
cart.remove_item("Smartphone")   # Remove smartphone


# class Attendee:
#     # Class variable to track the total number of people in the meeting
#     people_in_meeting = 0

#     def __init__(self):
#         """Increases the number of people in the meeting when a new Attendee is created."""
#         Attendee.people_in_meeting += 1  # A new person joins the meeting
#         print(f"Welcome! There are {Attendee.people_in_meeting} people in the meeting.")

#     def leave_meeting(self):
#         """Decreases the number of people in the meeting when this Attendee leaves."""
#         if Attendee.people_in_meeting > 0:
#             Attendee.people_in_meeting -= 1
#             print(f"Someone left the meeting. There are now {Attendee.people_in_meeting} people in the meeting.")
#         else:
#             print("No one is in the meeting to leave.")

#     def get_people_in_meeting(self):
#         """Returns the current number of people in the meeting."""
#         return Attendee.people_in_meeting

# # Example usage:
# attendee1 = Attendee()  # First attendee joins
# attendee2 = Attendee()  # Second attendee joins
# attendee3 = Attendee()  # Third attendee joins

# # Someone leaves the meeting
# attendee2.leave_meeting()

# # Display current number of people
# print(f"Current people in meeting: {attendee1.get_people_in_meeting()}")


class WizCoinPurse:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        """Initializes a WizCoinPurse with the given number of galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def knuts_value(self):
        """Returns the total value of the purse in knuts."""
        total_knuts = self.knuts + (self.sickles * 29) + (self.galleons * 493)
        return total_knuts

    def weight(self):
        """Returns the weight of the purse in grams."""
        total_weight = (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5)
        return total_weight

    def __str__(self):
        """Returns a string representation of the WizCoinPurse."""
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

# Example usage:
purse = WizCoinPurse(galleons=2, sickles=10, knuts=15)
print(purse)
print("Value of purse in knuts:", purse.knuts_value())
print(f"Weight: {purse.weight()} grams")