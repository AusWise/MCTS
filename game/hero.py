from game.resource import HP, Mana

class Character:
    def lose_health(self, points):
        self.health -= points

    def is_alive(self):
        return self.health > 0


class Hero(Character):
    def __init__(self, name, deck, health=20, mana=1):
        self.name = name
        self.mana = Mana(mana)
        self.health = health
        self.deck = deck
        self.hand = set()

    def pick(self, n=1):
        for i in range(n):
            self.hand.add(self.deck.pop())

    def burn_mana(self, points):
        self.mana.points -= points

    def has_enough_mana(self, cost):
        return self.mana.points >= cost

    def __str__(self):
        mana = self.mana
        hp = self.health
        return "{}: [HP:{}/{}, mana: {}/{}]".format(
            self.name, hp, 20, mana.points, mana._max)

    def __repr__(self):
        return self.name
