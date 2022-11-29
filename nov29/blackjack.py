class Card:
    def __init__(self,rank, suits):
        self.rank = rank 
        self.suits = suits
        self.hard , self.soft = self.points()

class NumberCard(Card):
    def points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def points(self):
        return 1, 11

class 