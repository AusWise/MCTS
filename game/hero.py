from game.resource import HP, Mana

class Hero:
    def __init__(self, deck, health=20, mana=10):
        self.mana = HP(health)
        self.health = Mana(mana)
        self.deck = deck
        self.hand = set()
