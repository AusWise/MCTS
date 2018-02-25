MAX_MANA = 10
MAX_MINIONS_ON_BOARD = 7
MINIONS_IN_DECK = 7
ABILITIES_IN_DECK = 3

import numpy as np

from mcts import Hero
from mcts.cards import CardFactory
from copy import deepcopy
from mcts import Board

def generateDeck():
    cardFactory = CardFactory()
    cards = cardFactory()
    deck = deepcopy(cards) + deepcopy(cards)
    deck = np.random.permutation(deck)



    return deck

hero1 = Hero(deck=generateDeck())
hero2 = Hero(deck=generateDeck())

board = Board(hero1, hero2)

turnNo = 1
turnOwn = hero1

turnOwn.mana = min([turnNo, MAX_MANA])


