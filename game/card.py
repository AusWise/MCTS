from game.resource import HP
from game.hero import Character
from enum import Enum

class CardType(Enum):
    ABILITY = 0
    MINION = 1

    def __str__(self):
        return self.name


class Card:
    def __init__(self, type, name, cost, text=None):
        self.name = name
        self.text = text
        self.type = type
        self.cost = cost

    def __str__(self):
        kwargs = dict(name=self.name, type=self.type, cost=self.cost)
        return "name: {name} ({type}), cost: {cost}".format(**kwargs)


class Minion(Card, Character):
    def __init__(self, name, text=None, cost=None, health=None, attack=None):
        super(Minion, self).__init__(type=CardType.MINION, name=name, cost=cost,
                                     text=text)
        self.attack = attack
        self.health = health
        self.action = None

    def __str__(self):
        card_descr = super(Minion, self).__str__()
        kwargs = {'attack': str(self.attack), 'health': str(self.health)}
        minion_descr = "attack: {attack}, HP: {health}".format(**kwargs)
        return "[{}, {}]".format(card_descr, minion_descr)


class Ability(Card):
    def __init__(self, name, text=None, cost=None):
        super(Ability, self).__init__(type=CardType.ABILITY, name=name,
                                      cost=cost, text=text)
        self.action = None

    def __str__(self):
        return "[{}]".format(super(Ability, self).__str__())


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
