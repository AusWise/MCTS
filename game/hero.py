from game.resource import HP, Mana

class Hero:
    def __init__(self, name, deck, health=20, mana=1):
        self.name = name
        self.mana = Mana(mana)
        self.health = health
        self.deck = deck
        self.hand = set()

    def pick(self, n=1):
        for i in range(n):
            self.hand.add(self.deck.pop())

    def __repr__(self):
        return self.name

