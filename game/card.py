from game.resource import HP
from game.hero import Character
from enum import Enum

class CardType(Enum):
    ABILITY = 0
    MINION = 1

    def __str__(self):
        return self.name

class Card:
    def __init__(self, type, name, cost, text=None, ability=None):
        self.name = name
        self.text = text
        self.type = type
        self.cost = cost
        self.ability = ability

    def has_ability(self):
        return self.ability is not None

    def __str__(self):

        kwargs = dict(name=self.name, type=self.type, cost=self.cost)
        return "{name} ({type}), cost: {cost}".format(**kwargs)


class Minion(Card, Character):
    def __init__(self, name, text=None, cost=None, health=None, attack=None, ability=None):
        super(Minion, self).__init__(type=CardType.MINION, name=name, cost=cost,
                                     text=text, ability=ability)
        self.attack = attack
        self.health = health

        self.used = True

    def __str__(self):
        used = "(USED) " if self.used else ""
        card_descr = super(Minion, self).__str__()
        kwargs = {'attack': str(self.attack), 'health': str(self.health)}
        minion_descr = "attack: {attack}, HP: {health}".format(**kwargs)
        return "[{}, {}]".format(card_descr, minion_descr)


class Spell(Card):
    def __init__(self, name, text=None, cost=None, ability = None):
        super(Spell, self).__init__(type=CardType.ABILITY, name=name,
                                      cost=cost, text=text, ability=ability)



    def __str__(self):
        return "[{}]".format(super(Spell, self).__str__())

class CardFactory:
    def __call__(self, *args, **kwargs):
        cards = [
                 arcaneExplosion,
                 vanish,
                 whirlwind,
                 Minion("Acidic Swamp Ooze", cost=2, attack=3, health=2),
                 Minion("Archmage", cost=6, attack=4, health=7),
                 Minion("Bloodfen Raptor", cost=2, attack=3, health=2),
                 Minion("Chillwind Yeti", cost=4, attack=4, health=5),
                 Minion("Booty Bay Bodyguard", cost=5, attack=5, health=4),
                 Minion("Kor'kron Elite", cost=4, attack=4, health=3, ability=charge),
                 Minion("Bluegill Warrior", cost=2, attack=2, health=1, ability=charge)
                ]

        return cards

def charge(state, card):
    card.used = False

class Ability:
    def __init__(self, damage=None):
        self.damage = damage

    def has_damage(self):
        return self.damage is not None

class DamageAllMionions(Ability):
    def __init__(self, damage=1):
        Ability.__init__(self, damage=damage)

    def __call__(self, state):
        for panel in state.board.panels.values():
            to_delete = []
            for minion in panel.minions:
                minion.lose_health(self.damage)

                if not minion.is_alive():
                    to_delete.append(minion)

            for minion in to_delete:
                panel.remove_card(minion)


damage_all_minions = DamageAllMionions()

class ReturnMinions(Ability):
    def __call__(self, state):
        self._return_minions(state, state.active_player)
        self._return_minions(state, state.enemy)

    def _return_minions(self, state, player):
        panel = state.board._panels[player]
        minions = set(panel.minions)
        panel.cards -= minions
        player.hand = player.hand | minions

return_minions = ReturnMinions()

class DamageEnemyMinions(Ability):
    def __init__(self, damage=1):
        Ability.__init__(self, damage=damage)

    def __call__(self, state):
        to_delete = []
        for minion in state.enemy_panel.minions:
            minion.lose_health(self.damage)

            if not minion.is_alive():
                to_delete.append(minion)

        for minion in to_delete:
            state.enemy_panel.remove_card(minion)

damage_enemy_minions = DamageEnemyMinions()

arcaneExplosion = Spell("Arcane Explosion", cost=2, ability = damage_enemy_minions)
vanish = Spell("Vanish", cost=6, ability = return_minions)
whirlwind =  Spell("Whirlwind", cost=1, ability = damage_all_minions)
