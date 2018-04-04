import random
from game.resource import HP, Mana
from game.move import *


class Character:
    def lose_health(self, points):
        self.health -= points

    def is_alive(self):
        return self.health > 0


class BaseHero(Character):
    def __init__(self, name, deck, health=20, mana=1):
        self.name = name
        self.mana = Mana(mana)
        self.health = health
        self.deck = deck
        self.hand = set()

    @property
    def hand_minions(self):
        from game.card import CardType
        return list(filter(lambda c: c.type == CardType.MINION, self.hand))

    @property
    def hand_abilities(self):
        from game.card import CardType
        return list(filter(lambda c: c.type == CardType.ABILITY, self.hand))

    def pick(self, n=1):
        cards_numb = min(len(self.deck), n)
        for i in range(cards_numb):
            self.hand.add(self.deck.pop())

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)

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


class Hero(BaseHero):
    pass


class AI(BaseHero):
    def choose_move(self, moves):
        raise NotImplemented

    def choose_move(self, moves):
        return min(moves, key=self._get_move_index)

    def _get_move_index(self, move):
        return self._order.index(type(move))


class RandomAI(AI):
    def choose_move(self, moves):
        return random.choice(moves)


class DefensiveAI(AI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._order = [MinionVsMinion, MinionVsHero, PlayMinionCard, PlayAbilityCard, FinishTurn]

class OffensiveAI(AI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._order = [MinionVsHero, MinionVsMinion, PlayMinionCard, PlayAbilityCard, FinishTurn]
