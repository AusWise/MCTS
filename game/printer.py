from game.move import *

class StatePrinter:
    def __init__(self):
        self.stateString = ''

    def printState(self, state):
        self.stateString = ''
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
        self.stateString += 'Round: ' + str(round) + '\n'

    def printTurnOwn(self, turn):
        self.stateString += 'Turn: ' + str(turn.name) + '\n \n'

    def printHero(self, hero):
        self.stateString +=  str(hero.name) + ': [mana: ' + str(hero.mana) + ', helth: ' + str(hero.health) +' ]'

    def printBoard(self, board):
        self.stateString += '--------------------------------------------------'
        self.stateString += '\n'

        for card in board.halfBoard1.cards:
            self.printCard(card)
            self.stateString += '\n'

        self.stateString += '\n'

        self.stateString += '\n'
        self.stateString += '--------------------------------------------------'
        self.stateString += '\n'

        self.stateString += '\n'

        for card in board.halfBoard2.cards:
            self.printCard(card)
            self.stateString += '\n'

        self.stateString += '\n'
        self.stateString += '--------------------------------------------------'

    def printCard(self, card):
        self.stateString += str(card)

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
        elif isinstance(move, MinionVsMinion):
            self.stateString += move.minion1.name + ' vs. ' + move.minion2.name
        elif isinstance(move, MinionVsHero):
            self.stateString += move.minion.name + ' vs. ' + move.hero.name
        elif isinstance(move, FinishTurn):
            self.stateString += 'Finish Turn'