class Board:
    def __init__(self, hero1, hero2):
        self.halfBoard1 = HalfBoard(hero1)
        self.halfBoard2 = HalfBoard(hero2)

class HalfBoard:
    def __init__(self, hero):
        self.hero = hero
        self.cards = set()