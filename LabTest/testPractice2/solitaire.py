import random


class Card:
    """Represents a single playing card."""
    SUITS = ['S', 'D', 'H', 'C']  # Spades, Diamonds, Hearts, Clubs
    RANKS = list(range(1, 14))  # Ace to King
    RANK_NAMES = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    COLOR = {'H': 'red', 'D': 'red', 'C': 'black', 'S': 'black'}  # Color based on suit

    def __init__(self, rank, suit):
        """
        Initialize a Card object.

        :param rank: Rank of the card (1-13).
        :param suit: Suit of the card ('S', 'D', 'H', 'C').
        """
        # Convert rank from string to integer if necessary
        if isinstance(rank, str):
            rank = {v: k for k, v in self.RANK_NAMES.items()}.get(rank, None)
            if rank is None:  # If rank is not valid
                raise ValueError("Invalid rank.")
        if rank not in self.RANKS:
            raise ValueError("Invalid rank.")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit.")

        self.rank = rank
        self.suit = suit

    def get_rank(self) -> int:
        """Return the rank of the card."""
        return self.rank

    def get_suit(self) -> str:
        """Return the suit of the card."""
        return self.suit

    def get_value(self) -> int:
        """Return value for sorting: Ace is 1, Jack is 11, Queen is 12, King is 13"""
        return self.rank

    def get_color(self):
        """Return color based on suit"""
        return self.COLOR[self.suit]

    def set_rank(self, new_rank):
        """Updates the rank of the card."""
        self.rank = new_rank

    def set_suit(self, new_suit):
        """Updates the suit of the card."""
        self.suit = new_suit

    def __str__(self):
        """Return a string representation of the card."""
        rank_str = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}.get(self.rank, str(self.rank))
        return f"{rank_str}{self.suit}"

    def __repr__(self):
        """Return a detailed string representation."""
        return f"Card(rank={self.rank}, suit='{self.suit}')"


class Deck:
    """Represents a standard deck of 52 playing cards."""

    def __init__(self):
        """Initialize a deck with 52 cards."""
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def deal(self):
        """
        Draw a card from the deck.
        :return: A Card object.
        :raises IndexError: If the deck is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot draw from an empty deck.")
        return self.cards.pop()

    def reset(self):
        """Reset the deck to 52 cards and shuffle."""
        self.__init__()
        self.shuffle()

    def is_empty(self):
        """Return True if the deck is empty, False otherwise."""
        return len(self.cards) == 0

    def __len__(self):
        """Return the number of cards remaining in the deck."""
        return len(self.cards)

    def __str__(self):
        """Return a string representation of all cards in the deck."""
        return " ".join(str(card) for card in self.cards)

    def __repr__(self):
        """Return a detailed string representation."""
        return f"Deck(cards={self.cards})"


# Tableau class
class Tableau:
    def __init__(self):
        self.columns = [[] for _ in range(7)]  # 7 columns of cards

    def add_cards_to_column(self, column_index, cards):
        """Add a list of cards to a tableau column."""
        self.columns[column_index].extend(cards)

    def get_top_card(self, column_index):
        """Return the top card of a given tableau column"""
        if self.columns[column_index]:
            return self.columns[column_index][-1]
        return None

    def is_empty(self, column_index):
        """Check if a column is empty"""
        return len(self.columns[column_index]) == 0

    def __str__(self):
        """Display tableau columns"""
        return '\n'.join([f"Column {i + 1}: " + ' '.join(str(card) for card in col) for i, col in enumerate(self.columns)])


# Foundation class
class Foundation:
    def __init__(self):
        self.piles = {'H': [], 'D': [], 'C': [], 'S': []}  # Each pile for a suit

    def can_place_in_foundation(self, card):
        """Check if a card can be placed in the foundation"""
        pile = self.piles[card.suit]
        if not pile:
            return card.get_rank() == 1  # Only Aces can go in an empty pile
        top_card = pile[-1]
        return top_card.get_value() + 1 == card.get_value()  # Stack cards in ascending order

    def place_card(self, card):
        """Place a card in the correct suit pile in the foundation"""
        self.piles[card.suit].append(card)

    def __str__(self):
        """Display foundation piles"""
        return '\n'.join([f"{suit}: " + ' '.join(str(card) for card in self.piles[suit]) for suit in self.piles])


# Stock class
class Stock:
    def __init__(self, deck):
        self.cards = deck
        self.used_cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        """Deal one card from stock to the tableau"""
        if not self.cards:
            self.cards = self.used_cards
            self.used_cards = []
            self.shuffle()
        card = self.cards.pop()
        self.used_cards.append(card)
        return card


# Game class
class EasthavenSolitaire:
    def __init__(self):
        # Initialize all components: tableau, foundation, stock
        self.tableau = Tableau()
        self.foundation = Foundation()
        self.stock = Stock(self.create_deck())
        self.stock.shuffle()
        self.setup_tableau()

    def create_deck(self):
        """Create and return a shuffled deck of 52 cards"""
        deck = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(deck)
        return deck

    def setup_tableau(self):
        """Setup the tableau with 7 columns of 3 cards each"""
        for i in range(7):
            for j in range(i + 1):
                self.tableau.add_cards_to_column(i, [self.stock.deal()])

    def move_within_tableau(self, from_col, to_col):
        """Move a card within the tableau if rules are met"""
        from_col -= 1
        to_col -= 1
        top_from_card = self.tableau.get_top_card(from_col)
        top_to_card = self.tableau.get_top_card(to_col)

        if top_from_card and (top_to_card is None or self.is_valid_move(top_from_card, top_to_card)):
            self.tableau.columns[to_col].append(self.tableau.columns[from_col].pop())
            print(f"Moved {top_from_card} from Column {from_col + 1} to Column {to_col + 1}")
        else:
            print("Invalid move within tableau")

    def is_valid_move(self, card1, card2):
        """Check if a move from card1 to card2 is valid (down rank and alternating color)"""
        return (card1.get_value() == card2.get_value() - 1) and (card1.get_color() != card2.get_color())

    def move_to_foundation(self, column_index):
        """Move the top card of a tableau column to the foundation if valid"""
        column_index -= 1
        card = self.tableau.get_top_card(column_index)
        if card and self.foundation.can_place_in_foundation(card):
            self.foundation.place_card(self.tableau.columns[column_index].pop())
            print(f"Moved {card} to the foundation")
        else:
            print(f"Cannot move {card} to foundation")

    def deal_from_stock(self):
        """Deal a card from the stock to each tableau column"""
        for i in range(7):
            self.tableau.add_cards_to_column(i, [self.stock.deal()])
        print("Dealt cards from the stock to each tableau column.")

    def game_loop(self):
        """Main game loop"""
        while True:
            print("\nTableau:\n", self.tableau)
            print("\nFoundation:\n", self.foundation)
            print("\nCommands: move_within_tableau, move_to_foundation, deal_from_stock, quit")
            command = input("Enter command: ").strip().lower()

            if command == "quit":
                print("Exiting the game.")
                break
            elif command.startswith("move_within_tableau"):
                _, from_col, to_col = command.split()
                self.move_within_tableau(int(from_col), int(to_col))
            elif command.startswith("move_to_foundation"):
                _, column = command.split()
                self.move_to_foundation(int(column))
            elif command == "deal_from_stock":
                self.deal_from_stock()
            else:
                print("Invalid command")


# Play the game
game = EasthavenSolitaire()
game.game_loop()




# Main Scope
# = Deck()
#a_deck.shuffle()
#a_card = a_deck.deal()
#print(a_card)

#print(a_card.get_suit())
#print(a_card.get_rank())

#jack_of_clubs = Card('J', 'C')
#print(jack_of_clubs)

#print(a_deck)