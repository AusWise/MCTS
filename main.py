# -*- coding: utf-8 -*-

from game.engine import GameEngine
from game.printer import StatePrinter
from game.builder import BoardBuilder
from game.hero import Hero, AI

def game_loop(engine, statePrinter):
    while(True):
        statePrinter.printState(engine.state)
        current_player = engine.board.active_player
        if isinstance(current_player, Hero):
            try:
                moveNo = int(input('Ktory ruch wybierasz: '))
                move = engine.moves[moveNo]
                statePrinter._printSeparator('*')
            except (IndexError, ValueError):
                print('Niepoprawny ruch, spróbuj ponownie.')
                continue
        elif isinstance(current_player, AI):
            move = current_player.choose_move(engine.moves)
            input("Kliknij aby kontynuuować")
        else:
            pass
        engine.performMove(move)

        print()
        print()
        print()


if __name__ == "__main__":
    statePrinter = StatePrinter()
    board = BoardBuilder().build()
    engine = GameEngine(board=board)
    game_loop(engine=engine, statePrinter=statePrinter)
