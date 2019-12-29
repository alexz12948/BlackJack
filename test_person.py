'''
Name: Alexander Zsikla
Date: 12/26/2019
test_person.py

Description: 
'''

import unittest
import card
import deck
import person

class TestPerson(unittest.TestCase):
    def test_one(self):
        '''
        Testing the constructor, the len, and the total
        '''

        myDeck = deck.Deck()
        card1 = myDeck.deal_card()
        card2 = myDeck.deal_card()
        myPerson = person.Person(card1, card2)

        self.assertEqual(len(myPerson), 2)
        self.assertEqual(myPerson.get_total(), card1.get_value() + card2.get_value())

    def test_two(self):
        '''
        Testing the add card function
        '''

        myDeck = deck.Deck()
        card1 = myDeck.deal_card()
        card2 = myDeck.deal_card()
        card3 = myDeck.deal_card()
        myPerson = person.Person(card1, card2)
        myPerson.add_card(card3)

        self.assertEqual(len(myPerson), 3)
        total = card1.get_value() + card2.get_value() + card3.get_value()
        self.assertEqual(myPerson.get_total(), total)

    def test_three(self):
        '''
        Testing the num_aces function
        '''

        myDeck = deck.Deck()
        card1 = card.Card(10, "J")
        card2 = card.Card(9, "9")
        myPerson = person.Person(card1, card2)
        self.assertEqual(myPerson.num_aces(), 0)

        card3 = card.Card(11, "A")
        myPerson.add_card(card3)
        self.assertEqual(myPerson.num_aces(), 1)

    def test_four(self):
        '''
        Testing the busted function
        '''
        myDeck = deck.Deck()
        card1 = card.Card(10, "J")
        card2 = card.Card(10, "Q")
        myPerson = person.Person(card1, card2)
        self.assertEqual(myPerson.busted(), False)

        card3 = card.Card(11, "A")
        myPerson.add_card(card3)
        self.assertEqual(myPerson.busted(), False)

        card4 = card.Card(11, "A")
        myPerson.add_card(card4)
        self.assertEqual(myPerson.busted(), True)


if __name__ == "__main__":
    unittest.main()