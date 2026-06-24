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
    
