from game.resource import HP
from enum import Enum

class CardType(Enum):
    ABILITY = 0
    MINION = 1


class Card:
    def __init__(self, type, name, text=None):
        self.name = name
        self.text = text
        self.type = type

    def __str__(self):
        return "[name: {n}, type: {t}]".format(n=self.name, t=self.type)


class Minion(Card):
    def __init__(self, name, text=None, cost=None, health=None, attack=None):
        super(Minion, self).__init__(type=CardType.MINION, name=name, text=text)
        self.cost = cost
        self.attack = attack
        self.health = health
        self.action = None

    def __str__(self):
        kwargs = {'name': self.name, 'type': str(self.type), 'cost': self.cost,
                  'attack': str(self.attack), 'health': str(self.health)}
        return "[name: {name}, type: {type}, cost: {cost}, attack: {attack},"\
                "health: {health}]]".format(**kwargs)


class Ability(Card):
    def __init__(self, name, text=None, cost=None):
        super(Ability, self).__init__(type=CardType.ABILITY, name=name, text=text)
        self.cost = cost
        self.action = None

    def __str__(self):
        kwargs = {'name': self.name, 'type': str(self.type), 'cost': self.cost}
        return "[name: {name}, type: {type}, cost: {cost}]".format(**kwargs)


class CardFactory:
    def __call__(self, *args, **kwargs):
        cards = [Ability("Card 1", cost=1),
                 Ability("Card 2", cost=2),
                 Ability("Card 3", cost=3),
                 Minion("Card 4", cost=4, health=1, attack=1),
                 Minion("Card 5", cost=5, health=2, attack=2),
                 Minion("Card 6", cost=6, health=3, attack=3),
                 Minion("Card 7", cost=7, health=4, attack=4),
                 Minion("Card 8", cost=8, health=5, attack=5),
                 Minion("Card 9", cost=9, health=6, attack=6),
                 Minion("Card 10", cost=10, health=7, attack=7)]

        return cards
