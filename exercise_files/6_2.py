import random

class Deck:
    suits = ["♥", "♦", "♣", "♠"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        
        self.cards = []

        for suit in self.suits:
            for face in self.faces:
                self.cards.append(f"{face}{suit}")

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class FrenchDeck(Deck):
    faces = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"]

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    
class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.deal_cards()

    def deal_cards(self):
        for i in range(0, 7):
            for player in self.players:
                player.add_card(self.deck.deal())


ryan = Player("Ryan")
guido = Player("Guido")

deck = Deck()
print(deck.suits)