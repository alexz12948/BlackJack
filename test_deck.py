'''

'''

import unittest
import deck

class TestDeck(unittest.TestCase):
    def test_one(self):
        '''
        Testing the constructor and the len
        '''

        myDeck = deck.Deck()
        self.assertEqual(len(myDeck), 52)

    def test_two(self):
        '''
        Testing the deal_card function
        '''

        myDeck = deck.Deck()
        with open("/dev/null", mode='w') as myFile:
            for i in range(len(myDeck)):
                myFile.write(str(myDeck.deal_card()))

        self.assertEqual(len(myDeck), 0)

if __name__ == "__main__":
    unittest.main()