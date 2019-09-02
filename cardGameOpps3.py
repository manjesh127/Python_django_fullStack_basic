from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J K Q A'.split()

# mycard = [(s,r) for s SUITE for r in RANKS]

class Deck:
    """
    this is the deck class the object is create a deck of card to initiate play
     """

    def __init__(self):
        print("create new order deck")
        self.allcard = [(s,r) for s SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcard)

    def split_in_half(self):
        return (self.allcard[:26],self.allcard[26:])        

class Hand:
    """
    this is the hand class each player has a hand ,and can add or remove the card from hand
    """     