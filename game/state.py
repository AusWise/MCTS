from game.move import PlayCard, MinionVsHero, MinionVsMinion, FinishTurn


class State:
    def __init__(self, board):
        self.MAX_MANA = 10
        self.board = board
        self.current_round = 1
        self.turn = self.board.hero1

        self.hero1.mana = 1
        self.hero1.mana = 1

        self.hero1.pick(3)
        self.hero2.pick(4)
        self.moves = self.generateMoves()

    @property
    def hero1(self):
        return self.board.hero1

    @property
    def hero2(self):
        return self.board.hero2

    def enemy(self, hero):
        if hero==self.hero1:
            return self.hero2

        if hero==self.hero2:
            return self.hero1

    def generateMoves(self):
        moves = []

        moves += self._generatePlayCardMoves()
        moves += self._generateMinionVsMinionMoves()
        moves += self._generateMinionVsHeroMoves()
        moves.append(FinishTurn())

        return moves

    def _generatePlayCardMoves(self):
        moves = []
        for card in self.turn.hand:
            if card.cost <= self.turn.mana:
                moves.append(PlayCard(card))

        return moves

    def _generateMinionVsMinionMoves(self):
        moves = []
        hero = self.turn
        enemy = self.enemy(hero)

        for heroMinion in self.board[hero].minions:
            for enemyMinion in self.board[enemy].minions:
                moves.append(MinionVsMinion(heroMinion, enemyMinion))

        return moves

    def _generateMinionVsHeroMoves(self):
        moves = []
        hero = self.turn
        enemy = self.enemy(hero)

        for minion in self.board[hero].minions:
            moves.append(MinionVsHero(minion, enemy))

        return moves

    def nextTurn(self):
        if self.turn == self.hero1:
            turn = self.hero2
            _round = self.current_round
        elif self.turn == self.hero2:
            _round = self.current_round + 1
            turn = self.hero1

    # adapt nextTurn after small refactor

    def nextMove(self):
        self.moves = self.generateMoves()
        return self
