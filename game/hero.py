from game.resource import HP, Mana

class Hero:
    def __init__(self, name, deck, health=20, mana=None):
        self.name = name
        self.mana = Mana(mana)
        self.health = health
        self.deck = deck
        self.hand = set()
