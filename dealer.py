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

    def __str__(self):
        to_print = self.blank_card

        for i in range(1, len(self.cards)):
            to_print += str(self.cards[i])

        return to_print