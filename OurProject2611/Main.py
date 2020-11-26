from OurProject2611.Card import Card
from  OurProject2611.Player import Player
import random
from  OurProject2611.Deckofcards import Deckofcards

c1 = Card(3,'heart')
deck = Deckofcards()
deck.package
print(deck)
print(c1)
random.shuffle(deck.package)



print(deck.show())
p1 = Player("arad", 6)
p1.set_hand()
print(p1)