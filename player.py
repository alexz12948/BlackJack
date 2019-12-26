'''
Name: Alexander Zsikla
Date: 12/25/2019
player.py

Description: This is the player module
'''

import card

class Player():

    balance = 100
    bet = 0

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def __str__(self):
        return "Balance: {0:>6}\nBet: {1:>6}".format(self.balance, self.bet)

    def anti_up(self):
        self.balance -= 5

    def bet(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            self.bet = amount
            return True

    def end_round(self, won):
        if won:
            self.balance += (2 * self.bet)
        else:
            self.bet = 0
