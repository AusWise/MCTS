from abc import ABC, abstractmethod
from game.exception import NotEnoughPoints


class Action(metaclass=ABC):
    @abstractmethod
    def perform(self, attacker, victim, card):
        pass


class BasicAttack(Action):
    def perform(self, attacker, victim, card):
        attack_cost = card.cost
        if attacker.mana.has_points_left(attack_cost):
            attacker.mana.subtract(attack_cost)
            victim.hp.subtract(card.attack)
        else:
            raise NotEnoughPoints("Player {} has no enough mana to perform\
                                  this action.".format(attacker.name))
