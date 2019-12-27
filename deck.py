'''
Name: Alexander Zsikla
Date: 12/25/2019
deck.py

Description: This is the deck module that includes a random assortment 
             of 52 cards, as well as two functions to get the size of
             the deck and to be able to "deal the card"
'''

import card
from random import shuffle, randint

class Deck():

    deck = []

    for i in range(2,11):
        for _ in range(4):
            deck.append(card.Card(i, str(i)))

    for _ in range(4):
        deck.append(card.Card(10, 'J'))
        deck.append(card.Card(10, 'Q'))
        deck.append(card.Card(10, 'K'))
        deck.append(card.Card(11, 'A'))

    shuffle(deck)

    def __len__(self):
        return len(self.deck)

    def deal_card(self):
        rand_card = randint(0, len(self.deck) - 1)
        return (self.deck).pop(rand_card)