class Card:
    def __init__(self,rank, suits):
        self.rank = rank 
        self.suits = suits
        

    def __str__(self):
         return f"{self.rank}"

class NumberCard(Card):
    def points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def points(self):
        return 1, 11

class FaceCard(Card):
        def points(self):
            return 10, 10
        
    
        
t = Card("Ace", 10)
print(t)