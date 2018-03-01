from game.state import State
from game.printer import StatePrinter

statePrinter = StatePrinter()

state = State()

statePrinter.printState(state)

print(statePrinter.stateString)

while(True):
    try:
        moveNo = int(input('Ktory ruch wybierasz: '))
        move = state.moves[moveNo]
    except (IndexError, ValueError):
        print('Niepoprawny ruch, spróbuj ponownie.')
        continue
    state = move(state)

    if state is None:
        break

    statePrinter.printState(state)

    print(statePrinter.stateString)
