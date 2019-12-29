'''
Name: Alexander Zsikla
Date: 12/25/2019
person.py

Description: This is the player module
'''

import card

class Person:
    def __init__(self, card1=card.Card(), card2=card.Card()):
        self.cards = [card1, card2]
        self.total = card1.get_value() + card2.get_value()

    def __len__(self):
        return len(self.cards)

    def get_total(self):
        if self.total > 21:
            return self.total - (self.num_aces() * 10)

        return self.total

    def add_card(self, card=card.Card()):
        self.total += card.get_value()
        (self.cards).append(card)

    def num_aces(self):
        aces = [card for card in (self.cards) if card.get_rank() == 'A']
        return len(aces)

    def busted(self):
        total = self.total - (self.num_aces() * 10)

        if total > 21:
            return True
        
        return False
