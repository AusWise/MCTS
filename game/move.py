class Move:
    pass

class PlayCard(Move):
    def __init__(self, card):
        self.card = card

    def __call__(self, board):
        board.active_panel.play_card(self.card)
        return board

    def __str__(self):
        return 'Play card ' + self.card.name


class PlayMinionCard(PlayCard):
    pass


class PlayAbilityCard(Move):
    def __init__(self, card, target):
        self.card = card
        self.target = target

    def __call__(self, board):
        # implement attack
        #board.active_panel.remove_card(self.card)
        board.active_player.remove_card(self.card)
        return board

    def __str__(self):
        return "Use ability " + self.card.name


class MinionVsMinion(Move):
    def __init__(self, minion1, minion2):
        self.minion1 = minion1
        self.minion2 = minion2

    def __call__(self, board):
        self.minion1.lose_health(self.minion2.attack)
        self.minion2.lose_health(self.minion1.attack)

        if not self.minion1.is_alive():
            board.active_panel.remove_card(self.minion1)

        if not self.minion2.is_alive():
            board.enemy_panel.remove_card(self.minion2)

        return board

    def __str__(self):
        return self.minion1.name + ' vs. ' + self.minion2.name

class MinionVsHero(Move):
    def __init__(self, minion, hero):
        self.minion = minion
        self.hero = hero

    def __call__(self, board):
        self.hero.lose_health(self.minion.attack)
        self.minion.used = True

        return board

    def __str__(self):
        return self.minion.name + ' vs. ' + self.hero.name

class FinishTurn(Move):
    def __call__(self, board):
        return board

    def __str__(self):
        return 'Finish Turn'
