'''
Name: Alexander Zsikla
Date: 12/25/2019
test_all.py

Description: runs all of the unit tests for all the modules
'''

import unittest
import card
import deck
import player

class TestPlayer(unittest.TestCase):
    def test_one(self):
        '''
        Testing the constructor and the print
        '''

        myDeck = deck.Deck()
        card1 = myDeck.deal_card()
        card2 = myDeck.deal_card()
        myPlayer = player.Player(card1, card2)

        self.assertEqual(str(myPlayer), "Balance: {0:>6}\nBet: {1:>6}\n{2}{3}\n".format(100, 0, str(card1), str(card2)))

    def test_two(self):
        '''
        Testing anti_up
        '''

        myDeck = deck.Deck()
        myPlayer = player.Player(myDeck.deal_card(), myDeck.deal_card())

        myPlayer.anti_up()
        self.assertEqual(myPlayer.get_balance(), 95)

    def test_three(self):
        '''
        Testing bet
        '''

        myDeck = deck.Deck()
        myPlayer = player.Player(myDeck.deal_card(), myDeck.deal_card())

if __name__ == "__main__":
    unittest.main()