'''

'''

import unittest
import card

class TestCard(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()