from game.move import PlayCard, MinionVsHero, MinionVsMinion, FinishTurn
from game.hero import Hero
from game.card import CardFactory
from game.board import Board
from collections import deque

from copy import deepcopy
import numpy as np

MAX_MANA = 10

def generateDeck():
    cardFactory = CardFactory()
    cards = cardFactory()
    deck = deepcopy(cards) + deepcopy(cards)
    deck = np.random.permutation(deck)
    deck = deque(deck)

    return deck

class State:
    def __init__(self, round=1, turn=None, board=None):
        if board is None:
            hero1 = Hero(name="Hero 1", deck=generateDeck())
            hero2 = Hero(name="Hero 2", deck=generateDeck())

            self.board = Board(hero1, hero2)
        else:
            self.board = board

        self.round = round
        if turn is None:
            self.turn = self.hero1
        else:
            self.turn = turn

        self.turn.mana = min([round, MAX_MANA])

        if self.round==1:
            if self.turn==self.hero1:
                self.turn.pick(3)
            elif self.turn==self.hero2:
                self.turn.pick(4)
        else:
            self.turn.pick()

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

        moves += self._genertatePlayCardMoves()
        moves += self._generateMinionVsMinionMoves()
        moves += self._generateMinionVsHeroMoves()
        moves.append(FinishTurn())

        self.moves = moves
        return moves

    def _genertatePlayCardMoves(self):
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
            round = self.round
        elif self.turn == self.hero2:
            round = self.round + 1
            turn = self.hero1

        board = self.board

        return State(round, turn, board)

    def nextMove(self):
        self.generateMoves()
        return self



