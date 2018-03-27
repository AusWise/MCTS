# -*- coding: utf-8 -*-

from game.engine import GameEngine
from game.printer import StatePrinter
from game.builder import BoardBuilder
import sys

def game_loop(engine):
    while(True):
        move = engine.activePlayerPicksMove()
        if move is None:
            continue
        winner = engine.performMove(move)
        if winner is not None:
            print('{} won!'.format(winner))
            sys.exit(0)

        print('\n' * 3, end='')


if __name__ == "__main__":
    statePrinter = StatePrinter()
    board = BoardBuilder().build()
    engine = GameEngine(board=board, statePrinter=statePrinter)
    game_loop(engine=engine)
