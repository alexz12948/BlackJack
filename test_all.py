'''
Name: Alexander Zsikla
Date: 12/25/2019
test_all.py

Description: runs all of the unit tests for all the modules
'''

import unittest
import card
import deck

class TestAll(unittest.TestCase):

    ### TESTING THE CARD MODULE ###
    def test_one(self):
        '''
        Testing the constructor
        '''

        mycard = card.Card()
        self.assertEqual(mycard.value, 1)
        self.assertEqual(mycard.rank, "1")

    def test_two(self):
        '''
        Testing the print
        '''

        mycard1 = card.Card(4, "4")
        mycard2 = card.Card(10, "10")
        self.assertEqual(str(mycard1), "/----\\\n|    |\n|  4 |\n|    |\n\\----/\n")
        self.assertEqual(str(mycard2), "/----\\\n|    |\n| 10 |\n|    |\n\\----/\n")

    def test_three(self):
        '''
        Testing the getter functions
        '''

        mycard = card.Card(11, "A")
        self.assertEqual(mycard.get_value(), 11)
        self.assertEqual(mycard.get_rank(), "A")

    def test_four(self):
        '''
        Testing the asserts
        '''

        #Testing a string for a value
        #mycard = card.Card("11", "A")

        # Testing an int for a rank
        #mycard = card.Card(3, 3)

        # Testing a float for a value
        # mycard = card.Card(3.0, "3")

        # Testing a string of length greater than one
        # mycard = card.Card(3, "33")
        self.assertEqual(1,1)

    ### TESTING THE DECK MODULE ###
    def test_five(self):
        '''
        Testing the constructor and the len
        '''

        mydeck = deck.Deck()
        self.assertEqual(len(mydeck), 52)

    def test_six(self):
        '''
        Testing the deal_card function
        '''

        mydeck = deck.Deck()
        with open("/dev/null", mode='w') as myFile:
            for i in range(len(mydeck)):
                myFile.write(str(mydeck.deal_card()))

        self.assertEqual(len(mydeck), 0)


if __name__ == "__main__":
    unittest.main()