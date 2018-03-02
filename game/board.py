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
        return self._switch_count % 2

    def nextPlayer(self):
        _before_round_count = self.rounds_count
        self._active_player = self._players_order[self._active_player]
        self._switch_count += 1
        if self.rounds_count - _before_round_count > 1:
            self._dealNewTurn()

    def playActivePlayersCard(self, card):
        self.active_panel.play(card)

    def removeActivePlayersCard(self, card):
        self.active_panel.remove(card)

    def _dealNewTurn(self):
        MAX_MANA = 10
        turn.mana = min([turn.mana + 1, MAX_MANA])
        turn.pick()


class PlayersPanel:
    def __init__(self, hero, cards_numb):
        self.hero = hero
        self.hero.pick(cards_numb)
        self.cards = set()

    @property
    def minions(self):
        return filter(lambda card: card.type==CardType.MINION, self.cards)

    def play(self, card):
        self.hero.hand.remove(card)
        self.cards.add(card)
        self.hero.mana -= self.card.cost

    def remove(self, card):
        self.cards.remove(card)
