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

    def show(self):
        return f'{self.name} have the package {self.pack}'


    def set_hand(self):
        pack = Deckofcards()
        pack = pack.suffle_the_pack()
        num = random.randint(1, 26)
        newpack = []
        for i in range(0,num-1):
            newpack.append(pack[i])
            self.pack = newpack
        return self.pack

    def random_card(self):
        packlen = len(self.pack)
        randnum = random.randint(0, packlen)
        return self.pack[randnum]

    def add_card(self, newcard):
        self.pack.append(newcard)
        return




