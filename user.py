'''
Name: Alexander Zsikla
Date: 12/25/2019
user.py

Description: This is the player module
'''

import card
import deck
import person

class User(person.Person):

    balance = 100
    my_bet = 0

    def __str__(self):
        return "Balance: {0:6}\nBet: {1:10}\n".format(self.balance, self.my_bet) + \
                '\n'.join([str(card) for card in (self.cards)]) + "\nTotal: {:3}".format(self.get_total())

    def get_balance(self):
        return self.balance

    def set_balance(self, new):
        self.balance = new

    def get_bet_amount(self):
        return self.my_bet

    def anti_up(self):
        self.balance -= 5

    def bet(self, amount):
        assert(type(amount) == int)

        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            self.my_bet = amount
            return True

    def end_round(self, won):
        assert(type(won) == bool)

        if won:
            self.balance += (2 * self.my_bet)
            self.my_bet = 0
        else:
            self.my_bet = 0