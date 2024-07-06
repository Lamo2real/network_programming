from enum import Enum
import random

# Enum class representing the four suits in a deck of cards
class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4

# Class representing a single card in the deck
class Card:
    def __init__(self, suit, value):
        assert isinstance(suit, Suit), "suit must be an instance of the Suit Enum"
        assert 1 <= value <= 13, "value must be between 1 and 13"
        self._suit = suit  # Sets the suit of the card
        self._value = value  # Sets the value of the card

    def getValue(self):
        return self._value  # Returns the value of the card

    def getSuit(self):
        return self._suit  # Returns the suit of the card

    def __str__(self):
        # Maps special values to their names and keeps other values as strings
        value_names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }.get(self._value, str(self._value))
        suit_str = self._suit.name.capitalize()  # Capitalizes the suit name
        return f"{value_names} of {suit_str}"  # Returns a formatted string representing the card

# Class representing a deck of cards
class CardDeck:
    def __init__(self):
        self.cards = []  # Initializes an empty list for the cards
        self.reset()  # Populates the deck with 52 cards

    def shuffle(self):
        random.shuffle(self.cards)  # Shuffles the cards in the deck

    def getCard(self):
        return self.cards.pop()  # Removes and returns the top card from the deck

    def size(self):
        return len(self.cards)  # Returns the number of cards remaining in the deck

    def reset(self):
        # Resets the deck to the initial state with 52 cards
        self.cards = [Card(suit, value) for suit in Suit for value in range(1, 14)]

# Test code to create a deck, shuffle it, and print all cards until the deck is empty
deck = CardDeck()  # Creates a new card deck
deck.shuffle()  # Shuffles the deck
while deck.size() > 0:  # Continues until the deck is empty
    card = deck.getCard()  # Gets the top card from the deck
    print(f"Card {card}")  # Prints the card and its value
