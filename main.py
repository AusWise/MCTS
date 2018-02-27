MAX_MANA = 10
MAX_MINIONS_ON_BOARD = 7
MINIONS_IN_DECK = 7
ABILITIES_IN_DECK = 3

from copy import deepcopy
import numpy as np

from game.hero import Hero
from game.card import CardFactory
from game.board import Board
from collections import deque

def generateDeck():
    cardFactory = CardFactory()
    cards = cardFactory()
    deck = deepcopy(cards) + deepcopy(cards)
    deck = np.random.permutation(deck)
    deck = deque(deck)

    return deck

class Move:
    pass

class PlayCard(Move):
    def __init__(self, card):
        self.card = card

    def __call__(self, state):
        state.turn.hand.remove(self.card)
        state.board[state.turn].cards.add(self.card)
        state.moves = state.generateMoves()
        state.turn.mana -= self.card.cost
        return state

class MinionVsMinion(Move):
    def __init__(self, minion1, minion2):
        self.minion1 = minion1
        self.minion2 = minion2

    def __call__(self, state):
        self.minion1.health -= self.minion2.attack
        self.minion2.health -= self.minion1.attack

        if self.minion1.health<=0:
            state.board[state.turn].cards.remove(self.minion1)

        if self.minion2.health <= 0:
            state.board[state.enemy(state.turn)].cards.remove(self.minion2)

        state.moves = state.generateMoves()

        return state


class Finish(Move):
    def __init__(self):
        pass

    def __call__(self, state):
        if state.turn == state.hero1:
            turn = state.hero2
            round = state.round
        elif state.turn == state.hero2:
            round = state.round + 1
            turn = state.hero1

        board = state.board

        return State(round, turn, board)

class StatePrinter:
    def __init__(self):
        self.stateString = ''

    def printState(self, state):
        self.stateString = ''
        self.printTurn(state.round)
        self.printTurnOwn(state.turn)
        self.printHand(state.board.hero1)
        self.printHero(state.board.hero1)
        self.stateString += '\n'
        self.printBoard(state.board)
        self.stateString += '\n'
        self.printHero(state.board.hero2)
        self.stateString += '\n'
        self.printHand(state.board.hero2)
        self.stateString += '\n'
        self.printMoves(state.moves)

    def printTurn(self, round):
        self.stateString += 'Round: ' + str(round) + '\n'

    def printTurnOwn(self, turn):
        self.stateString += 'Turn: ' + str(turn.name) + '\n \n'

    def printHero(self, hero):
        self.stateString +=  str(hero.name) + ': [mana: ' + str(hero.mana) + ', helth: ' + str(hero.health) +' ]'

    def printBoard(self, board):
        self.stateString += '--------------------------------------------------'
        self.stateString += '\n'

        for card in board.halfBoard1.cards:
            self.printCard(card)
            self.stateString += '\n'

        self.stateString += '\n'

        self.stateString += '\n'
        self.stateString += '--------------------------------------------------'
        self.stateString += '\n'

        self.stateString += '\n'

        for card in board.halfBoard2.cards:
            self.printCard(card)
            self.stateString += '\n'

        self.stateString += '\n'
        self.stateString += '--------------------------------------------------'

    def printCard(self, card):
        self.stateString += str(card)

    def printHand(self, hero):
        for card in hero.hand:
            self.stateString += str(card) + '\n'

    def printMoves(self, moves):
        self.stateString += 'Moves: \n'
        for moveNo in range(len(moves)):
            move = moves[moveNo]
            self.printMove(move, moveNo)
            self.stateString += '\n'

    def printMove(self, move, moveNo):
        self.stateString += str(moveNo) + '. '
        if isinstance(move, PlayCard):
            self.stateString += 'Play card ' + move.card.name
        elif isinstance(move, MinionVsMinion):
            self.stateString += move.minion1.name + ' vs. ' + move.minion2.name
        elif isinstance(move, Finish):
            self.stateString += 'Finish Turn'

statePrinter = StatePrinter()

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
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
            elif self.turn==self.hero2:
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
        else:
            self.turn.hand.add(self.turn.deck.pop())

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
        for card in self.turn.hand:
            if card.cost<=self.turn.mana:
                moves.append(PlayCard(card))

        hero = self.turn
        enemy = self.enemy(hero)

        for heroMinion in self.board[hero].minions:
            for enemyMinion in self.board[enemy].minions:
                moves.append(MinionVsMinion(heroMinion, enemyMinion))

        moves.append(Finish())
        return moves

state = State()

statePrinter.printState(state)

print(statePrinter.stateString)

while(True):
    moveNo = int(input('Ktory ruch wybierasz: '))

    move = state.moves[moveNo]
    state = move(state)

    # state.generateMoves()
    statePrinter.printState(state)

    print(statePrinter.stateString)

# turnNo = 1
# turnOwn = hero2
#
# turnOwn.mana = min(turnNo, MAX_MANA)
#
# turnOwn.hand.add(turnOwn.deck.pop())
# turnOwn.hand.add(turnOwn.deck.pop())
# turnOwn.hand.add(turnOwn.deck.pop())
# turnOwn.hand.add(turnOwn.deck.pop())
#
# print(printStateStrategy.printState())

