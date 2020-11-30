from OurProject2611.Deckofcards import Deckofcards
from OurProject2611.Card import Card
import random


class Player:
    def __init__(self, name, pack=10):
        self.name = name
        self.pack = []

    def __str__(self):
        return f'{self.name} have the package {self.pack}'

    def show(self):
        return f'{self.name} have the package {self.pack}'

    def set_hand(self, deck, cardsnum):
        for i in range(0, cardsnum):
            self.pack.append(deck.pop(i))
        return self.pack

    def get_random_card(self):
        packlen = len(self.pack)
        randnum = random.randint(0, packlen-1)
        return self.pack[randnum]

    def add_card(self, newcard):
        self.pack.append(newcard)
        return
