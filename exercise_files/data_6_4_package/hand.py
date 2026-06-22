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

print(__name__)