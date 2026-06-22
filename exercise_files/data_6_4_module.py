class Suit:
    HEART = ("♥", "Hearts")
    DIAMOND = ("♦", "Diamonds")
    CLUB = ("♣", "Clubs")
    SPADE = ("♠", "Spades")

class Face:
    ACE = ("A", 1)
    TWO = ("2", 2)
    THREE = ("3", 3)
    FOUR = ("4", 4)
    FIVE = ("5", 5)
    SIX = ("6", 6)
    SEVEN = ("7", 7)
    EIGHT = ("8", 8)
    NINE = ("9", 9)
    TEN = ("10", 10)
    JACK = ("J", 11)
    QUEEN = ("Q", 12)
    KING = ("K", 13)

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
        return f'{len(self)} cards in the deck: {self.cards}'

    def __len__(self):
        return len(self.cards)

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return f'{self.face[0]}{self.suit[0]}'

    def __add__(self, card):
        return self.face[1] + card.face[1]

    def __radd__(self, int_val):
	    return int_val + self.face[1]


class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def __eq__(self, hand):
        return sum(self.cards) == sum(hand.cards)
    
    def __lt__(self, hand):
        return sum(self.cards) < sum(hand.cards)
    
    def __gt__(self, hand):
        return sum(self.cards) > sum(hand.cards)

    def __ne__(self, hand):
        return sum(self.cards) != sum(hand.cards)
    
    def __le__(self, hand):
        return sum(self.cards) <= sum(hand.cards)

    def __ge__(self, hand):
        return sum(self.cards) >= sum(hand.cards)
    
    def __str__(self):
        return ', '.join([str(c) for c in self.cards])


if __name__ == "__main__":
    print("This is supposed to be a module, not imported directly!")
