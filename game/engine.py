from game.move import PlayCard, MinionVsHero, MinionVsMinion, FinishTurn, PlayMinionCard, PlayAbilityCard


class GameEngine:
    def __init__(self, board):
        self.board = board
        self.generateMoves()

    def nextTurn(self):
        self.board.nextPlayer()
        self.generateMoves()

    def performMove(self, move):
        if isinstance(move, FinishTurn):
            self.nextTurn()
        else:
            #TODO: extract state
            move(self)
            self.nextMove()

    def nextMove(self):
        self.generateMoves()

    def generateMoves(self):
        self.moves = []

        self.moves += self._generateMinionCardMoves()
        self.moves += self._generateAbilityCardMoves()
        self.moves += self._generateMinionVsMinionMoves()
        self.moves += self._generateMinionVsHeroMoves()
        self.moves.append(FinishTurn())

    def _generateMinionCardMoves(self):
        moves = []

        for card in self.board.active_player.hand_minions:
            if self.board.active_player.has_enough_mana(card.cost):
                moves.append(PlayMinionCard(card))

        return moves


    def _generateAbilityCardMoves(self):
        moves = []
        enemy = self.board.enemy

        for card in self.board.active_player.hand_abilities:
            if self.board.active_player.has_enough_mana(card.cost):
                moves.append(PlayAbilityCard(card, enemy))

        return moves


    def _generateMinionVsMinionMoves(self):
        moves = []

        for heroMinion in self.board.active_player_panel.minions:
            for enemyMinion in self.board.enemy_panel.minions:
                moves.append(MinionVsMinion(heroMinion, enemyMinion))

        return moves

    def _generateMinionVsHeroMoves(self):
        moves = []
        enemy = self.board.enemy

        for minion in self.board.active_player_panel.minions:
            moves.append(MinionVsHero(minion, enemy))

        return moves
