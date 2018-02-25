class Card:
    def __init__(self, name, text=None):
        self.name = name
        self.text = text

    def __str__(self):
        return self.name

class Ability(Card):
    def __init__(self):
        self.cost = None
        self.action = None

class Minion(Card):
    def __init__(self):
        self.cost = None
        self.attack = None
        self.health = None
        self.action = None