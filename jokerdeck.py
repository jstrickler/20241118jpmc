from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _create_deck(self):
        super()._create_deck()
        joker1 = Card("**JOKER1**", "**JOKER1**")
        self._cards.append(joker1)
        joker2 = Card("**JOKER2**", "**JOKER2**")
        self._cards.append(joker1)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(f"{j.cards = }")
    for i in range(10):
        card = j.deal()
        print(card)
