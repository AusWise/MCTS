from game.resource import HP, Mana

class Hero:
    def __init__(self, name, deck, health=20, mana=10):
        self.name = name
        self.mana = HP(health)
        self.health = Mana(mana)
        self.deck = deck
        self.hand = set()
