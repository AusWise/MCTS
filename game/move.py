class Move:
    pass

class PlayCard(Move):
    def __init__(self, card):
        self.card = card

    def __call__(self, state):
        state.board[state.turn].play(self.card)

    def __str__(self):
        return 'Play card ' + self.card.name


class MinionVsMinion(Move):
    def __init__(self, minion1, minion2):
        self.minion1 = minion1
        self.minion2 = minion2

    def __call__(self, state):
        self.minion1.health -= self.minion2.attack
        self.minion2.health -= self.minion1.attack

        if self.minion1.health<=0:
            state.board[state.turn].remove(self.minion1)

        if self.minion2.health <= 0:
            state.board[state.enemy(state.turn)].remove(self.minion2)

    def __str__(self):
        return self.minion1.name + ' vs. ' + self.minion2.name

class MinionVsHero(Move):
    def __init__(self, minion, hero):
        self.minion = minion
        self.hero = hero

    def __call__(self, state):
        self.hero.health -= self.minion.attack

        if self.hero.health <= 0:
            return None

    def __str__(self):
        return self.minion.name + ' vs. ' + self.hero.name

class FinishTurn(Move):
    def __call__(self, state):
        return state.nextTurn()

    def __str__(self):
        return 'Finish Turn'
