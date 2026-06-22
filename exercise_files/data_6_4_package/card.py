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


print(__name__)