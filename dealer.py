'''
Name: Alexander Zsikla
Date: 12/26/2019
dealer.py

Description: 
'''

import card
import deck
import person

class Dealer(person.Person):
    blank_card = "/----\\\n|    |\n Blank\n|    |\n\\----/\n"

    dealer_round = False

    def switch_round(self):
        self.dealer_round = not (self.dealer_round)

    def __str__(self):
        if self.dealer_round:
            return '\n'.join([str(card) for card in (self.cards)]) + \
                   "\nTotal: {:3}".format(self.get_total())

        to_print = self.blank_card

        for i in range(1, len(self.cards)):
            to_print += str(self.cards[i])
            to_print += "\n"

        return to_print
