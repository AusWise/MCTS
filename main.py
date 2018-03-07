from game.state import GameEngine
from game.printer import StatePrinter
from game.builder import BoardBuilder
from game.move import FinishTurn


def game_loop(engine, statePrinter):
    while(True):
        statePrinter.printState(engine)

        try:
            moveNo = int(input('Ktory ruch wybierasz: '))
            move = engine.moves[moveNo]
        except (IndexError, ValueError):
            print('Niepoprawny ruch, spróbuj ponownie.')
            continue
        engine.performMove(move)


if __name__ == "__main__":
    statePrinter = StatePrinter()
    board = BoardBuilder().build()
    engine = GameEngine(board=board)
    game_loop(engine=engine, statePrinter=statePrinter)
