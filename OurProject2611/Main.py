from OurProject2611.Card import Card
import random

from  OurProject2611.Deckofcards import Deckofcards
c1 = Card(3,'heart')
deck = Deckofcards()
print(deck)
print(c1)
random.shuffle(deck.package)

for i in range(40):
    deck.deal_one()

print(deck.show())