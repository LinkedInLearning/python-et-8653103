import random



class Deck:
    def __init__(self):
        suits = ["♥", "♦", "♣", "♠"]
        faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []

        for suit in suits:
            for face in faces:
                self.cards.append(f"{face}{suit}")

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

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

class GoFishGame:
    def __init__(self, deck, players):
        pass

deck = Deck()
deck.shuffle()

ryan = Player("Ryan")
guido = Player("Guido")

game = Game(deck, (ryan, guido))

print(ryan.cards)
print(guido.cards)