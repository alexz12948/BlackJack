'''
Name: Alexander Zsikla
Date: 12/26/2019
test_dealer.py

Description: 
'''

import unittest
import card
import deck
import dealer

class TestDealer(unittest.TestCase):
    def test_one(self):
        '''
        Constructor and Printing
        '''

        myDeck = deck.Deck()
        card1 = myDeck.deal_card()
        card2 = myDeck.deal_card()
        myDealer = dealer.Dealer(card1, card2)

        self.assertEqual(str(myDealer), myDealer.blank_card + str(card2))

if __name__ == "__main__":
    unittest.main()