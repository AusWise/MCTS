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
        return state

class Finish(Move):
    def __init__(self):
        pass

    def __call__(self, state):
        if state.turn == state.hero1:
            state.turn = state.hero2
        elif state.turn == state.hero2:
            state.round += 1
            state.turn = state.hero1

        return state

class StatePrinter:
    def __init__(self):
        self.stateString = ''

    def printState(self, state):
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
        self.stateString += 'Turn No: ' + str(round) + '\n'

    def printTurnOwn(self, turn):
        self.stateString += 'Turn Own: ' + str(turn.name) + '\n \n'

    def printHero(self, hero):
        self.stateString +=  str(hero.name) + ': [mana: ' + str(hero.mana) + ', helth: ' + str(hero.health) +' ]'

    def printBoard(self, board):
        pass

    def printCard(self, card):
        self.stateString += card.name

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
        elif isinstance(move, Finish):
            self.stateString += 'Finish Turn'

statePrinter = StatePrinter()

class State:
    def __init__(self, round=1, turn=None):
        hero1 = Hero(name="Hero 1", deck=generateDeck())
        hero2 = Hero(name="Hero 2", deck=generateDeck())

        self.board = Board(hero1, hero2)

        self.round = round
        if turn is None:
            self.turn = hero1
        else:
            self.turn = turn

        self.turn.mana = min([round, MAX_MANA])

        if self.round==1:
            if self.turn==hero1:
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
            elif self.turn==hero2:
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())
                self.turn.hand.add(self.turn.deck.pop())

        self.moves = self.generateMoves()

    @property
    def hero1(self):
        return self.board.hero1

    @property
    def hero2(self):
        return self.board.hero2

    def generateMoves(self):
        moves = []
        for card in self.turn.hand:
            moves.append(PlayCard(card))

        moves.append(Finish())
        return moves

state = State()

statePrinter.printState(state)

print(statePrinter.stateString)

moveNo = int(input('Ktory ruch wybierasz: '))

move = state.moves[moveNo]
state = move(state)

state.generateMoves()
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

