class StatePrinter:
    def printState(self, state):
        print('*' * 60)
        self.printTurn(state.current_round)
        self.printTurnOwn(state.turn)
        self.printHand(state.board.hero1)
        self.printHero(state.board.hero1)
        self.printBoard(state.board)
        self.printHero(state.board.hero2)
        self.printHand(state.board.hero2)
        self.printMoves(state.moves)

    def printTurn(self, _round):
        print('Round: ' + str(_round))

    def printTurnOwn(self, turn):
        print('Turn: ' + str(turn.name) + '\n')

    def printHero(self, hero):
        print( str(hero.name) + ': [mana: ' + str(hero.mana) + ', health: ' + str(hero.health) +' ]')

    def printBoard(self, board):
        print('--------------------------------------------------')
        def _print_player_board(cards):
            for _card in cards:
                self.printCard(_card)
                print()
            print('\n--------------------------------------------------')

        _print_player_board(board.halfBoard1.cards)
        _print_player_board(board.halfBoard2.cards)

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
