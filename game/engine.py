from game.move import PlayCard, MinionVsHero, MinionVsMinion, FinishTurn, PlayMinionCard, PlayAbilityCard

class State:
    def __init__(self, board, moves=None):
        self.board = board
        self.moves = moves

    @property
    def active_player(self):
        return self.board.active_player

    @property
    def enemy(self):
        return self.board.enemy

    @property
    def round(self):
        return self.board.rounds_count

    @property
    def active_player_panel(self):
        return self.board.panels[self.active_player]

    @property
    def enemy_panel(self):
        return self.board.panels[self.enemy]

class GameEngine:
    def __init__(self, board):
        self.state = State(board)
        self.nextMove()

    @property
    def board(self):
        return self.state.board

    def nextTurn(self):
        self.board._nextPlayer()
        self.nextMove()

    def performMove(self, move):
        if isinstance(move, FinishTurn):
            self.nextTurn()
        else:
            self.state = move(self.state)
            self.nextMove()

    def nextMove(self):
        self.state.moves = self.generateMoves()

    def generateMoves(self):
        moves = []

        moves += self._generateMinionCardMoves()
        moves += self._generateAbilityCardMoves()
        moves += self._generateMinionVsMinionMoves()
        moves += self._generateMinionVsHeroMoves()
        moves.append(FinishTurn())

        return moves

    @property
    def active_player(self):
        return self.state.active_player

    @property
    def enemy(self):
        return self.state.enemy

    @property
    def active_player_panel(self):
        return self.board.panels[self.active_player]

    @property
    def enemy_panel(self):
        return self.board.panels[self.enemy]

    def _generateMinionCardMoves(self):
        moves = []

        for card in self.active_player.hand_minions:
            if self.active_player.has_enough_mana(card.cost):
                moves.append(PlayMinionCard(card))

        return moves

    def _generateAbilityCardMoves(self):
        moves = []
        enemy = self.enemy

        for card in self.active_player.hand_abilities:
            if self.active_player.has_enough_mana(card.cost):
                moves.append(PlayAbilityCard(card, enemy))

        return moves

    def _generateMinionVsMinionMoves(self):
        moves = []

        for heroMinion in self.active_player_panel.minions:
            for enemyMinion in self.enemy_panel.minions:
                moves.append(MinionVsMinion(heroMinion, enemyMinion))

        return moves

    def _generateMinionVsHeroMoves(self):
        moves = []
        enemy = self.enemy

        for minion in self.active_player_panel.minions:
            moves.append(MinionVsHero(minion, enemy))

        return moves

    @property
    def moves(self):
        return self.state.moves
