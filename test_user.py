'''
Name: Alexander Zsikla
Date: 12/25/2019
test_all.py

Description: runs all of the unit tests for all the modules
'''

import unittest
import card
import deck
import user

class TestUser(unittest.TestCase):
    def test_one(self):
        '''
        Testing the constructor and the print
        '''

        myDeck = deck.Deck()
        card1 = myDeck.deal_card()
        card2 = myDeck.deal_card()
        myPlayer = user.User(card1, card2)

        self.assertEqual(str(myPlayer), "Balance: {0:>6}\nBet: {1:>10}\n{2}\n{3}".format(100, 0, str(card1), str(card2)))

    def test_two(self):
        '''
        Testing anti_up
        '''

        myDeck = deck.Deck()
        myPlayer = user.User(myDeck.deal_card(), myDeck.deal_card())

        myPlayer.anti_up()
        self.assertEqual(myPlayer.get_balance(), 95)

    def test_three(self):
        '''
        Testing bet, overspent
        '''

        myDeck = deck.Deck()
        myPlayer = user.User(myDeck.deal_card(), myDeck.deal_card())

        self.assertEqual(myPlayer.bet(101), False)

    def test_four(self):
        '''
        Testing bet, perfect amount
        '''

        myDeck = deck.Deck()
        myPlayer = user.User(myDeck.deal_card(), myDeck.deal_card())

        self.assertEqual(myPlayer.bet(100), True)
        self.assertEqual(myPlayer.get_balance(), 0)
        self.assertEqual(myPlayer.get_bet_amount(), 100)

    def test_five(self):
        '''
        Testing end_round, won = True
        '''

        myDeck = deck.Deck()
        myPlayer = user.User(myDeck.deal_card(), myDeck.deal_card())

        myPlayer.bet(100)
        myPlayer.end_round(True)

        self.assertEqual(myPlayer.get_balance(), 200)
        self.assertEqual(myPlayer.get_bet_amount(), 0)

    def test_six(self):
        '''
        Testing end_round, won = False
        '''

        myDeck = deck.Deck()
        myPlayer = user.User(myDeck.deal_card(), myDeck.deal_card())

        myPlayer.bet(50)
        myPlayer.end_round(False)

        self.assertEqual(myPlayer.get_balance(), 50)
        self.assertEqual(myPlayer.get_bet_amount(), 0)


if __name__ == "__main__":
    unittest.main()