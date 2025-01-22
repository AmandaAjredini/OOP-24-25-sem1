class Currency(object):
    """INSERT A DOC STRING HERE"""

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP']

    RATES = {("EUR", "USD"): 1.069229,
             ("USD", "EUR"): 0.939218,
             ("EUR", "GBP"): 0.860186,
             ("GBP", "EUR"): 1.15896,
             ("USD", "GBP"): 0.81039,
             ("GBP", "USD"): 1.23396}

    def __init__(self, amount=1, currency_type='EUR'):
        # a quick way of checking for valid currencies
        # for a limited subset of valid currencies
        if currency_type in Currency.VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type: str):

        if new_currency_type == self.currency_type:
            # nothing to do
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in Currency.VALID_CURRENCIES \
                or self.currency_type not in Currency.VALID_CURRENCIES:
            print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
            return

        # Extract the exchange rate from the RATES dictionary
        rate = Currency.RATES[(self.currency_type, new_currency_type)]
        amount = self.amount * rate

        print("{} {} => {} {}".format(self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        return f"{self.amount} {self.currency_type}"

    def __repr__(self):
        return (self.amount, self.currency_type)

    def __add__(self, other_curr):

        if isinstance(other_curr, int) or isinstance(other_curr, float):
            other_curr = Currency(other_curr, self.currency_type)

        if not isinstance(other_curr, Currency):
            raise ValueError("Addition only works between Currency types")

        if self.currency_type == other_curr.currency_type:
            new_amount = self.amount + other_curr.amount
        else:
            new_other_curr = other_curr.convert_to(self.currency_type)
            new_amount = new_other_curr.amount + self.amount

        return Currency(new_amount, self.currency_type)

    def __sub__(self, other_curr):
        if isinstance(other_curr, int) or isinstance(other_curr, float):
            other_curr = Currency(other_curr, self.currency_type)

        if not isinstance(other_curr, Currency):
            raise ValueError("Subtraction only works between Currency types")

        if self.currency_type == other_curr.currency_type:
            new_amount = self.amount - other_curr.amount
        else:
            new_other_curr = other_curr.convert_to(self.currency_type)
            new_amount = new_other_curr.amount - self.amount

        return Currency(new_amount, self.currency_type)

    def __radd__(self, other_curr):
        return self.__add__(other_curr)

    def __rsub__(self, other_curr):
        return self.__sub__(other_curr)

    def __gt__(self, other_curr):
        if isinstance(other_curr, int) or isinstance(other_curr, float):
            other_curr = Currency(other_curr, self.currency_type)

        if not isinstance(other_curr, Currency):
            raise ValueError("Comparison only works between Currency types")

        if self.currency_type == other_curr.currency_type:
            return self.amount > other_curr.amount
        else:
            new_other_curr = other_curr.convert_to(self.currency_type)
            return self.amount > new_other_curr.amount


# This main is incomplete because not all methods are tested
# Some outputs are given by the comments next to the commands. Your code should be able to output these when
# you remove the '#' in the beginning of the lines

curr = Currency(7.50, 'USD')
curr2 = Currency(2, 'EUR')
#new_curr = curr2.convert_to("USD")  # 2.000000 EUR => 2.211600 USD

curr3 = curr + curr2  # curr.__add__(curr2)
print(curr3)

#print(curr) # 7.50 USD
#curr2 = Currency(2, 'EUR')
#print(curr2)  # 2.00 EUR
#new_curr = curr2.convert_to(curr.currency_type) # 2.000000 EUR => 2.211600 USD
#print(new_curr) # 2.21 USD
#sum_curr = curr + curr2 # 2.000000 EUR => 2.211600 USD
#print(sum_curr) # 9.71 USD
#sum_curr2 = curr + 5.5
#print(sum_curr2) # 13.00 USD
#print(curr > curr2)