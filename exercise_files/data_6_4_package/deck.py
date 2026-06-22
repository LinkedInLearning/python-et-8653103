from data_6_4_package.suit import Suit
from data_6_4_package.face import Face
from data_6_4_package.card import Card

class Deck:
    suits = [Suit.HEART, Suit.DIAMOND, Suit.CLUB, Suit.SPADE]
    faces = [Face.ACE, Face.TWO, Face.THREE, Face.FOUR, Face.FIVE, Face.SIX, Face.SEVEN, Face.EIGHT, Face.NINE, Face.TEN, Face.JACK, Face.QUEEN, Face.KING]

    def __init__(self, cards=None):
        self.cards = cards
        if not self.cards:
            self.cards = []
            for suit in self.suits:
                for face in self.faces:
                    self.cards.append(Card(face, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __mul__(self, factor):
        return Deck(cards=self.cards * factor)

    def __str__(self):
        return f'{len(self)} cards in the deck: {[str(c) for c in self.cards]}'

    def __len__(self):
        return len(self.cards)


print(__name__)