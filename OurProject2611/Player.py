from OurProject2611.Deckofcards import Deckofcards
from OurProject2611.Card import Card
import random

class Player:
    def __init__(self, name, pack=10):
        self.name = name
        deck = Deckofcards()
        deck.suffle_the_pack()
        self.pack = deck.package


    def __str__(self):
        return f'{self.name} have the package {self.pack}'


    def set_hand(self):
        pack = Deckofcards()
        pack = pack.suffle_the_pack()
        num = random.randint(1, 26)
        newpack = []
        for i in range(1,num):
            # x = pack[i]
            newpack.append(pack[i])
        return newpack