from OurProject2611.Card import Card
from OurProject2611.Player import Player
import random
from OurProject2611.Deckofcards import Deckofcards
from OurProject2611.CardGame import CardGame


c = CardGame("Nitzan", "Arad")

print(c.player1.show())
print(c.player2.show())
for i in range(10):
    lst1=c.player1.get_random_card()
    lst2=c.player1.get_random_card()
    card1=Card(lst1[0], lst1[1])
    card2=Card(lst2[0], lst2[1])
    card1.war(card2)