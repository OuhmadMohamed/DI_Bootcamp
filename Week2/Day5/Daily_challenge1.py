#Exercise 1: Quiz Answers

#1. What is a class? A class is a blueprint or template used to create objects. It defines the attributes (data) and methods (functions) that the objects will have.

#2. What is an instance? An instance is a specific object created from a class.

#3. What is encapsulation? Encapsulation is the practice of bundling data and methods together within a class and restricting direct access to some data

#4. What is abstraction? Abstraction means hiding implementation details and showing only the essential features of an object.

#5. What is inheritance? Inheritance allows one class to acquire the attributes and methods of another class.

#6. What is multiple inheritance? Multiple inheritance occurs when a class inherits from more than one parent class

#7. What is polymorphism? Polymorphism allows different classes to have methods with the same name but different behaviors.

#8. What is Method Resolution Order (MRO)? MRO is the order in which Python searches for methods in a class hierarchy, especially when multiple inheritance is involved.

#Exercise 2: Deck of Cards

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        """
        Creates a full deck of 52 cards and shuffles it.
        """
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(suit, value)
                      for suit in suits
                      for value in values]

        random.shuffle(self.cards)

    def deal(self):
        """
        Deals one card and removes it from the deck.
        """
        if len(self.cards) == 0:
            return "No cards left in the deck."

        return self.cards.pop()
