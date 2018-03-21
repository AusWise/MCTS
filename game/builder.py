from game.board import Board
from game.card import CardFactory
from game.hero import Hero, RandomAI, DefensiveAI
from copy import deepcopy
import numpy as np
from collections import deque

class BoardBuilder:
    def generateDeck(self):
        cardFactory = CardFactory()
        cards = cardFactory()
        deck = deepcopy(cards) + deepcopy(cards)
        deck = np.random.permutation(deck)
        deck = deque(deck)

        return deck

    def build(self):
        hero1 = Hero(name="Hero 1", deck=self.generateDeck())
        hero2 = Hero(name="Hero 2", deck=self.generateDeck())
        board = Board(hero1, hero2)

        return board