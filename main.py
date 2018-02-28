from game.state import State
from game.printer import StatePrinter

statePrinter = StatePrinter()

state = State()

statePrinter.printState(state)

print(statePrinter.stateString)

while(True):
    moveNo = int(input('Ktory ruch wybierasz: '))

    move = state.moves[moveNo]
    state = move(state)

    if state is None:
        break

    statePrinter.printState(state)

    print(statePrinter.stateString)
