# Lab Test 2
# Name: Amanda Ajredini
# Student Number: C23388586
# Date: 03/12/2024


import random

class GameParticipant:
    """Class to represent a game participant"""

    def __init__(self, name: str, age: int, balance: float = 0):
        self.name = name
        self.age = age
        self.balance = balance

    def getName(self):
        """Method that returns the name of the participant"""
        return self.name

    def getAge(self):
        """Method that returns the age of the participant"""
        return self.age

    def getBalance(self):
        """Method that returns the balance of the participant"""
        return self.balance

    def increase_balance(self, amount: float):
        """Method that increases the balance of the participant"""

        # Only increase the balance if the amount is a positive value
        if amount < 0:
            raise ValueError("Amount to add must be positive.")

        self.balance += amount

    def decrease_balance(self, amount: float):
        """Method that decreases the balance of the participant"""

        # Check if amount is a negative number
        if amount < 0:
            raise ValueError("Amount to reduce must be positive.")

        # Check if user's balance is greater than amount to decrease it by
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount

    def __str__(self):
        return (f"Player:\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Balance: {self.balance}\n")


class Player(GameParticipant):
    """Class to represent a player"""

    def __init__(self, name: str, age: int, balance: float):
        GameParticipant.__init__(self, name, age, balance)
        self.current_bet = 0
        self.choice = ''

    def place_bet(self, amount: float, choice: str):
        """Method that allows player to place a bet"""

        # Make sure the bet amount is positive
        if amount <= 0:
            raise ValueError("Bet amount must be positive.")

        # Make sure user has enough in their balance to place bet amount
        if amount > self.balance:
            raise ValueError("Insufficient balance to place the bet.")


        self.decrease_balance(amount) # Decrease bet from their balance
        self.current_bet = amount
        self.choice = choice


    def check_win(self, dice_sum: int) -> bool:
        """ Check if the player won based on outcome of the dice."""

        # If dice sum is even, outcome is "cho", if sum is odd, outcome is "han"
        if dice_sum % 2 == 0:
            outcome = "cho"
        else:
            outcome = "han"

        # If the user's choice is equal to the outcome
        if self.choice == outcome:
            win = self.current_bet * 2 # Double their bet amount and add it to balance
            self.increase_balance(win)
            self.current_bet = 0
            return True

        # If user's choice is different to the outcome
        else:
            self.current_bet = 0
            return False

    def __str__(self):
        return GameParticipant.__str__(self) + f"\nCurrent bet: {self.current_bet}"


class DiceCup:
    """Class to represent a dice cup"""
    def __init__(self):
        self.dice = [0, 0]

    def roll(self) -> int:
        """Method that rolls the dice using random module"""

        self.dice[0] = random.randint(1, 6)
        self.dice[1] = random.randint(1, 6)
        return sum(self.dice)

    def outcome(self, dice_sum: int) -> str:
        """Method that returns the outcome of the dice cup"""
        if dice_sum % 2 == 0:
            return "cho"
        else:
            return "han"

    def __str__(self):
        dice_sum = sum(self.dice)
        return f"\nDice rolled: {self.dice}, Sum: {dice_sum}, Outcome: {self.outcome(dice_sum)}\n"



# Main scope

# Create instances
p1 = Player("Amanda", 20, 400.0)
dice_cup = DiceCup()


# Simulate single round of Cho-Han
print(f"Welcome to Cho-han\n"
      f"Place a bet on whether the sum of the dice will be \"cho\" (even) or \"han\" (odd).")

print(f"Current balance: {p1.getBalance()}")
bet_amount = float(input("Enter your bet amount: "))
choice = input('Enter your choice ("cho" for even, "han" for odd): ').lower()

# Place bet
p1.place_bet(bet_amount, choice)

# Roll the dice
dice_sum = dice_cup.roll()
print(dice_cup)

# Check if player wins
player_won = p1.check_win(dice_sum)

# Print round outcome
if player_won:
    print("Congratulations! You won the round!")
else:
    print("Better luck next time!")

print(f"Updated balance: {p1.getBalance()}")









