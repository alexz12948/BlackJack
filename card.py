'''
Name: Alexander Zsikla
Date: 12/25/2019
card.py

Description: This is the card module that contains a constructor,
             a print module, and getters for the user assigned values
'''

class Card():
    def __init__(self, value=1, rank='1'):
        assert (type(value) == int)
        assert (type(rank) == str and (len(rank) == 1 or rank == "10"))

        self.value = value
        self.rank = rank

    def __str__(self):
        r1 = f"/----\\\n"
        blank_row = f"|    |\n"
        r3 = "| {0:>2} |\n".format(self.rank)
        r5 = f"\\----/"
        return r1 + blank_row + r3 + blank_row + r5

    def get_value(self):
        return self.value

    def get_rank(self):
        return self.rank
