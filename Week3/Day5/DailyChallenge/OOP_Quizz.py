import random

# Part 1 : Quizz :


#     What is a class?
#         A class is a blueprint or template for creating objects that encapsulate data and behavior.
#
#     What is an instance?
#         An instance is a specific occurrence of a class, representing a unique object created based on the class blueprint.
#
#     What is encapsulation?
#         Encapsulation is the principle of bundling data and methods together within a class, hiding the internal implementation details and providing a controlled interface to interact with the object.
#
#     What is abstraction?
#         Abstraction is the process of simplifying complex systems by representing the essential features and hiding unnecessary details. It allows focusing on high-level concepts and ignoring implementation specifics.
#
#     What is inheritance?
#         Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties and behaviors from another class, called a parent or superclass. It promotes code reuse and the creation of hierarchical relationships.
#
#     What is multiple inheritance?
#         Multiple inheritance is a feature of some programming languages where a class can inherit properties and behaviors from multiple parent classes. It allows a subclass to inherit from multiple superclasses.
#
#     What is polymorphism?
#         Polymorphism refers to the ability of objects of different classes to be treated as objects of a common superclass. It allows objects to be used interchangeably, providing flexibility and extensibility in code design.
#
#     What is method resolution order or MRO?
#         Method resolution order (MRO) is the order in which methods are searched for and executed in a class hierarchy. It defines the precedence of method resolution when dealing with inheritance and multiple inheritance scenarios.







# ----------------------------------------------------------------------------------------
# Part 2: Create a deck of cards class.
# instruction: The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suit in Card.suits:
            for value in Card.values:
                card = Card(suit, value)
                self.cards.append(card)

    # instruction: should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
    def shuffle(self):
        random.shuffle(self.cards)

    # instruction: should have a method called deal which deals a single card from the deck.
    # instruction: After a card is dealt, it should be removed from the deck.
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
