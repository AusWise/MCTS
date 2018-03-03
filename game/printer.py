class StatePrinter:
    def __init__(self):
        self.separator_quanitity = 60

    def printState(self, state):
        top_player = state.board.enemy
        bottom_player = state.board.active_player

        self._printSeparator('*')
        self.printTurn(state.board.rounds_count)
        self.printTurnOwn(top_player)

        self.printHand(top_player)
        self.printHero(top_player)

        self.printBoard(state.board)

        self.printHero(bottom_player)
        self.printHand(bottom_player)

        self._printSeparator('*')
        self.printMoves(state.moves)

    def printTurn(self, _round):
        print('Round: ' + str(_round))

    def printTurnOwn(self, player):
        print('Turn: ' + str(player.name) + '\n')

    def printHero(self, hero):
        print(hero)

    def printBoard(self, board):
        self._printSeparator('-')
        def _print_player_board(cards):
            for _card in cards:
                self.printCard(_card)
                print()
            print()
            self._printSeparator('-')

        _print_player_board(board.active_player_panel.cards)
        _print_player_board(board.enemy_panel.cards)

    def printCard(self, card):
        print(str(card), end='')

    def printHand(self, hero):
        for card in hero.hand:
            print(str(card))

    def printMoves(self, moves):
        print('Moves: ')
        for moveNo in range(len(moves)):
            move = moves[moveNo]
            self.printMove(move, moveNo)
            print()

    def printMove(self, move, moveNo):
        print("{}. {}".format(moveNo, move), end='')

    def _printSeparator(self, char, quantity=60):
        print(char * quantity)
