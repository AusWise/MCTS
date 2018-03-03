class Move:
    pass

class PlayCard(Move):
    def __init__(self, card):
        self.card = card

    def __call__(self, state):
        state.board.active_panel.play_card(self.card)

    def __str__(self):
        return 'Play card ' + self.card.name


class MinionVsMinion(Move):
    def __init__(self, minion1, minion2):
        self.minion1 = minion1
        self.minion2 = minion2

    def __call__(self, state):
        self.minion1.lose_health(self.minion2.attack)
        self.minion2.lose_health(self.minion1.attack)

        if not self.minion1.is_alive():
            state.board.active_panel.remove_card(self.minion1)

        if not self.minion2.is_alive():
            state.board.enemy_panel.remove_card(self.minion2)

    def __str__(self):
        return self.minion1.name + ' vs. ' + self.minion2.name

class MinionVsHero(Move):
    def __init__(self, minion, hero):
        self.minion = minion
        self.hero = hero

    def __call__(self, state):
        self.hero.lose_health(self.minion.attack)

        if not self.hero.is_alive():
            return None

    def __str__(self):
        return self.minion.name + ' vs. ' + self.hero.name

class FinishTurn(Move):
    def __call__(self, state):
        pass

    def __str__(self):
        return 'Finish Turn'
