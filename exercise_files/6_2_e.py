
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)


class Deck:
    suits = ["♥", "♦", "♣", "♠"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(f'{face}{suit}')

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class FrenchDeck(Deck):
    faces = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"]

class RussianDeck(Deck):
    faces = ["Т", "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К"]

class CanastaDeck(Deck):
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for face in self.faces*2:
                self.cards.append(f'{face}{suit}')
        self.cards.extend(["BJ", "BJ", "RJ", "RJ"])

class FrenchCanastaDeck(CanastaDeck, FrenchDeck):
    pass


class GameBase:
    deck_class = Deck
    starting_cards = 11
    def __init__(self, players):
        self.deck = self.deck_class()
        self.deck.shuffle()
        self.players = players
        self.deal_cards()

    def deal_cards(self):
        for i in range(0, self.starting_cards):
            for player in self.players:
                player.add_card(self.deck.deal())


class Canasta(GameBase):
	deck_class = CanastaDeck
	starting_cards = 11


p1 = Player("Ryan")
p2 = Player("Guido")
p3 = Player("Alice")
p4 = Player("Bob")

game = Canasta((p1, p2, p3, p4))

for p in game.players:
    print(p.cards)
