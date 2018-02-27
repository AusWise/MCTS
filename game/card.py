from game.resource import HP


class Card:
    def __init__(self, name, text=None):
        self.name = name
        self.text = text

    def __str__(self):
        return self.name


class Minion(Card):
    def __init__(self, name, health, text=None):
        super(Minion, self).__init__(name=name, text=text)
        self.cost = None
        self.attack = None
        self.health = HP(health, min_value=1)
        self.action = None


class Ability(Card):
    def __init__(self, name, text=None):
        super(Ability, self).__init__(name=name, text=text)
        self.cost = None
        self.action = None


class CardFactory:
    def __call__(self, *args, **kwargs):
        cards = [Card("Card 1"), Card("Card 2"),
                 Card("Card 3"), Card("Card 4"),
                 Card("Card 5"), Card("Card 6"),
                 Card("Card 7"), Card("Card 8"),
                 Card("Card 9"), Card("Card 10")]

        return cards
