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

class StatePrinter:
    def __init__(self):
        self.stateString = ''

    def printState(self):
        self.printTurn()
        self.printTurnOwn()
        self.printHand(board.hero1)
        self.printHero(board.hero1)
        self.stateString += '\n'
        self.printBoard(board)
        self.stateString += '\n'
        self.printHero(board.hero2)
        self.stateString += '\n'
        self.printHand(board.hero2)
        self.stateString += '\n'
        self.printMoves(moves)

    def printTurn(self):
        self.stateString += 'Turn No: ' + str(turnNo) + '\n'

    def printTurnOwn(self):
        self.stateString += 'Turn Own: ' + str(turnOwn.name) + '\n \n'

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
        for move in moves:
            self.stateString += move

statePrinter = StatePrinter()

hero1 = Hero(name="Hero 1", deck=generateDeck())
hero2 = Hero(name="Hero 2", deck=generateDeck())

board = Board(hero1, hero2)

turnNo = 1
turnOwn = hero1

turnOwn.mana = min([turnNo, MAX_MANA])

turnOwn.hand.add(turnOwn.deck.pop())
turnOwn.hand.add(turnOwn.deck.pop())
turnOwn.hand.add(turnOwn.deck.pop())

def generateMoves():
    return []

moves = generateMoves()

statePrinter.printState()

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

