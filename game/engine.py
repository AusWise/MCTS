from game.move import (PlayCard, MinionVsHero, MinionVsMinion, FinishTurn,
                       PlayMinionCard, PlayAbilityCard)
from game.hero import Hero, AI
from game.mcts.algorithm import MonteCarloTreeSearch


class GameEngine:
    def __init__(self, board, statePrinter):
        self.board = board
        self.statePrinter = statePrinter
        self.nextMove()
        self.mcts = MonteCarloTreeSearch(board, self)

    @property
    def moves(self):
        return self.board.moves

    def nextTurn(self):
        self.board._nextPlayer()
        self.nextMove()

    def performMove(self, move):
        if isinstance(move, FinishTurn):
            self.nextTurn()
        else:
            self.board = move(self.board)
            winner = self.board.winner()
            if winner is not None:
                return winner
            else:
                self.nextMove()

    def activePlayerPicksMove(self):
        player = self.board.active_player
        self.statePrinter.printState(self.board)
        self.statePrinter.printMoves(self.moves)
        move = None

        if isinstance(player, Hero):
            try:
                moveNo = int(input('Ktory ruch wybierasz: '))
                move = self.moves[moveNo]
                self.statePrinter._printSeparator('*')
            except (IndexError, ValueError):
                print('Niepoprawny ruch, spróbuj ponownie.')
        elif isinstance(player, AI):
            move = player.choose_move(self.moves)

        return move

    def nextMove(self):
        self.board.moves = self.generateMoves()

    def generateMoves(self):
        moves = []

        moves += self._generateMinionCardMoves()
        moves += self._generateAbilityCardMoves()
        moves += self._generateMinionVsMinionMoves()
        moves += self._generateMinionVsHeroMoves()
        moves.append(FinishTurn())

        return moves

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
