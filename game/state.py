from game.move import PlayCard, MinionVsHero, MinionVsMinion, FinishTurn


class State:
    def __init__(self, board):
        self.board = board
        self.generateMoves()

    def nextTurn(self):
        self.board.nextPlayer()
        self.generateMoves()

    def nextMove(self):
        self.generateMoves()

    def generateMoves(self):
        self.moves = []

        self.moves += self._generatePlayCardMoves()
        self.moves += self._generateMinionVsMinionMoves()
        self.moves += self._generateMinionVsHeroMoves()
        self.moves.append(FinishTurn())

    def _generatePlayCardMoves(self):
        moves = []

        for card in self.board.active_player.hand:
            if self.board.active_player.has_enough_mana(card.cost):
                moves.append(PlayCard(card))

        return moves

    def _generateMinionVsMinionMoves(self):
        moves = []

        for heroMinion in self.board.active_player_panel.minions:
            for enemyMinion in self.board.enemy_panel.minions:
                moves.append(MinionVsMinion(heroMinion, enemyMinion))

        return moves

    def _generateMinionVsHeroMoves(self):
        moves = []

        for minion in self.board.active_player_panel.minions:
            moves.append(MinionVsHero(minion, enemy))

        return moves
