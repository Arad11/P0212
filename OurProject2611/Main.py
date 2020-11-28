from OurProject2611.Card import Card
from  OurProject2611.Player import Player

import random
from  OurProject2611.Deckofcards import Deckofcards

c1 = Card(3,'heart')
deck = Deckofcards()

p1 = Player("arad", 5)
p1.set_hand()
print(p1.pack)
p1.add_card((3,'heart'))
print(p1.pack)