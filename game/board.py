from .card import CardType


class Board:
    def __init__(self, hero1, hero2):
        self._panels = {
            hero1: PlayersPanel(hero1, cards_numb=3),
            hero2: PlayersPanel(hero2, cards_numb=4)
        }
        self._players_order = {
            hero1: hero2,
            hero2: hero1
        }
        self._active_player = hero1
        self._switch_count = 0

    @property
    def active_player(self):
        return self._active_player

    @property
    def enemy(self):
        return self._players_order[self.active_player]

    @property
    def active_player_panel(self):
        return self._panels[self.active_player]

    @property
    def enemy_panel(self):
        return self._panels[self.enemy]


    @property
    def active_panel(self):
        return self._panels[self._active_player]

    @property
    def rounds_count(self):
        return self._switch_count // 2 + 1

    def nextPlayer(self):
        _before_round_count = self.rounds_count
        self._active_player = self._players_order[self._active_player]
        self._switch_count += 1
        diff = self.rounds_count - _before_round_count
        if diff < 1:
            self._dealNewTurn()

    def _dealNewTurn(self):
        MAX_MANA = 10
        for player in self._players_order.keys():
            player.mana.points = min([self.rounds_count, MAX_MANA])
            player.pick()
            self._panels[player].enable_cards()


class PlayersPanel:
    def __init__(self, hero, cards_numb):
        self.hero = hero
        self.hero.pick(cards_numb)
        self.cards = set()

    @property
    def minions(self):
        return filter(lambda card: card.type==CardType.MINION and not card.used,
                      self.cards)

    def play_card(self, card):
        self.hero.hand.remove(card)
        self.cards.add(card)
        self.hero.burn_mana(card.cost)

    def remove_card(self, card):
        self.cards.remove(card)

    def enable_cards(self):
        for card in self.cards:
            card.used = False
