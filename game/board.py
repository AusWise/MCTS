class Board:
    def __init__(self, hero1, hero2):
        self.halfBoard1 = HalfBoard(hero1)
        self.halfBoard2 = HalfBoard(hero2)

    @property
    def hero1(self):
        return self.halfBoard1.hero

    @property
    def hero2(self):
        return self.halfBoard2.hero

    def __getitem__(self, hero):
        if hero == self.hero1:
            return self.halfBoard1

        if hero == self.hero2:
            return self.halfBoard2

        raise Exception()

class HalfBoard:
    def __init__(self, hero):
        self.hero = hero
        self.cards = set()

