from game.move import (PlayCard, MinionVsHero, MinionVsMinion, FinishTurn,
                       PlayMinionCard, PlayAbilityCard)
from game.hero import Hero, AI

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
    def __init__(self, board, statePrinter):
        self.state = State(board)
        self.board = board
        self.statePrinter = statePrinter
        self.nextMove()

    def nextTurn(self):
        self.board._nextPlayer()
        self.nextMove()

    def performMove(self, move):
        if isinstance(move, FinishTurn):
            self.nextTurn()
        else:
            self.state = move(self.state)
            winner = self.board.winner()
            if winner is not None:
                return winner
            else:
                self.nextMove()

    def activePlayerPicksMove(self):
        player = self.state.active_player
        self.statePrinter.printState(self.state)
        move = None

        if isinstance(player, Hero):
            try:
                moveNo = int(input('Ktory ruch wybierasz: '))
                move = self.state.moves[moveNo]
                self.statePrinter._printSeparator('*')
            except (IndexError, ValueError):
                print('Niepoprawny ruch, spróbuj ponownie.')
        elif isinstance(player, AI):
            move = player.choose_move(self.state.moves)

        return move

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

    def _generateMinionCardMoves(self):
        moves = []

        for card in self.state.active_player.hand_minions:
            if self.state.active_player.has_enough_mana(card.cost):
                moves.append(PlayMinionCard(card))

        return moves

    def _generateAbilityCardMoves(self):
        moves = []
        enemy = self.state.enemy

        for card in self.state.active_player.hand_abilities:
            if self.state.active_player.has_enough_mana(card.cost):
                moves.append(PlayAbilityCard(card, enemy))

        return moves

    def _generateMinionVsMinionMoves(self):
        moves = []

        for heroMinion in self.state.active_player_panel.minions:
            for enemyMinion in self.state.enemy_panel.minions:
                moves.append(MinionVsMinion(heroMinion, enemyMinion))

        return moves

    def _generateMinionVsHeroMoves(self):
        moves = []
        enemy = self.state.enemy

        for minion in self.state.active_player_panel.minions:
            moves.append(MinionVsHero(minion, enemy))

        return moves
