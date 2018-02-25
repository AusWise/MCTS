DEFAULT_INIT_HEALTH = 20

class Hero:
    def __init__(self, deck, health=DEFAULT_INIT_HEALTH):
        self.mana = None
        self.deck = deck
        self.health = health
        self.hand = set()