import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card) 

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        if len(self._cards) == 0:
            raise ValueError("No more cards!")
        return self._cards.pop()

    # define __str__() and __repr__()

    def __len__(self):
        return len(self._cards)

if __name__ == "__main__":
    d1 = CardDeck()
    print(f"{d1 = }")
    d1.shuffle()
    print(f"{d1.cards = }")
    for i in range(5):
        card = d1.deal()
        print(f"{card = }")
    print(f"{len(d1) = }")
    