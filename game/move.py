class Move:
    pass

class PlayCard(Move):
    def __init__(self, card):
        self.card = card

    def __call__(self, state):
        state.board[state.turn].play(self.card)
        return state.nextMove()

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

        return state.nextMove()

class MinionVsHero(Move):
    def __init__(self, minion, hero):
        self.minion = minion
        self.hero = hero

    def __call__(self, state):
        self.hero.health -= self.minion.attack

        if self.hero.health <= 0:
            return None

        return state.nextMove()

class FinishTurn(Move):
    def __init__(self):
        pass

    def __call__(self, state):
        return state.nextTurn()