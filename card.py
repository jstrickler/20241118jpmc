
# dataclasses
from dataclasses import dataclass

@dataclass  # streamlined class creation
class XCard:
    rank: str
    suit: str


class Card: # inherits from object
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):
        return self._rank
    # rank = property(rank)

    @rank.setter
    def rank(self, value): # setter method
        if isinstance(value, str) and len(value) < 3:
            self._rank = value
        else:
            raise ValueError("Invalid rank")
    
    @property
    def suit(self): # getter property
        return self._suit

    def __str__(self):  # str(instance)
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return(f"Card('{self.rank}', '{self.suit}')")

if __name__ == "__main__":
    c = Card('8', 'Diamonds')   # Card.__init__()
    print(f"{type(c) = }")
    print(c)  # str(c)  -> __str__()
    print(f"{c = }")   #  repr(c)  ->  __repr__()
    
    print(f"{c.rank = }")
    print(f"{c.suit = }")
    
    c.rank = "8"
    print(f"{c.rank = }")
    

