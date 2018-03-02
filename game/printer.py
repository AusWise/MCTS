class StatePrinter:
    def printState(self, state):
        print('*' * 60)
        self.printTurn(state.board.rounds_count)
        self.printTurnOwn(state.board.active_player)
        self.printHand(state.board.active_player)
        self.printHero(state.board.active_player)
        self.printBoard(state.board)
        self.printHero(state.board.enemy)
        self.printHand(state.board.enemy)
        self.printMoves(state.moves)

    def printTurn(self, _round):
        print('Round: ' + str(_round))

    def printTurnOwn(self, player):
        print('Turn: ' + str(player.name) + '\n')

    def printHero(self, hero):
        print( str(hero.name) + ': [mana: ' + str(hero.mana) + ', health: ' + str(hero.health) +' ]')

    def printBoard(self, board):
        print('--------------------------------------------------')
        def _print_player_board(cards):
            for _card in cards:
                self.printCard(_card)
                print()
            print('\n--------------------------------------------------')

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
