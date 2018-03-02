from game.state import State
from game.printer import StatePrinter
from game.builder import BoardBuilder
from game.move import FinishTurn


def game_loop(state, statePrinter):
    while(True):
        statePrinter.printState(state)

        try:
            moveNo = int(input('Ktory ruch wybierasz: '))
            move = state.moves[moveNo]
        except (IndexError, ValueError):
            print('Niepoprawny ruch, spróbuj ponownie.')
            continue

        if isinstance(move, FinishTurn):
            state.nextTurn()
        else:
            move(state)
            state.nextMove()


if __name__ == "__main__":
    statePrinter = StatePrinter()
    board = BoardBuilder().build()
    state = State(board=board)
    game_loop(state=state, statePrinter=statePrinter)
